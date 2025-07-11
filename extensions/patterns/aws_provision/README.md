
# Ansible pattern for Red Hat AI in AWS

This pattern will deploy a Red Hat AI in AWS.

Some resources need to be prepared before pattern can be run.
Prepare in AAP:
- SCM credential for github - PAT token
  - Follow https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_ansible_automation_platform_self-service_technology_preview/self-service-using-scm-credentials-private-repos_aap-self-service-using
  - Used for pre-seeding job template
  - copy of github PAT token is used to git clone during preseeding.
- AWS credential
  - Used when running this pattern

To use this pattern in RHDH:
- configure RHDH to use https://github.com/justinc1/ansible-rhdh-templates-rhel-ai/blob/develop/seed.yaml
  This is set in app-config.local.yaml file.
  - if you are testing [rhdh-local](https://github.com/redhat-developer/rhdh-local), file path is ./configs/app-config/app-config.local.yaml
  - if using openshift: TODO
- in RHDH UI, when running preseed template:
  - use https://github.com/jcinkelj/ansible-pattern-loader, branch rhelai.
    This in turn will use https://github.com/ansible-collections/infra.ai, branch patterns

Example vars to set in RHDH UI:
