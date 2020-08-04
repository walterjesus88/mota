# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields

#----------------------------------------------------------
# Stock Picking
#----------------------------------------------------------
class stock_picking(models.Model):
    _inherit = 'stock.picking'
    _description = 'Transferencia de inventario'

    #numeral = fields.Integer(required=True,string='Guia de Remision de Remitente Nº')
    punto_llegada = fields.Char(string='Domicilio del punto de llegada')
    punto_partida = fields.Char(string='Domicilio del punto de partida')
    ruc = fields.Char(string='ruc')
    destinatario = fields.Char(string='Destinatario')

    fecha_traslado = fields.Datetime(
        'Fecha Inicio Traslado',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        #states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
        help="Creation Date, usually the time of the order")
    fecha_emision = fields.Datetime(
        'Fecha de emision',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date, usually the time of the order")
    variable = fields.Selection([('weight', 'Weight'), ('volume', 'Volume'), ('wv', 'Weight * Volume'), ('price', 'Price'), ('quantity', 'Quantity')], required=True, default='weight')
    motivo_traslado = fields.Selection([
        ('venta', 'venta'),
        ('compra', 'Compra'),
        ('devolucion', 'Devolucion')]
        )
    vehiculo_id = fields.Many2one('fleet.vehicle', 'vehiculos', track_visibility="onchange", help='Driver of the vehicle', copy=False, auto_join=True)
    #outgoing
    #pedido = fields.Char(string='N de pedido')
    obra = fields.Char(string='Obra/Centro de costos')
    area = fields.Char(string='Frente/area')
    codigo = fields.Char(string='Codigo')
    partida = fields.Char(string='Partida')
    autorizado = fields.Many2one('res.users', string='Autorizado por', states={'draft': [('readonly', False)], 'completado': [('readonly', False)]}, change_default=True, index=True, track_visibility='always', track_sequence=1, help="d.")
    recibido = fields.Many2one('res.users', string='Recibido por', states={'draft': [('readonly', False)], 'completado': [('readonly', False)]},  change_default=True, index=True, track_visibility='always', track_sequence=1, help="Y.")
    solicitante = fields.Many2one('res.users', string='Solicitado por', states={'draft': [('readonly', False)], 'completado': [('readonly', False)]},  change_default=True, index=True, track_visibility='always', track_sequence=1, help="Yo.") 
    
    

class VehicleMota(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Vehicle mota'
     
class StockMoveLineMota(models.Model):
    _inherit = 'stock.move'
    _description = 'Stock Move Line Mota'
    unidad = fields.Char(string='Unidad')
    peso = fields.Char(string='Peso')
    pedido_obs = fields.Char(string='Pedido Observaciones')
    