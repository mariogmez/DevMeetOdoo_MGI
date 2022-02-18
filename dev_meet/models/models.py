# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class developer(models.Model):
    _name = 'dev_meet.developer'
    _description = 'dev_meet.developer'

    
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Este es el nombre')
    description = fields.Text()
    birth_year = fields.Integer()
    dni = fields.Char(string="DNI")
    photo = fields.Image(max_width=200, max_height=200)

    tecnologia = fields.Many2many(comodel_name='dev_meet.tecnologia', relation='tecnologia_developer', column1='developer_id', column2='tecnologia_id')
    evento = fields.Many2many(comodel_name='dev_meet.evento', relation='developer_evento', column1='developer_id', column2='evento_id')

    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[a-z]\Z', re.I) #re.I ignoreCase
        for student in self:
            # Ahora vamos a validar si se cumple la condición
            if regex.match(student.dni):
                _logger.info('DNI correcto')
            else:
                # No coinciden por lo que tenemos que informar e impedir que se guarde
                raise ValidationError('Formato incorrecto: DNI')
                # Si el DNI no es válido no nos permitirá guardar

    _sql_constraints = [('dni_uniq', 'unique(dni)', 'DNI can\'t be repeated')] #Todos los mensajes los deberíamos poner en inglés y luego traducir




class tecnologia(models.Model):
    _name = 'dev_meet.tecnologia'
    _description = 'dev_meet.tecnologia'

    name = fields.Char()
    description = fields.Text() 
    pageoficial = fields.Char(string="Pagina oficial")
    logo = fields.Image(max_width=100, max_height=100)

    evento = fields.Many2many(comodel_name='dev_meet.evento', relation='tecnologia_evento', column1='tecnologia_id', column2='evento_id')
    developer = fields.Many2many(comodel_name='dev_meet.developer', relation='tecnologia_developer', column1='tecnologia_id', column2='developer_id')

class evento(models.Model):
    _name = 'dev_meet.evento'
    _description = 'dev_meet.evento'

    name = fields.Char()
    description = fields.Text()
    fechainicio = fields.Integer()
    fechafin = fields.Integer()
    presencial = fields.Boolean()

    tecnologia = fields.Many2many(comodel_name='dev_meet.tecnologia', relation='tecnologia_evento', column1='evento_id', column2='tecnologia_id')
    developer = fields.Many2many(comodel_name='dev_meet.developer', relation='evento_developer', column1='evento_id', column2='developer_id')