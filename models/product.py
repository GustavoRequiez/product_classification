# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class ProductClasification(models.Model):
    _inherit = 'product.template'
    _name = 'product.template'

    its_line = fields.Boolean(string="its line")
    classification_ABC = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')], string="classification ABC", required=True)
    classification_XYZ = fields.Selection([
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z')], string="classification XYZ", required=True)
