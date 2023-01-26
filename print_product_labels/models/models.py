# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_price(self):
        pricelist_id = self.env['product.pricelist'].search([], limit=1)
        price = pricelist_id.get_product_price(self, 1, False)
        price_tax_included = self.taxes_id.compute_all(price, handle_price_include=False)['total_included']
        return '€ ' + str('%.2f' % round(price_tax_included, 2)).replace('.', ',')



