# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class StockMoveLineClassification(models.Model):
    _inherit = 'stock.move.line'
    _name = 'stock.move.line'

    line = fields.Boolean(
        string='Its Line', related='product_id.its_line')
    abc = fields.Selection(
        string='Classification ABC', related='product_id.classification_ABC')
    xyz = fields.Selection(
        string='Classification XYZ', related='product_id.classification_XYZ')
    categ = fields.Many2one(
        string='Category', related='product_id.categ_id')
    sellers = fields.One2many(
        string='Seller', related='product_id.seller_ids')
