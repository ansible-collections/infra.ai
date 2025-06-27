# infra.ai playbooks

## AWS Orchestration for RHEL AI

The ``infra.ai`` AWS playbooks provide automation for provisioning and managing cloud infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments. The suite includes the following key playbooks:

- Provision – Launches and configures AWS resources needed to deploy RHEL AI.
- Teardown – Destroys provisioned resources to ensure a clean and complete shutdown.
- Proxy – Sets up an NGINX reverse proxy with SSL support for secure request forwarding.

### AWS Provisioning Playbook: infra.ai.aws_provision

This playbook automates the provisioning of AWS EC2 infrastructure to host RHEL AI AMIs. It manages the creation and configuration of:

- Key pairs
- Virtual Private Cloud (VPC) and networking components
- Security groups
- EC2 instances

Resources are automatically prefixed using the ``rhelai_aws_resource_name`` variable, which can be defined in your variable file for naming consistency.

This playbook includes the following roles:

 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**


#### Example Usage

Ensure AWS credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.aws_provision -i rhelai.aws_ec2.yml -e @sample_vars.yml
```

### AWS Teardown Playbook: infra.ai.aws_teardown

This playbook decommissions all infrastructure previously provisioned via the infra.ai.aws_provision playbook. It is also integrated into test workflows to ensure clean-up during failures or post-integration testing.

This playbook uses the following roles:
 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.manage_ec2_instance](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/manage_ec2_instance)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**

#### Example Usage

Ensure AWS credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.aws_teardown -i rhelai.aws_ec2.yml -e @sample_vars.yml
```

### Proxy Setup Playbook: infra.ai.proxy

This playbook configures a reverse NGINX proxy designed to:

- Support self-signed SSL certificates
- Route requests to the deployed ``instructlab`` service

The proxy runs inside a Podman container and includes automated installation of all required dependencies.

This playbook relies on the following role:

 - **infra.ai.nginx_proxy**


#### Example Usage

Ensure AWS credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.proxy -i rhelai.aws_ec2.yml -e @sample_vars.yml
```

## Baremetal Orchestration for RHEL AI

The ``infra.ai`` baremetal playbooks provide automation for provisioning and managing baremetal infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments. The suite includes the following key playbooks:

- baremetal_provision.yml – Creates an ISO image. The ISO image is used for provisioning a baremetal host.

### Provisioning Playbook: infra.ai.baremetal_provision

This playbook automates the creation of an ISO image for provisioning a baremetal host.

After ISO image is built, use it to boot a baremetal host from it.
The baremetal host will be automatically reinstalled.
No human interaction is required.
User is not asked for any confirmation.

NOTE: if wrong host is booted from ISO, then operation system will be destroyed.

Before running the playbook:
 - RHEL AI ISO image needs to be downloaded.
   It is available at [Download Red Hat Enterprise Linux AI](https://developers.redhat.com/products/rhel-ai/download).
 - Container registry credentials for pulling RHEL AI updates needs to be created.
   Generate them at https://access.redhat.com/RegistryAuthentication.

#### Example Usage

Ensure container registry credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.baremetal_provision -e @sample_vars.yml
```

## Google Cloud Orchestration for RHEL AI

Google Cloud ``infra.ai`` playbooks provide automation for provisioning and managing GCP infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments.
The suite includes the following key playbooks:

- Provision – Launches and configures Google Cloud resources needed to deploy RHEL AI.
- Teardown – Destroys provisioned resources to ensure a clean and complete shutdown.

### Provisioning Playbook: infra.ai.gcp_provision

This playbook automates the provisioning of Google Cloud VM instances to host RHEL AI. It manages the creation and configuration of:

- Key pairs
- Addresses
- VM instances

Resources are automatically prefixed using the ``rhelai_gcp_resource_name`` variable, which can be defined in your variable file for naming consistency.

#### Example Usage

Ensure Google Cloud account is set, the credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.gcp_provision -e @vars.yml
```

### Teardown Playbook: infra.ai.gcp_teardown

This playbook decommissions all infrastructure previously provisioned via the `infra.ai.gcp_provision` playbook. It is also integrated into test workflows to ensure clean-up during failures or post-integration testing.

#### Example Usage

Ensure Google Cloud account is set, the credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.gcp_teardown -e @vars.yml
```

## Azure Orchestration for RHEL AI

The ``infra.ai`` playbooks provide automation for provisioning and managing cloud infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments in Azure.
The suite includes the following key playbooks:

- Provision – Launches and configures Azure resources needed to deploy RHEL AI.
- Teardown – Destroys provisioned Azure resources to ensure a clean and complete shutdown.

### Azure Provisioning Playbook: infra.ai.azure_provision

This playbook automates the provisioning of Azure infrastructure to host RHEL AI AMIs. It manages the creation and configuration of:

- Key pairs
- Virtual networking components
- Security groups
- Azure VMs

Resources are automatically tagged using the tags defined by ``rhelai_azure_tags`` variable.
The ``rhelai_azure_tags`` variable can be defined in your variable file.

This playbook includes the following roles:

 - **[cloud.azure_ops.azure_manage_resource_group](https://github.com/redhat-cop/cloud.azure_ops/tree/main/roles/azure_manage_resource_group)**
 - **[cloud.azure_ops.azure_virtual_machine_with_public_ip](https://github.com/redhat-cop/cloud.azure_ops/tree/main/roles/azure_virtual_machine_with_public_ip)**

#### Example Usage

Ensure Azure credentials are configured and necessary variables are defined before execution.

```shell
ansible-playbook infra.ai.azure_provision -i localhost, -e @sample_vars.yml
```

### Azure Teardown Playbook: infra.ai.azure_teardown

This playbook decommissions all infrastructure previously provisioned via the infra.ai.azure_provision playbook.

This playbook uses the following roles:
 - **[cloud.azure_ops.azure_manage_resource_group](https://github.com/redhat-cop/cloud.azure_ops/tree/main/roles/azure_manage_resource_group)**
 - **[cloud.azure_ops.azure_virtual_machine_with_public_ip](https://github.com/redhat-cop/cloud.azure_ops/tree/main/roles/azure_virtual_machine_with_public_ip)**

#### Example Usage

Ensure Azure credentials are configured and necessary variables are defined before execution.

```shell
ansible-playbook infra.ai.azure_teardown -i localhost, -e @sample_vars.yml
```
