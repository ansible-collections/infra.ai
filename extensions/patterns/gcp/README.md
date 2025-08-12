# GCP pattern for Ansible infra.ai collection

## Description

The pattern can provision or teardown RHEL AI on GCP.

## Usage

Pattern includes two playbooks:

- run_gcp_provision.yml will provision infrastructure
- run_gcp_teardown.yml will teardown infrustructure.

Parameters are documented in respective `<playbook>.meta.yml` files.

Before running the playbooks AAP needs to be setup with:
- github.com credential - a token is needed to update AAP project before running it
  - the pattern is part of https://github.com/ansible-collections/infra.ai,
    and this is a private repository.
- container registry credentails - needed to pull EE image
  - currentlly the credential name must be `RHEL Infra AI / EE Image Credential`
- SSH private key corresponding to `rhelai_gcp_key_material`
- GCP inventory
- GCP credentials

## Created AAP resources

Created resources are easily identified as the names begin with `<rhelai_gcp_resource_name>` prefix.
Following resources are created:

- `<rhelai_gcp_resource_name>-instance` - VM instance
- `<rhelai_gcp_resource_name>-disk` - a VM disk
- `<rhelai_gcp_resource_name>-network` - a network
- `<rhelai_gcp_resource_name>-ilab` - a firewall
