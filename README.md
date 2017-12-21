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
    versions:         # a list of versions to install
      - 18.3
      - 20.1
    global: 20.1      # set as a global version, optional
```

The variable `asdf_user` sets a user for which the role is installed:

```yaml
asdf_user: "deploy"
```

The variable `asdf_legacy_version_file` specifies if plugins which support this feature should read the version files used by other version managers (e.g. `.ruby-version` in the case of Ruby's rbenv).

```yaml
asdf_legacy_version_file: "yes"
```

To set additional plugin dependencies, use the variable `asdf_plugin_dependencies` (see `vars/main.yml`):

```yaml
asdf_plugin_dependencies: []
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

## License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).
