# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Module name",
    "summary": "Module summary",
    "version": "9.0.1.0.0",
    "category": "Tools",
    "website": "https://github.com/michotm/remote_debug",
    "author": "<Michael Michot>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "post_load": "post_load",
    "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": ['ptvsd'],
        "bin": [],
    },
    "depends": [
        "base",
        "base_setup"
    ],
    "data": [
        "views/remote_debug_data.xml",
    ],
    "demo": [
        "demo/remote_debug_demo.xml",
    ],
    "qweb": [
    ]
}