#!/usr/bin/env bash

set -eu

function cleanup {
    ansible-playbook infra.ai.aws_teardown -i rhelai.aws_ec2.yml -e @defaults/main.yml
    unset ANSIBLE_CACHE_PLUGIN
    unset ANSIBLE_CACHE_PLUGIN_CONNECTION
}

trap 'cleanup "$@"' EXIT

# test infrastructure pre-orchestration
ansible-playbook test_infra.yml -i rhelai.aws_ec2.yml -e @defaults/main.yml -e action=pre

# provision the infrastructure
ansible-playbook infra.ai.aws_provision -i rhelai.aws_ec2.yml -e @defaults/main.yml

# test infrastructure post-orchestration
ansible-playbook test_infra.yml -i rhelai.aws_ec2.yml -e @defaults/main.yml -e action=post
