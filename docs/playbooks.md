# infra.ai playbooks

## AWS Orchestration for RHEL AI

The ``infra.ai`` AWS playbooks provide automation for provisioning and managing cloud infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments. The suite includes the following key playbooks:

- Provision – Launches and configures AWS resources needed to deploy RHEL AI.
- Teardown – Destroys provisioned resources to ensure a clean and complete shutdown.
- Proxy – Sets up an NGINX reverse proxy with SSL support for secure request forwarding.

### Provisioning Playbook: infra.ai.provision

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
ansible-playbook infra.ai.aws_provision -i rhelai.aws_ec2.yml -e @aws_sample_vars.yml
```

### Teardown Playbook: infra.ai.teardown

This playbook decommissions all infrastructure previously provisioned via the infra.ai.provision playbook. It is also integrated into test workflows to ensure clean-up during failures or post-integration testing.

This playbook uses the following roles:
 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.manage_ec2_instance](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/manage_ec2_instance)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**

#### Example Usage

Ensure AWS credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.aws_teardown -i rhelai.aws_ec2.yml -e @aws_sample_vars.yml
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
ansible-playbook infra.ai.proxy -i rhelai.aws_ec2.yml -e @aws_sample_vars.yml
```

## Baremetal Orchestration for RHEL AI

The ``infra.ai`` baremetal playbooks provide automation for provisioning and managing baremetal infrastructure in support of Red Hat Enterprise Linux AI (RHEL AI) environments. The suite includes the following key playbooks:

- baremetal_provision.yml – Creates an ISO image. The ISO image is used for provisioning a baremetal host.

### Provisioning Playbook: infra.ai.baremetal_provision

This playbook automates the creation of an ISO image for for provisioning a baremetal host.

Before running the playbook:
 - RHAI ISO image needs to be downloaded.
   It is available at ()[].
 - Container registry credentials for pulling RHAI updates needs to be created.
   Generate them at https://access.redhat.com/RegistryAuthentication.

#### Example Usage

Ensure container registry credentials are configured and necessary variables are defined before execution.

Run the playbook with:

```shell
ansible-playbook infra.ai.baremetal_provision -e @baremetal_sample_vars.yml
```
