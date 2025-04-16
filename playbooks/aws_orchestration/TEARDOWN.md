# infra.ai.aws_orchestration.teardown playbook

Teardown the provisioned EC2 instance and accompanying resources.
Is used in integration tests on failure as well (as a cleanup). See more at [runme.sh](../../tests/integration/targets/test_nginx_proxy/runme.sh).

This playbook uses the following roles:
 - **[cloud.aws_ops.aws_setup_credentials](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/aws_setup_credentials)**
 - **[cloud.aws_ops.manage_ec2_instance](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/manage_ec2_instance)**
 - **[cloud.aws_ops.ec2_networking_resources](https://github.com/redhat-cop/cloud.aws_ops/tree/main/roles/ec2_networking_resources)**

The following collections are used as well:
 - **[amazon.aws](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)**

## Example Usage

Follow [README](../../README.md) on setting up AWS credentials.

```shell
ansible-playbook infra.ai.aws_orchestration.teardown -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
