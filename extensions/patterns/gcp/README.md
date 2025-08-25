# GCP pattern for Ansible infra.ai collection

## Description

The pattern can provision or teardown RHEL AI on GCP.

## Usage

Pattern includes two playbooks:

- run_gcp_provision.yml will provision infrastructure
- run_gcp_teardown.yml will teardown infrustructure.

Parameters are documented in respective `<playbook>.meta.yml` files.

Before running the playbooks AAP needs to be setup with:
- build EE image and push it to your private automation hub.
  Image name needs to be `infra/infra-ai-ee:latest`.
- SSH private key corresponding to `rhelai_gcp_key_material`
- GCP inventory
- GCP credentials

## Created AAP resources

Pattern will create resources in AAP:

- Controller execution environment:
  - infra-ai-ee
- Controller labels:
  - infra_ai
  - infra_pattern
  - run_gcp_provision
  - run_gcp_teardown
- Controller project
  - RHEL Infra AI / Project
- Controller job templates
  - RHEL Infra AI / Provision GCP
  - RHEL Infra AI / Teardown GCP
