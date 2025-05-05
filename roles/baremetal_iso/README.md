# nginx_proxy

A role to create ISO image for automated Red Hat AI installation on baremetal host.

## Requirements

- The source ISO image needs to be downloaded beforehand.
- The `mkksiso` program is required. Install it using `sudo dnf install lorax`.

## Role Variables

- **baremetal_iso_source_image**: Path to source Red Hat AI ISO image. Download it at https://developers.redhat.com/products/rhel-ai/download.
- **baremetal_iso_unique_name**: The string will be included into output ISO filename. Use it to generate unique ISO images for multiple hosts.
- **baremetal_iso_root_password_plain**: Root user password.
- **baremetal_iso_root_ssh_key**: Root user SSH public key.
- **baremetal_iso_username**: Unprivileged user username.
- **baremetal_iso_password_plain**: Unprivileged user password.
- **baremetal_iso_ssh_key**: Unprivileged user SSH public key.
- **baremetal_iso_registry_username**: Username for downloading OS updates. Generate it at https://access.redhat.com/RegistryAuthentication.
- **baremetal_iso_registry_password**: Password for downloading OS updates.
- **baremetal_iso_registry_host**: Registry containing OS updates.
- **baremetal_iso_oci_image**: The image to download as an OS update.

## Return Values

- **baremetal_iso_image**: Path to generated ISO image.

## Example Playbook

```yaml
---
- name: Provision baremetal infrastructure
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Remaster RHEL AI source ISO image
      ansible.builtin.include_role:
        name: infra.ai.baremetal_iso
      vars:
        baremetal_iso_root_password_plain: "TODO"
        baremetal_iso_ssh_key: "ssh-ed25519 AAAAC3N..."
        baremetal_iso_registry_username: "1234567|description"
        baremetal_iso_registry_password: "TODO"
        baremetal_iso_source_image: "/path/to/rhel-ai-nvidia-1.4-1739107830-x86_64-boot.iso"
        # optional static network configuration
        baremetal_iso_network_mode: static
        baremetal_iso_network_address: 192.168.122.10
        baremetal_iso_network_netmask: 255.255.255.0
        baremetal_iso_network_gateway: 192.168.122.1
```

## License

GNU General Public License v3.0 or later

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Justin Cinkelj (@justinc1)
