# infra.ai playbooks

## AWS playbooks

Playbooks to orchestrate AWS instances in order to facilitate RHELAI infrastructure:

 - [aws provision](./aws_orchestration/PROVISION.md)
 - [aws teardown](./aws_orchestration/TEARDOWN.md)

## Proxy playbook

The reverse nginx proxy that handles either self-signed certificates,
own certificate files or Let's encrypt downloaded ones.

Playbook installs necessary dependencies and runs the nginx proxy in a
podman containerized environment, that proxies the requests to the
installed `instructlab` software.

See more: [proxy playbook](./proxy/README.md)
