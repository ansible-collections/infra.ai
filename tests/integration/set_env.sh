#!/bin/sh

set -eu

if [ -f "/home/runner/work/infra.ai/infra.ai/$AWS_CONFIG_FILE" ]; then
    echo "Copying cloud-config-aws.ini to ansible collection directory"
    cp "/home/runner/work/infra.ai/infra.ai/$AWS_CONFIG_FILE" ./tests/integration
fi

# generate a temporary file for the GCP tests cancelling
touch ./tests/integration/targets/test_infra_gcp/.github_runner
