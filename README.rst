.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==============
{Remote debug}
==============

This module allow you to remote debug Odoo with ptvsd 

Installation
============

To install this module, you need to:

#. Do this ...

Configuration
=============

To configure this module, you need to:

#. Go to configuration

set the secret and the host:port

Usage
=====

To use this module, you need to:

[VSCode][] debugger. If you use this editor with its python module, you will
find it useful.

.vscode/launch.json
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Attach to debug in devel.yaml",
            "type": "python",
            "request": "attach",
            "localRoot": "${workspaceRoot}/odoo",
            "remoteRoot": "/opt/odoo",
            "port": 6899,
            "secret": "my_secret",
            "host": "localhost"
        }
    ]
}
```
Known issues / Roadmap
======================

* ...

Bug Tracker
===========

Credits
=======

Images
------


Contributors
------------

* Michael Michot <michael.michot@noviat.com> (http://www.noviat.com)

Do not contact contributors directly about support or help with technical issues.
