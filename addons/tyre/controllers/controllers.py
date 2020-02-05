# -*- coding: utf-8 -*-
# from odoo import http


# class Tyre(http.Controller):
#     @http.route('/tyre/tyre/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tyre/tyre/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tyre.listing', {
#             'root': '/tyre/tyre',
#             'objects': http.request.env['tyre.tyre'].search([]),
#         })

#     @http.route('/tyre/tyre/objects/<model("tyre.tyre"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tyre.object', {
#             'object': obj
#         })
