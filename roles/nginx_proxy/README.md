# nginx_proxy

A role to create nginx reverse proxy with optional Let's Encrypt TLS certificates.

## Requirements

- The target instance must be running a service on a specified port (default is 8000), which NGINX will proxy requests to.
- The role supports both Let's Encrypt certificates and self-signed certificates out of the box.

## Role Variables

- **nginx_proxy_fqdn**: Fully-qualified domain name for the nginx proxy service, also the domain for which the Let's Encrypt TLS cert to be fetched (if enabled).
- **nginx_proxy_install_dir**: Installation directory for the NGINX proxy.
- **nginx_proxy_tls_organization_name**: Organization name to use when generating self-signed certificates.

## Example Playbook

```yaml
    ---
    - hosts: localhost
      roles:
        - role: infra.ai.nginx_proxy
          nginx_proxy_fqdn: rp.example.com
          nginx_proxy_install_dir: /home/ec2-user
          nginx_proxy_tls_organization_name: ACME Inc.
```

## License

GNU General Public License v3.0 or later

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information

- Peter Grlica (pgrlica@redhat.com)
