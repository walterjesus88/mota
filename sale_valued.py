# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields


#----------------------------------------------------------
# Stock Picking
#----------------------------------------------------------
class order_mota(models.Model):
    _inherit = 'sale.order' 
    pedido = fields.Char(string='N de pedido')
    obra = fields.Char(string='Obra/Centro de costos')
    area = fields.Char(string='Frente/area')
    codigo = fields.Char(string='Codigo')
    partida = fields.Char(string='Partida')
    autorizado = fields.Many2one('res.users', string='Autorizado por', readonly=True, states={'inicial': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="d.")
    recibido = fields.Many2one('res.users', string='Recibido por', readonly=True, states={'inicial': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="Y.")
    solicitante = fields.Many2one('res.users', string='Solicitado por', readonly=True, states={'inicial': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="Yo.") 
    state = fields.Selection([
        ('inicial','Borrador'),
        ('completado', 'completado'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='inicial')
    #order_linextend = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)

    # fecha = fields.Datetime(
    #     'Fecha',
    #     default=fields.Datetime.now, index=True, track_visibility='onchange',
    #     help="Creation Date, usually the time of the order")
class order_mota_line(models.Model):
    _inherit = 'sale.order.line' 