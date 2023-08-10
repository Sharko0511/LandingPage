# -*- coding: utf-8 -*-
# from odoo import http


# class LinkShop(http.Controller):
#     @http.route('/link_shop/link_shop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/link_shop/link_shop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('link_shop.listing', {
#             'root': '/link_shop/link_shop',
#             'objects': http.request.env['link_shop.link_shop'].search([]),
#         })

#     @http.route('/link_shop/link_shop/objects/<model("link_shop.link_shop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('link_shop.object', {
#             'object': obj
#         })
