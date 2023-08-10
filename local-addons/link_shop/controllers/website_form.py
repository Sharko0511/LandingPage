from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/daily-report'], type='http', auth="user", website=True)
    def daily_report(self):
        print("Send..............")
        return request.render("link_shop.daily_report_form", {})

    @http.route(['/daily-report/submit'], type='http', auth="user", website=True)
    def daily_report_success(self, **kw):
        print("Data received")
        # request.env['link.shop'].sudo().creat(kw)
        return request.render("link_shop.user_thank", {})