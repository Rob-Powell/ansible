#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'core'}


DOCUMENTATION = '''
---
author:
    - "Ansible Core Team (@ansible)"
module: import_role
short_description: Import a role into a play
description:
     - Mostly like the `roles:` keyword this action loads a role, but it allows you to control when the tasks run in between other playbook tasks.
     - Most keyworkds, loops and conditionals will not be applied to this action, but to the imported tasks instead.
       If you want the opposite behaviour, use M(import_role) instead.
version_added: "2.4"
options:
  name:
    description:
      - The name of the role to be executed.
    required: True
  tasks_from:
    description:
      - "File to load from a Role's tasks/ directory."
    required: False
    default: 'main'
  vars_from:
    description:
      - "File to load from a Role's vars/ directory."
    required: False
    default: 'main'
  defaults_from:
    description:
      - "File to load from a Role's defaults/ directory."
    required: False
    default: 'main'
  allow_duplicates:
    description:
      - Overrides the role's metadata setting to allow using a role more than once with the same parameters.
    required: False
    default: True
  private:
    description:
      - If True the variables from defaults/ and vars/ in a role will not be made available to the rest of the play.
    default: None
notes:
    - Handlers are made available to the whole play.
'''

EXAMPLES = """
- hosts: all
  tasks:
    - import_role:
       name: myrole

    - name: Run tasks/other.yml instead of 'main'
      import_role:
        name: myrole
        tasks_from: other

    - name: Pass variables to role
      import_role:
        name: myrole
      vars:
        rolevar1: 'value from task'

    - name: Apply loop to each task in role
      import_role:
        name: myrole
      with_items:
        - '{{ roleinput1 }}'
        - '{{ roleinput2 }}'
      loop_control:
        loop_var: roleinputvar

    - name: Apply condition to each task in role
      import_role:
        name: myrole
      when: not idontwanttorun
"""

RETURN = """
# this module does not return anything except tasks to execute
"""
