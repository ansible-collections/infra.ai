# infra.ai.aws_orchestration.provision playbook

A playbook to support provisioning AWS EC2 instances to host RHELAI AMI images. It automates the setup of:

- Key pairs
- VPC and associated networking resources
- Security groups
- EC2 instance launch

All resources created are prefixed using the ``rhelai_aws_resource_name`` variable, which can be configured in your variable file.

This playbook includes the following roles:

 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**


## Example Usage

Before running the playbook, ensure your AWS credentials are properly configured and variables are set.

Run the playbook with:

```shell
ansible-playbook infra.ai.aws_orchestration.provision -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
