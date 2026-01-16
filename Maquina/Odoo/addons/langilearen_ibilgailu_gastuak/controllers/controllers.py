# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeVehicleExpenses(http.Controller):
#     @http.route('/employee_vehicle_expenses/employee_vehicle_expenses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_vehicle_expenses/employee_vehicle_expenses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_vehicle_expenses.listing', {
#             'root': '/employee_vehicle_expenses/employee_vehicle_expenses',
#             'objects': http.request.env['employee_vehicle_expenses.employee_vehicle_expenses'].search([]),
#         })

#     @http.route('/employee_vehicle_expenses/employee_vehicle_expenses/objects/<model("employee_vehicle_expenses.employee_vehicle_expenses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_vehicle_expenses.object', {
#             'object': obj
#         })

