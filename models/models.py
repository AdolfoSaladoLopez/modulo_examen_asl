# -*- coding: utf-8 -*-
from datetime import date

from odoo import models, fields, api
import time


# class modulo_examen_asl(models.Model):
#     _name = 'modulo_examen_asl.modulo_examen_asl'
#     _description = 'modulo_examen_asl.modulo_examen_asl'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Cliente(models.Model):
    _name = 'cliente.modulo'
    _description = 'Cliente'

    nombre = fields.Char()
    direccion = fields.Char()
    ciudad = fields.Char()
    estado = fields.Char()
    codigo_postal = fields.Char()
    pais = fields.Char()
    facturas_id = fields.One2many(comodel_name='factura.modulo', inverse_name='cliente_id', string="Factura",
                                  required=False)


class Factura(models.Model):
    _name = 'factura.modulo'
    _description = 'Factura'

    numero_factura = fields.Char()
    fecha_emision = fields.Date(default=fields.Date.today())
    fecha_vencimiento = fields.Date()
    monto_total = fields.Float()
    cliente_id = fields.Many2one(comodel_name='cliente.modulo', ondelete='set null', string="Cliente", index=True)


class Producto(models.Model):
    _name = 'producto.modulo'
    _description = 'Producto'

    nombre = fields.Char()
    descripcion = fields.Text()
    precio = fields.Float()
