# infra.ai Validated Content Collection

This repository holds the `infra.ai` Ansible Collection.

## Description
This collection is curated to provide users with a robust set of roles, playbooks, and rulebooks that simplify and streamline AWS infrastructure operations related to RHEL AI.

## Requirements

The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [cloud.aws_ops](https://github.com/redhat-cop/cloud.aws_ops) collections MUST be installed in order for this collection to work.

### Ansible version compatibility
This collection has been tested against following Ansible versions: >=2.15.0.

### Included content
Click on the name of a role, playbook, or rulebook to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[infra.ai.nginx_proxy](roles/nginx_proxy/README.md)|A role to orchestrate nginx proxy.

### Playbooks
Name | Description
--- | ---
[infra.ai.aws_provision.provision](playbooks/aws_orchestration/PROVISION.md)|AWS provisioning EC2 instances playbook.
[infra.ai.aws_provision.teardown](playbooks/aws_orchestration/TEARDOWN.md)|Facilitating teardown of created EC2 instances.
[infra.ai.proxy.proxy](playbooks/proxy/README.md)|Orchestration of the nginx proxy on the provisioned instances.
<!--end collection content-->

## Installation

```shell
$ ansible-galaxy collection install -r requirements.yml
```

## Usage

### Setting up aws-related settings

Set your dev env:
```shell
# using the "default" profile on AWS
aws configure set aws_access_key_id     my-access-key
aws configure set aws_secret_access_key my-secret-key
aws configure set region                eu-central-1

ansible-test integration [target]
```

### Setup variables

```shell
$ cp sample_vars.yml vars.yml
```

## Use Cases

### Playbooks

You can provision and teardown the infrastructure with playbooks.

#### Provisioning

```shell
ansible-playbook playbooks/aws_orchestration/provision.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

#### Teardown
```shell
ansible-playbook playbooks/aws_orchestration/teardown.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

#### Inventory
```shell
ansible-inventory -i inventory/rhelai.aws_ec2.yml --graph
```

#### Installing proxy
```shell
ansible-playbook playbooks/proxy/proxy.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

### Roles

Set variables and include the role to use `nginx_proxy`.

```yml
---
- name: Install and provision nginx proxy
  hosts: all
  roles:
    - role: infra.ai.nginx_proxy
      nginx_proxy_fqdn: example.ltd
      nginx_proxy_install_dir: /home/ec2-user
      module_defaults:
        group/aws:
          region: "{{ aws_region | default(lookup('ansible.builtin.env', 'AWS_REGION')) }}"
          aws_access_key: "{{ aws_access_key | default(lookup('ansible.builtin.env', 'AWS_ACCESS_KEY')) }}"
          aws_secret_key: "{{ aws_secret_key | default(lookup('ansible.builtin.env', 'AWS_SECRET_KEY')) }}"
```

## Testing

The project uses `ansible-lint` and `black`.
Assuming this repository is checked out in the proper structure,
e.g. `collections_root/ansible_collections/infra/ai/`, run:

```shell
tox -e linters
```

Sanity and unit tests are run as normal:

```shell
ansible-test sanity
```

If you want to run cloud integration tests, ensure you log in to the cloud:

```shell
# using the "default" profile on AWS
aws configure set aws_access_key_id     my-access-key
aws configure set aws_secret_access_key my-secret-key
aws configure set region                eu-central-1

ansible-test integration [target]
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.
See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## Support

For the latest supported versions, refer to the release notes below.

If you encounter issues or have questions, you can submit a support request through the following channels:
 - GitHub Issues: Report bugs, request features, or ask questions by opening an issue in the [GitHub repository](https://github.com/ansible-collections/infra.ai/).
 - Ansible Community: Engage with the Ansible community on the Ansible Project Mailing List or [Ansible Forum](https://forum.ansible.com/g/AWS).

## Release Notes

See the [raw generated changelog](https://github.com/ansible-collections/infra.ai/blob/main/CHANGELOG.rst).


## Related Information

 - [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html).
 - [Ansible Rulebook documentation](https://ansible.readthedocs.io/projects/rulebook/en/stable/index.html).
 - [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.