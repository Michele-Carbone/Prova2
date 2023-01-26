# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class print_product_labels(models.Model):
#     _name = 'print_product_labels.print_product_labels'
#     _description = 'print_product_labels.print_product_labels'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     cliente = fields.Many2one('res.partner', string='Cliente')
#     prodotto = fields.Many2one('product.template', string='Prodotto')
# #
# #     @api.depends('value')
# #     def _value_pc(self):
# #         for record in self:
# #             record.value2 = float(record.value) / 100


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_price(self):
        pricelist_id = self.env['product.pricelist'].search([], limit=1)
        price = pricelist_id.get_product_price(self, 1, False)
        price_tax_included = self.taxes_id.compute_all(price, handle_price_include=False)['total_included']
        return '€ ' + str('%.2f' % round(price_tax_included, 2)).replace('.', ',')



