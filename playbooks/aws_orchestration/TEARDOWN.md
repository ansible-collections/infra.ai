# infra.ai.aws_orchestration.teardown playbook

This playbook tears down the provisioned EC2 instances and related AWS infrastructure.
It is also used during integration testing to clean up resources if a failure occurs.

This playbook uses the following roles:
 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.manage_ec2_instance](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/manage_ec2_instance)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**

## Example Usage

Before running the playbook, ensure your AWS credentials are properly configured and variables are set.

Run the playbook with:

```shell
ansible-playbook infra.ai.aws_orchestration.teardown -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
