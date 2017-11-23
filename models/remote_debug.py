# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields


class RemoteDebug(models.Model):
    _inherit = "base.config.settings"

    secret = fields.Char(string="Secret")
    host = fields.Char(string="Host")
    port  = fields.Char(string="Port")
