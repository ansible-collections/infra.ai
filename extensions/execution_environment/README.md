# Execution Environment

EE for running this collection in AAP.

File `ansible.cfg` should contain URL and token for automation hub.
Get token for automation hub at https://console.redhat.com/ansible/automation-hub/token.
Also setup access to container registry where EE image will be pushed.

```bash
cd extensions/execution_environment
cp -i context/configs/sample-ansible.cfg context/configs/ansible.cfg
nano context/configs/ansible.cfg
cp -i secrets.yml.template secrets.yml
nano secrets.yml
```

To build this EE:

```bash
ansible-galaxy collection install infra.ee_utilities
pip install ansible-builder
ansible-playbook -e @secrets.yml build_ee.yml # -e ee_image_push=false
```
