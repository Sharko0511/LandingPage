from odoo import models, fields, api


class DailyRevenue(models.Model):
    _name = 'daily.revenue'
    _description = 'Daily Revenue Model'

    shop_id = fields.Many2one('link.shop', string='Shop Code')
    daily_shop_name = fields.Char(string='Shop Name', compute='_get_daily_shop_name')
    shop_rev = fields.Float(string='Discount', compute='_get_shop_rev')
    creation_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
    trade_volume = fields.Float(string='Total', invisible=True)
    total_transfer = fields.Float(string='Total Transfer', compute='_compute_total_transfer')

    @api.depends('shop_id')
    @api.onchange('shop_id')
    def _get_shop_rev(self):
        for record in self:
            if record.shop_id:
                self.shop_rev = record.shop_id.discount_percent
            else:
                self.shop_rev = 0

    def _get_daily_shop_name(self):
        for record in self:
            if record.shop_id:
                self.daily_shop_name = record.shop_id.name
            else:
                self.daily_shop_name = ''

    @api.depends('trade_volume', 'shop_rev', 'shop_id')
    @api.onchange('shop_id', 'trade_volume', 'shop_rev')
    def _compute_total_transfer(self):
        for record in self:
            record.total_transfer = record.trade_volume * record.shop_rev / 100

    def compute_transfer(self):
        return self._compute_total_transfer()

    @api.model
    def create(self, vals):
        vals["trade_volume"] = float(vals["trade_volume"])
        vals["total_transfer"] = vals["trade_volume"] * float(self.shop_rev)
        res = super(DailyRevenue, self).create(vals)
        return res
