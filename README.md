ASDF role
=========

An Ansible Role that installs [asdf](https://github.com/asdf-vm/asdf.git) version manager with plugins.

Requirements
----------------

None.

Role Variables
----------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```
asdf_plugins: []
```

List of plugins to install.

Dependencies
----------------

None.

Example Playbook
----------------

Example:

```yaml
- hosts: web
  roles:
  - role: asdf
    asdf_plugins:
    - name: "erlang"
      versions:
      - 18.3
      - 20.1
      global: 20.1
    - name: "elixir"
      versions: 1.3.1
```

License
-------

MIT

