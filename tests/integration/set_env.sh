#!/bin/sh

for i in tests/integration/targets/*; do
    if [ ! -d "$i" ]; then
        continue
    fi

    cat <<EOF >> "${i}/defaults/main.yml"
aws_access_key: ${AWS_ACCESS_KEY_ID}
aws_secret_key: ${AWS_SECRET_ACCESS_KEY}
aws_region: ${AWS_REGION}
EOF

    cat <<EOF >> "${i}/rhelai.aws_ec2.yml"
aws_access_key_id: ${AWS_ACCESS_KEY_ID}
aws_secret_access_key: ${AWS_SECRET_ACCESS_KEY}
aws_region: ${AWS_REGION}
EOF
done

