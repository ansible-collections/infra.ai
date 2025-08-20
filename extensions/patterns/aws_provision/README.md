# AWS pattern for Ansible infra.ai collection

## Description

The pattern can provision or teardown RHEL AI on AWS.

## Usage

Pattern includes two playbooks:

- run_aws_provision.yml will provision infrastructure
- run_aws_teardown.yml will teardown infrustructure.

Parameters are documented in respective `<playbook>.meta.yml` files.

Before running the playbooks AAP needs to be setup with:
- github.com credential - a token is needed to update AAP project before running it
  - the pattern is part of https://github.com/ansible-collections/infra.ai,
    and this is a private repository.
- container registry credentials - needed to pull EE image
  - currentlly the credential name must be `RHEL Infra AI / EE Image Credential`
- SSH private key corresponding to `rhelai_aws_key_material`
- AWS inventory
- AWS credentials

## Created AAP resources

Following resources are created:

- `<rhelai_aws_resource_name>-instance` - EC2 instance
- SSH key pair:
  - `<rhelai_aws_key_name>` if `rhelai_aws_key_name` is specifed
  - `<rhelai_aws_resource_name>-key` otherwise
- `<rhelai_aws_resource_name>-vpc` - VPC
- `<rhelai_aws_subnet_cidr>` - VPC subnet
- `<rhelai_aws_resource_name>-sg>` - security group
