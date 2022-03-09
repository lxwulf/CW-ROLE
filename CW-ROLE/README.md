# CW-ROLE_v0.1.0

This is the role for automated installation of Nextcloud.
The role setup Nextcloud with `PHP 7.4`, `PostgresSQL 13.4` and `firewall-cmd`.
At the end, you should have a working, secured cloud server with the logins you defined in the variables.

## Requirements

- Linux OS like Fedora, RHEL or CentOS. (Tested only with Fedora)
- Ansible
- Ansible-Core
- Ansible-Lint (Optional)
- Code Editor of your choice (ex. VSCodium)
- Base knowledge about ansible (like managining templates or variables)

## Role Variables

The role variables for the different tasks and configurations are in `CW-ROLE_v0.1.0/vars/j2_vars`, `CW-ROLE_v0.1.0/vars/task_vars`
and in the root folder of `CW-ROLE_v0.1.0/vars`.

## Dependencies

There are no dependencies. All special modules should be provided by ansible itself.
Despite that there are some community functions from ansible-galaxy. There mostly installed
when you install `ansible` itself and `ansible-core`.

## Author Information

### [Github Profile](https://github.com/lxwulf)
