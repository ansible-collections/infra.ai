#!/usr/bin/env bash

set -eu

if [[ -f .github_runner ]]; then
    echo "Running GCP tests on GH actions currently unsupported. Exiting."
    exit 0
fi

function cleanup {
    ansible-playbook infra.ai.gcp_teardown -e @defaults/main.yml -e rhelai_gcp_service_account_file=../service-account.json
    unset ANSIBLE_CACHE_PLUGIN
    unset ANSIBLE_CACHE_PLUGIN_CONNECTION
}

trap 'cleanup "$@"' EXIT

# test infrastructure pre-orchestration
ansible-playbook test_infra.yml -e @defaults/main.yml -e action=pre -e rhelai_gcp_service_account_file=service-account.json

# provision the Google Cloud infrastructure
ansible-playbook infra.ai.gcp_provision -e @defaults/main.yml -e rhelai_gcp_service_account_file=../service-account.json

# test infrastructure post-orchestration
ansible-playbook test_infra.yml -e @defaults/main.yml -e action=post -e rhelai_gcp_service_account_file=service-account.json
