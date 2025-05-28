#!/usr/bin/env bash

set -eu

function cleanup {
    e=$?

    ansible-playbook infra.ai.aws_teardown -e @defaults/main.yml
    unset ANSIBLE_CACHE_PLUGIN
    unset ANSIBLE_CACHE_PLUGIN_CONNECTION

    if [[ -n "${GITHUB_ACTIONS+x}" ]]; then
        exit $e
    fi

    ansible-playbook infra.ai.gcp_teardown -e @defaults/main.yml
}

trap 'cleanup "$@"' EXIT

# test infrastructure pre-orchestration
ansible-playbook test_infra.yml -i rhelai.aws_ec2.yml -e @defaults/main.yml -e action=pre

# provision the infrastructure
ansible-playbook infra.ai.aws_provision -i rhelai.aws_ec2.yml -e @defaults/main.yml

# test infrastructure post-orchestration
ansible-playbook test_infra.yml -i rhelai.aws_ec2.yml -e @defaults/main.yml -e action=post

if [[ -n "${GITHUB_ACTIONS+x}" ]]; then
    exit 0
fi

# test infrastructure pre-orchestration
ansible-playbook test_gcp_infra.yml -e @defaults/main.yml -e action=pre -e rhelai_gcp_service_account_file=service-account.json

# provision the Google Cloud infrastructure
ansible-playbook infra.ai.gcp_provision -e @defaults/main.yml

# test infrastructure post-orchestration
ansible-playbook test_gcp_infra.yml -e @defaults/main.yml -e action=post -e rhelai_gcp_service_account_file=service-account.json
