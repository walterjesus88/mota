# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#from odoo import models,fields,api
from odoo import api, fields, models, _

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
    autorizado = fields.Many2one('res.users', string='Autorizado por', readonly=True, states={'draft': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="d.")
    recibido = fields.Many2one('res.users', string='Recibido por', readonly=True, states={'draft': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="Y.")
    solicitante = fields.Many2one('res.users', string='Solicitado por', readonly=True, states={'draft': [('readonly', False)], 'completado': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="Yo.") 

    fecha_entrega = fields.Datetime(
        'Fecha de Entrega Material',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date")

    # state = fields.Selection([
    #     ('inicial','Borrador'),
    #     ('completado', 'completado'),
    #     ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    
class order_mota_line(models.Model):
    _inherit = 'sale.order.line' 
    
    @api.depends('fecha_retiro','fecha_baja')
    def _total(self):
        print(self)
        print('----------------------------------------------------------------------->')
        for r in self:
            print(r.fecha_baja)
            print(r.fecha_retiro)
            tiempo_vida = r.fecha_baja - r.fecha_retiro
            #tiempo_vida = r.tiempo_vida
            print(tiempo_vida.days)
            r.tiempo_vida = tiempo_vida.days

    fecha_retiro = fields.Datetime(
        'Fecha de retiro',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date")
    fecha_baja = fields.Datetime(
        'Fecha de baja',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date")

    tiempo_vida = fields.Integer(string='Tiempo vida', compute='_total', store=True)

class purchase_guia(models.Model):
    _inherit = 'purchase.order' 
    file = fields.Binary(string='Guía de Remisión', attachment=True)


