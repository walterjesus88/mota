# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields


#----------------------------------------------------------
# Stock Picking
#----------------------------------------------------------
class stock_picking(models.Model):
    _inherit = 'purchase.order'
    numeral = fields.Integer(required=True,string='Guia de Remision de Remitente Nº')
    punto_llegada = fields.Char(string='Domicilio del punto de llegada')
    punto_partida = fields.Char(string='Domicilio del punto de partida')
    ruc = fields.Char(string='ruc')
    destinatario = fields.Char(string='Destinatario')

    fecha_traslado = fields.Datetime(
        'Fecha Inicio Traslado',
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


class PurchaseOrderLineMota(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line Mota'
    unidad = fields.Char(string='Unidad')
    peso = fields.Char(string='Peso')
    pedido_obs = fields.Char(string='Pedido Observaciones')
    