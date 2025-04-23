# infra.ai.proxy.proxy playbook

This playbook sets up all necessary components on the target node to run a reverse NGINX proxy. It supports both self-signed certificates and automated certificate provisioning using Let's Encrypt.

This playbook relies on the following role:

- **infra.ai.nginx_proxy**

## Example Usage

Before running the playbook, ensure your AWS credentials are properly configured and variables are set.

Run the playbook with:

```shell
ansible-playbook infra.ai.proxy.proxy -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
