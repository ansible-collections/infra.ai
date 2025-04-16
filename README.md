# infra.ai Content Collection
<!-- Add CI and code coverage badges here. Samples included below. -->
[![CI](https://github.com/ansible-collections/REPONAMEHERE/workflows/CI/badge.svg?event=push)](https://github.com/ansible-collections/REPONAMEHERE/actions) [![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/REPONAMEHERE)](https://codecov.io/gh/ansible-collections/REPONAMEHERE)

## Description
This collection is curated to provide users with a robust set of roles, playbooks, and rulebooks that simplify and streamline AWS infrastructure operations related to RHEL AI.

## Installation

```shell
$ ansible-galaxy collection install -r requirements.yml
```

## Usage

### Setting up aws-related settings

Set your dev env:
```shell
# using the "default" profile on AWS
aws configure set aws_access_key_id     my-access-key
aws configure set aws_secret_access_key my-secret-key
aws configure set region                eu-central-1

ansible-test integration [target]
```

#### Setup variables

```shell
$ cp sample_vars.yml vars.yml
```

#### Dev orchestration and teardown
```shell
# up
$ ansible-playbook playbooks/aws_orchestration/provision.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml

# down
$ ansible-playbook playbooks/aws_orchestration/teardown.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml

# display inventory
$ ansible-inventory -i inventory/rhelai.aws_ec2.yml --graph

# install nginx proxy
$ ansible-playbook playbooks/proxy/proxy.yml -i inventory/rhelai.aws_ec2.yml -e @vars.yml
```

## Testing

### Integration

```shell
$ ansible-test integration
```

## More information

<!-- List out where the user can find additional information, such as working group meeting times, slack/IRC channels, or documentation for the product this collection automates. At a minimum, link to: -->

- [Ansible user guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible collections requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html)
- [Ansible community Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible contributor newsletter)](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)
- [Important announcements for maintainers](https://github.com/ansible-collections/news-for-maintainers)

## Licensing

<!-- Include the appropriate license information here and a pointer to the full licensing details. If the collection contains modules migrated from the ansible/ansible repo, you must use the same license that existed in the ansible/ansible repo. See the GNU license example below. -->

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
