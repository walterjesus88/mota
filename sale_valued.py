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
    autorizado = fields.Many2one('res.partner', string='Autorizado por', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="You can find a customer by its Name, TIN, Email or Internal Reference.")
    recibido = fields.Many2one('res.partner', string='Recibido por', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="You can find a customer by its Name, TIN, Email or Internal Reference.")
    solicitante = fields.Many2one('res.partner', string='Solicitado por', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="You can find a customer by its Name, TIN, Email or Internal Reference.") 
    fecha = fields.Datetime(
        'Fecha',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date, usually the time of the order")
   