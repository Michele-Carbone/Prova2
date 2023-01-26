# -*- coding: utf-8 -*-
# from odoo import http


# class PrintProductLabels(http.Controller):
#     @http.route('/print_product_labels/print_product_labels', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/print_product_labels/print_product_labels/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('print_product_labels.listing', {
#             'root': '/print_product_labels/print_product_labels',
#             'objects': http.request.env['print_product_labels.print_product_labels'].search([]),
#         })

#     @http.route('/print_product_labels/print_product_labels/objects/<model("print_product_labels.print_product_labels"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('print_product_labels.object', {
#             'object': obj
#         })
