# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

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
