# infra.ai Validated Content Collection

This repository hosts the ``infra.ai`` Ansible Collection.

## Description

This collection is curated to provide users with a robust set of roles and playbooks that simplify and streamline Amazon Web Services (AWS) infrastructure operations in Red Hat Enterprise Linux AI (RHEL AI) environments.

As a Red Hat Ansible [Certified Content](https://catalog.redhat.com/software/search?target_platforms=Red%20Hat%20Ansible%20Automation%20Platform), this collection is entitled to [support](https://access.redhat.com/support/) through [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) (AAP) through the Red Hat Ansible team.

## Requirements

The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [cloud.aws_ops](https://github.com/redhat-cop/cloud.aws_ops) collections MUST be installed in order for this collection to work.

<!--start requires_ansible-->
### Ansible Version Compatibility

This collection has been tested against following Ansible versions: **>=2.16.0**.
<!--end requires_ansible-->

### Python Version Compatibility

This collection requires Python 3.10 or newer.

## Installation

To consume this Validated Content from Automation Hub, please ensure that you add the following lines to your ``ansible.cfg`` file.

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
The token can be obtained from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

Once the above steps are done, you can run the following command to install the collection.

```bash
ansible-galaxy collection install infra.ai
```

You can also include it in a ``requirements.yml`` file and install it with ``ansible-galaxy collection install -r requirements.yml``, using the format:

```yaml
---
collections:
  - name: infra.ai
```

Note that if you install any collections from Ansible Galaxy, they will not be upgraded automatically when you upgrade the Ansible package. To upgrade the collection to the latest available version, run the following command:

```bash
ansible-galaxy collection install infra.ai --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 1.0.0:

```bash
ansible-galaxy collection install infra.ai:==1.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.


## Using This Xollection

### Set Up AWS Credentials

```shell
# using the "default" profile on AWS
aws configure set aws_access_key_id     my-access-key
aws configure set aws_secret_access_key my-secret-key
aws configure set region                eu-central-1
```

### Set Variables

```shell
cp sample_vars.yml vars.yml
```

The ``sample_vars.yml`` file provides a well-documented starting point for setting up your configuration.
You are encouraged to customize ``vars.yml`` to suit your specific environment and use case.

## Use Cases

You can provision and teardown the infrastructure using the following playbooks:

### Provision Infrastructure

```shell
ansible-playbook playbooks/aws_orchestration/provision.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

### Teardown Infrastructure

```shell
ansible-playbook playbooks/aws_orchestration/teardown.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

#### View the AWS inventory graph
```shell
ansible-inventory -i inventory/rhelai.aws_ec2.yml --graph
```

#### Instal NGINX Proxy

You can install the nginx proxy using the following playbook:

```shell
ansible-playbook playbooks/proxy/proxy.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

The ``playbooks/proxy/proxy.yml`` imports the ``infra.ai.nginx_proxy`` role, but you could also use the role individually by iincluding and setting the required variables as follows:

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

This Collection uses `ansible-lint` and `black`.
Assuming this repository is checked out in the proper structure,
e.g. `collections_root/ansible_collections/infra/ai/`, run:

```shell
tox -e linters
```

Sanity and unit tests are run as normal:

```shell
ansible-test sanity
```

Run integration tests (ensure AWS credentials are configured):

```shell
ansible-test integration [target]
```

## Release Notes

Consult the CHANGELOG.rst included in the collection for details.

## Related Information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GNU General Public License v3.0 or later

Consult the LICENSE included in the collection to see the full text.
