#!/usr/bin/env python3

"""
helper for RHDH ansible pattern development
Input: RHDH template
Output: AAP surway
"""

import sys
import yaml
import logging
import argparse

_level = logging.DEBUG
logging.basicConfig(level=_level)
logger = logging.getLogger(__name__)

def flatten_list_of_lists(xss):
    return [
        x
        for xs in xss
        for x in xs
    ]


def flatten_list_of_dicts(xss):
    out = dict()
    for xs in xss:
        out.update(xs)
    return out


# Allowed AAP types:
#     msg: 'Failed to update survey: ''dict'' in survey question 2 is not one of ''text,
#        textarea, password, multiplechoice, multiselect, integer, float'' allowed question
#        types.'
_map_rhdh_type_to_aap_type = {
    "string": "text",
    "dict": "textarea",
    # "list": "list",
}

def convert(rhdh, old_aap):
    aap = dict()
    aap.update(
        name=rhdh["metadata"]["title"],
        description=rhdh["metadata"]["description"],
    )

    """
    AAP desired output:
    spec:
    - question_name: "AWS resource name"
        question_description: "Please enter the AWS resource name, it is used to generate name for EC2 instance and other related resources."
        required: false
        variable: "rhelai_aws_resource_name"
        type: "text"
        default: myRHELAIInstance

    RHDH param
        azureRegion:
          title: Azure region
          description: Azure region
          type: string
          default: eastus        
    """
    rhdh_param_propertiers = flatten_list_of_dicts([
        param["properties"]
        for param
        in rhdh["spec"]["parameters"]
        if param["title"] == "Survey"
    ])
    # print(f"rhdh_param_propertiers={rhdh_param_propertiers}")
    rhdh_required_vars = flatten_list_of_lists([
        param["required"]
        for param
        in rhdh["spec"]["parameters"]
        if param["title"] == "Survey"
    ])
    # print(f"rhdh_required_vars={rhdh_required_vars}")
    rhdh_extra_vars = flatten_list_of_dicts([
        step["input"]["values"]["extraVariables"]
        for step
        in rhdh["spec"]["steps"]
        if step["action"] == "rhaap:launch-job-template"
    ])
    # print(f"rhdh_extra_vars={rhdh_extra_vars}")

    spec_all = []
    for var_name in rhdh_extra_vars:
        # print(f"var_name={var_name}")
        var_value = rhdh_extra_vars[var_name]
        if not isinstance(var_value, str) or not var_value.startswith("${{") or not var_value.endswith("}}"):
            # this is not a trivial 1-1 mapping from a RHDH param
            old_spec = [
                oldspec
                for oldspec in 
                old_aap["spec"]
                if oldspec["variable"] == var_name
            ]
            if old_spec:
                assert len(old_spec) == 1
                logger.warning(f"Variable {var_name} is complex, keep old value.")
                spec = old_spec[0]
            else:
                logger.warning(f"Variable {var_name} is complex, insert placeholder.")
                spec = dict(variable=var_name)
            spec_all.append(spec)
            continue
        # find a RHDH param
        param_name = var_value[3:-2].strip()
        assert "{{" not in param_name
        assert "}}" not in param_name
        assert " " not in param_name
        assert param_name.startswith("parameters.")
        param_name = param_name[len("parameters."):]
        # print(f"  param_name={param_name}")
        param = rhdh_param_propertiers[param_name]
        spec = dict(
            question_name=param["title"],
            question_description=param["description"],
            required=param_name in rhdh_required_vars,
            variable=var_name,
        )
        if "default" in param:
            spec["default"] = param["default"]
        # aap_type = "string"
        if "type" in param:
            rhdh_type = param["type"]
            aap_type = _map_rhdh_type_to_aap_type[rhdh_type]
            spec["type"] = aap_type
        spec_all.append(spec)

    aap.update(spec=spec_all)
    return aap


def main():
    parser = argparse.ArgumentParser(
                        description='Converter from RHDH template to AAP surway.',
                        )
    parser.add_argument(
        'rhdh_path',
        help="Path to RHDH template. Example 'extensions/patterns/myusecase/template_rhdh/mytemplate.yaml'.",
        default="extensions/patterns/azure/template_rhdh/azure_provision.yml"
        )
    
    if 1:
        args = parser.parse_args()
        rhdh_path = args.rhdh_path
    else:
        # debuger
        rhdh_path = "extensions/patterns/azure/template_rhdh/azure_provision.yml"

    if "template_rhdh/" not in rhdh_path:
        logger.error("Script expects 'template_rhdh/' string in path.")
        sys.exit(1)

    aap_path = rhdh_path.replace("template_rhdh/", "template_surveys/")
    
    with open(rhdh_path) as fin:
        rhdh = yaml.safe_load(fin)

    old_aap = None
    try:
        with open(aap_path) as fold:
            old_aap = yaml.safe_load(fold)
    except FileNotFoundError:
        pass

    aap = convert(rhdh, old_aap)

    with open(aap_path, "w") as fout:
        yaml.dump(aap, fout, indent=2, width=2, explicit_start=True)


if __name__ == "__main__":
    main()
