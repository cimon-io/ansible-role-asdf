[![Build Status](https://travis-ci.org/cimon-io/ansible-role-asdf.svg?branch=master)](https://travis-ci.org/cimon-io/ansible-role-asdf)

# Ansible ASDF role

An Ansible Role that installs [asdf](https://github.com/asdf-vm/asdf.git) version manager with plugins.

## Requirements

None

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`). The variable `asdf_plugins` specifies a list of plugins to install:

```yaml
asdf_plugins: []
```

Each plugin can be given in the following format:

```yaml
asdf_plugins:
  - name: "erlang"    # a plugin name
    repository: ""    # a plugin repository, optional
    versions:         # a list of versions to install
      - 18.3
      - 20.1
    global: 20.1      # set as a global version, optional
```

The variable `asdf_user` sets a user for which the role is installed:

```yaml
asdf_user: "deploy"
```

By default the role installs `asdf` and its plugins in the `~/.asdf` for this
user. This behaviour can be changed by setting `asdf_dir`. This is useful in
situations where multiple users need access to installed plugins and tools (e.g.
a deploy user, the app user, and possibly developer users).

```yaml
asdf_dir: "/opt/asdf-vm"
```

The variable `asdf_legacy_version_file` specifies if plugins which support this feature should read the version files used by other version managers (e.g. `.ruby-version` in the case of Ruby's rbenv).

```yaml
asdf_legacy_version_file: "yes"
```

The variable `asdf_plugin_dependencies` sets packages which are needed for plugins (see `defaults/main.yml`):

```yaml
asdf_plugin_dependencies: []
```

The variable `asdf_version` sets the git tag of asdf:

```yaml
asdf_version: v0.9.0
```

## Dependencies

None

## Example Playbook

Playbook example is given below:

```yaml
- hosts: web
  roles:
  - role: ansible-role-asdf
    asdf_plugins:
    - name: "erlang"
      versions: ["18.3", "20.1"]
      global: "20.1"
    - name: "elixir"
      versions: "1.3.1"
```

A more complex example for CentOS is:

```yaml
- name: install asdf
  hosts: '*'
  become: true
  vars:
    asdf_version: v0.6.2
    asdf_user: ci
    asdf_plugins:
      - name: erlang
      - name: elixir
      - name: nodejs
        versions: ["8.11.3"]
        global: "8.11.3"
  roles:
    - asdf
```

Installing asdf into a shared directory accessible to the `developers` group:

```yaml
- name: install asdf
  hosts: '*'
  become: true
  vars:
    asdf_user: deploy
    asdf_group: developers
    asdf_dir: /opt/asdf-vm
    asdf_plugins:
      - name: erlang
      - name: elixir
      - name: nodejs
        versions: ["8.11.3"]
        global: "8.11.3"
  roles:
    - asdf
```

## License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).
