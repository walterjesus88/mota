# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields


#----------------------------------------------------------
# Stock Picking
#----------------------------------------------------------
class stock_picking(models.Model):
    _inherit = 'stock.picking'
    numeral = fields.Char(string='Nro Guia de Remision de Remitente')
    punto_llegada = fields.Char(string='Domicilio del punto de llegada')
    punto_partida = fields.Char(string='Domicilio del punto de partida')
    ruc = fields.Char(string='ruc')
    destinatario = fields.Char(string='destinatario')

    fecha_traslado = fields.Datetime(
        'fecha de inicio de traslado',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
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
