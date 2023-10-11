from odoo import models, fields, api


class DailyRevenue(models.Model):
    _name = 'daily.revenue'
    _description = 'Daily Revenue Model'

    shop_id = fields.Many2one('link.shop', string='Shop Code')
    daily_shop_name = fields.Char(string='Shop Name')
    shop_rev = fields.Float(string='Discount')
    creation_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
    trade_volume = fields.Float(string='Total', invisible=True)
    total_transfer = fields.Float(string='Total Transfer', compute='_compute_total_transfer')

    @api.onchange('shop_id')
    def _get_shop_rev(self):
        if self.shop_id:
            self.shop_rev = self.shop_id.discount_percent
        else:
            self.shop_rev = 0

    @api.onchange('shop_id')
    def _get_daily_shop_name(self):
        if self.shop_id:
            self.daily_shop_name = self.shop_id.name
        else:
            self.daily_shop_name = ''

    @api.depends('trade_volume', 'shop_rev', 'shop_id')
    @api.onchange('shop_id', 'trade_volume', 'shop_rev')
    def _compute_total_transfer(self):
        for record in self:
            record.total_transfer = record.trade_volume * record.shop_rev / 100
