# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tyre(models.Model):
    _name = 'tyre.tyre'
    _description = 'tyre.tyre'
    tyre_name=fields.Char()
    tyre_type=fields.Char()
    vehicle_assign=fields.Char()
    km_limit=fields.Integer()
    tyre_size=fields.Integer()
    tread_depth=fields.Float()

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
