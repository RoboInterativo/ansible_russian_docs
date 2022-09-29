.. _ansible_configuration_settings:

==============================
Ansible Configuration Settings
==============================

Ansible supports several sources for configuring its behavior, including an ini file named ``ansible.cfg``, environment variables, command-line options, playbook keywords, and variables. See :ref:`general_precedence_rules` for details on the relative precedence of each source.

The ``ansible-config`` utility allows users to see all the configuration settings available, their defaults, how to set them and
where their current value comes from. See :ref:`ansible-config` for more information.

.. _ansible_configuration_settings_locations:

The configuration file
======================

Changes can be made and used in a configuration file which will be searched for in the following order:

 * ``ANSIBLE_CONFIG`` (environment variable if set)
 * ``ansible.cfg`` (in the current directory)
 * ``~/.ansible.cfg`` (in the home directory)
 * ``/etc/ansible/ansible.cfg``

Ansible will process the above list and use the first file found, all others are ignored.

.. note::

   The configuration file is one variant of an INI format.
   Both the hash sign (``#``) and semicolon (``;``) are allowed as
   comment markers when the comment starts the line.
   However, if the comment is inline with regular values,
   only the semicolon is allowed to introduce the comment.
   For instance::

        # some basic default values...
        inventory = /etc/ansible/hosts  ; This points to the file that lists your hosts


.. _cfg_in_world_writable_dir:

Avoiding security risks with ``ansible.cfg`` in the current directory
---------------------------------------------------------------------


If Ansible were to load ``ansible.cfg`` from a world-writable current working
directory, it would create a serious security risk. Another user could place
their own config file there, designed to make Ansible run malicious code both
locally and remotely, possibly with elevated privileges. For this reason,
Ansible will not automatically load a config file from the current working
directory if the directory is world-writable.

If you depend on using Ansible with a config file in the current working
directory, the best way to avoid this problem is to restrict access to your
Ansible directories to particular user(s) and/or group(s). If your Ansible
directories live on a filesystem which has to emulate Unix permissions, like
Vagrant or Windows Subsystem for Linux (WSL), you may, at first, not know how
you can fix this as ``chmod``, ``chown``, and ``chgrp`` might not work there.
In most of those cases, the correct fix is to modify the mount options of the
filesystem so the files and directories are readable and writable by the users
and groups running Ansible but closed to others.  For more details on the
correct settings, see:

* for Vagrant, Jeremy Kendall's `blog post <http://jeremykendall.net/2013/08/09/vagrant-synced-folders-permissions/>`_ covers synced folder permissions.
* for WSL, the `WSL docs <https://docs.microsoft.com/en-us/windows/wsl/wsl-config#set-wsl-launch-settings>`_
  and this `Microsoft blog post <https://blogs.msdn.microsoft.com/commandline/2018/01/12/chmod-chown-wsl-improvements/>`_ cover mount options.

If you absolutely depend on storing your Ansible config in a world-writable current
working directory, you can explicitly specify the config file via the
:envvar:`ANSIBLE_CONFIG` environment variable. Please take
appropriate steps to mitigate the security concerns above before doing so.


Relative paths for configuration
--------------------------------

You can specify a relative path for many configuration options. In most of
those cases the path used will be relative to the ``ansible.cfg`` file used
for the current execution. If you need a path relative to your current working
directory (CWD) you can use the ``{{CWD}}`` macro to specify
it. We do not recommend this approach, as using your CWD as the root of
relative paths can be a security risk. For example:
``cd /tmp; secureinfo=./newrootpassword ansible-playbook ~/safestuff/change_root_pwd.yml``.


Common Options
==============

This is a copy of the options available from our release, your local install might have extra options due to additional plugins,
you can use the command line utility mentioned above (`ansible-config`) to browse through those.



.. _ACTION_WARNINGS:

ACTION_WARNINGS
---------------

:Description: By default Ansible will issue a warning when received from a task action (module or action plugin) These warnings can be silenced by adjusting this setting to False.
:Type: boolean
:Default: True
:Version Added: 2.5
:Ini:
     :Section: [defaults]
     :Key: action_warnings
:Environment:
     :Variable: :envvar:`ANSIBLE_ACTION_WARNINGS`

.. _AGNOSTIC_BECOME_PROMPT:

AGNOSTIC_BECOME_PROMPT
----------------------

:Description: Display an agnostic become prompt instead of displaying a prompt containing the command line supplied become method
:Type: boolean
:Default: True
:Version Added: 2.5
:Ini:
     :Section: [privilege_escalation]
     :Key: agnostic_become_prompt
:Environment:
     :Variable: :envvar:`ANSIBLE_AGNOSTIC_BECOME_PROMPT`

.. _ALLOW_WORLD_READABLE_TMPFILES:

ALLOW_WORLD_READABLE_TMPFILES
-----------------------------

:Description: This makes the temporary files created on the machine to be world readable and will issue a warning instead of failing the task. It is useful when becoming an unprivileged user.
:Type: boolean
:Default: False
:Version Added: 2.1
:Ini:
     :Section: [defaults]
     :Key: allow_world_readable_tmpfiles

.. _ANSIBLE_CONNECTION_PATH:

ANSIBLE_CONNECTION_PATH
-----------------------

:Description: Specify where to look for the ansible-connection script. This location will be checked before searching $PATH. If null, ansible will start with the same directory as the ansible script.
:Type: path
:Default: None
:Version Added: 2.8
:Ini:
     :Section: [persistent_connection]
     :Key: ansible_connection_path
:Environment:
     :Variable: :envvar:`ANSIBLE_CONNECTION_PATH`

.. _ANSIBLE_COW_PATH:

ANSIBLE_COW_PATH
----------------

:Description: Specify a custom cowsay path or swap in your cowsay implementation of choice
:Type: string
:Default: None
:Ini:
     :Section: [defaults]
     :Key: cowpath
:Environment:
     :Variable: :envvar:`ANSIBLE_COW_PATH`

.. _ANSIBLE_COW_SELECTION:

ANSIBLE_COW_SELECTION
---------------------

:Description: This allows you to chose a specific cowsay stencil for the banners or use 'random' to cycle through them.
:Default: default
:Ini:
     :Section: [defaults]
     :Key: cow_selection
:Environment:
     :Variable: :envvar:`ANSIBLE_COW_SELECTION`

.. _ANSIBLE_COW_WHITELIST:

ANSIBLE_COW_WHITELIST
---------------------

:Description: White list of cowsay templates that are 'safe' to use, set to empty list if you want to enable all installed templates.
:Type: list
:Default: ['bud-frogs', 'bunny', 'cheese', 'daemon', 'default', 'dragon', 'elephant-in-snake', 'elephant', 'eyes', 'hellokitty', 'kitty', 'luke-koala', 'meow', 'milk', 'moofasa', 'moose', 'ren', 'sheep', 'small', 'stegosaurus', 'stimpy', 'supermilker', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader-koala', 'vader', 'www']
:Ini:
     :Section: [defaults]
     :Key: cow_whitelist
:Environment:
     :Variable: :envvar:`ANSIBLE_COW_WHITELIST`

.. _ANSIBLE_FORCE_COLOR:

ANSIBLE_FORCE_COLOR
-------------------

:Description: This options forces color mode even when running without a TTY or the "nocolor" setting is True.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: force_color
:Environment:
     :Variable: :envvar:`ANSIBLE_FORCE_COLOR`

.. _ANSIBLE_NOCOLOR:

ANSIBLE_NOCOLOR
---------------

:Description: This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: nocolor
:Environment:
     :Variable: :envvar:`ANSIBLE_NOCOLOR`

.. _ANSIBLE_NOCOWS:

ANSIBLE_NOCOWS
--------------

:Description: If you have cowsay installed but want to avoid the 'cows' (why????), use this.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: nocows
:Environment:
     :Variable: :envvar:`ANSIBLE_NOCOWS`

.. _ANSIBLE_PIPELINING:

ANSIBLE_PIPELINING
------------------

:Description: Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer. This can result in a very significant performance improvement when enabled. However this conflicts with privilege escalation (become). For example, when using 'sudo:' operations you must first disable 'requiretty' in /etc/sudoers on all managed hosts, which is why it is disabled by default. This options is disabled if ``ANSIBLE_KEEP_REMOTE_FILES`` is enabled.
:Type: boolean
:Default: False
:Ini:
     - :Section: [connection]
       :Key: pipelining
     - :Section: [ssh_connection]
       :Key: pipelining
:Environment:
     - :Variable: :envvar:`ANSIBLE_PIPELINING`
     - :Variable: :envvar:`ANSIBLE_SSH_PIPELINING`

.. _ANSIBLE_SSH_ARGS:

ANSIBLE_SSH_ARGS
----------------

:Description: If set, this will override the Ansible default ssh arguments. In particular, users may wish to raise the ControlPersist time to encourage performance.  A value of 30 minutes may be appropriate. Be aware that if `-o ControlPath` is set in ssh_args, the control path setting is not used.
:Default: -C -o ControlMaster=auto -o ControlPersist=60s
:Ini:
     :Section: [ssh_connection]
     :Key: ssh_args
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_ARGS`

.. _ANSIBLE_SSH_CONTROL_PATH:

ANSIBLE_SSH_CONTROL_PATH
------------------------

:Description: This is the location to save ssh's ControlPath sockets, it uses ssh's variable substitution. Since 2.3, if null, ansible will generate a unique hash. Use `%(directory)s` to indicate where to use the control dir path setting. Before 2.3 it defaulted to `control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r`. Be aware that this setting is ignored if `-o ControlPath` is set in ssh args.
:Default: None
:Ini:
     :Section: [ssh_connection]
     :Key: control_path
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_CONTROL_PATH`

.. _ANSIBLE_SSH_CONTROL_PATH_DIR:

ANSIBLE_SSH_CONTROL_PATH_DIR
----------------------------

:Description: This sets the directory to use for ssh control path if the control path setting is null. Also, provides the `%(directory)s` variable for the control path setting.
:Default: ~/.ansible/cp
:Ini:
     :Section: [ssh_connection]
     :Key: control_path_dir
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_CONTROL_PATH_DIR`

.. _ANSIBLE_SSH_EXECUTABLE:

ANSIBLE_SSH_EXECUTABLE
----------------------

:Description: This defines the location of the ssh binary. It defaults to `ssh` which will use the first ssh binary available in $PATH. This option is usually not required, it might be useful when access to system ssh is restricted, or when using ssh wrappers to connect to remote hosts.
:Default: ssh
:Version Added: 2.2
:Ini:
     :Section: [ssh_connection]
     :Key: ssh_executable
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_EXECUTABLE`

.. _ANSIBLE_SSH_RETRIES:

ANSIBLE_SSH_RETRIES
-------------------

:Description: Number of attempts to establish a connection before we give up and report the host as 'UNREACHABLE'
:Type: integer
:Default: 0
:Ini:
     :Section: [ssh_connection]
     :Key: retries
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_RETRIES`

.. _ANY_ERRORS_FATAL:

ANY_ERRORS_FATAL
----------------

:Description: Sets the default value for the any_errors_fatal keyword, if True, Task failures will be considered fatal errors.
:Type: boolean
:Default: False
:Version Added: 2.4
:Ini:
     :Section: [defaults]
     :Key: any_errors_fatal
:Environment:
     :Variable: :envvar:`ANSIBLE_ANY_ERRORS_FATAL`

.. _BECOME_ALLOW_SAME_USER:

BECOME_ALLOW_SAME_USER
----------------------

:Description: This setting controls if become is skipped when remote user and become user are the same. I.E root sudo to root.
:Type: boolean
:Default: False
:Ini:
     :Section: [privilege_escalation]
     :Key: become_allow_same_user
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_ALLOW_SAME_USER`

.. _BECOME_PLUGIN_PATH:

BECOME_PLUGIN_PATH
------------------

:Description: Colon separated paths in which Ansible will search for Become Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/become:/usr/share/ansible/plugins/become
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: become_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_PLUGINS`

.. _CACHE_PLUGIN:

CACHE_PLUGIN
------------

:Description: Chooses which cache plugin to use, the default 'memory' is ephimeral.
:Default: memory
:Ini:
     :Section: [defaults]
     :Key: fact_caching
:Environment:
     :Variable: :envvar:`ANSIBLE_CACHE_PLUGIN`

.. _CACHE_PLUGIN_CONNECTION:

CACHE_PLUGIN_CONNECTION
-----------------------

:Description: Defines connection or path information for the cache plugin
:Default: None
:Ini:
     :Section: [defaults]
     :Key: fact_caching_connection
:Environment:
     :Variable: :envvar:`ANSIBLE_CACHE_PLUGIN_CONNECTION`

.. _CACHE_PLUGIN_PREFIX:

CACHE_PLUGIN_PREFIX
-------------------

:Description: Prefix to use for cache plugin files/tables
:Default: ansible_facts
:Ini:
     :Section: [defaults]
     :Key: fact_caching_prefix
:Environment:
     :Variable: :envvar:`ANSIBLE_CACHE_PLUGIN_PREFIX`

.. _CACHE_PLUGIN_TIMEOUT:

CACHE_PLUGIN_TIMEOUT
--------------------

:Description: Expiration timeout for the cache plugin data
:Type: integer
:Default: 86400
:Ini:
     :Section: [defaults]
     :Key: fact_caching_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_CACHE_PLUGIN_TIMEOUT`

.. _COLLECTIONS_PATHS:

COLLECTIONS_PATHS
-----------------

:Description: Colon separated paths in which Ansible will search for collections content.
:Type: pathspec
:Default: ~/.ansible/collections:/usr/share/ansible/collections
:Ini:
     :Section: [defaults]
     :Key: collections_paths
:Environment:
     :Variable: :envvar:`ANSIBLE_COLLECTIONS_PATHS`

.. _COLOR_CHANGED:

COLOR_CHANGED
-------------

:Description: Defines the color to use on 'Changed' task status
:Default: yellow
:Ini:
     :Section: [colors]
     :Key: changed
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_CHANGED`

.. _COLOR_CONSOLE_PROMPT:

COLOR_CONSOLE_PROMPT
--------------------

:Description: Defines the default color to use for ansible-console
:Default: white
:Version Added: 2.7
:Ini:
     :Section: [colors]
     :Key: console_prompt
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_CONSOLE_PROMPT`

.. _COLOR_DEBUG:

COLOR_DEBUG
-----------

:Description: Defines the color to use when emitting debug messages
:Default: dark gray
:Ini:
     :Section: [colors]
     :Key: debug
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_DEBUG`

.. _COLOR_DEPRECATE:

COLOR_DEPRECATE
---------------

:Description: Defines the color to use when emitting deprecation messages
:Default: purple
:Ini:
     :Section: [colors]
     :Key: deprecate
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_DEPRECATE`

.. _COLOR_DIFF_ADD:

COLOR_DIFF_ADD
--------------

:Description: Defines the color to use when showing added lines in diffs
:Default: green
:Ini:
     :Section: [colors]
     :Key: diff_add
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_DIFF_ADD`

.. _COLOR_DIFF_LINES:

COLOR_DIFF_LINES
----------------

:Description: Defines the color to use when showing diffs
:Default: cyan
:Ini:
     :Section: [colors]
     :Key: diff_lines
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_DIFF_LINES`

.. _COLOR_DIFF_REMOVE:

COLOR_DIFF_REMOVE
-----------------

:Description: Defines the color to use when showing removed lines in diffs
:Default: red
:Ini:
     :Section: [colors]
     :Key: diff_remove
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_DIFF_REMOVE`

.. _COLOR_ERROR:

COLOR_ERROR
-----------

:Description: Defines the color to use when emitting error messages
:Default: red
:Ini:
     :Section: [colors]
     :Key: error
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_ERROR`

.. _COLOR_HIGHLIGHT:

COLOR_HIGHLIGHT
---------------

:Description: Defines the color to use for highlighting
:Default: white
:Ini:
     :Section: [colors]
     :Key: highlight
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_HIGHLIGHT`

.. _COLOR_OK:

COLOR_OK
--------

:Description: Defines the color to use when showing 'OK' task status
:Default: green
:Ini:
     :Section: [colors]
     :Key: ok
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_OK`

.. _COLOR_SKIP:

COLOR_SKIP
----------

:Description: Defines the color to use when showing 'Skipped' task status
:Default: cyan
:Ini:
     :Section: [colors]
     :Key: skip
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_SKIP`

.. _COLOR_UNREACHABLE:

COLOR_UNREACHABLE
-----------------

:Description: Defines the color to use on 'Unreachable' status
:Default: bright red
:Ini:
     :Section: [colors]
     :Key: unreachable
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_UNREACHABLE`

.. _COLOR_VERBOSE:

COLOR_VERBOSE
-------------

:Description: Defines the color to use when emitting verbose messages. i.e those that show with '-v's.
:Default: blue
:Ini:
     :Section: [colors]
     :Key: verbose
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_VERBOSE`

.. _COLOR_WARN:

COLOR_WARN
----------

:Description: Defines the color to use when emitting warning messages
:Default: bright purple
:Ini:
     :Section: [colors]
     :Key: warn
:Environment:
     :Variable: :envvar:`ANSIBLE_COLOR_WARN`

.. _COMMAND_WARNINGS:

COMMAND_WARNINGS
----------------

:Description: By default Ansible will issue a warning when the shell or command module is used and the command appears to be similar to an existing Ansible module. These warnings can be silenced by adjusting this setting to False. You can also control this at the task level with the module option ``warn``.
:Type: boolean
:Default: True
:Version Added: 1.8
:Ini:
     :Section: [defaults]
     :Key: command_warnings
:Environment:
     :Variable: :envvar:`ANSIBLE_COMMAND_WARNINGS`

.. _CONDITIONAL_BARE_VARS:

CONDITIONAL_BARE_VARS
---------------------

:Description: With this setting on (True), running conditional evaluation 'var' is treated differently than 'var.subkey' as the first is evaluated directly while the second goes through the Jinja2 parser. But 'false' strings in 'var' get evaluated as booleans. With this setting off they both evaluate the same but in cases in which 'var' was 'false' (a string) it won't get evaluated as a boolean anymore. Currently this setting defaults to 'True' but will soon change to 'False' and the setting itself will be removed in the future. Expect the default to change in version 2.10 and that this setting eventually will be deprecated after 2.12
:Type: boolean
:Default: True
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: conditional_bare_variables
:Environment:
     :Variable: :envvar:`ANSIBLE_CONDITIONAL_BARE_VARS`

.. _CONNECTION_FACTS_MODULES:

CONNECTION_FACTS_MODULES
------------------------

:Description: Which modules to run during a play's fact gathering stage based on connection
:Type: dict
:Default: {'asa': 'asa_facts', 'cisco.asa.asa': 'cisco.asa.asa_facts', 'eos': 'eos_facts', 'arista.eos.eos': 'arista.eos.eos_facts', 'frr': 'frr_facts', 'frr.frr.frr': 'frr.frr.frr_facts', 'ios': 'ios_facts', 'cisco.ios.ios': 'cisco.ios.ios_facts', 'iosxr': 'iosxr_facts', 'cisco.iosxr.iosxr': 'cisco.iosxr.iosxr_facts', 'junos': 'junos_facts', 'junipernetworks.junos.junos': 'junipernetworks.junos.junos_facts', 'nxos': 'nxos_facts', 'cisco.nxos.nxos': 'cisco.nxos.nxos_facts', 'vyos': 'vyos_facts', 'vyos.vyos.vyos': 'vyos.vyos.vyos_facts', 'exos': 'exos_facts', 'extreme.exos.exos': 'extreme.exos.exos_facts', 'slxos': 'slxos_facts', 'extreme.slxos.slxos': 'extreme.slxos.slxos_facts', 'voss': 'voss_facts', 'extreme.voss.voss': 'extreme.voss.voss_facts', 'ironware': 'ironware_facts', 'community.network.ironware': 'community.network.ironware_facts'}
:Ini:
     :Section: [defaults]
     :Key: connection_facts_modules
:Environment:
     :Variable: :envvar:`ANSIBLE_CONNECTION_FACTS_MODULES`

.. _COVERAGE_REMOTE_OUTPUT:

COVERAGE_REMOTE_OUTPUT
----------------------

:Description: Sets the output directory on the remote host to generate coverage reports to. Currently only used for remote coverage on PowerShell modules. This is for internal use only.
:Type: str
:Version Added: 2.9
:Environment:
     :Variable: :envvar:`_ANSIBLE_COVERAGE_REMOTE_OUTPUT`
:Variables:
     :name: `_ansible_coverage_remote_output`

.. _COVERAGE_REMOTE_WHITELIST:

COVERAGE_REMOTE_WHITELIST
-------------------------

:Description: A list of paths for files on the Ansible controller to run coverage for when executing on the remote host. Only files that match the path glob will have its coverage collected. Multiple path globs can be specified and are separated by ``:``. Currently only used for remote coverage on PowerShell modules. This is for internal use only.
:Type: str
:Default: *
:Version Added: 2.9
:Environment:
     :Variable: :envvar:`_ANSIBLE_COVERAGE_REMOTE_WHITELIST`

.. _DEFAULT_ACTION_PLUGIN_PATH:

DEFAULT_ACTION_PLUGIN_PATH
--------------------------

:Description: Colon separated paths in which Ansible will search for Action Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/action:/usr/share/ansible/plugins/action
:Ini:
     :Section: [defaults]
     :Key: action_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_ACTION_PLUGINS`

.. _DEFAULT_ALLOW_UNSAFE_LOOKUPS:

DEFAULT_ALLOW_UNSAFE_LOOKUPS
----------------------------

:Description: When enabled, this option allows lookup plugins (whether used in variables as ``{{lookup('foo')}}`` or as a loop as with_foo) to return data that is not marked 'unsafe'. By default, such data is marked as unsafe to prevent the templating engine from evaluating any jinja2 templating language, as this could represent a security risk.  This option is provided to allow for backwards-compatibility, however users should first consider adding allow_unsafe=True to any lookups which may be expected to contain data which may be run through the templating engine late
:Type: boolean
:Default: False
:Version Added: 2.2.3
:Ini:
     :Section: [defaults]
     :Key: allow_unsafe_lookups

.. _DEFAULT_ASK_PASS:

DEFAULT_ASK_PASS
----------------

:Description: This controls whether an Ansible playbook should prompt for a login password. If using SSH keys for authentication, you probably do not needed to change this setting.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: ask_pass
:Environment:
     :Variable: :envvar:`ANSIBLE_ASK_PASS`

.. _DEFAULT_ASK_VAULT_PASS:

DEFAULT_ASK_VAULT_PASS
----------------------

:Description: This controls whether an Ansible playbook should prompt for a vault password.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: ask_vault_pass
:Environment:
     :Variable: :envvar:`ANSIBLE_ASK_VAULT_PASS`

.. _DEFAULT_BECOME:

DEFAULT_BECOME
--------------

:Description: Toggles the use of privilege escalation, allowing you to 'become' another user after login.
:Type: boolean
:Default: False
:Ini:
     :Section: [privilege_escalation]
     :Key: become
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME`

.. _DEFAULT_BECOME_ASK_PASS:

DEFAULT_BECOME_ASK_PASS
-----------------------

:Description: Toggle to prompt for privilege escalation password.
:Type: boolean
:Default: False
:Ini:
     :Section: [privilege_escalation]
     :Key: become_ask_pass
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_ASK_PASS`

.. _DEFAULT_BECOME_EXE:

DEFAULT_BECOME_EXE
------------------

:Description: executable to use for privilege escalation, otherwise Ansible will depend on PATH
:Default: None
:Ini:
     :Section: [privilege_escalation]
     :Key: become_exe
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_EXE`

.. _DEFAULT_BECOME_FLAGS:

DEFAULT_BECOME_FLAGS
--------------------

:Description: Flags to pass to the privilege escalation executable.
:Default: 
:Ini:
     :Section: [privilege_escalation]
     :Key: become_flags
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_FLAGS`

.. _DEFAULT_BECOME_METHOD:

DEFAULT_BECOME_METHOD
---------------------

:Description: Privilege escalation method to use when `become` is enabled.
:Default: sudo
:Ini:
     :Section: [privilege_escalation]
     :Key: become_method
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_METHOD`

.. _DEFAULT_BECOME_USER:

DEFAULT_BECOME_USER
-------------------

:Description: The user your login/remote user 'becomes' when using privilege escalation, most systems will use 'root' when no user is specified.
:Default: root
:Ini:
     :Section: [privilege_escalation]
     :Key: become_user
:Environment:
     :Variable: :envvar:`ANSIBLE_BECOME_USER`

.. _DEFAULT_CACHE_PLUGIN_PATH:

DEFAULT_CACHE_PLUGIN_PATH
-------------------------

:Description: Colon separated paths in which Ansible will search for Cache Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/cache:/usr/share/ansible/plugins/cache
:Ini:
     :Section: [defaults]
     :Key: cache_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_CACHE_PLUGINS`

.. _DEFAULT_CALLABLE_WHITELIST:

DEFAULT_CALLABLE_WHITELIST
--------------------------

:Description: Whitelist of callable methods to be made available to template evaluation
:Type: list
:Default: []
:Ini:
     :Section: [defaults]
     :Key: callable_whitelist
:Environment:
     :Variable: :envvar:`ANSIBLE_CALLABLE_WHITELIST`

.. _DEFAULT_CALLBACK_PLUGIN_PATH:

DEFAULT_CALLBACK_PLUGIN_PATH
----------------------------

:Description: Colon separated paths in which Ansible will search for Callback Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/callback:/usr/share/ansible/plugins/callback
:Ini:
     :Section: [defaults]
     :Key: callback_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_CALLBACK_PLUGINS`

.. _DEFAULT_CALLBACK_WHITELIST:

DEFAULT_CALLBACK_WHITELIST
--------------------------

:Description: List of whitelisted callbacks, not all callbacks need whitelisting, but many of those shipped with Ansible do as we don't want them activated by default.
:Type: list
:Default: []
:Ini:
     :Section: [defaults]
     :Key: callback_whitelist
:Environment:
     :Variable: :envvar:`ANSIBLE_CALLBACK_WHITELIST`

.. _DEFAULT_CLICONF_PLUGIN_PATH:

DEFAULT_CLICONF_PLUGIN_PATH
---------------------------

:Description: Colon separated paths in which Ansible will search for Cliconf Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/cliconf:/usr/share/ansible/plugins/cliconf
:Ini:
     :Section: [defaults]
     :Key: cliconf_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_CLICONF_PLUGINS`

.. _DEFAULT_CONNECTION_PLUGIN_PATH:

DEFAULT_CONNECTION_PLUGIN_PATH
------------------------------

:Description: Colon separated paths in which Ansible will search for Connection Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/connection:/usr/share/ansible/plugins/connection
:Ini:
     :Section: [defaults]
     :Key: connection_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_CONNECTION_PLUGINS`

.. _DEFAULT_DEBUG:

DEFAULT_DEBUG
-------------

:Description: Toggles debug output in Ansible. This is *very* verbose and can hinder multiprocessing.  Debug output can also include secret information despite no_log settings being enabled, which means debug mode should not be used in production.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: debug
:Environment:
     :Variable: :envvar:`ANSIBLE_DEBUG`

.. _DEFAULT_EXECUTABLE:

DEFAULT_EXECUTABLE
------------------

:Description: This indicates the command to use to spawn a shell under for Ansible's execution needs on a target. Users may need to change this in rare instances when shell usage is constrained, but in most cases it may be left as is.
:Default: /bin/sh
:Ini:
     :Section: [defaults]
     :Key: executable
:Environment:
     :Variable: :envvar:`ANSIBLE_EXECUTABLE`

.. _DEFAULT_FACT_PATH:

DEFAULT_FACT_PATH
-----------------

:Description: This option allows you to globally configure a custom path for 'local_facts' for the implied M(setup) task when using fact gathering. If not set, it will fallback to the default from the M(setup) module: ``/etc/ansible/facts.d``. This does **not** affect  user defined tasks that use the M(setup) module.
:Type: path
:Default: None
:Ini:
     :Section: [defaults]
     :Key: fact_path
:Environment:
     :Variable: :envvar:`ANSIBLE_FACT_PATH`

.. _DEFAULT_FILTER_PLUGIN_PATH:

DEFAULT_FILTER_PLUGIN_PATH
--------------------------

:Description: Colon separated paths in which Ansible will search for Jinja2 Filter Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/filter:/usr/share/ansible/plugins/filter
:Ini:
     :Section: [defaults]
     :Key: filter_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_FILTER_PLUGINS`

.. _DEFAULT_FORCE_HANDLERS:

DEFAULT_FORCE_HANDLERS
----------------------

:Description: This option controls if notified handlers run on a host even if a failure occurs on that host. When false, the handlers will not run if a failure has occurred on a host. This can also be set per play or on the command line. See Handlers and Failure for more details.
:Type: boolean
:Default: False
:Version Added: 1.9.1
:Ini:
     :Section: [defaults]
     :Key: force_handlers
:Environment:
     :Variable: :envvar:`ANSIBLE_FORCE_HANDLERS`

.. _DEFAULT_FORKS:

DEFAULT_FORKS
-------------

:Description: Maximum number of forks Ansible will use to execute tasks on target hosts.
:Type: integer
:Default: 5
:Ini:
     :Section: [defaults]
     :Key: forks
:Environment:
     :Variable: :envvar:`ANSIBLE_FORKS`

.. _DEFAULT_GATHER_SUBSET:

DEFAULT_GATHER_SUBSET
---------------------

:Description: Set the `gather_subset` option for the M(setup) task in the implicit fact gathering. See the module documentation for specifics. It does **not** apply to user defined M(setup) tasks.
:Type: list
:Default: ['all']
:Version Added: 2.1
:Ini:
     :Section: [defaults]
     :Key: gather_subset
:Environment:
     :Variable: :envvar:`ANSIBLE_GATHER_SUBSET`

.. _DEFAULT_GATHER_TIMEOUT:

DEFAULT_GATHER_TIMEOUT
----------------------

:Description: Set the timeout in seconds for the implicit fact gathering. It does **not** apply to user defined M(setup) tasks.
:Type: integer
:Default: 10
:Ini:
     :Section: [defaults]
     :Key: gather_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_GATHER_TIMEOUT`

.. _DEFAULT_GATHERING:

DEFAULT_GATHERING
-----------------

:Description: This setting controls the default policy of fact gathering (facts discovered about remote systems). When 'implicit' (the default), the cache plugin will be ignored and facts will be gathered per play unless 'gather_facts: False' is set. When 'explicit' the inverse is true, facts will not be gathered unless directly requested in the play. The 'smart' value means each new host that has no facts discovered will be scanned, but if the same host is addressed in multiple plays it will not be contacted again in the playbook run. This option can be useful for those wishing to save fact gathering time. Both 'smart' and 'explicit' will use the cache plugin.
:Default: implicit
:Choices:
    - :smart:
    - :explicit:
    - :implicit:
:Version Added: 1.6
:Ini:
     :Section: [defaults]
     :Key: gathering
:Environment:
     :Variable: :envvar:`ANSIBLE_GATHERING`

.. _DEFAULT_HANDLER_INCLUDES_STATIC:

DEFAULT_HANDLER_INCLUDES_STATIC
-------------------------------

:Description: Since 2.0 M(include) can be 'dynamic', this setting (if True) forces that if the include appears in a ``handlers`` section to be 'static'.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: handler_includes_static
:Environment:
     :Variable: :envvar:`ANSIBLE_HANDLER_INCLUDES_STATIC`
:Deprecated in: 2.12
:Deprecated detail: include itself is deprecated and this setting will not matter in the future
:Deprecated alternatives: none as its already built into the decision between include_tasks and import_tasks

.. _DEFAULT_HASH_BEHAVIOUR:

DEFAULT_HASH_BEHAVIOUR
----------------------

:Description: This setting controls how variables merge in Ansible. By default Ansible will override variables in specific precedence orders, as described in Variables. When a variable of higher precedence wins, it will replace the other value. Some users prefer that variables that are hashes (aka 'dictionaries' in Python terms) are merged. This setting is called 'merge'. This is not the default behavior and it does not affect variables whose values are scalars (integers, strings) or arrays.  We generally recommend not using this setting unless you think you have an absolute need for it, and playbooks in the official examples repos do not use this setting In version 2.0 a ``combine`` filter was added to allow doing this for a particular variable (described in Filters).
:Type: string
:Default: replace
:Choices:
    - :replace:
    - :merge:
:Ini:
     :Section: [defaults]
     :Key: hash_behaviour
:Environment:
     :Variable: :envvar:`ANSIBLE_HASH_BEHAVIOUR`

.. _DEFAULT_HOST_LIST:

DEFAULT_HOST_LIST
-----------------

:Description: Comma separated list of Ansible inventory sources
:Type: pathlist
:Default: /etc/ansible/hosts
:Ini:
     :Section: [defaults]
     :Key: inventory
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY`

.. _DEFAULT_HTTPAPI_PLUGIN_PATH:

DEFAULT_HTTPAPI_PLUGIN_PATH
---------------------------

:Description: Colon separated paths in which Ansible will search for HttpApi Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/httpapi:/usr/share/ansible/plugins/httpapi
:Ini:
     :Section: [defaults]
     :Key: httpapi_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_HTTPAPI_PLUGINS`

.. _DEFAULT_INTERNAL_POLL_INTERVAL:

DEFAULT_INTERNAL_POLL_INTERVAL
------------------------------

:Description: This sets the interval (in seconds) of Ansible internal processes polling each other. Lower values improve performance with large playbooks at the expense of extra CPU load. Higher values are more suitable for Ansible usage in automation scenarios, when UI responsiveness is not required but CPU usage might be a concern. The default corresponds to the value hardcoded in Ansible <= 2.1
:Type: float
:Default: 0.001
:Version Added: 2.2
:Ini:
     :Section: [defaults]
     :Key: internal_poll_interval

.. _DEFAULT_INVENTORY_PLUGIN_PATH:

DEFAULT_INVENTORY_PLUGIN_PATH
-----------------------------

:Description: Colon separated paths in which Ansible will search for Inventory Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/inventory:/usr/share/ansible/plugins/inventory
:Ini:
     :Section: [defaults]
     :Key: inventory_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_PLUGINS`

.. _DEFAULT_JINJA2_EXTENSIONS:

DEFAULT_JINJA2_EXTENSIONS
-------------------------

:Description: This is a developer-specific feature that allows enabling additional Jinja2 extensions. See the Jinja2 documentation for details. If you do not know what these do, you probably don't need to change this setting :)
:Default: []
:Ini:
     :Section: [defaults]
     :Key: jinja2_extensions
:Environment:
     :Variable: :envvar:`ANSIBLE_JINJA2_EXTENSIONS`

.. _DEFAULT_JINJA2_NATIVE:

DEFAULT_JINJA2_NATIVE
---------------------

:Description: This option preserves variable types during template operations. This requires Jinja2 >= 2.10.
:Type: boolean
:Default: False
:Version Added: 2.7
:Ini:
     :Section: [defaults]
     :Key: jinja2_native
:Environment:
     :Variable: :envvar:`ANSIBLE_JINJA2_NATIVE`

.. _DEFAULT_KEEP_REMOTE_FILES:

DEFAULT_KEEP_REMOTE_FILES
-------------------------

:Description: Enables/disables the cleaning up of the temporary files Ansible used to execute the tasks on the remote. If this option is enabled it will disable ``ANSIBLE_PIPELINING``.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: keep_remote_files
:Environment:
     :Variable: :envvar:`ANSIBLE_KEEP_REMOTE_FILES`

.. _DEFAULT_LIBVIRT_LXC_NOSECLABEL:

DEFAULT_LIBVIRT_LXC_NOSECLABEL
------------------------------

:Description: This setting causes libvirt to connect to lxc containers by passing --noseclabel to virsh. This is necessary when running on systems which do not have SELinux.
:Type: boolean
:Default: False
:Version Added: 2.1
:Ini:
     :Section: [selinux]
     :Key: libvirt_lxc_noseclabel
:Environment:
     - :Variable: :envvar:`ANSIBLE_LIBVIRT_LXC_NOSECLABEL`
     - :Variable: :envvar:`LIBVIRT_LXC_NOSECLABEL`
       :Deprecated in: 2.12
       :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
       :Deprecated alternatives: the ``ANSIBLE_LIBVIRT_LXC_NOSECLABEL`` environment variable

.. _DEFAULT_LOAD_CALLBACK_PLUGINS:

DEFAULT_LOAD_CALLBACK_PLUGINS
-----------------------------

:Description: Controls whether callback plugins are loaded when running /usr/bin/ansible. This may be used to log activity from the command line, send notifications, and so on. Callback plugins are always loaded for ``ansible-playbook``.
:Type: boolean
:Default: False
:Version Added: 1.8
:Ini:
     :Section: [defaults]
     :Key: bin_ansible_callbacks
:Environment:
     :Variable: :envvar:`ANSIBLE_LOAD_CALLBACK_PLUGINS`

.. _DEFAULT_LOCAL_TMP:

DEFAULT_LOCAL_TMP
-----------------

:Description: Temporary directory for Ansible to use on the controller.
:Type: tmppath
:Default: ~/.ansible/tmp
:Ini:
     :Section: [defaults]
     :Key: local_tmp
:Environment:
     :Variable: :envvar:`ANSIBLE_LOCAL_TEMP`

.. _DEFAULT_LOG_FILTER:

DEFAULT_LOG_FILTER
------------------

:Description: List of logger names to filter out of the log file
:Type: list
:Default: []
:Ini:
     :Section: [defaults]
     :Key: log_filter
:Environment:
     :Variable: :envvar:`ANSIBLE_LOG_FILTER`

.. _DEFAULT_LOG_PATH:

DEFAULT_LOG_PATH
----------------

:Description: File to which Ansible will log on the controller. When empty logging is disabled.
:Type: path
:Default: None
:Ini:
     :Section: [defaults]
     :Key: log_path
:Environment:
     :Variable: :envvar:`ANSIBLE_LOG_PATH`

.. _DEFAULT_LOOKUP_PLUGIN_PATH:

DEFAULT_LOOKUP_PLUGIN_PATH
--------------------------

:Description: Colon separated paths in which Ansible will search for Lookup Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/lookup:/usr/share/ansible/plugins/lookup
:Ini:
     :Section: [defaults]
     :Key: lookup_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_LOOKUP_PLUGINS`

.. _DEFAULT_MANAGED_STR:

DEFAULT_MANAGED_STR
-------------------

:Description: Sets the macro for the 'ansible_managed' variable available for M(template) and M(win_template) modules.  This is only relevant for those two modules.
:Default: Ansible managed
:Ini:
     :Section: [defaults]
     :Key: ansible_managed

.. _DEFAULT_MODULE_ARGS:

DEFAULT_MODULE_ARGS
-------------------

:Description: This sets the default arguments to pass to the ``ansible`` adhoc binary if no ``-a`` is specified.
:Default: 
:Ini:
     :Section: [defaults]
     :Key: module_args
:Environment:
     :Variable: :envvar:`ANSIBLE_MODULE_ARGS`

.. _DEFAULT_MODULE_COMPRESSION:

DEFAULT_MODULE_COMPRESSION
--------------------------

:Description: Compression scheme to use when transferring Python modules to the target.
:Default: ZIP_DEFLATED
:Ini:
     :Section: [defaults]
     :Key: module_compression

.. _DEFAULT_MODULE_NAME:

DEFAULT_MODULE_NAME
-------------------

:Description: Module to use with the ``ansible`` AdHoc command, if none is specified via ``-m``.
:Default: command
:Ini:
     :Section: [defaults]
     :Key: module_name

.. _DEFAULT_MODULE_PATH:

DEFAULT_MODULE_PATH
-------------------

:Description: Colon separated paths in which Ansible will search for Modules.
:Type: pathspec
:Default: ~/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
:Ini:
     :Section: [defaults]
     :Key: library
:Environment:
     :Variable: :envvar:`ANSIBLE_LIBRARY`

.. _DEFAULT_MODULE_UTILS_PATH:

DEFAULT_MODULE_UTILS_PATH
-------------------------

:Description: Colon separated paths in which Ansible will search for Module utils files, which are shared by modules.
:Type: pathspec
:Default: ~/.ansible/plugins/module_utils:/usr/share/ansible/plugins/module_utils
:Ini:
     :Section: [defaults]
     :Key: module_utils
:Environment:
     :Variable: :envvar:`ANSIBLE_MODULE_UTILS`

.. _DEFAULT_NETCONF_PLUGIN_PATH:

DEFAULT_NETCONF_PLUGIN_PATH
---------------------------

:Description: Colon separated paths in which Ansible will search for Netconf Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/netconf:/usr/share/ansible/plugins/netconf
:Ini:
     :Section: [defaults]
     :Key: netconf_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_NETCONF_PLUGINS`

.. _DEFAULT_NO_LOG:

DEFAULT_NO_LOG
--------------

:Description: Toggle Ansible's display and logging of task details, mainly used to avoid security disclosures.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: no_log
:Environment:
     :Variable: :envvar:`ANSIBLE_NO_LOG`

.. _DEFAULT_NO_TARGET_SYSLOG:

DEFAULT_NO_TARGET_SYSLOG
------------------------

:Description: Toggle Ansible logging to syslog on the target when it executes tasks.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: no_target_syslog
:Environment:
     :Variable: :envvar:`ANSIBLE_NO_TARGET_SYSLOG`

.. _DEFAULT_NULL_REPRESENTATION:

DEFAULT_NULL_REPRESENTATION
---------------------------

:Description: What templating should return as a 'null' value. When not set it will let Jinja2 decide.
:Type: none
:Default: None
:Ini:
     :Section: [defaults]
     :Key: null_representation
:Environment:
     :Variable: :envvar:`ANSIBLE_NULL_REPRESENTATION`

.. _DEFAULT_POLL_INTERVAL:

DEFAULT_POLL_INTERVAL
---------------------

:Description: For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how often to check back on the status of those tasks when an explicit poll interval is not supplied. The default is a reasonably moderate 15 seconds which is a tradeoff between checking in frequently and providing a quick turnaround when something may have completed.
:Type: integer
:Default: 15
:Ini:
     :Section: [defaults]
     :Key: poll_interval
:Environment:
     :Variable: :envvar:`ANSIBLE_POLL_INTERVAL`

.. _DEFAULT_PRIVATE_KEY_FILE:

DEFAULT_PRIVATE_KEY_FILE
------------------------

:Description: Option for connections using a certificate or key file to authenticate, rather than an agent or passwords, you can set the default value here to avoid re-specifying --private-key with every invocation.
:Type: path
:Default: None
:Ini:
     :Section: [defaults]
     :Key: private_key_file
:Environment:
     :Variable: :envvar:`ANSIBLE_PRIVATE_KEY_FILE`

.. _DEFAULT_PRIVATE_ROLE_VARS:

DEFAULT_PRIVATE_ROLE_VARS
-------------------------

:Description: Makes role variables inaccessible from other roles. This was introduced as a way to reset role variables to default values if a role is used more than once in a playbook.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: private_role_vars
:Environment:
     :Variable: :envvar:`ANSIBLE_PRIVATE_ROLE_VARS`

.. _DEFAULT_REMOTE_PORT:

DEFAULT_REMOTE_PORT
-------------------

:Description: Port to use in remote connections, when blank it will use the connection plugin default.
:Type: integer
:Default: None
:Ini:
     :Section: [defaults]
     :Key: remote_port
:Environment:
     :Variable: :envvar:`ANSIBLE_REMOTE_PORT`

.. _DEFAULT_REMOTE_USER:

DEFAULT_REMOTE_USER
-------------------

:Description: Sets the login user for the target machines When blank it uses the connection plugin's default, normally the user currently executing Ansible.
:Default: None
:Ini:
     :Section: [defaults]
     :Key: remote_user
:Environment:
     :Variable: :envvar:`ANSIBLE_REMOTE_USER`

.. _DEFAULT_ROLES_PATH:

DEFAULT_ROLES_PATH
------------------

:Description: Colon separated paths in which Ansible will search for Roles.
:Type: pathspec
:Default: ~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
:Ini:
     :Section: [defaults]
     :Key: roles_path
:Environment:
     :Variable: :envvar:`ANSIBLE_ROLES_PATH`

.. _DEFAULT_SCP_IF_SSH:

DEFAULT_SCP_IF_SSH
------------------

:Description: Preferred method to use when transferring files over ssh. When set to smart, Ansible will try them until one succeeds or they all fail. If set to True, it will force 'scp', if False it will use 'sftp'.
:Default: smart
:Ini:
     :Section: [ssh_connection]
     :Key: scp_if_ssh
:Environment:
     :Variable: :envvar:`ANSIBLE_SCP_IF_SSH`

.. _DEFAULT_SELINUX_SPECIAL_FS:

DEFAULT_SELINUX_SPECIAL_FS
--------------------------

:Description: Some filesystems do not support safe operations and/or return inconsistent errors, this setting makes Ansible 'tolerate' those in the list w/o causing fatal errors. Data corruption may occur and writes are not always verified when a filesystem is in the list.
:Type: list
:Default: fuse, nfs, vboxsf, ramfs, 9p, vfat
:Ini:
     :Section: [selinux]
     :Key: special_context_filesystems
:Environment:
     :Variable: :envvar:`ANSIBLE_SELINUX_SPECIAL_FS`
       :Version Added: 2.9

.. _DEFAULT_SFTP_BATCH_MODE:

DEFAULT_SFTP_BATCH_MODE
-----------------------

:Type: boolean
:Default: True
:Ini:
     :Section: [ssh_connection]
     :Key: sftp_batch_mode
:Environment:
     :Variable: :envvar:`ANSIBLE_SFTP_BATCH_MODE`

.. _DEFAULT_SQUASH_ACTIONS:

DEFAULT_SQUASH_ACTIONS
----------------------

:Description: Ansible can optimise actions that call modules that support list parameters when using ``with_`` looping. Instead of calling the module once for each item, the module is called once with the full list. The default value for this setting is only for certain package managers, but it can be used for any module. Currently, this is only supported for modules that have a name or pkg parameter, and only when the item is the only thing being passed to the parameter.
:Type: list
:Default: apk, apt, dnf, homebrew, openbsd_pkg, pacman, pip, pkgng, yum, zypper
:Version Added: 2.0
:Ini:
     :Section: [defaults]
     :Key: squash_actions
:Environment:
     :Variable: :envvar:`ANSIBLE_SQUASH_ACTIONS`
:Deprecated in: 2.11
:Deprecated detail: Loop squashing is deprecated and this configuration will no longer be used
:Deprecated alternatives: a list directly with the module argument

.. _DEFAULT_SSH_TRANSFER_METHOD:

DEFAULT_SSH_TRANSFER_METHOD
---------------------------

:Description: unused?
:Default: None
:Ini:
     :Section: [ssh_connection]
     :Key: transfer_method
:Environment:
     :Variable: :envvar:`ANSIBLE_SSH_TRANSFER_METHOD`

.. _DEFAULT_STDOUT_CALLBACK:

DEFAULT_STDOUT_CALLBACK
-----------------------

:Description: Set the main callback used to display Ansible output, you can only have one at a time. You can have many other callbacks, but just one can be in charge of stdout.
:Default: default
:Ini:
     :Section: [defaults]
     :Key: stdout_callback
:Environment:
     :Variable: :envvar:`ANSIBLE_STDOUT_CALLBACK`

.. _DEFAULT_STRATEGY:

DEFAULT_STRATEGY
----------------

:Description: Set the default strategy used for plays.
:Default: linear
:Version Added: 2.3
:Ini:
     :Section: [defaults]
     :Key: strategy
:Environment:
     :Variable: :envvar:`ANSIBLE_STRATEGY`

.. _DEFAULT_STRATEGY_PLUGIN_PATH:

DEFAULT_STRATEGY_PLUGIN_PATH
----------------------------

:Description: Colon separated paths in which Ansible will search for Strategy Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/strategy:/usr/share/ansible/plugins/strategy
:Ini:
     :Section: [defaults]
     :Key: strategy_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_STRATEGY_PLUGINS`

.. _DEFAULT_SU:

DEFAULT_SU
----------

:Description: Toggle the use of "su" for tasks.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: su
:Environment:
     :Variable: :envvar:`ANSIBLE_SU`

.. _DEFAULT_SYSLOG_FACILITY:

DEFAULT_SYSLOG_FACILITY
-----------------------

:Description: Syslog facility to use when Ansible logs to the remote target
:Default: LOG_USER
:Ini:
     :Section: [defaults]
     :Key: syslog_facility
:Environment:
     :Variable: :envvar:`ANSIBLE_SYSLOG_FACILITY`

.. _DEFAULT_TASK_INCLUDES_STATIC:

DEFAULT_TASK_INCLUDES_STATIC
----------------------------

:Description: The `include` tasks can be static or dynamic, this toggles the default expected behaviour if autodetection fails and it is not explicitly set in task.
:Type: boolean
:Default: False
:Version Added: 2.1
:Ini:
     :Section: [defaults]
     :Key: task_includes_static
:Environment:
     :Variable: :envvar:`ANSIBLE_TASK_INCLUDES_STATIC`
:Deprecated in: 2.12
:Deprecated detail: include itself is deprecated and this setting will not matter in the future
:Deprecated alternatives: None, as its already built into the decision between include_tasks and import_tasks

.. _DEFAULT_TERMINAL_PLUGIN_PATH:

DEFAULT_TERMINAL_PLUGIN_PATH
----------------------------

:Description: Colon separated paths in which Ansible will search for Terminal Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/terminal:/usr/share/ansible/plugins/terminal
:Ini:
     :Section: [defaults]
     :Key: terminal_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_TERMINAL_PLUGINS`

.. _DEFAULT_TEST_PLUGIN_PATH:

DEFAULT_TEST_PLUGIN_PATH
------------------------

:Description: Colon separated paths in which Ansible will search for Jinja2 Test Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/test:/usr/share/ansible/plugins/test
:Ini:
     :Section: [defaults]
     :Key: test_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_TEST_PLUGINS`

.. _DEFAULT_TIMEOUT:

DEFAULT_TIMEOUT
---------------

:Description: This is the default timeout for connection plugins to use.
:Type: integer
:Default: 10
:Ini:
     :Section: [defaults]
     :Key: timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_TIMEOUT`

.. _DEFAULT_TRANSPORT:

DEFAULT_TRANSPORT
-----------------

:Description: Default connection plugin to use, the 'smart' option will toggle between 'ssh' and 'paramiko' depending on controller OS and ssh versions
:Default: smart
:Ini:
     :Section: [defaults]
     :Key: transport
:Environment:
     :Variable: :envvar:`ANSIBLE_TRANSPORT`

.. _DEFAULT_UNDEFINED_VAR_BEHAVIOR:

DEFAULT_UNDEFINED_VAR_BEHAVIOR
------------------------------

:Description: When True, this causes ansible templating to fail steps that reference variable names that are likely typoed. Otherwise, any '{{ template_expression }}' that contains undefined variables will be rendered in a template or ansible action line exactly as written.
:Type: boolean
:Default: True
:Version Added: 1.3
:Ini:
     :Section: [defaults]
     :Key: error_on_undefined_vars
:Environment:
     :Variable: :envvar:`ANSIBLE_ERROR_ON_UNDEFINED_VARS`

.. _DEFAULT_VARS_PLUGIN_PATH:

DEFAULT_VARS_PLUGIN_PATH
------------------------

:Description: Colon separated paths in which Ansible will search for Vars Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/vars:/usr/share/ansible/plugins/vars
:Ini:
     :Section: [defaults]
     :Key: vars_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_VARS_PLUGINS`

.. _DEFAULT_VAULT_ENCRYPT_IDENTITY:

DEFAULT_VAULT_ENCRYPT_IDENTITY
------------------------------

:Description: The vault_id to use for encrypting by default. If multiple vault_ids are provided, this specifies which to use for encryption. The --encrypt-vault-id cli option overrides the configured value.
:Default: None
:Ini:
     :Section: [defaults]
     :Key: vault_encrypt_identity
:Environment:
     :Variable: :envvar:`ANSIBLE_VAULT_ENCRYPT_IDENTITY`

.. _DEFAULT_VAULT_ID_MATCH:

DEFAULT_VAULT_ID_MATCH
----------------------

:Description: If true, decrypting vaults with a vault id will only try the password from the matching vault-id
:Default: False
:Ini:
     :Section: [defaults]
     :Key: vault_id_match
:Environment:
     :Variable: :envvar:`ANSIBLE_VAULT_ID_MATCH`

.. _DEFAULT_VAULT_IDENTITY:

DEFAULT_VAULT_IDENTITY
----------------------

:Description: The label to use for the default vault id label in cases where a vault id label is not provided
:Default: default
:Ini:
     :Section: [defaults]
     :Key: vault_identity
:Environment:
     :Variable: :envvar:`ANSIBLE_VAULT_IDENTITY`

.. _DEFAULT_VAULT_IDENTITY_LIST:

DEFAULT_VAULT_IDENTITY_LIST
---------------------------

:Description: A list of vault-ids to use by default. Equivalent to multiple --vault-id args. Vault-ids are tried in order.
:Type: list
:Default: []
:Ini:
     :Section: [defaults]
     :Key: vault_identity_list
:Environment:
     :Variable: :envvar:`ANSIBLE_VAULT_IDENTITY_LIST`

.. _DEFAULT_VAULT_PASSWORD_FILE:

DEFAULT_VAULT_PASSWORD_FILE
---------------------------

:Description: The vault password file to use. Equivalent to --vault-password-file or --vault-id
:Type: path
:Default: None
:Ini:
     :Section: [defaults]
     :Key: vault_password_file
:Environment:
     :Variable: :envvar:`ANSIBLE_VAULT_PASSWORD_FILE`

.. _DEFAULT_VERBOSITY:

DEFAULT_VERBOSITY
-----------------

:Description: Sets the default verbosity, equivalent to the number of ``-v`` passed in the command line.
:Type: integer
:Default: 0
:Ini:
     :Section: [defaults]
     :Key: verbosity
:Environment:
     :Variable: :envvar:`ANSIBLE_VERBOSITY`

.. _DEPRECATION_WARNINGS:

DEPRECATION_WARNINGS
--------------------

:Description: Toggle to control the showing of deprecation warnings
:Type: boolean
:Default: True
:Ini:
     :Section: [defaults]
     :Key: deprecation_warnings
:Environment:
     :Variable: :envvar:`ANSIBLE_DEPRECATION_WARNINGS`

.. _DIFF_ALWAYS:

DIFF_ALWAYS
-----------

:Description: Configuration toggle to tell modules to show differences when in 'changed' status, equivalent to ``--diff``.
:Type: bool
:Default: False
:Ini:
     :Section: [diff]
     :Key: always
:Environment:
     :Variable: :envvar:`ANSIBLE_DIFF_ALWAYS`

.. _DIFF_CONTEXT:

DIFF_CONTEXT
------------

:Description: How many lines of context to show when displaying the differences between files.
:Type: integer
:Default: 3
:Ini:
     :Section: [diff]
     :Key: context
:Environment:
     :Variable: :envvar:`ANSIBLE_DIFF_CONTEXT`

.. _DISPLAY_ARGS_TO_STDOUT:

DISPLAY_ARGS_TO_STDOUT
----------------------

:Description: Normally ``ansible-playbook`` will print a header for each task that is run. These headers will contain the name: field from the task if you specified one. If you didn't then ``ansible-playbook`` uses the task's action to help you tell which task is presently running. Sometimes you run many of the same action and so you want more information about the task to differentiate it from others of the same action. If you set this variable to True in the config then ``ansible-playbook`` will also include the task's arguments in the header. This setting defaults to False because there is a chance that you have sensitive values in your parameters and you do not want those to be printed. If you set this to True you should be sure that you have secured your environment's stdout (no one can shoulder surf your screen and you aren't saving stdout to an insecure file) or made sure that all of your playbooks explicitly added the ``no_log: True`` parameter to tasks which have sensitive values See How do I keep secret data in my playbook? for more information.
:Type: boolean
:Default: False
:Version Added: 2.1
:Ini:
     :Section: [defaults]
     :Key: display_args_to_stdout
:Environment:
     :Variable: :envvar:`ANSIBLE_DISPLAY_ARGS_TO_STDOUT`

.. _DISPLAY_SKIPPED_HOSTS:

DISPLAY_SKIPPED_HOSTS
---------------------

:Description: Toggle to control displaying skipped task/host entries in a task in the default callback
:Type: boolean
:Default: True
:Ini:
     :Section: [defaults]
     :Key: display_skipped_hosts
:Environment:
     - :Variable: :envvar:`ANSIBLE_DISPLAY_SKIPPED_HOSTS`
     - :Variable: :envvar:`DISPLAY_SKIPPED_HOSTS`
       :Deprecated in: 2.12
       :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
       :Deprecated alternatives: the ``ANSIBLE_DISPLAY_SKIPPED_HOSTS`` environment variable

.. _DOC_FRAGMENT_PLUGIN_PATH:

DOC_FRAGMENT_PLUGIN_PATH
------------------------

:Description: Colon separated paths in which Ansible will search for Documentation Fragments Plugins.
:Type: pathspec
:Default: ~/.ansible/plugins/doc_fragments:/usr/share/ansible/plugins/doc_fragments
:Ini:
     :Section: [defaults]
     :Key: doc_fragment_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_DOC_FRAGMENT_PLUGINS`

.. _DOCSITE_ROOT_URL:

DOCSITE_ROOT_URL
----------------

:Description: Root docsite URL used to generate docs URLs in warning/error text; must be an absolute URL with valid scheme and trailing slash.
:Default: https://docs.ansible.com/ansible/
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: docsite_root_url

.. _DUPLICATE_YAML_DICT_KEY:

DUPLICATE_YAML_DICT_KEY
-----------------------

:Description: By default Ansible will issue a warning when a duplicate dict key is encountered in YAML. These warnings can be silenced by adjusting this setting to False.
:Type: string
:Default: warn
:Choices:
    - :warn:
    - :error:
    - :ignore:
:Version Added: 2.9
:Ini:
     :Section: [defaults]
     :Key: duplicate_dict_key
:Environment:
     :Variable: :envvar:`ANSIBLE_DUPLICATE_YAML_DICT_KEY`

.. _ENABLE_TASK_DEBUGGER:

ENABLE_TASK_DEBUGGER
--------------------

:Description: Whether or not to enable the task debugger, this previously was done as a strategy plugin. Now all strategy plugins can inherit this behavior. The debugger defaults to activating when a task is failed on unreachable. Use the debugger keyword for more flexibility.
:Type: boolean
:Default: False
:Version Added: 2.5
:Ini:
     :Section: [defaults]
     :Key: enable_task_debugger
:Environment:
     :Variable: :envvar:`ANSIBLE_ENABLE_TASK_DEBUGGER`

.. _ERROR_ON_MISSING_HANDLER:

ERROR_ON_MISSING_HANDLER
------------------------

:Description: Toggle to allow missing handlers to become a warning instead of an error when notifying.
:Type: boolean
:Default: True
:Ini:
     :Section: [defaults]
     :Key: error_on_missing_handler
:Environment:
     :Variable: :envvar:`ANSIBLE_ERROR_ON_MISSING_HANDLER`

.. _FACTS_MODULES:

FACTS_MODULES
-------------

:Description: Which modules to run during a play's fact gathering stage, using the default of 'smart' will try to figure it out based on connection type.
:Type: list
:Default: ['smart']
:Ini:
     :Section: [defaults]
     :Key: facts_modules
:Environment:
     :Variable: :envvar:`ANSIBLE_FACTS_MODULES`
:Variables:
     :name: `ansible_facts_modules`

.. _GALAXY_IGNORE_CERTS:

GALAXY_IGNORE_CERTS
-------------------

:Description: If set to yes, ansible-galaxy will not validate TLS certificates. This can be useful for testing against a server with a self-signed certificate.
:Type: boolean
:Default: False
:Ini:
     :Section: [galaxy]
     :Key: ignore_certs
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_IGNORE`

.. _GALAXY_ROLE_SKELETON:

GALAXY_ROLE_SKELETON
--------------------

:Description: Role or collection skeleton directory to use as a template for the ``init`` action in ``ansible-galaxy``, same as ``--role-skeleton``.
:Type: path
:Default: None
:Ini:
     :Section: [galaxy]
     :Key: role_skeleton
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_ROLE_SKELETON`

.. _GALAXY_ROLE_SKELETON_IGNORE:

GALAXY_ROLE_SKELETON_IGNORE
---------------------------

:Description: patterns of files to ignore inside a Galaxy role or collection skeleton directory
:Type: list
:Default: ['^.git$', '^.*/.git_keep$']
:Ini:
     :Section: [galaxy]
     :Key: role_skeleton_ignore
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE`

.. _GALAXY_SERVER:

GALAXY_SERVER
-------------

:Description: URL to prepend when roles don't specify the full URI, assume they are referencing this server as the source.
:Default: https://galaxy.ansible.com
:Ini:
     :Section: [galaxy]
     :Key: server
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_SERVER`

.. _GALAXY_SERVER_LIST:

GALAXY_SERVER_LIST
------------------

:Description: A list of Galaxy servers to use when installing a collection. The value corresponds to the config ini header ``[galaxy_server.{{item}}]`` which defines the server details. See :ref:`galaxy_server_config` for more details on how to define a Galaxy server. The order of servers in this list is used to as the order in which a collection is resolved. Setting this config option will ignore the :ref:`galaxy_server` config option.
:Type: list
:Version Added: 2.9
:Ini:
     :Section: [galaxy]
     :Key: server_list
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_SERVER_LIST`

.. _GALAXY_TOKEN_PATH:

GALAXY_TOKEN_PATH
-----------------

:Description: Local path to galaxy access token file
:Type: path
:Default: ~/.ansible/galaxy_token
:Version Added: 2.9
:Ini:
     :Section: [galaxy]
     :Key: token_path
:Environment:
     :Variable: :envvar:`ANSIBLE_GALAXY_TOKEN_PATH`

.. _HOST_KEY_CHECKING:

HOST_KEY_CHECKING
-----------------

:Description: Set this to "False" if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host
:Type: boolean
:Default: True
:Ini:
     :Section: [defaults]
     :Key: host_key_checking
:Environment:
     :Variable: :envvar:`ANSIBLE_HOST_KEY_CHECKING`

.. _HOST_PATTERN_MISMATCH:

HOST_PATTERN_MISMATCH
---------------------

:Description: This setting changes the behaviour of mismatched host patterns, it allows you to force a fatal error, a warning or just ignore it
:Default: warning
:Choices:
    - :warning:
    - :error:
    - :ignore:
:Version Added: 2.8
:Ini:
     :Section: [inventory]
     :Key: host_pattern_mismatch
:Environment:
     :Variable: :envvar:`ANSIBLE_HOST_PATTERN_MISMATCH`

.. _INJECT_FACTS_AS_VARS:

INJECT_FACTS_AS_VARS
--------------------

:Description: Facts are available inside the `ansible_facts` variable, this setting also pushes them as their own vars in the main namespace. Unlike inside the `ansible_facts` dictionary, these will have an `ansible_` prefix.
:Type: boolean
:Default: True
:Version Added: 2.5
:Ini:
     :Section: [defaults]
     :Key: inject_facts_as_vars
:Environment:
     :Variable: :envvar:`ANSIBLE_INJECT_FACT_VARS`

.. _INTERPRETER_PYTHON:

INTERPRETER_PYTHON
------------------

:Description: Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode. Supported discovery modes are ``auto``, ``auto_silent``, and ``auto_legacy`` (the default). All discovery modes employ a lookup table to use the included system Python (on distributions known to include one), falling back to a fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed later may change which one is used). This warning behavior can be disabled by setting ``auto_silent``. The default value of ``auto_legacy`` provides all the same behavior, but for backwards-compatibility with older Ansible releases that always defaulted to ``/usr/bin/python``, will use that interpreter if present (and issue a warning that the default behavior will change to that of ``auto`` in a future Ansible release.
:Default: auto_legacy
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: interpreter_python
:Environment:
     :Variable: :envvar:`ANSIBLE_PYTHON_INTERPRETER`
:Variables:
     :name: `ansible_python_interpreter`

.. _INTERPRETER_PYTHON_DISTRO_MAP:

INTERPRETER_PYTHON_DISTRO_MAP
-----------------------------

:Default: {'centos': {'6': '/usr/bin/python', '8': '/usr/libexec/platform-python'}, 'fedora': {'23': '/usr/bin/python3'}, 'redhat': {'6': '/usr/bin/python', '8': '/usr/libexec/platform-python'}, 'rhel': {'6': '/usr/bin/python', '8': '/usr/libexec/platform-python'}, 'ubuntu': {'14': '/usr/bin/python', '16': '/usr/bin/python3'}}
:Version Added: 2.8

.. _INTERPRETER_PYTHON_FALLBACK:

INTERPRETER_PYTHON_FALLBACK
---------------------------

:Default: ['/usr/bin/python', 'python3.7', 'python3.6', 'python3.5', 'python2.7', 'python2.6', '/usr/libexec/platform-python', '/usr/bin/python3', 'python']
:Version Added: 2.8

.. _INVALID_TASK_ATTRIBUTE_FAILED:

INVALID_TASK_ATTRIBUTE_FAILED
-----------------------------

:Description: If 'false', invalid attributes for a task will result in warnings instead of errors
:Type: boolean
:Default: True
:Version Added: 2.7
:Ini:
     :Section: [defaults]
     :Key: invalid_task_attribute_failed
:Environment:
     :Variable: :envvar:`ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED`

.. _INVENTORY_ANY_UNPARSED_IS_FAILED:

INVENTORY_ANY_UNPARSED_IS_FAILED
--------------------------------

:Description: If 'true', it is a fatal error when any given inventory source cannot be successfully parsed by any available inventory plugin; otherwise, this situation only attracts a warning.

:Type: boolean
:Default: False
:Version Added: 2.7
:Ini:
     :Section: [inventory]
     :Key: any_unparsed_is_failed
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED`

.. _INVENTORY_CACHE_ENABLED:

INVENTORY_CACHE_ENABLED
-----------------------

:Description: Toggle to turn on inventory caching
:Type: bool
:Default: False
:Ini:
     :Section: [inventory]
     :Key: cache
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_CACHE`

.. _INVENTORY_CACHE_PLUGIN:

INVENTORY_CACHE_PLUGIN
----------------------

:Description: The plugin for caching inventory. If INVENTORY_CACHE_PLUGIN is not provided CACHE_PLUGIN can be used instead.
:Ini:
     :Section: [inventory]
     :Key: cache_plugin
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_CACHE_PLUGIN`

.. _INVENTORY_CACHE_PLUGIN_CONNECTION:

INVENTORY_CACHE_PLUGIN_CONNECTION
---------------------------------

:Description: The inventory cache connection. If INVENTORY_CACHE_PLUGIN_CONNECTION is not provided CACHE_PLUGIN_CONNECTION can be used instead.
:Ini:
     :Section: [inventory]
     :Key: cache_connection
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_CACHE_CONNECTION`

.. _INVENTORY_CACHE_PLUGIN_PREFIX:

INVENTORY_CACHE_PLUGIN_PREFIX
-----------------------------

:Description: The table prefix for the cache plugin. If INVENTORY_CACHE_PLUGIN_PREFIX is not provided CACHE_PLUGIN_PREFIX can be used instead.
:Default: ansible_facts
:Ini:
     :Section: [inventory]
     :Key: cache_prefix
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`

.. _INVENTORY_CACHE_TIMEOUT:

INVENTORY_CACHE_TIMEOUT
-----------------------

:Description: Expiration timeout for the inventory cache plugin data. If INVENTORY_CACHE_TIMEOUT is not provided CACHE_TIMEOUT can be used instead.
:Default: 3600
:Ini:
     :Section: [inventory]
     :Key: cache_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_CACHE_TIMEOUT`

.. _INVENTORY_ENABLED:

INVENTORY_ENABLED
-----------------

:Description: List of enabled inventory plugins, it also determines the order in which they are used.
:Type: list
:Default: ['host_list', 'script', 'auto', 'yaml', 'ini', 'toml']
:Ini:
     :Section: [inventory]
     :Key: enable_plugins
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_ENABLED`

.. _INVENTORY_EXPORT:

INVENTORY_EXPORT
----------------

:Description: Controls if ansible-inventory will accurately reflect Ansible's view into inventory or its optimized for exporting.
:Type: bool
:Default: False
:Ini:
     :Section: [inventory]
     :Key: export
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_EXPORT`

.. _INVENTORY_IGNORE_EXTS:

INVENTORY_IGNORE_EXTS
---------------------

:Description: List of extensions to ignore when using a directory as an inventory source
:Type: list
:Default: {{(BLACKLIST_EXTS + ( '.orig', '.ini', '.cfg', '.retry'))}}
:Ini:
     - :Section: [defaults]
       :Key: inventory_ignore_extensions
     - :Section: [inventory]
       :Key: ignore_extensions
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_IGNORE`

.. _INVENTORY_IGNORE_PATTERNS:

INVENTORY_IGNORE_PATTERNS
-------------------------

:Description: List of patterns to ignore when using a directory as an inventory source
:Type: list
:Default: []
:Ini:
     - :Section: [defaults]
       :Key: inventory_ignore_patterns
     - :Section: [inventory]
       :Key: ignore_patterns
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_IGNORE_REGEX`

.. _INVENTORY_UNPARSED_IS_FAILED:

INVENTORY_UNPARSED_IS_FAILED
----------------------------

:Description: If 'true' it is a fatal error if every single potential inventory source fails to parse, otherwise this situation will only attract a warning.

:Type: bool
:Default: False
:Ini:
     :Section: [inventory]
     :Key: unparsed_is_failed
:Environment:
     :Variable: :envvar:`ANSIBLE_INVENTORY_UNPARSED_FAILED`

.. _LOCALHOST_WARNING:

LOCALHOST_WARNING
-----------------

:Description: By default Ansible will issue a warning when there are no hosts in the inventory. These warnings can be silenced by adjusting this setting to False.
:Type: boolean
:Default: True
:Version Added: 2.6
:Ini:
     :Section: [defaults]
     :Key: localhost_warning
:Environment:
     :Variable: :envvar:`ANSIBLE_LOCALHOST_WARNING`

.. _MAX_FILE_SIZE_FOR_DIFF:

MAX_FILE_SIZE_FOR_DIFF
----------------------

:Description: Maximum size of files to be considered for diff display
:Type: int
:Default: 104448
:Ini:
     :Section: [defaults]
     :Key: max_diff_size
:Environment:
     :Variable: :envvar:`ANSIBLE_MAX_DIFF_SIZE`

.. _NETCONF_SSH_CONFIG:

NETCONF_SSH_CONFIG
------------------

:Description: This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.
:Default: None
:Ini:
     :Section: [netconf_connection]
     :Key: ssh_config
:Environment:
     :Variable: :envvar:`ANSIBLE_NETCONF_SSH_CONFIG`

.. _NETWORK_GROUP_MODULES:

NETWORK_GROUP_MODULES
---------------------

:Type: list
:Default: ['eos', 'nxos', 'ios', 'iosxr', 'junos', 'enos', 'ce', 'vyos', 'sros', 'dellos9', 'dellos10', 'dellos6', 'asa', 'aruba', 'aireos', 'bigip', 'ironware', 'onyx', 'netconf']
:Ini:
     :Section: [defaults]
     :Key: network_group_modules
:Environment:
     - :Variable: :envvar:`ANSIBLE_NETWORK_GROUP_MODULES`
     - :Variable: :envvar:`NETWORK_GROUP_MODULES`
       :Deprecated in: 2.12
       :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
       :Deprecated alternatives: the ``ANSIBLE_NETWORK_GROUP_MODULES`` environment variable

.. _OLD_PLUGIN_CACHE_CLEARING:

OLD_PLUGIN_CACHE_CLEARING
-------------------------

:Description: Previouslly Ansible would only clear some of the plugin loading caches when loading new roles, this led to some behaviours in which a plugin loaded in prevoius plays would be unexpectedly 'sticky'. This setting allows to return to that behaviour.
:Type: boolean
:Default: False
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: old_plugin_cache_clear
:Environment:
     :Variable: :envvar:`ANSIBLE_OLD_PLUGIN_CACHE_CLEAR`

.. _PARAMIKO_HOST_KEY_AUTO_ADD:

PARAMIKO_HOST_KEY_AUTO_ADD
--------------------------

:Type: boolean
:Default: False
:Ini:
     :Section: [paramiko_connection]
     :Key: host_key_auto_add
:Environment:
     :Variable: :envvar:`ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD`

.. _PARAMIKO_LOOK_FOR_KEYS:

PARAMIKO_LOOK_FOR_KEYS
----------------------

:Type: boolean
:Default: True
:Ini:
     :Section: [paramiko_connection]
     :Key: look_for_keys
:Environment:
     :Variable: :envvar:`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS`

.. _PERSISTENT_COMMAND_TIMEOUT:

PERSISTENT_COMMAND_TIMEOUT
--------------------------

:Description: This controls the amount of time to wait for response from remote device before timing out persistent connection.
:Type: int
:Default: 30
:Ini:
     :Section: [persistent_connection]
     :Key: command_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`

.. _PERSISTENT_CONNECT_RETRY_TIMEOUT:

PERSISTENT_CONNECT_RETRY_TIMEOUT
--------------------------------

:Description: This controls the retry timeout for persistent connection to connect to the local domain socket.
:Type: integer
:Default: 15
:Ini:
     :Section: [persistent_connection]
     :Key: connect_retry_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT`

.. _PERSISTENT_CONNECT_TIMEOUT:

PERSISTENT_CONNECT_TIMEOUT
--------------------------

:Description: This controls how long the persistent connection will remain idle before it is destroyed.
:Type: integer
:Default: 30
:Ini:
     :Section: [persistent_connection]
     :Key: connect_timeout
:Environment:
     :Variable: :envvar:`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`

.. _PERSISTENT_CONTROL_PATH_DIR:

PERSISTENT_CONTROL_PATH_DIR
---------------------------

:Description: Path to socket to be used by the connection persistence system.
:Type: path
:Default: ~/.ansible/pc
:Ini:
     :Section: [persistent_connection]
     :Key: control_path_dir
:Environment:
     :Variable: :envvar:`ANSIBLE_PERSISTENT_CONTROL_PATH_DIR`

.. _PLAYBOOK_DIR:

PLAYBOOK_DIR
------------

:Description: A number of non-playbook CLIs have a ``--playbook-dir`` argument; this sets the default value for it.
:Type: path
:Version Added: 2.9
:Ini:
     :Section: [defaults]
     :Key: playbook_dir
:Environment:
     :Variable: :envvar:`ANSIBLE_PLAYBOOK_DIR`

.. _PLAYBOOK_VARS_ROOT:

PLAYBOOK_VARS_ROOT
------------------

:Description: This sets which playbook dirs will be used as a root to process vars plugins, which includes finding host_vars/group_vars The ``top`` option follows the traditional behaviour of using the top playbook in the chain to find the root directory. The ``bottom`` option follows the 2.4.0 behaviour of using the current playbook to find the root directory. The ``all`` option examines from the first parent to the current playbook.
:Default: top
:Choices:
    - :top:
    - :bottom:
    - :all:
:Version Added: 2.4.1
:Ini:
     :Section: [defaults]
     :Key: playbook_vars_root
:Environment:
     :Variable: :envvar:`ANSIBLE_PLAYBOOK_VARS_ROOT`

.. _PLUGIN_FILTERS_CFG:

PLUGIN_FILTERS_CFG
------------------

:Description: A path to configuration for filtering which plugins installed on the system are allowed to be used. See :ref:`plugin_filtering_config` for details of the filter file's format.  The default is /etc/ansible/plugin_filters.yml
:Type: path
:Default: None
:Version Added: 2.5.0
:Ini:
     - :Section: [default]
       :Key: plugin_filters_cfg
       :Deprecated in: 2.12
       :Deprecated detail: Specifying "plugin_filters_cfg" under the "default" section is deprecated
       :Deprecated alternatives: the "defaults" section instead
     - :Section: [defaults]
       :Key: plugin_filters_cfg

.. _PYTHON_MODULE_RLIMIT_NOFILE:

PYTHON_MODULE_RLIMIT_NOFILE
---------------------------

:Description: Attempts to set RLIMIT_NOFILE soft limit to the specified value when executing Python modules (can speed up subprocess usage on Python 2.x. See https://bugs.python.org/issue11284). The value will be limited by the existing hard limit. Default value of 0 does not attempt to adjust existing system-defined limits.
:Default: 0
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: python_module_rlimit_nofile
:Environment:
     :Variable: :envvar:`ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE`
:Variables:
     :name: `ansible_python_module_rlimit_nofile`

.. _RETRY_FILES_ENABLED:

RETRY_FILES_ENABLED
-------------------

:Description: This controls whether a failed Ansible playbook should create a .retry file.
:Type: bool
:Default: False
:Ini:
     :Section: [defaults]
     :Key: retry_files_enabled
:Environment:
     :Variable: :envvar:`ANSIBLE_RETRY_FILES_ENABLED`

.. _RETRY_FILES_SAVE_PATH:

RETRY_FILES_SAVE_PATH
---------------------

:Description: This sets the path in which Ansible will save .retry files when a playbook fails and retry files are enabled.
:Type: path
:Default: None
:Ini:
     :Section: [defaults]
     :Key: retry_files_save_path
:Environment:
     :Variable: :envvar:`ANSIBLE_RETRY_FILES_SAVE_PATH`

.. _SHOW_CUSTOM_STATS:

SHOW_CUSTOM_STATS
-----------------

:Description: This adds the custom stats set via the set_stats plugin to the default output
:Type: bool
:Default: False
:Ini:
     :Section: [defaults]
     :Key: show_custom_stats
:Environment:
     :Variable: :envvar:`ANSIBLE_SHOW_CUSTOM_STATS`

.. _STRING_CONVERSION_ACTION:

STRING_CONVERSION_ACTION
------------------------

:Description: Action to take when a module parameter value is converted to a string (this does not affect variables). For string parameters, values such as '1.00', "['a', 'b',]", and 'yes', 'y', etc. will be converted by the YAML parser unless fully quoted. Valid options are 'error', 'warn', and 'ignore'. Since 2.8, this option defaults to 'warn' but will change to 'error' in 2.12.
:Type: string
:Default: warn
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: string_conversion_action
:Environment:
     :Variable: :envvar:`ANSIBLE_STRING_CONVERSION_ACTION`

.. _STRING_TYPE_FILTERS:

STRING_TYPE_FILTERS
-------------------

:Description: This list of filters avoids 'type conversion' when templating variables Useful when you want to avoid conversion into lists or dictionaries for JSON strings, for example.
:Type: list
:Default: ['string', 'to_json', 'to_nice_json', 'to_yaml', 'ppretty', 'json']
:Ini:
     :Section: [jinja2]
     :Key: dont_type_filters
:Environment:
     :Variable: :envvar:`ANSIBLE_STRING_TYPE_FILTERS`

.. _SYSTEM_WARNINGS:

SYSTEM_WARNINGS
---------------

:Description: Allows disabling of warnings related to potential issues on the system running ansible itself (not on the managed hosts) These may include warnings about 3rd party packages or other conditions that should be resolved if possible.
:Type: boolean
:Default: True
:Ini:
     :Section: [defaults]
     :Key: system_warnings
:Environment:
     :Variable: :envvar:`ANSIBLE_SYSTEM_WARNINGS`

.. _TAGS_RUN:

TAGS_RUN
--------

:Description: default list of tags to run in your plays, Skip Tags has precedence.
:Type: list
:Default: []
:Version Added: 2.5
:Ini:
     :Section: [tags]
     :Key: run
:Environment:
     :Variable: :envvar:`ANSIBLE_RUN_TAGS`

.. _TAGS_SKIP:

TAGS_SKIP
---------

:Description: default list of tags to skip in your plays, has precedence over Run Tags
:Type: list
:Default: []
:Version Added: 2.5
:Ini:
     :Section: [tags]
     :Key: skip
:Environment:
     :Variable: :envvar:`ANSIBLE_SKIP_TAGS`

.. _TASK_DEBUGGER_IGNORE_ERRORS:

TASK_DEBUGGER_IGNORE_ERRORS
---------------------------

:Description: This option defines whether the task debugger will be invoked on a failed task when ignore_errors=True is specified. True specifies that the debugger will honor ignore_errors, False will not honor ignore_errors.
:Type: boolean
:Default: True
:Version Added: 2.7
:Ini:
     :Section: [defaults]
     :Key: task_debugger_ignore_errors
:Environment:
     :Variable: :envvar:`ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS`

.. _TRANSFORM_INVALID_GROUP_CHARS:

TRANSFORM_INVALID_GROUP_CHARS
-----------------------------

:Description: Make ansible transform invalid characters in group names supplied by inventory sources. If 'never' it will allow for the group name but warn about the issue. When 'ignore', it does the same as 'never', without issuing a warning. When 'always' it will replace any invalid charachters with '_' (underscore) and warn the user When 'silently', it does the same as 'always', without issuing a warning.
:Type: string
:Default: never
:Choices:
    - :always:
    - :never:
    - :ignore:
    - :silently:
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: force_valid_group_names
:Environment:
     :Variable: :envvar:`ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS`

.. _USE_PERSISTENT_CONNECTIONS:

USE_PERSISTENT_CONNECTIONS
--------------------------

:Description: Toggles the use of persistence for connections.
:Type: boolean
:Default: False
:Ini:
     :Section: [defaults]
     :Key: use_persistent_connections
:Environment:
     :Variable: :envvar:`ANSIBLE_USE_PERSISTENT_CONNECTIONS`

.. _VARIABLE_PRECEDENCE:

VARIABLE_PRECEDENCE
-------------------

:Description: Allows to change the group variable precedence merge order.
:Type: list
:Default: ['all_inventory', 'groups_inventory', 'all_plugins_inventory', 'all_plugins_play', 'groups_plugins_inventory', 'groups_plugins_play']
:Version Added: 2.4
:Ini:
     :Section: [defaults]
     :Key: precedence
:Environment:
     :Variable: :envvar:`ANSIBLE_PRECEDENCE`

.. _VERBOSE_TO_STDERR:

VERBOSE_TO_STDERR
-----------------

:Description: Force 'verbose' option to use stderr instead of stdout
:Type: bool
:Default: False
:Version Added: 2.8
:Ini:
     :Section: [defaults]
     :Key: verbose_to_stderr
:Environment:
     :Variable: :envvar:`ANSIBLE_VERBOSE_TO_STDERR`

.. _YAML_FILENAME_EXTENSIONS:

YAML_FILENAME_EXTENSIONS
------------------------

:Description: Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these. This affects vars_files, include_vars, inventory and vars plugins among others.
:Type: list
:Default: ['.yml', '.yaml', '.json']
:Ini:
     :Section: [defaults]
     :Key: yaml_valid_extensions
:Environment:
     :Variable: :envvar:`ANSIBLE_YAML_FILENAME_EXT`


Environment Variables
=====================

.. envvar:: ANSIBLE_CONFIG


    Override the default ansible config file



.. envvar:: ANSIBLE_CONNECTION_PATH

    Specify where to look for the ansible-connection script. This location will be checked before searching $PATH.If null, ansible will start with the same directory as the ansible script.

    See also :ref:`ANSIBLE_CONNECTION_PATH <ANSIBLE_CONNECTION_PATH>`



.. envvar:: ANSIBLE_COW_SELECTION

    This allows you to chose a specific cowsay stencil for the banners or use 'random' to cycle through them.

    See also :ref:`ANSIBLE_COW_SELECTION <ANSIBLE_COW_SELECTION>`



.. envvar:: ANSIBLE_COW_WHITELIST

    White list of cowsay templates that are 'safe' to use, set to empty list if you want to enable all installed templates.

    See also :ref:`ANSIBLE_COW_WHITELIST <ANSIBLE_COW_WHITELIST>`



.. envvar:: ANSIBLE_FORCE_COLOR

    This options forces color mode even when running without a TTY or the "nocolor" setting is True.

    See also :ref:`ANSIBLE_FORCE_COLOR <ANSIBLE_FORCE_COLOR>`



.. envvar:: ANSIBLE_NOCOLOR

    This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.

    See also :ref:`ANSIBLE_NOCOLOR <ANSIBLE_NOCOLOR>`



.. envvar:: ANSIBLE_NOCOWS

    If you have cowsay installed but want to avoid the 'cows' (why????), use this.

    See also :ref:`ANSIBLE_NOCOWS <ANSIBLE_NOCOWS>`



.. envvar:: ANSIBLE_COW_PATH

    Specify a custom cowsay path or swap in your cowsay implementation of choice

    See also :ref:`ANSIBLE_COW_PATH <ANSIBLE_COW_PATH>`



.. envvar:: ANSIBLE_PIPELINING

    Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer.This can result in a very significant performance improvement when enabled.However this conflicts with privilege escalation (become). For example, when using 'sudo:' operations you must first disable 'requiretty' in /etc/sudoers on all managed hosts, which is why it is disabled by default.This options is disabled if ``ANSIBLE_KEEP_REMOTE_FILES`` is enabled.

    See also :ref:`ANSIBLE_PIPELINING <ANSIBLE_PIPELINING>`


.. envvar:: ANSIBLE_SSH_PIPELINING

    Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer.This can result in a very significant performance improvement when enabled.However this conflicts with privilege escalation (become). For example, when using 'sudo:' operations you must first disable 'requiretty' in /etc/sudoers on all managed hosts, which is why it is disabled by default.This options is disabled if ``ANSIBLE_KEEP_REMOTE_FILES`` is enabled.

    See also :ref:`ANSIBLE_PIPELINING <ANSIBLE_PIPELINING>`



.. envvar:: ANSIBLE_SSH_ARGS

    If set, this will override the Ansible default ssh arguments.In particular, users may wish to raise the ControlPersist time to encourage performance.  A value of 30 minutes may be appropriate.Be aware that if `-o ControlPath` is set in ssh_args, the control path setting is not used.

    See also :ref:`ANSIBLE_SSH_ARGS <ANSIBLE_SSH_ARGS>`



.. envvar:: ANSIBLE_SSH_CONTROL_PATH

    This is the location to save ssh's ControlPath sockets, it uses ssh's variable substitution.Since 2.3, if null, ansible will generate a unique hash. Use `%(directory)s` to indicate where to use the control dir path setting.Before 2.3 it defaulted to `control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r`.Be aware that this setting is ignored if `-o ControlPath` is set in ssh args.

    See also :ref:`ANSIBLE_SSH_CONTROL_PATH <ANSIBLE_SSH_CONTROL_PATH>`



.. envvar:: ANSIBLE_SSH_CONTROL_PATH_DIR

    This sets the directory to use for ssh control path if the control path setting is null.Also, provides the `%(directory)s` variable for the control path setting.

    See also :ref:`ANSIBLE_SSH_CONTROL_PATH_DIR <ANSIBLE_SSH_CONTROL_PATH_DIR>`



.. envvar:: ANSIBLE_SSH_EXECUTABLE

    This defines the location of the ssh binary. It defaults to `ssh` which will use the first ssh binary available in $PATH.This option is usually not required, it might be useful when access to system ssh is restricted, or when using ssh wrappers to connect to remote hosts.

    See also :ref:`ANSIBLE_SSH_EXECUTABLE <ANSIBLE_SSH_EXECUTABLE>`



.. envvar:: ANSIBLE_SSH_RETRIES

    Number of attempts to establish a connection before we give up and report the host as 'UNREACHABLE'

    See also :ref:`ANSIBLE_SSH_RETRIES <ANSIBLE_SSH_RETRIES>`



.. envvar:: ANSIBLE_ANY_ERRORS_FATAL

    Sets the default value for the any_errors_fatal keyword, if True, Task failures will be considered fatal errors.

    See also :ref:`ANY_ERRORS_FATAL <ANY_ERRORS_FATAL>`



.. envvar:: ANSIBLE_BECOME_ALLOW_SAME_USER

    This setting controls if become is skipped when remote user and become user are the same. I.E root sudo to root.

    See also :ref:`BECOME_ALLOW_SAME_USER <BECOME_ALLOW_SAME_USER>`



.. envvar:: ANSIBLE_AGNOSTIC_BECOME_PROMPT

    Display an agnostic become prompt instead of displaying a prompt containing the command line supplied become method

    See also :ref:`AGNOSTIC_BECOME_PROMPT <AGNOSTIC_BECOME_PROMPT>`



.. envvar:: ANSIBLE_CACHE_PLUGIN

    Chooses which cache plugin to use, the default 'memory' is ephimeral.

    See also :ref:`CACHE_PLUGIN <CACHE_PLUGIN>`



.. envvar:: ANSIBLE_CACHE_PLUGIN_CONNECTION

    Defines connection or path information for the cache plugin

    See also :ref:`CACHE_PLUGIN_CONNECTION <CACHE_PLUGIN_CONNECTION>`



.. envvar:: ANSIBLE_CACHE_PLUGIN_PREFIX

    Prefix to use for cache plugin files/tables

    See also :ref:`CACHE_PLUGIN_PREFIX <CACHE_PLUGIN_PREFIX>`



.. envvar:: ANSIBLE_CACHE_PLUGIN_TIMEOUT

    Expiration timeout for the cache plugin data

    See also :ref:`CACHE_PLUGIN_TIMEOUT <CACHE_PLUGIN_TIMEOUT>`



.. envvar:: ANSIBLE_COLLECTIONS_PATHS

    Colon separated paths in which Ansible will search for collections content.

    See also :ref:`COLLECTIONS_PATHS <COLLECTIONS_PATHS>`



.. envvar:: ANSIBLE_COLOR_CHANGED

    Defines the color to use on 'Changed' task status

    See also :ref:`COLOR_CHANGED <COLOR_CHANGED>`



.. envvar:: ANSIBLE_COLOR_CONSOLE_PROMPT

    Defines the default color to use for ansible-console

    See also :ref:`COLOR_CONSOLE_PROMPT <COLOR_CONSOLE_PROMPT>`



.. envvar:: ANSIBLE_COLOR_DEBUG

    Defines the color to use when emitting debug messages

    See also :ref:`COLOR_DEBUG <COLOR_DEBUG>`



.. envvar:: ANSIBLE_COLOR_DEPRECATE

    Defines the color to use when emitting deprecation messages

    See also :ref:`COLOR_DEPRECATE <COLOR_DEPRECATE>`



.. envvar:: ANSIBLE_COLOR_DIFF_ADD

    Defines the color to use when showing added lines in diffs

    See also :ref:`COLOR_DIFF_ADD <COLOR_DIFF_ADD>`



.. envvar:: ANSIBLE_COLOR_DIFF_LINES

    Defines the color to use when showing diffs

    See also :ref:`COLOR_DIFF_LINES <COLOR_DIFF_LINES>`



.. envvar:: ANSIBLE_COLOR_DIFF_REMOVE

    Defines the color to use when showing removed lines in diffs

    See also :ref:`COLOR_DIFF_REMOVE <COLOR_DIFF_REMOVE>`



.. envvar:: ANSIBLE_COLOR_ERROR

    Defines the color to use when emitting error messages

    See also :ref:`COLOR_ERROR <COLOR_ERROR>`



.. envvar:: ANSIBLE_COLOR_HIGHLIGHT

    Defines the color to use for highlighting

    See also :ref:`COLOR_HIGHLIGHT <COLOR_HIGHLIGHT>`



.. envvar:: ANSIBLE_COLOR_OK

    Defines the color to use when showing 'OK' task status

    See also :ref:`COLOR_OK <COLOR_OK>`



.. envvar:: ANSIBLE_COLOR_SKIP

    Defines the color to use when showing 'Skipped' task status

    See also :ref:`COLOR_SKIP <COLOR_SKIP>`



.. envvar:: ANSIBLE_COLOR_UNREACHABLE

    Defines the color to use on 'Unreachable' status

    See also :ref:`COLOR_UNREACHABLE <COLOR_UNREACHABLE>`



.. envvar:: ANSIBLE_COLOR_VERBOSE

    Defines the color to use when emitting verbose messages. i.e those that show with '-v's.

    See also :ref:`COLOR_VERBOSE <COLOR_VERBOSE>`



.. envvar:: ANSIBLE_COLOR_WARN

    Defines the color to use when emitting warning messages

    See also :ref:`COLOR_WARN <COLOR_WARN>`



.. envvar:: ANSIBLE_CONDITIONAL_BARE_VARS

    With this setting on (True), running conditional evaluation 'var' is treated differently than 'var.subkey' as the first is evaluated directly while the second goes through the Jinja2 parser. But 'false' strings in 'var' get evaluated as booleans.With this setting off they both evaluate the same but in cases in which 'var' was 'false' (a string) it won't get evaluated as a boolean anymore.Currently this setting defaults to 'True' but will soon change to 'False' and the setting itself will be removed in the future.Expect the default to change in version 2.10 and that this setting eventually will be deprecated after 2.12

    See also :ref:`CONDITIONAL_BARE_VARS <CONDITIONAL_BARE_VARS>`



.. envvar:: _ANSIBLE_COVERAGE_REMOTE_OUTPUT

    Sets the output directory on the remote host to generate coverage reports to.Currently only used for remote coverage on PowerShell modules.This is for internal use only.

    See also :ref:`COVERAGE_REMOTE_OUTPUT <COVERAGE_REMOTE_OUTPUT>`



.. envvar:: _ANSIBLE_COVERAGE_REMOTE_WHITELIST

    A list of paths for files on the Ansible controller to run coverage for when executing on the remote host.Only files that match the path glob will have its coverage collected.Multiple path globs can be specified and are separated by ``:``.Currently only used for remote coverage on PowerShell modules.This is for internal use only.

    See also :ref:`COVERAGE_REMOTE_WHITELIST <COVERAGE_REMOTE_WHITELIST>`



.. envvar:: ANSIBLE_ACTION_WARNINGS

    By default Ansible will issue a warning when received from a task action (module or action plugin)These warnings can be silenced by adjusting this setting to False.

    See also :ref:`ACTION_WARNINGS <ACTION_WARNINGS>`



.. envvar:: ANSIBLE_COMMAND_WARNINGS

    By default Ansible will issue a warning when the shell or command module is used and the command appears to be similar to an existing Ansible module.These warnings can be silenced by adjusting this setting to False. You can also control this at the task level with the module option ``warn``.

    See also :ref:`COMMAND_WARNINGS <COMMAND_WARNINGS>`



.. envvar:: ANSIBLE_LOCALHOST_WARNING

    By default Ansible will issue a warning when there are no hosts in the inventory.These warnings can be silenced by adjusting this setting to False.

    See also :ref:`LOCALHOST_WARNING <LOCALHOST_WARNING>`



.. envvar:: ANSIBLE_DOC_FRAGMENT_PLUGINS

    Colon separated paths in which Ansible will search for Documentation Fragments Plugins.

    See also :ref:`DOC_FRAGMENT_PLUGIN_PATH <DOC_FRAGMENT_PLUGIN_PATH>`



.. envvar:: ANSIBLE_ACTION_PLUGINS

    Colon separated paths in which Ansible will search for Action Plugins.

    See also :ref:`DEFAULT_ACTION_PLUGIN_PATH <DEFAULT_ACTION_PLUGIN_PATH>`




.. envvar:: ANSIBLE_ASK_PASS

    This controls whether an Ansible playbook should prompt for a login password. If using SSH keys for authentication, you probably do not needed to change this setting.

    See also :ref:`DEFAULT_ASK_PASS <DEFAULT_ASK_PASS>`



.. envvar:: ANSIBLE_ASK_VAULT_PASS

    This controls whether an Ansible playbook should prompt for a vault password.

    See also :ref:`DEFAULT_ASK_VAULT_PASS <DEFAULT_ASK_VAULT_PASS>`



.. envvar:: ANSIBLE_BECOME

    Toggles the use of privilege escalation, allowing you to 'become' another user after login.

    See also :ref:`DEFAULT_BECOME <DEFAULT_BECOME>`



.. envvar:: ANSIBLE_BECOME_ASK_PASS

    Toggle to prompt for privilege escalation password.

    See also :ref:`DEFAULT_BECOME_ASK_PASS <DEFAULT_BECOME_ASK_PASS>`



.. envvar:: ANSIBLE_BECOME_METHOD

    Privilege escalation method to use when `become` is enabled.

    See also :ref:`DEFAULT_BECOME_METHOD <DEFAULT_BECOME_METHOD>`



.. envvar:: ANSIBLE_BECOME_EXE

    executable to use for privilege escalation, otherwise Ansible will depend on PATH

    See also :ref:`DEFAULT_BECOME_EXE <DEFAULT_BECOME_EXE>`



.. envvar:: ANSIBLE_BECOME_FLAGS

    Flags to pass to the privilege escalation executable.

    See also :ref:`DEFAULT_BECOME_FLAGS <DEFAULT_BECOME_FLAGS>`



.. envvar:: ANSIBLE_BECOME_PLUGINS

    Colon separated paths in which Ansible will search for Become Plugins.

    See also :ref:`BECOME_PLUGIN_PATH <BECOME_PLUGIN_PATH>`



.. envvar:: ANSIBLE_BECOME_USER

    The user your login/remote user 'becomes' when using privilege escalation, most systems will use 'root' when no user is specified.

    See also :ref:`DEFAULT_BECOME_USER <DEFAULT_BECOME_USER>`



.. envvar:: ANSIBLE_CACHE_PLUGINS

    Colon separated paths in which Ansible will search for Cache Plugins.

    See also :ref:`DEFAULT_CACHE_PLUGIN_PATH <DEFAULT_CACHE_PLUGIN_PATH>`



.. envvar:: ANSIBLE_CALLABLE_WHITELIST

    Whitelist of callable methods to be made available to template evaluation

    See also :ref:`DEFAULT_CALLABLE_WHITELIST <DEFAULT_CALLABLE_WHITELIST>`



.. envvar:: ANSIBLE_CALLBACK_PLUGINS

    Colon separated paths in which Ansible will search for Callback Plugins.

    See also :ref:`DEFAULT_CALLBACK_PLUGIN_PATH <DEFAULT_CALLBACK_PLUGIN_PATH>`



.. envvar:: ANSIBLE_CALLBACK_WHITELIST

    List of whitelisted callbacks, not all callbacks need whitelisting, but many of those shipped with Ansible do as we don't want them activated by default.

    See also :ref:`DEFAULT_CALLBACK_WHITELIST <DEFAULT_CALLBACK_WHITELIST>`



.. envvar:: ANSIBLE_CLICONF_PLUGINS

    Colon separated paths in which Ansible will search for Cliconf Plugins.

    See also :ref:`DEFAULT_CLICONF_PLUGIN_PATH <DEFAULT_CLICONF_PLUGIN_PATH>`



.. envvar:: ANSIBLE_CONNECTION_PLUGINS

    Colon separated paths in which Ansible will search for Connection Plugins.

    See also :ref:`DEFAULT_CONNECTION_PLUGIN_PATH <DEFAULT_CONNECTION_PLUGIN_PATH>`



.. envvar:: ANSIBLE_DEBUG

    Toggles debug output in Ansible. This is *very* verbose and can hinder multiprocessing.  Debug output can also include secret information despite no_log settings being enabled, which means debug mode should not be used in production.

    See also :ref:`DEFAULT_DEBUG <DEFAULT_DEBUG>`



.. envvar:: ANSIBLE_EXECUTABLE

    This indicates the command to use to spawn a shell under for Ansible's execution needs on a target. Users may need to change this in rare instances when shell usage is constrained, but in most cases it may be left as is.

    See also :ref:`DEFAULT_EXECUTABLE <DEFAULT_EXECUTABLE>`



.. envvar:: ANSIBLE_FACT_PATH

    This option allows you to globally configure a custom path for 'local_facts' for the implied M(setup) task when using fact gathering.If not set, it will fallback to the default from the M(setup) module: ``/etc/ansible/facts.d``.This does **not** affect  user defined tasks that use the M(setup) module.

    See also :ref:`DEFAULT_FACT_PATH <DEFAULT_FACT_PATH>`



.. envvar:: ANSIBLE_FILTER_PLUGINS

    Colon separated paths in which Ansible will search for Jinja2 Filter Plugins.

    See also :ref:`DEFAULT_FILTER_PLUGIN_PATH <DEFAULT_FILTER_PLUGIN_PATH>`



.. envvar:: ANSIBLE_FORCE_HANDLERS

    This option controls if notified handlers run on a host even if a failure occurs on that host.When false, the handlers will not run if a failure has occurred on a host.This can also be set per play or on the command line. See Handlers and Failure for more details.

    See also :ref:`DEFAULT_FORCE_HANDLERS <DEFAULT_FORCE_HANDLERS>`



.. envvar:: ANSIBLE_FORKS

    Maximum number of forks Ansible will use to execute tasks on target hosts.

    See also :ref:`DEFAULT_FORKS <DEFAULT_FORKS>`



.. envvar:: ANSIBLE_GATHERING

    This setting controls the default policy of fact gathering (facts discovered about remote systems).When 'implicit' (the default), the cache plugin will be ignored and facts will be gathered per play unless 'gather_facts: False' is set.When 'explicit' the inverse is true, facts will not be gathered unless directly requested in the play.The 'smart' value means each new host that has no facts discovered will be scanned, but if the same host is addressed in multiple plays it will not be contacted again in the playbook run.This option can be useful for those wishing to save fact gathering time. Both 'smart' and 'explicit' will use the cache plugin.

    See also :ref:`DEFAULT_GATHERING <DEFAULT_GATHERING>`



.. envvar:: ANSIBLE_GATHER_SUBSET

    Set the `gather_subset` option for the M(setup) task in the implicit fact gathering. See the module documentation for specifics.It does **not** apply to user defined M(setup) tasks.

    See also :ref:`DEFAULT_GATHER_SUBSET <DEFAULT_GATHER_SUBSET>`



.. envvar:: ANSIBLE_GATHER_TIMEOUT

    Set the timeout in seconds for the implicit fact gathering.It does **not** apply to user defined M(setup) tasks.

    See also :ref:`DEFAULT_GATHER_TIMEOUT <DEFAULT_GATHER_TIMEOUT>`



.. envvar:: ANSIBLE_HANDLER_INCLUDES_STATIC

    Since 2.0 M(include) can be 'dynamic', this setting (if True) forces that if the include appears in a ``handlers`` section to be 'static'.

    See also :ref:`DEFAULT_HANDLER_INCLUDES_STATIC <DEFAULT_HANDLER_INCLUDES_STATIC>`



.. envvar:: ANSIBLE_HASH_BEHAVIOUR

    This setting controls how variables merge in Ansible. By default Ansible will override variables in specific precedence orders, as described in Variables. When a variable of higher precedence wins, it will replace the other value.Some users prefer that variables that are hashes (aka 'dictionaries' in Python terms) are merged. This setting is called 'merge'. This is not the default behavior and it does not affect variables whose values are scalars (integers, strings) or arrays.  We generally recommend not using this setting unless you think you have an absolute need for it, and playbooks in the official examples repos do not use this settingIn version 2.0 a ``combine`` filter was added to allow doing this for a particular variable (described in Filters).

    See also :ref:`DEFAULT_HASH_BEHAVIOUR <DEFAULT_HASH_BEHAVIOUR>`



.. envvar:: ANSIBLE_INVENTORY

    Comma separated list of Ansible inventory sources

    See also :ref:`DEFAULT_HOST_LIST <DEFAULT_HOST_LIST>`



.. envvar:: ANSIBLE_HTTPAPI_PLUGINS

    Colon separated paths in which Ansible will search for HttpApi Plugins.

    See also :ref:`DEFAULT_HTTPAPI_PLUGIN_PATH <DEFAULT_HTTPAPI_PLUGIN_PATH>`




.. envvar:: ANSIBLE_INVENTORY_PLUGINS

    Colon separated paths in which Ansible will search for Inventory Plugins.

    See also :ref:`DEFAULT_INVENTORY_PLUGIN_PATH <DEFAULT_INVENTORY_PLUGIN_PATH>`



.. envvar:: ANSIBLE_JINJA2_EXTENSIONS

    This is a developer-specific feature that allows enabling additional Jinja2 extensions.See the Jinja2 documentation for details. If you do not know what these do, you probably don't need to change this setting :)

    See also :ref:`DEFAULT_JINJA2_EXTENSIONS <DEFAULT_JINJA2_EXTENSIONS>`



.. envvar:: ANSIBLE_JINJA2_NATIVE

    This option preserves variable types during template operations. This requires Jinja2 >= 2.10.

    See also :ref:`DEFAULT_JINJA2_NATIVE <DEFAULT_JINJA2_NATIVE>`



.. envvar:: ANSIBLE_KEEP_REMOTE_FILES

    Enables/disables the cleaning up of the temporary files Ansible used to execute the tasks on the remote.If this option is enabled it will disable ``ANSIBLE_PIPELINING``.

    See also :ref:`DEFAULT_KEEP_REMOTE_FILES <DEFAULT_KEEP_REMOTE_FILES>`



.. envvar:: LIBVIRT_LXC_NOSECLABEL

    This setting causes libvirt to connect to lxc containers by passing --noseclabel to virsh. This is necessary when running on systems which do not have SELinux.

    See also :ref:`DEFAULT_LIBVIRT_LXC_NOSECLABEL <DEFAULT_LIBVIRT_LXC_NOSECLABEL>`

    :Deprecated in: 2.12
    :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
    :Deprecated alternatives: the ``ANSIBLE_LIBVIRT_LXC_NOSECLABEL`` environment variable

.. envvar:: ANSIBLE_LIBVIRT_LXC_NOSECLABEL

    This setting causes libvirt to connect to lxc containers by passing --noseclabel to virsh. This is necessary when running on systems which do not have SELinux.

    See also :ref:`DEFAULT_LIBVIRT_LXC_NOSECLABEL <DEFAULT_LIBVIRT_LXC_NOSECLABEL>`



.. envvar:: ANSIBLE_LOAD_CALLBACK_PLUGINS

    Controls whether callback plugins are loaded when running /usr/bin/ansible. This may be used to log activity from the command line, send notifications, and so on. Callback plugins are always loaded for ``ansible-playbook``.

    See also :ref:`DEFAULT_LOAD_CALLBACK_PLUGINS <DEFAULT_LOAD_CALLBACK_PLUGINS>`



.. envvar:: ANSIBLE_LOCAL_TEMP

    Temporary directory for Ansible to use on the controller.

    See also :ref:`DEFAULT_LOCAL_TMP <DEFAULT_LOCAL_TMP>`



.. envvar:: ANSIBLE_LOG_PATH

    File to which Ansible will log on the controller. When empty logging is disabled.

    See also :ref:`DEFAULT_LOG_PATH <DEFAULT_LOG_PATH>`



.. envvar:: ANSIBLE_LOG_FILTER

    List of logger names to filter out of the log file

    See also :ref:`DEFAULT_LOG_FILTER <DEFAULT_LOG_FILTER>`



.. envvar:: ANSIBLE_LOOKUP_PLUGINS

    Colon separated paths in which Ansible will search for Lookup Plugins.

    See also :ref:`DEFAULT_LOOKUP_PLUGIN_PATH <DEFAULT_LOOKUP_PLUGIN_PATH>`




.. envvar:: ANSIBLE_MODULE_ARGS

    This sets the default arguments to pass to the ``ansible`` adhoc binary if no ``-a`` is specified.

    See also :ref:`DEFAULT_MODULE_ARGS <DEFAULT_MODULE_ARGS>`





.. envvar:: ANSIBLE_LIBRARY

    Colon separated paths in which Ansible will search for Modules.

    See also :ref:`DEFAULT_MODULE_PATH <DEFAULT_MODULE_PATH>`



.. envvar:: ANSIBLE_MODULE_UTILS

    Colon separated paths in which Ansible will search for Module utils files, which are shared by modules.

    See also :ref:`DEFAULT_MODULE_UTILS_PATH <DEFAULT_MODULE_UTILS_PATH>`



.. envvar:: ANSIBLE_NETCONF_PLUGINS

    Colon separated paths in which Ansible will search for Netconf Plugins.

    See also :ref:`DEFAULT_NETCONF_PLUGIN_PATH <DEFAULT_NETCONF_PLUGIN_PATH>`



.. envvar:: ANSIBLE_NO_LOG

    Toggle Ansible's display and logging of task details, mainly used to avoid security disclosures.

    See also :ref:`DEFAULT_NO_LOG <DEFAULT_NO_LOG>`



.. envvar:: ANSIBLE_NO_TARGET_SYSLOG

    Toggle Ansible logging to syslog on the target when it executes tasks.

    See also :ref:`DEFAULT_NO_TARGET_SYSLOG <DEFAULT_NO_TARGET_SYSLOG>`



.. envvar:: ANSIBLE_NULL_REPRESENTATION

    What templating should return as a 'null' value. When not set it will let Jinja2 decide.

    See also :ref:`DEFAULT_NULL_REPRESENTATION <DEFAULT_NULL_REPRESENTATION>`



.. envvar:: ANSIBLE_POLL_INTERVAL

    For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how often to check back on the status of those tasks when an explicit poll interval is not supplied. The default is a reasonably moderate 15 seconds which is a tradeoff between checking in frequently and providing a quick turnaround when something may have completed.

    See also :ref:`DEFAULT_POLL_INTERVAL <DEFAULT_POLL_INTERVAL>`



.. envvar:: ANSIBLE_PRIVATE_KEY_FILE

    Option for connections using a certificate or key file to authenticate, rather than an agent or passwords, you can set the default value here to avoid re-specifying --private-key with every invocation.

    See also :ref:`DEFAULT_PRIVATE_KEY_FILE <DEFAULT_PRIVATE_KEY_FILE>`



.. envvar:: ANSIBLE_PRIVATE_ROLE_VARS

    Makes role variables inaccessible from other roles.This was introduced as a way to reset role variables to default values if a role is used more than once in a playbook.

    See also :ref:`DEFAULT_PRIVATE_ROLE_VARS <DEFAULT_PRIVATE_ROLE_VARS>`



.. envvar:: ANSIBLE_REMOTE_PORT

    Port to use in remote connections, when blank it will use the connection plugin default.

    See also :ref:`DEFAULT_REMOTE_PORT <DEFAULT_REMOTE_PORT>`



.. envvar:: ANSIBLE_REMOTE_USER

    Sets the login user for the target machinesWhen blank it uses the connection plugin's default, normally the user currently executing Ansible.

    See also :ref:`DEFAULT_REMOTE_USER <DEFAULT_REMOTE_USER>`



.. envvar:: ANSIBLE_ROLES_PATH

    Colon separated paths in which Ansible will search for Roles.

    See also :ref:`DEFAULT_ROLES_PATH <DEFAULT_ROLES_PATH>`



.. envvar:: ANSIBLE_SCP_IF_SSH

    Preferred method to use when transferring files over ssh.When set to smart, Ansible will try them until one succeeds or they all fail.If set to True, it will force 'scp', if False it will use 'sftp'.

    See also :ref:`DEFAULT_SCP_IF_SSH <DEFAULT_SCP_IF_SSH>`



.. envvar:: ANSIBLE_SELINUX_SPECIAL_FS

    Some filesystems do not support safe operations and/or return inconsistent errors, this setting makes Ansible 'tolerate' those in the list w/o causing fatal errors.Data corruption may occur and writes are not always verified when a filesystem is in the list.

    See also :ref:`DEFAULT_SELINUX_SPECIAL_FS <DEFAULT_SELINUX_SPECIAL_FS>`

    :Version Added: 2.9


.. envvar:: ANSIBLE_SFTP_BATCH_MODE


    See also :ref:`DEFAULT_SFTP_BATCH_MODE <DEFAULT_SFTP_BATCH_MODE>`



.. envvar:: ANSIBLE_SQUASH_ACTIONS

    Ansible can optimise actions that call modules that support list parameters when using ``with_`` looping. Instead of calling the module once for each item, the module is called once with the full list.The default value for this setting is only for certain package managers, but it can be used for any module.Currently, this is only supported for modules that have a name or pkg parameter, and only when the item is the only thing being passed to the parameter.

    See also :ref:`DEFAULT_SQUASH_ACTIONS <DEFAULT_SQUASH_ACTIONS>`



.. envvar:: ANSIBLE_SSH_TRANSFER_METHOD

    unused?

    See also :ref:`DEFAULT_SSH_TRANSFER_METHOD <DEFAULT_SSH_TRANSFER_METHOD>`



.. envvar:: ANSIBLE_STDOUT_CALLBACK

    Set the main callback used to display Ansible output, you can only have one at a time.You can have many other callbacks, but just one can be in charge of stdout.

    See also :ref:`DEFAULT_STDOUT_CALLBACK <DEFAULT_STDOUT_CALLBACK>`



.. envvar:: ANSIBLE_ENABLE_TASK_DEBUGGER

    Whether or not to enable the task debugger, this previously was done as a strategy plugin.Now all strategy plugins can inherit this behavior. The debugger defaults to activating whena task is failed on unreachable. Use the debugger keyword for more flexibility.

    See also :ref:`ENABLE_TASK_DEBUGGER <ENABLE_TASK_DEBUGGER>`



.. envvar:: ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS

    This option defines whether the task debugger will be invoked on a failed task when ignore_errors=True is specified.True specifies that the debugger will honor ignore_errors, False will not honor ignore_errors.

    See also :ref:`TASK_DEBUGGER_IGNORE_ERRORS <TASK_DEBUGGER_IGNORE_ERRORS>`



.. envvar:: ANSIBLE_STRATEGY

    Set the default strategy used for plays.

    See also :ref:`DEFAULT_STRATEGY <DEFAULT_STRATEGY>`



.. envvar:: ANSIBLE_STRATEGY_PLUGINS

    Colon separated paths in which Ansible will search for Strategy Plugins.

    See also :ref:`DEFAULT_STRATEGY_PLUGIN_PATH <DEFAULT_STRATEGY_PLUGIN_PATH>`



.. envvar:: ANSIBLE_SU

    Toggle the use of "su" for tasks.

    See also :ref:`DEFAULT_SU <DEFAULT_SU>`



.. envvar:: ANSIBLE_SYSLOG_FACILITY

    Syslog facility to use when Ansible logs to the remote target

    See also :ref:`DEFAULT_SYSLOG_FACILITY <DEFAULT_SYSLOG_FACILITY>`



.. envvar:: ANSIBLE_TASK_INCLUDES_STATIC

    The `include` tasks can be static or dynamic, this toggles the default expected behaviour if autodetection fails and it is not explicitly set in task.

    See also :ref:`DEFAULT_TASK_INCLUDES_STATIC <DEFAULT_TASK_INCLUDES_STATIC>`



.. envvar:: ANSIBLE_TERMINAL_PLUGINS

    Colon separated paths in which Ansible will search for Terminal Plugins.

    See also :ref:`DEFAULT_TERMINAL_PLUGIN_PATH <DEFAULT_TERMINAL_PLUGIN_PATH>`



.. envvar:: ANSIBLE_TEST_PLUGINS

    Colon separated paths in which Ansible will search for Jinja2 Test Plugins.

    See also :ref:`DEFAULT_TEST_PLUGIN_PATH <DEFAULT_TEST_PLUGIN_PATH>`



.. envvar:: ANSIBLE_TIMEOUT

    This is the default timeout for connection plugins to use.

    See also :ref:`DEFAULT_TIMEOUT <DEFAULT_TIMEOUT>`



.. envvar:: ANSIBLE_TRANSPORT

    Default connection plugin to use, the 'smart' option will toggle between 'ssh' and 'paramiko' depending on controller OS and ssh versions

    See also :ref:`DEFAULT_TRANSPORT <DEFAULT_TRANSPORT>`



.. envvar:: ANSIBLE_ERROR_ON_UNDEFINED_VARS

    When True, this causes ansible templating to fail steps that reference variable names that are likely typoed.Otherwise, any '{{ template_expression }}' that contains undefined variables will be rendered in a template or ansible action line exactly as written.

    See also :ref:`DEFAULT_UNDEFINED_VAR_BEHAVIOR <DEFAULT_UNDEFINED_VAR_BEHAVIOR>`



.. envvar:: ANSIBLE_VARS_PLUGINS

    Colon separated paths in which Ansible will search for Vars Plugins.

    See also :ref:`DEFAULT_VARS_PLUGIN_PATH <DEFAULT_VARS_PLUGIN_PATH>`



.. envvar:: ANSIBLE_VAULT_ID_MATCH

    If true, decrypting vaults with a vault id will only try the password from the matching vault-id

    See also :ref:`DEFAULT_VAULT_ID_MATCH <DEFAULT_VAULT_ID_MATCH>`



.. envvar:: ANSIBLE_VAULT_IDENTITY

    The label to use for the default vault id label in cases where a vault id label is not provided

    See also :ref:`DEFAULT_VAULT_IDENTITY <DEFAULT_VAULT_IDENTITY>`



.. envvar:: ANSIBLE_VAULT_ENCRYPT_IDENTITY

    The vault_id to use for encrypting by default. If multiple vault_ids are provided, this specifies which to use for encryption. The --encrypt-vault-id cli option overrides the configured value.

    See also :ref:`DEFAULT_VAULT_ENCRYPT_IDENTITY <DEFAULT_VAULT_ENCRYPT_IDENTITY>`



.. envvar:: ANSIBLE_VAULT_IDENTITY_LIST

    A list of vault-ids to use by default. Equivalent to multiple --vault-id args. Vault-ids are tried in order.

    See also :ref:`DEFAULT_VAULT_IDENTITY_LIST <DEFAULT_VAULT_IDENTITY_LIST>`



.. envvar:: ANSIBLE_VAULT_PASSWORD_FILE

    The vault password file to use. Equivalent to --vault-password-file or --vault-id

    See also :ref:`DEFAULT_VAULT_PASSWORD_FILE <DEFAULT_VAULT_PASSWORD_FILE>`



.. envvar:: ANSIBLE_VERBOSITY

    Sets the default verbosity, equivalent to the number of ``-v`` passed in the command line.

    See also :ref:`DEFAULT_VERBOSITY <DEFAULT_VERBOSITY>`



.. envvar:: ANSIBLE_DEPRECATION_WARNINGS

    Toggle to control the showing of deprecation warnings

    See also :ref:`DEPRECATION_WARNINGS <DEPRECATION_WARNINGS>`



.. envvar:: ANSIBLE_DIFF_ALWAYS

    Configuration toggle to tell modules to show differences when in 'changed' status, equivalent to ``--diff``.

    See also :ref:`DIFF_ALWAYS <DIFF_ALWAYS>`



.. envvar:: ANSIBLE_DIFF_CONTEXT

    How many lines of context to show when displaying the differences between files.

    See also :ref:`DIFF_CONTEXT <DIFF_CONTEXT>`



.. envvar:: ANSIBLE_DISPLAY_ARGS_TO_STDOUT

    Normally ``ansible-playbook`` will print a header for each task that is run. These headers will contain the name: field from the task if you specified one. If you didn't then ``ansible-playbook`` uses the task's action to help you tell which task is presently running. Sometimes you run many of the same action and so you want more information about the task to differentiate it from others of the same action. If you set this variable to True in the config then ``ansible-playbook`` will also include the task's arguments in the header.This setting defaults to False because there is a chance that you have sensitive values in your parameters and you do not want those to be printed.If you set this to True you should be sure that you have secured your environment's stdout (no one can shoulder surf your screen and you aren't saving stdout to an insecure file) or made sure that all of your playbooks explicitly added the ``no_log: True`` parameter to tasks which have sensitive values See How do I keep secret data in my playbook? for more information.

    See also :ref:`DISPLAY_ARGS_TO_STDOUT <DISPLAY_ARGS_TO_STDOUT>`



.. envvar:: DISPLAY_SKIPPED_HOSTS

    Toggle to control displaying skipped task/host entries in a task in the default callback

    See also :ref:`DISPLAY_SKIPPED_HOSTS <DISPLAY_SKIPPED_HOSTS>`

    :Deprecated in: 2.12
    :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
    :Deprecated alternatives: the ``ANSIBLE_DISPLAY_SKIPPED_HOSTS`` environment variable

.. envvar:: ANSIBLE_DISPLAY_SKIPPED_HOSTS

    Toggle to control displaying skipped task/host entries in a task in the default callback

    See also :ref:`DISPLAY_SKIPPED_HOSTS <DISPLAY_SKIPPED_HOSTS>`




.. envvar:: ANSIBLE_DUPLICATE_YAML_DICT_KEY

    By default Ansible will issue a warning when a duplicate dict key is encountered in YAML.These warnings can be silenced by adjusting this setting to False.

    See also :ref:`DUPLICATE_YAML_DICT_KEY <DUPLICATE_YAML_DICT_KEY>`



.. envvar:: ANSIBLE_ERROR_ON_MISSING_HANDLER

    Toggle to allow missing handlers to become a warning instead of an error when notifying.

    See also :ref:`ERROR_ON_MISSING_HANDLER <ERROR_ON_MISSING_HANDLER>`



.. envvar:: ANSIBLE_CONNECTION_FACTS_MODULES

    Which modules to run during a play's fact gathering stage based on connection

    See also :ref:`CONNECTION_FACTS_MODULES <CONNECTION_FACTS_MODULES>`



.. envvar:: ANSIBLE_FACTS_MODULES

    Which modules to run during a play's fact gathering stage, using the default of 'smart' will try to figure it out based on connection type.

    See also :ref:`FACTS_MODULES <FACTS_MODULES>`



.. envvar:: ANSIBLE_GALAXY_IGNORE

    If set to yes, ansible-galaxy will not validate TLS certificates. This can be useful for testing against a server with a self-signed certificate.

    See also :ref:`GALAXY_IGNORE_CERTS <GALAXY_IGNORE_CERTS>`



.. envvar:: ANSIBLE_GALAXY_ROLE_SKELETON

    Role or collection skeleton directory to use as a template for the ``init`` action in ``ansible-galaxy``, same as ``--role-skeleton``.

    See also :ref:`GALAXY_ROLE_SKELETON <GALAXY_ROLE_SKELETON>`



.. envvar:: ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE

    patterns of files to ignore inside a Galaxy role or collection skeleton directory

    See also :ref:`GALAXY_ROLE_SKELETON_IGNORE <GALAXY_ROLE_SKELETON_IGNORE>`



.. envvar:: ANSIBLE_GALAXY_SERVER

    URL to prepend when roles don't specify the full URI, assume they are referencing this server as the source.

    See also :ref:`GALAXY_SERVER <GALAXY_SERVER>`



.. envvar:: ANSIBLE_GALAXY_SERVER_LIST

    A list of Galaxy servers to use when installing a collection.The value corresponds to the config ini header ``[galaxy_server.{{item}}]`` which defines the server details.See :ref:`galaxy_server_config` for more details on how to define a Galaxy server.The order of servers in this list is used to as the order in which a collection is resolved.Setting this config option will ignore the :ref:`galaxy_server` config option.

    See also :ref:`GALAXY_SERVER_LIST <GALAXY_SERVER_LIST>`



.. envvar:: ANSIBLE_GALAXY_TOKEN_PATH

    Local path to galaxy access token file

    See also :ref:`GALAXY_TOKEN_PATH <GALAXY_TOKEN_PATH>`



.. envvar:: ANSIBLE_HOST_KEY_CHECKING

    Set this to "False" if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

    See also :ref:`HOST_KEY_CHECKING <HOST_KEY_CHECKING>`



.. envvar:: ANSIBLE_HOST_PATTERN_MISMATCH

    This setting changes the behaviour of mismatched host patterns, it allows you to force a fatal error, a warning or just ignore it

    See also :ref:`HOST_PATTERN_MISMATCH <HOST_PATTERN_MISMATCH>`



.. envvar:: ANSIBLE_PYTHON_INTERPRETER

    Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode. Supported discovery modes are ``auto``, ``auto_silent``, and ``auto_legacy`` (the default). All discovery modes employ a lookup table to use the included system Python (on distributions known to include one), falling back to a fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed later may change which one is used). This warning behavior can be disabled by setting ``auto_silent``. The default value of ``auto_legacy`` provides all the same behavior, but for backwards-compatibility with older Ansible releases that always defaulted to ``/usr/bin/python``, will use that interpreter if present (and issue a warning that the default behavior will change to that of ``auto`` in a future Ansible release.

    See also :ref:`INTERPRETER_PYTHON <INTERPRETER_PYTHON>`





.. envvar:: ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS

    Make ansible transform invalid characters in group names supplied by inventory sources.If 'never' it will allow for the group name but warn about the issue.When 'ignore', it does the same as 'never', without issuing a warning.When 'always' it will replace any invalid charachters with '_' (underscore) and warn the userWhen 'silently', it does the same as 'always', without issuing a warning.

    See also :ref:`TRANSFORM_INVALID_GROUP_CHARS <TRANSFORM_INVALID_GROUP_CHARS>`



.. envvar:: ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED

    If 'false', invalid attributes for a task will result in warnings instead of errors

    See also :ref:`INVALID_TASK_ATTRIBUTE_FAILED <INVALID_TASK_ATTRIBUTE_FAILED>`



.. envvar:: ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED

    If 'true', it is a fatal error when any given inventory source cannot be successfully parsed by any available inventory plugin; otherwise, this situation only attracts a warning.


    See also :ref:`INVENTORY_ANY_UNPARSED_IS_FAILED <INVENTORY_ANY_UNPARSED_IS_FAILED>`



.. envvar:: ANSIBLE_INVENTORY_CACHE

    Toggle to turn on inventory caching

    See also :ref:`INVENTORY_CACHE_ENABLED <INVENTORY_CACHE_ENABLED>`



.. envvar:: ANSIBLE_INVENTORY_CACHE_PLUGIN

    The plugin for caching inventory. If INVENTORY_CACHE_PLUGIN is not provided CACHE_PLUGIN can be used instead.

    See also :ref:`INVENTORY_CACHE_PLUGIN <INVENTORY_CACHE_PLUGIN>`



.. envvar:: ANSIBLE_INVENTORY_CACHE_CONNECTION

    The inventory cache connection. If INVENTORY_CACHE_PLUGIN_CONNECTION is not provided CACHE_PLUGIN_CONNECTION can be used instead.

    See also :ref:`INVENTORY_CACHE_PLUGIN_CONNECTION <INVENTORY_CACHE_PLUGIN_CONNECTION>`



.. envvar:: ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX

    The table prefix for the cache plugin. If INVENTORY_CACHE_PLUGIN_PREFIX is not provided CACHE_PLUGIN_PREFIX can be used instead.

    See also :ref:`INVENTORY_CACHE_PLUGIN_PREFIX <INVENTORY_CACHE_PLUGIN_PREFIX>`



.. envvar:: ANSIBLE_INVENTORY_CACHE_TIMEOUT

    Expiration timeout for the inventory cache plugin data. If INVENTORY_CACHE_TIMEOUT is not provided CACHE_TIMEOUT can be used instead.

    See also :ref:`INVENTORY_CACHE_TIMEOUT <INVENTORY_CACHE_TIMEOUT>`



.. envvar:: ANSIBLE_INVENTORY_ENABLED

    List of enabled inventory plugins, it also determines the order in which they are used.

    See also :ref:`INVENTORY_ENABLED <INVENTORY_ENABLED>`



.. envvar:: ANSIBLE_INVENTORY_EXPORT

    Controls if ansible-inventory will accurately reflect Ansible's view into inventory or its optimized for exporting.

    See also :ref:`INVENTORY_EXPORT <INVENTORY_EXPORT>`



.. envvar:: ANSIBLE_INVENTORY_IGNORE

    List of extensions to ignore when using a directory as an inventory source

    See also :ref:`INVENTORY_IGNORE_EXTS <INVENTORY_IGNORE_EXTS>`



.. envvar:: ANSIBLE_INVENTORY_IGNORE_REGEX

    List of patterns to ignore when using a directory as an inventory source

    See also :ref:`INVENTORY_IGNORE_PATTERNS <INVENTORY_IGNORE_PATTERNS>`



.. envvar:: ANSIBLE_INVENTORY_UNPARSED_FAILED

    If 'true' it is a fatal error if every single potential inventory source fails to parse, otherwise this situation will only attract a warning.


    See also :ref:`INVENTORY_UNPARSED_IS_FAILED <INVENTORY_UNPARSED_IS_FAILED>`



.. envvar:: ANSIBLE_MAX_DIFF_SIZE

    Maximum size of files to be considered for diff display

    See also :ref:`MAX_FILE_SIZE_FOR_DIFF <MAX_FILE_SIZE_FOR_DIFF>`



.. envvar:: NETWORK_GROUP_MODULES


    See also :ref:`NETWORK_GROUP_MODULES <NETWORK_GROUP_MODULES>`

    :Deprecated in: 2.12
    :Deprecated detail: environment variables without ``ANSIBLE_`` prefix are deprecated
    :Deprecated alternatives: the ``ANSIBLE_NETWORK_GROUP_MODULES`` environment variable

.. envvar:: ANSIBLE_NETWORK_GROUP_MODULES


    See also :ref:`NETWORK_GROUP_MODULES <NETWORK_GROUP_MODULES>`



.. envvar:: ANSIBLE_INJECT_FACT_VARS

    Facts are available inside the `ansible_facts` variable, this setting also pushes them as their own vars in the main namespace.Unlike inside the `ansible_facts` dictionary, these will have an `ansible_` prefix.

    See also :ref:`INJECT_FACTS_AS_VARS <INJECT_FACTS_AS_VARS>`



.. envvar:: ANSIBLE_OLD_PLUGIN_CACHE_CLEAR

    Previouslly Ansible would only clear some of the plugin loading caches when loading new roles, this led to some behaviours in which a plugin loaded in prevoius plays would be unexpectedly 'sticky'. This setting allows to return to that behaviour.

    See also :ref:`OLD_PLUGIN_CACHE_CLEARING <OLD_PLUGIN_CACHE_CLEARING>`



.. envvar:: ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD


    See also :ref:`PARAMIKO_HOST_KEY_AUTO_ADD <PARAMIKO_HOST_KEY_AUTO_ADD>`



.. envvar:: ANSIBLE_PARAMIKO_LOOK_FOR_KEYS


    See also :ref:`PARAMIKO_LOOK_FOR_KEYS <PARAMIKO_LOOK_FOR_KEYS>`



.. envvar:: ANSIBLE_PERSISTENT_CONTROL_PATH_DIR

    Path to socket to be used by the connection persistence system.

    See also :ref:`PERSISTENT_CONTROL_PATH_DIR <PERSISTENT_CONTROL_PATH_DIR>`



.. envvar:: ANSIBLE_PERSISTENT_CONNECT_TIMEOUT

    This controls how long the persistent connection will remain idle before it is destroyed.

    See also :ref:`PERSISTENT_CONNECT_TIMEOUT <PERSISTENT_CONNECT_TIMEOUT>`



.. envvar:: ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT

    This controls the retry timeout for persistent connection to connect to the local domain socket.

    See also :ref:`PERSISTENT_CONNECT_RETRY_TIMEOUT <PERSISTENT_CONNECT_RETRY_TIMEOUT>`



.. envvar:: ANSIBLE_PERSISTENT_COMMAND_TIMEOUT

    This controls the amount of time to wait for response from remote device before timing out persistent connection.

    See also :ref:`PERSISTENT_COMMAND_TIMEOUT <PERSISTENT_COMMAND_TIMEOUT>`



.. envvar:: ANSIBLE_PLAYBOOK_DIR

    A number of non-playbook CLIs have a ``--playbook-dir`` argument; this sets the default value for it.

    See also :ref:`PLAYBOOK_DIR <PLAYBOOK_DIR>`



.. envvar:: ANSIBLE_PLAYBOOK_VARS_ROOT

    This sets which playbook dirs will be used as a root to process vars plugins, which includes finding host_vars/group_varsThe ``top`` option follows the traditional behaviour of using the top playbook in the chain to find the root directory.The ``bottom`` option follows the 2.4.0 behaviour of using the current playbook to find the root directory.The ``all`` option examines from the first parent to the current playbook.

    See also :ref:`PLAYBOOK_VARS_ROOT <PLAYBOOK_VARS_ROOT>`




.. envvar:: ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE

    Attempts to set RLIMIT_NOFILE soft limit to the specified value when executing Python modules (can speed up subprocess usage on Python 2.x. See https://bugs.python.org/issue11284). The value will be limited by the existing hard limit. Default value of 0 does not attempt to adjust existing system-defined limits.

    See also :ref:`PYTHON_MODULE_RLIMIT_NOFILE <PYTHON_MODULE_RLIMIT_NOFILE>`



.. envvar:: ANSIBLE_RETRY_FILES_ENABLED

    This controls whether a failed Ansible playbook should create a .retry file.

    See also :ref:`RETRY_FILES_ENABLED <RETRY_FILES_ENABLED>`



.. envvar:: ANSIBLE_RETRY_FILES_SAVE_PATH

    This sets the path in which Ansible will save .retry files when a playbook fails and retry files are enabled.

    See also :ref:`RETRY_FILES_SAVE_PATH <RETRY_FILES_SAVE_PATH>`



.. envvar:: ANSIBLE_SHOW_CUSTOM_STATS

    This adds the custom stats set via the set_stats plugin to the default output

    See also :ref:`SHOW_CUSTOM_STATS <SHOW_CUSTOM_STATS>`



.. envvar:: ANSIBLE_STRING_TYPE_FILTERS

    This list of filters avoids 'type conversion' when templating variablesUseful when you want to avoid conversion into lists or dictionaries for JSON strings, for example.

    See also :ref:`STRING_TYPE_FILTERS <STRING_TYPE_FILTERS>`



.. envvar:: ANSIBLE_SYSTEM_WARNINGS

    Allows disabling of warnings related to potential issues on the system running ansible itself (not on the managed hosts)These may include warnings about 3rd party packages or other conditions that should be resolved if possible.

    See also :ref:`SYSTEM_WARNINGS <SYSTEM_WARNINGS>`



.. envvar:: ANSIBLE_RUN_TAGS

    default list of tags to run in your plays, Skip Tags has precedence.

    See also :ref:`TAGS_RUN <TAGS_RUN>`



.. envvar:: ANSIBLE_SKIP_TAGS

    default list of tags to skip in your plays, has precedence over Run Tags

    See also :ref:`TAGS_SKIP <TAGS_SKIP>`



.. envvar:: ANSIBLE_USE_PERSISTENT_CONNECTIONS

    Toggles the use of persistence for connections.

    See also :ref:`USE_PERSISTENT_CONNECTIONS <USE_PERSISTENT_CONNECTIONS>`



.. envvar:: ANSIBLE_PRECEDENCE

    Allows to change the group variable precedence merge order.

    See also :ref:`VARIABLE_PRECEDENCE <VARIABLE_PRECEDENCE>`



.. envvar:: ANSIBLE_YAML_FILENAME_EXT

    Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these.This affects vars_files, include_vars, inventory and vars plugins among others.

    See also :ref:`YAML_FILENAME_EXTENSIONS <YAML_FILENAME_EXTENSIONS>`



.. envvar:: ANSIBLE_NETCONF_SSH_CONFIG

    This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.

    See also :ref:`NETCONF_SSH_CONFIG <NETCONF_SSH_CONFIG>`



.. envvar:: ANSIBLE_STRING_CONVERSION_ACTION

    Action to take when a module parameter value is converted to a string (this does not affect variables). For string parameters, values such as '1.00', "['a', 'b',]", and 'yes', 'y', etc. will be converted by the YAML parser unless fully quoted.Valid options are 'error', 'warn', and 'ignore'.Since 2.8, this option defaults to 'warn' but will change to 'error' in 2.12.

    See also :ref:`STRING_CONVERSION_ACTION <STRING_CONVERSION_ACTION>`



.. envvar:: ANSIBLE_VERBOSE_TO_STDERR

    Force 'verbose' option to use stderr instead of stdout

    See also :ref:`VERBOSE_TO_STDERR <VERBOSE_TO_STDERR>`




