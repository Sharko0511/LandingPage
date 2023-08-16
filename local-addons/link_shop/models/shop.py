from odoo import models, fields


class LinkShop(models.Model):
    _name = 'link.shop'
    _description = 'Shop Model'
    _rec_name = 'shop_code'

    name = fields.Char(string='Shop Name', required=True,)
    shop_code = fields.Char(string='Shop Code', required=True,)
    daily_rev_id = fields.One2many('daily.revenue', 'shop_id', string='Daily Revenue')
    discount_percent = fields.Float(string='Discount', required=True,)


