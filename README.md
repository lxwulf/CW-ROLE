# CW-ROLE v1.0

![logo](docs/src/logo_cw_role_optimized.svg)

---

`CW-Role v1` is an automation repository build with Ansible. It
installs Nextcloud with your preferred settings from PHP over
Redis until to the Nextcloud settings itself as far as it is
possible and reasonable.

## 💡 Motivation

On my first installation of Nextcloud, I needed to reinstall
it several times because I messed up something. Sure, most
things then were also new for me. Anyway, it was a
time-consuming act to reset and install everything new. Yes,
today I know more and a better way to reset Nextcloud, but
then I didn't know that.

So I thought can I or better say how can I automate this
procedure. It occurred to me: There is something called
Ansible. This tool was already on my list for review and
learning it. The timing was never better, and so the journey
began.

## ⚙️ Features

There are already some repositories with automated
installation of Nextcloud. Most of them are only the Nextcloud
installation itself with Apache and Ubuntu as base system –
which I don't like, especially Ubuntu.

I try to be more focused on update reliability and security.
So I decided to use `Fedora Server` with activated `SELinux`.
Fedora Server can be updated frequently with new recent
updates and even can be upgraded to the next release version
with an inbuilt mechanic.

**TLDR chosen OS:**

- Fedora Server
- Regular Updates of the System
- SELinux activated
- Stable

I tried to find a good way between performance, security and
also stability. So I decided to use `NGINX`, for performance
and efficient. `Redis` for caching and even more performance
boost. `Nextcloud` was decided to use because of the feature
rich environment they have. Also, you can decide if you want
to have the full-fledged O365 replacement or just a cloud
server.
As database backend, I use `PostgreSQL 14` because it's also very
fast and can be exactly configured to your needs. To handle
the dynamic sites part of `Nextcloud`, I use `PHP 8.1`.

**TLDR chosen stack (LNPP):**

- NGINX for performance
- Redis for even more performance boost
- Nextcloud feature-rich cloud environment
- PostgreSQL for a reliable and fast database
- PHP 8.1 to handle the dynamic sites

## 🧰 Prerequisites

- Fedora Linux (Server)
- Ansible
- Base Knowledge about Ansible would be advantageous
- No fear from the command line

## 🏗️ Configuration

Luckily, you only need to focus on two files.

1st is in:

`CW-ROLE/vars/main/task_vars/task_variable_list.yml`

2nd is in:

`CW-ROLE/vars/main/template_vars/template_variable_list.yml`

The explanations of the variables are documented in the files
itself. Here are direct links to it:

[1st: task_variable_list.yml](CW-ROLE/vars/main/task_vars/task_variable_list.yml)

[2nd: template_variable_list.yml](CW-ROLE/vars/main/task_vars/task_variable_list.yml)

Do not forget to add the `hostname` or `ip adress` of
`your host` you want to install `CW-Role`. You can do this in the [hosts](hosts) file, which is in the root directory of the project.

Example:

```bash
[groupname]
192.168.1.13
192.168.1.37

[groupname2]
pro-cw-01
dev-cw-02
```

## ▶️ How to Execute

For execute the playbook you require, `ansible` installed, sure.

Keep in mind your `Ansible` machine OS doesn't matter that
much, in turn, of the remote host, this should be `Fedora
Linux`, else the playbook will not work.

```bash
# Fedora and other Red Hat derivates

dnf install ansible ansible-core

# Debian and friends like Ubuntu

apt install ansible ansible-core
```

If it's not available on your distribution, or it is a very old
version, you can install it also with `pip` which I recommend doing it.

```bash
pip install ansible ansible-core
```

After the installation, you can execute the playbook with the
following command:

```bash
ansible-playbook cw-role_playbook.yml
```

## 🗂️ Credits

**Tool:**

- [Ansible](https://github.com/ansible/ansible)

**Software:**

- [Fedora Linux](https://getfedora.org/)
- [Nextcloud](https://github.com/nextcloud/server)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [NGINX](https://www.nginx.com/)

**Contributions:**

- [LxWulf](https://github.com/lxwulf)

## License

MIT © [LxWulf](https://github.com/lxwulf)
