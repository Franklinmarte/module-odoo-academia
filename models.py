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
    maestro = fields.Many2one('openacademy.maestro', 'Maestro')
    aula = fields.Char(string="Aula")
    precio = fields.Integer(string="Precio")
    estudiantes = fields.Char(string="Estudiantes")

class Maestros(models.Model):

    _name = 'openacademy.maestro'

    name = fields.Char(string="Nombre", required=True)
    profesion = fields.Char(string="profesion", required=True)
    cursos_asignados = fields.Many2many('openacademy.course')

 

