# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

import ptvsd

PARAMS = [
    ("secret", "remote_debug.secret"),
    ("host", "remote_debug.host"),
    ("port", "remote_debug.port"),
]

class RemoteDebugSettings(models.Model):
    _name = 'remote.debug.settings'
    _inherit = 'res.config.settings'

    secret = fields.Char(string="Secret")
    host = fields.Char(string="Host")
    port  = fields.Char(string="Port")

    @api.multi
    def set_params(self):
        self.ensure_one()

        for field_name, key_name in PARAMS:
            value = getattr(self, field_name, '').strip()
            self.env['ir.config_parameter'].set_param(key_name, value)

    @api.multi
    def get_default_params(self, fields):
        res = {}
        for field_name, key_name in PARAMS:
            res[field_name] = self.env['ir.config_parameter'].get_param(key_name, '').strip()
        return res

    @api.multi
    def start_debug(self):
        ptvsd.enable_attach("my_secret", address=("0.0.0.0", 6899))
        

