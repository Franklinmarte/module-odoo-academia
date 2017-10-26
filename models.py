# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MiLibros(models.Model):
    _name = 'milibro.libro'

    name = fields.Char('Titulo', require=True)
    paginas = fields.Integer('paginas')
    autor = fields.Char('Autor')
    editorial = fields.Char('Editorial')

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    duracion = fields.Integer(string="duracion")
    
    description = fields.Text()

