# -*- coding: utf-8 -*-
from odoo import models, fields

class EmployeeVehicleExpense(models.Model):
    _name = 'employee.vehicle.expense'
    _description = 'Langileei esleitutako ibilgailuen gastuak'

    name = fields.Char(
        string='Erregistroaren izena',
        required=True
    )

    employee_id = fields.Many2one(
        'hr.employee',
        string='Langilea',
        required=True
    )

    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Ibilgailua',
        required=True
    )

    expense_date = fields.Date(
        string='Gastuen data',
        required=True,
        default=fields.Date.today
    )

    expense_type = fields.Selection(
        [
            ('fuel', 'Erregaia'),
            ('maintenance', 'Mantentzea'),
            ('insurance', 'Asegurua'),
            ('other', 'Bestelakoa')
        ],
        string='Gastu mota',
        required=True
    )

    amount = fields.Monetary(
        string='Zenbatekoa',
        required=True,
        currency_field='currency_id'
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Moneta',
        default=lambda self: self.env.company.currency_id
    )

    description = fields.Text(
        string='Azalpena'
    )
