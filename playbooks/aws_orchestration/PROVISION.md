# infra.ai.aws_orchestration.provision playbook

A playbook to support provisioning AWS EC2 instances to host RHELAI AMI images.

It orchestrates key generation, VPC and security groups as well as EC2 instance.
All the resources created are prepended with `rhelai_aws_resource_name` variable, see more at [sample_vars.yml](../../sample_vars.yml).

This playbook uses the following roles:
 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**

The following collections are used as well:
 - **[amazon.aws](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)**

## Example Usage

Follow [README](../../README.md) on setting up AWS credentials.

```shell
ansible-playbook infra.ai.aws_orchestration.provision -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
