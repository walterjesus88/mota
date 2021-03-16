# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api

#----------------------------------------------------------
# Stock Picking
#----------------------------------------------------------
class stock_picking(models.Model):
    _inherit = 'stock.picking'
    _description = 'Transferencia de inventario'

    #numeral = fields.Integer(required=True,string='Guia de Remision de Remitente Nº')
    punto_llegada = fields.Char(string='Domicilio del punto de llegada')
    punto_partida = fields.Char(string='Domicilio del punto de partida')
    ruc = fields.Char(string='Ruc')
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
        ('venta sujeta a confirmación de comprador', 'venta sujeta a confirmacion de comprador'),
        ('compra', 'Compra'),
        ('consignacion', 'consignacion'),
        ('devolucion', 'Devolucion'),
        ('Traslado entre establecimientos de una misma empresa', 'Traslado entre establecimientos de una misma empresa'),
        ('Traslado de bienes para transformación', 'Traslado de bienes para transformación'),
        #('Recojo de bienes para transformación', 'Recojo de bienes para transformación'),
        ('Recojo de bienes transformados', 'Recojo de bienes transformados'),
        ('Traslado por emisor itinerante de pago', 'Traslado por emisor itinerante de pago'),
        ('Traslado de zona primaria', 'Traslado de zona primaria'),
        ('Importación ', 'Importación'),
        ('Exportación ', 'Exportación'),
        ('Otros ', 'Otros'),
        ]
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
    
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

        res = super(stock_picking, self).fields_view_get(
            view_id=view_id,
            view_type=view_type,
            toolbar=toolbar,
            submenu=submenu)
        #if res.get('fields').get('state')['selection'][0][1] == 'assigned':      

        a = []
        if res.get('toolbar', False) and res.get('toolbar').get('print', False):
            print("www")

            reports = res.get('toolbar').get('print')
            #for report in reports:
                #print(res['toolbar']['print'])   
                #if report.get('report_file', False) and report.get('report_file') == 'stock.report_deliveryslip':
                #    res['toolbar']['print'].remove(report)              
                #if report.get('report_file') == 'stock.label_transfer_template_view_pdf' and report.get('report_file') == 'stock.label_transfer_template_view_zpl':
                #    res['toolbar']['print'].remove(report)
             
                #if report.get('report_file') == 'stock.label_transfer_template_view_zpl':
                #if report.get('print_report_name') == False:
                    #print_report_name

                    #res['toolbar']['print'].remove(report)
                #a.append(res)
                #print(res)
            #a.append(res)
        return res
class VehicleMota(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Vehicle mota'
     
class StockMoveLineMota(models.Model):
    _inherit = 'stock.move'
    _description = 'Stock Move Line Mota'
    unidad = fields.Char(string='Unidad')
    peso = fields.Char(string='Peso')
    pedido_obs = fields.Char(string='Pedido Observaciones')
    