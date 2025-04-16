# infra.ai.proxy.proxy playbook

A playbook that installs necessary requirements on the target node to run a reverse proxy with the self-signed certificates or Letsencrypt support.

This playbook uses the following roles:
 - **[infra.ai.nginx_proxy](../../roles/nginx_proxy/README.md)**

## Example Usage

Follow [README](../../README.md) on setting up AWS credentials.

```shell
ansible-playbook infra.ai.proxy.proxy -i rhelai.aws_ec2.yml -e @sample_vars.yml
```
