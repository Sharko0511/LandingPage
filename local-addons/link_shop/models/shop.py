from odoo import models, fields, api

class Shop(models.Model):
    _name = 'link.shop'
    _description = 'Shop Model'

    name = fields.Char(string='Shop Name', required=True)
    shop_id = fields.Char(string='Shop ID', required=True)
    day_of_trade = fields.Date(string='Day')
    volume_of_trade = fields.Float(string='Total', invisible=True)
    percent_of_discount = fields.Float(string='Percent', invisible=False)
    total_transfer = fields.Float(string='Total Transfer', compute='_compute_total_transfer', store=True)

    @api.depends('volume_of_trade', 'percent_of_discount')
    def _compute_total_transfer(self):
        for record in self:
            record.total_transfer = record.volume_of_trade * record.percent_of_discount / 100
