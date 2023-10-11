from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/daily-report'], type='http', auth="user", website=True)
    def daily_report(self):
        return request.render("link_shop.daily_report_form", {})

    @http.route(['/daily-report/submit'], type='http', auth="user", website=True)
    def daily_report_success(self, **kw):
        shop_id = kw.get('shop_id')
        trade_volume = float(kw.get('trade_volume', 0.0))

        shop = request.env['link.shop'].sudo().browse(int(shop_id))

        shop_name = shop.name
        discount_percent = shop.discount_percent
        total_transfer = trade_volume * discount_percent / 100

        vals = {
            'shop_id': shop_id,
            'daily_shop_name': shop_name,
            'shop_rev': discount_percent,
            'trade_volume': trade_volume,
            'total_transfer': total_transfer,
        }
        request.env['daily.revenue'].sudo().create(vals)
        return request.render("link_shop.user_thank", {})

    @http.route(['/get-shop-name'], type='http', auth='public')
    def get_shop_name(self, shop_id):
        shop = http.request.env['link.shop'].sudo().browse(int(shop_id))
        return shop.name if shop else ''
