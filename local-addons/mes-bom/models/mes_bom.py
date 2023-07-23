# -*- coding: utf-8 -*-

from odoo import models, fields, api


# TO DO
# REFACTOR WORKER INTO DIFFERENT ADD-ON: MES-WORKER
class MrpWorkerGroup(models.Model):
    """Worker Group for BOM and other modules in MRP"""
    _name = 'worker.group'
    _rec_name = 'name'

    name = fields.Char(string='Group Name')
    code = fields.Char(string='Group Code')
    expertise_level = fields.Selection(selection=[('type_one', 'Type 1'),
                                                  ('type_two', 'Type 2'),
                                                  ('type_three', 'Type 3')])
    capacity = fields.Float(string='Capacity',
                            help='Capacity is in hours')
    worker_ids = fields.Many2many('res.users',
                                  string="Worker List")
    bom_id = fields.Many2one('mrp.bom', string='BOM')
    tech_process_id = fields.Many2one('tech.process', string='Technical Process')


class ProductProducts(models.Model):
    _inherit = 'product.product'

    tech_process_id = fields.Many2one('tech.process', string='Tech Process')
    manufacturing_type = fields.Selection(selection=[('sfg', 'SFG'), ('material', 'Material')],
                                          default='sfg')


class TechSequence(models.Model):
    """Technological Sequence to be added"""
    _name = 'tech.sequence'
    _rec_name = 'order'

    order = fields.Integer(string='Order')


class TechStage(models.Model):
    _name = 'tech.stage'
    _rec_name = 'name'
    _order = "sequence"

    name = fields.Char(string='Stage Name')
    code = fields.Char(sring='Stage Code')
    sub_stage = fields.Boolean('Sub Stage', default=False)
    machine_ids = fields.Char('Machines')
    worker_group_id = fields.Many2one('worker.group', 'Worker Group')
    description = fields.Char('Description')
    waste_percent = fields.Float('Waste Percent')
    consumption_percent = fields.Float('Consumption Percent', help='Only fill this field after select the machine in stage because consumption percent must follow the selected equipment/machine', default=0)
    sequence = fields.Many2one('tech.sequence', string='Sequence')
    tech_process_id = fields.Many2one('tech.process')
    consumption = fields.Float(string='Consumption in hours')
    sub_stage_ids = fields.One2many('tech.stage', 'parent_stage', string='Sub Stage Lines')
    parent_stage = fields.Many2one('tech.stage', string='Parent Stage')


class TechProcess(models.Model):
    _name = 'tech.process'
    _rec_name = 'name'
    _order = "sequence"

    name = fields.Char(string='Process Name')
    code = fields.Char(string='Process Code')
    tech_stage_ids = fields.One2many('tech.stage',
                                     'tech_process_id',
                                     string='Technical Stages')
    description = fields.Char(string='Process Description')
    input_description = fields.Html(string='Input Description')
    input = fields.One2many('product.product',
                            'tech_process_id',
                            string="Input")
    output_description = fields.Html(string='Output Description')
    output = fields.Many2one('product.product',
                             string='Output')
    sfg = fields.Boolean(string='SFG', default=False)
    image = fields.Image(string='Image')
    documents = fields.Binary(string='Document')
    document_name = fields.Char(string="File Name")
    sequence = fields.Many2one('tech.sequence', string='Sequence')
    ng_percent = fields.Float(string='NG Percent')
    bom_id = fields.Many2one('mrp.bom',
                             string='BOM')
    worker_group_ids = fields.One2many('worker.group', 'tech_process_id', string='Worker Group')


class Bom(models.Model):
    _inherit = ['mrp.bom']

    tech_process_ids = fields.One2many('tech.process', 'bom_id',
                                       string='Technical Process')
    time_process = fields.Float('Time Process*',
                                required=True,
                                default=0)
    consumption = fields.Float(string='Consumption Rate')
    waste_percent = fields.Float(string='Waste Percent*')
    ng_percent = fields.Float(string='NG Percent*',
                              required=True,
                              default=0)
    created_by = fields.Many2one('res.users',
                                 string='Created By*',
                                 required=True)
    worker_group_ids = fields.One2many('worker.group', 'bom_id', string='Worker Group')
    bom_quantity = fields.Float(string='Qty*', required=True)
    bom_uom = fields.Char(string='UOM', help="Unit of measurement")
