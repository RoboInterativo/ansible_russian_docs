:source: commands/command.py

:orphan:

.. _command_module:


command -- Execute commands on targets
++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The ``command`` module takes the command name followed by a list of space-delimited arguments.
- The given command will be executed on all selected nodes.
- The command(s) will not be processed through the shell, so variables like ``$HOME`` and operations like ``"<"``, ``">"``, ``"|"``, ``";"`` and ``"&"`` will not work. Use the :ref:`shell <shell_module>` module if you need these features.
- To create ``command`` tasks that are easier to read than the ones using space-delimited arguments, pass parameters using the ``args`` `task keyword <../reference_appendices/playbooks_keywords.html#task>`_ or use ``cmd`` parameter.
- Either a free form command or ``cmd`` parameter is required, see the examples.
- For Windows targets, use the :ref:`win_command <win_command_module>` module instead.




Parameters
----------

.. raw:: html

    <table   border=1 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Параметр</th>
            <th>Значения/<br><font color="blue">По умолчанию</font></th>
                        <th width="80%">Comments</th>
        </tr>
                    <tr>
                    <td " colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-argv"></div>
                    <b>argv</b>
                    <a class="ansibleOptionLink" href="#parameter-argv" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                                                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.6</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Passes the command as a list rather than a string.</div>
                                            <div>Use <code>argv</code> to avoid quoting values that would otherwise be interpreted incorrectly (for example &quot;user name&quot;).</div>
                                            <div>Only the string or the list form can be provided, not both.  One or the other must be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-chdir"></div>
                    <b>chdir</b>
                    <a class="ansibleOptionLink" href="#parameter-chdir" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Change into this directory before running the command.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cmd"></div>
                    <b>cmd</b>
                    <a class="ansibleOptionLink" href="#parameter-cmd" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The command to run.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-creates"></div>
                    <b>creates</b>
                    <a class="ansibleOptionLink" href="#parameter-creates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A filename or (since 2.0) glob pattern. If it already exists, this step <b>won&#x27;t</b> be run.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-free_form"></div>
                    <b>free_form</b>
                    <a class="ansibleOptionLink" href="#parameter-free_form" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The command module takes a free form command to run.</div>
                                            <div>There is no actual parameter named &#x27;free form&#x27;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-removes"></div>
                    <b>removes</b>
                    <a class="ansibleOptionLink" href="#parameter-removes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A filename or (since 2.0) glob pattern. If it already exists, this step <b>will</b> be run.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-stdin"></div>
                    <b>stdin</b>
                    <a class="ansibleOptionLink" href="#parameter-stdin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.4</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Set the stdin of the command directly to the specified value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-stdin_add_newline"></div>
                    <b>stdin_add_newline</b>
                    <a class="ansibleOptionLink" href="#parameter-stdin_add_newline" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.8</div>                </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If set to <code>yes</code>, append a newline to stdin data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-strip_empty_ends"></div>
                    <b>strip_empty_ends</b>
                    <a class="ansibleOptionLink" href="#parameter-strip_empty_ends" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.8</div>                </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Strip empty lines from the end of stdout/stderr in result.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-warn"></div>
                    <b>warn</b>
                    <a class="ansibleOptionLink" href="#parameter-warn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Enable or disable task warnings.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
   - If you want to run a command through the shell (say you are using ``<``, ``>``, ``|``, etc), you actually want the :ref:`shell <shell_module>` module instead. Parsing shell metacharacters can lead to unexpected commands being executed if quoting is not done correctly so it is more secure to use the ``command`` module when possible.
   -  ``creates``, ``removes``, and ``chdir`` can be specified after the command. For instance, if you only want to run a command if a certain file does not exist, use this.
   - Check mode is supported when passing ``creates`` or ``removes``. If running in check mode and either of these are specified, the module will check for the existence of the file and report the correct changed status. If these are not supplied, the task will be skipped.
   - The ``executable`` parameter is removed since version 2.4. If you have a need for this parameter, use the :ref:`shell <shell_module>` module instead.
   - For Windows targets, use the :ref:`win_command <win_command_module>` module instead.
   - For rebooting systems, use the :ref:`reboot <reboot_module>` or :ref:`win_reboot <win_reboot_module>` module.


See Also
--------

.. seealso::

   :ref:`raw_module`
      The official documentation on the **raw** module.
   :ref:`script_module`
      The official documentation on the **script** module.
   :ref:`shell_module`
      The official documentation on the **shell** module.
   :ref:`win_command_module`
      The official documentation on the **win_command** module.


Examples
--------

.. code-block:: yaml+jinja


    - name: return motd to registered var
      command: cat /etc/motd
      register: mymotd

    - name: Run command if /path/to/database does not exist (without 'args' keyword).
      command: /usr/bin/make_database.sh db_user db_name creates=/path/to/database

    # 'args' is a task keyword, passed at the same level as the module
    - name: Run command if /path/to/database does not exist (with 'args' keyword).
      command: /usr/bin/make_database.sh db_user db_name
      args:
        creates: /path/to/database

    # 'cmd' is module parameter
    - name: Run command if /path/to/database does not exist (with 'cmd' parameter).
      command:
        cmd: /usr/bin/make_database.sh db_user db_name
        creates: /path/to/database

    - name: Change the working directory to somedir/ and run the command as db_owner if /path/to/database does not exist.
      command: /usr/bin/make_database.sh db_user db_name
      become: yes
      become_user: db_owner
      args:
        chdir: somedir/
        creates: /path/to/database

    # 'argv' is a parameter, indented one level from the module
    - name: Use 'argv' to send a command as a list - leave 'command' empty
      command:
        argv:
          - /usr/bin/make_database.sh
          - Username with whitespace
          - dbname with whitespace

    - name: safely use templated variable to run command. Always use the quote filter to avoid injection issues.
      command: cat {{ myfile|quote }}
      register: myoutput




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cmd"></div>
                    <b>cmd</b>
                    <a class="ansibleOptionLink" href="#return-cmd" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>the cmd that was run on the remote machine</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;echo&#x27;, &#x27;hello&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-delta"></div>
                    <b>delta</b>
                    <a class="ansibleOptionLink" href="#return-delta" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>cmd end time - cmd start time</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">0.001529</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-end"></div>
                    <b>end</b>
                    <a class="ansibleOptionLink" href="#return-end" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>cmd end time</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2017-09-29 22:03:48.084657</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-start"></div>
                    <b>start</b>
                    <a class="ansibleOptionLink" href="#return-start" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>cmd start time</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2017-09-29 22:03:48.083128</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




- This module is guaranteed to have backward compatible interface changes going forward. *[stableinterface]*


- This module is :ref:`maintained by the Ansible Core Team <modules_support>`. *[core]*

Red Hat Support
~~~~~~~~~~~~~~~

More information about Red Hat's support of this module is available from this `Red Hat Knowledge Base article <https://access.redhat.com/articles/3166901>`_.




Authors
~~~~~~~

- Ansible Core Team
- Michael DeHaan


.. hint::
    If you notice any issues in this documentation, you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/commands/command.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
