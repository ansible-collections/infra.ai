# infra.ai playbooks

## AWS playbooks

These playbooks are designed to orchestrate AWS infrastructure in support of RHEL AI environments:

- Provision – Launch and configure AWS instances required for your RHEL AI deployment.
- Teardown – Safely remove all provisioned resources to ensure a clean shutdown of the environment.

## Proxy playbook

This playbook sets up a reverse NGINX proxy, capable of handling:

- Self-signed certificates
- Custom certificate files
- Certificates issued by Let's Encrypt

It installs all required dependencies and runs the proxy inside a Podman container. The proxy forwards requests to the deployed ``instructlab`` service.
