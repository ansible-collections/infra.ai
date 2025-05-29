# infra.ai Validated Content Collection

This repository hosts the ``infra.ai`` Validated Content Collection.

## Description

This collection is curated to provide users with a robust set of roles and playbooks that simplify and streamline Amazon Web Services (AWS) infrastructure operations in Red Hat Enterprise Linux AI (RHEL AI) environments.

**Note**: This collection is provided as validated content, meaning it's intended as a flexible, customizable starting point. As such, Red Hat does not officially support this collection. For feedback or requests, please contact your Red Hat account representative.

## Requirements

To use this collection, the following dependencies MUST be installed:
- [amazon.aws](https://github.com/ansible-collections/amazon.aws)
- [cloud.aws_ops](https://github.com/redhat-cop/cloud.aws_ops)
- [google.cloud](https://docs.ansible.com/ansible/latest/collections/google/cloud/index.html)

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

Once the above steps are done, you need to install it with the Ansible Galaxy command-line tool:


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


## Use Case - AWS

### Set Variables

```shell
cp sample_vars.yml vars.yml
```

The ``sample_vars.yml`` file provides a well-documented starting point for setting up your configuration.
You are encouraged to customize ``vars.yml`` to suit your specific environment and use case.

### Using Google Cloud infrastructure

Create the service account file and save the json cred file to be used with `rhelai_gcp_service_account_file` in the `vars.yml` file.
```shell
# initialize gcloud cli tool if not already
gcloud init

# generate the service account file
gcloud iam service-accounts keys create <path_to_json_cred_output_file> --iam-account=<iam_account>
```

### Using AWS infrastructure

Create the default AWS credentials
```shell
# using the "default" profile on AWS
aws configure set aws_access_key_id     my-access-key
aws configure set aws_secret_access_key my-secret-key
aws configure set region                eu-central-1
```

### View the AWS inventory graph

Generate a graphical view of your AWS inventory:
```shell
ansible-inventory -i inventory/rhelai.aws_ec2.yml --graph
```

### Playbooks Included in the Collection

#### 1. Provision Infrastructure
Launch and configure AWS resources for RHEL AI:
```shell
ansible-playbook infra.ai.aws_provision -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

Launch and configure resources for RHEL AI using Google Cloud:
```shell
ansible-playbook infra.ai.gcp_provision -e @vars.yml
```

#### 2. Teardown Infrastructure
Cleanly decommission provisioned AWS resources:
```shell
ansible-playbook infra.ai.aws_teardown -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

Cleanly decommission provisioned Google Cloud resources:
```shell
ansible-playbook infra.ai.gcp_teardown -e @vars.yml
```

#### 3. Deploy NGINX Proxy
Set up a reverse proxy (with SSL support) for services like instructlab:

```shell
ansible-playbook infra.ai.proxy -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

The ``infra.ai.proxy`` imports the ``infra.ai.nginx_proxy`` role, but you could also use the role individually by including and setting the required variables as follows:

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

## Use Case - baremetal

The collection automates the creation of an ISO image for provisioning a baremetal host.

After ISO image is built, use it to boot a baremetal host from it.
The baremetal host will be automatically reinstalled.
No human interaction is required.
User is not asked for any confirmation.

NOTE: if wrong host is booted from ISO, then operation system will be destoryed.

Before running the playbook:
 - RHEL AI ISO image needs to be downloaded.
   It is available at [Download Red Hat Enterprise Linux AI](https://developers.redhat.com/products/rhel-ai/download).
 - Container registry credentials for pulling RHEL AI updates needs to be created.
   Generate them at https://access.redhat.com/RegistryAuthentication.

### Set Variables

```shell
cp sample_vars.yml vars.yml
vi vars.yml
```

The ``vars.yml`` file needs to be adjusted for your environment (path to downloaded ISO image etc.).

### Playbooks Included in the Collection

#### 1. Build ISO image
Build ISO image:

```shell
ansible-playbook infra.ai.baremetal_provision -e @vars.yml
```

A path to ISO image is shown on screen.
Transfer the ISO image to USB thumbdrive, and boot baremetal host from thumbdrive.

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

### Google Cloud integration tests setup

In order to run the integration tests on Google Cloud, make sure to perform the initial installation.
Once that is done, create the file `tests/integration/cloud-config-gcp.ini` containing the following:

```ini
[default]
gcp_project: <project ID>
gcp_cred_file: </path/to/cred/file.json>
gcp_cred_kind: serviceaccount
```

Run integration tests (ensure AWS credentials are configured):

```shell
ansible-test integration [target]
```

## Release Notes and Roadmap

Consult the CHANGELOG.rst included in the collection for details.

## License

GNU General Public License v3.0 or later

Consult the LICENSE included in the collection to see the full text.
