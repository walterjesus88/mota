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

    
# class order_mota_line(models.Model):
#     _inherit = 'sale.order.line' 
    
#     @api.depends('fecha_retiro','fecha_baja')
#     def _total(self):
#         for r in self:
#             print(r.fecha_baja)
#             print(r.fecha_retiro)
#             tiempo_vida = r.fecha_baja - r.fecha_retiro
#             #tiempo_vida = r.tiempo_vida
#             print(tiempo_vida.days)
#             r.tiempo_vida = tiempo_vida.days

#     fecha_retiro = fields.Datetime(
#         'Fecha de retiro',
#         default=fields.Datetime.now, index=True, track_visibility='onchange',
#         help="Creation Date")
#     fecha_baja = fields.Datetime(
#         'Fecha de baja',
#         default=fields.Datetime.now, index=True, track_visibility='onchange',
#         help="Creation Date")

#     tiempo_vida = fields.Integer(string='Tiempo vida', compute='_total', store=True)

class purchase_guia(models.Model):
    _inherit = 'purchase.order' 
    file_guia = fields.Binary(string='Guía de Remisión', attachment=True)

class Pedido(models.Model):
    _name='mota.pedido'
    _description = 'Transferencia de pedido'
    nombre = fields.Char(string='Descripcion')  
    moneda = fields.Char(string='Moneda del presupuesto operativo')
    tipo_cambio = fields.Char(string='Tipo de cambio')
    responsable = fields.Selection([
        ('Usuario', 'usuarios'),
        ('Compras', 'compras')])
    prioridad = fields.Selection([
        ('Alta', 'alta'),
        ('Media', 'media'),
        ('Baja', 'baja'),])
    fecha_emision = fields.Datetime(
        'Fecha de emision',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Fecha de Emision")
    centro_productivo = fields.Char(string='Centro productivo')
    centro_costos = fields.Char(string='Centro de costos')
    order_line = fields.One2many('mota.line.pedido', 'order_id', string='Order Lines',copy=True)

class Pedido_detalle(models.Model):
    _name='mota.line.pedido'
    _description = 'Transferencia de pedido'

    order_id = fields.Many2one('mota.pedido', string='Order Reference', index=True, required=True, ondelete='cascade')
    unidad = fields.Char(string='Unidad')
    cantidad = fields.Char(string='Cantidad')
    calidad = fields.Char(string='Certificado calidad')
    descripcion = fields.Char(string='Descripcion')    
    posicion = fields.Char(string='Posicion')
    codigo_articulo = fields.Char(string='Codigo articulo SAP')
    codigo_fabricante = fields.Char(string='Codigo fabricante')
    fecha_maxima_entrega = fields.Char(string='Fecha maxima entrega')
    numero_solicitudes = fields.Char(string='No solicitudes pedido')

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
class stock_qua(models.Model):
    _inherit = 'stock.quant' 
    #file = fields.Binary(string='Guía de Remisión', attachment=True)

class product_template_in(models.Model):
    _inherit = 'product.template' 

    @api.depends('fecha_retiro','fecha_baja')
    def _total(self):
        for r in self:
            print(r.fecha_baja)
            print(r.fecha_retiro)
            tiempo_vida = r.fecha_baja - r.fecha_retiro
            
            print(tiempo_vida.days)
            #r.tiempo_vida = tiempo_vida.days

    @api.depends('tiempo_llegada','tiempo_vida')
    def _stock(self):
        for r in self:
            print(r.tiempo_llegada)
            print(r.tiempo_vida)
            if r.tiempo_vida>0:
                res = round((r.tiempo_llegada/r.tiempo_vida)*0.3)
            else:
                res = 0
            #r.stock_critico = res

    fecha_retiro = fields.Datetime(
        'Fecha de retiro',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date")
    fecha_baja = fields.Datetime(
        'Fecha de baja',
        default=fields.Datetime.now, index=True, track_visibility='onchange',
        help="Creation Date")

    tiempo_vida = fields.Integer(string='Tiempo vida', compute='_total', store=True)
    tiempo_llegada = fields.Integer()
    stock_critico = fields.Integer(string='Stock Critico', compute='_stock', store=True)

    def write(self, vals):
        res = super(product_template_in, self).write(vals)
        id_product = self.env['product.product'].sudo().search([('product_tmpl_id', '=', self.id)])
        loc = self.env['stock.location'].sudo().search([('complete_name', '=', 'CH/Stock')])
        stock_quant = self.env['stock.quant'].sudo().search([('product_id', '=', id_product.id),('location_id','=',loc.id)]) 
        new_stock = stock_quant.quantity + self.stock_critico   
        value = {'quantity': new_stock}
        new_quant = self.env['stock.quant'].sudo().browse(stock_quant.id)
        new_quant.write(value)
        return res



