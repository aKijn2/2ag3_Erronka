# -*- coding: utf-8 -*-
from odoo import models, fields

class HQDirectorAssignment(models.Model):
    _name = 'hq.director.assignment'
    _description = 'Historial de asignación de directores por delegación'

    name = fields.Char(
        string='Izendapenaren izena',
        required=True
    )

    employee_id = fields.Many2one(
        'hr.employee',
        string='Zuzendaria',
        required=True
    )

    branch_id = fields.Many2one(
        'res.company',
        string='Ordezkaritza',
        required=True
    )

    start_date = fields.Date(
        string='Hasiera data',
        required=True
    )

    end_date = fields.Date(
        string='Amaiera data'
    )

    total_billing = fields.Monetary(
        string='Fakturazio osoa',
        currency_field='currency_id'
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Moneta',
        default=lambda self: self.env.company.currency_id
    )

    notes = fields.Text(
        string='Oharrak'
    )
