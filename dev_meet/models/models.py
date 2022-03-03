# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re

_logger = logging.getLogger(__name__)

class developer(models.Model):
    _name = 'dev_meet.developer'
    _description = 'Desarrollador'

    #CAMPOS
    name = fields.Char(string="Nombre", readonly=False, required=True, help='Este es el nombre')
    birth_year = fields.Date(string="Fecha nacimiento")
    dni = fields.Char(string="DNI")


    #RELACION CON LOS MODELOS
    tecnologia = fields.Many2many(comodel_name='dev_meet.tecnologia',
                                 relation='tecnologia_developer',
                                 column1='developer_id',
                                 column2='tecnologia_id')                            

    evento = fields.Many2many(comodel_name='dev_meet.evento', 
                              relation='developer_evento', 
                              column1='developer_id', 
                              column2='evento_id')
   
    #METODO CHECK DNI
    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[a-z]\Z', re.I) 
        for student in self:

            if regex.match(student.dni):
                _logger.info('DNI correcto')
            else:
                raise ValidationError('Formato incorrecto: DNI')

    _sql_constraints = [('dni_uniq', 'unique(dni)', 'DNI can\'t be repeated')]


class tecnologia(models.Model):
    _name = 'dev_meet.tecnologia'
    _description = 'Tecnologias'

    name = fields.Char()
    pageoficial = fields.Char(string="Pagina oficial")
    logo = fields.Image(max_width=100, max_height=100)

    developer = fields.Many2many(comodel_name='dev_meet.developer',
                                  relation='tecnologia_developer',
                                  column1='tecnologia_id',
                                  column2='developer_id')

    evento = fields.One2many(string="Evento", comodel_name='dev_meet.evento', inverse_name='tecnologia', readonly=True)

class evento(models.Model):
    _name = 'dev_meet.evento'
    _description = 'Eventos'

    name = fields.Char()
    fechainicio = fields.Integer()
    fechafin = fields.Integer()
    presencial = fields.Boolean()

    developer = fields.Many2many(comodel_name='dev_meet.developer', relation='evento_developer', column1='evento_id', column2='developer_id',readonly=True)
    tecnologia = fields.Many2one("dev_meet.tecnologia", ondelete='set null', help='Clase a la que pertenece')
   
   