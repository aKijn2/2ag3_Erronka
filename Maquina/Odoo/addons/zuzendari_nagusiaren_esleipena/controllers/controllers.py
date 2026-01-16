# -*- coding: utf-8 -*-
# from odoo import http


# class HqDirectorAssignment(http.Controller):
#     @http.route('/hq_director_assignment/hq_director_assignment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hq_director_assignment/hq_director_assignment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hq_director_assignment.listing', {
#             'root': '/hq_director_assignment/hq_director_assignment',
#             'objects': http.request.env['hq_director_assignment.hq_director_assignment'].search([]),
#         })

#     @http.route('/hq_director_assignment/hq_director_assignment/objects/<model("hq_director_assignment.hq_director_assignment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hq_director_assignment.object', {
#             'object': obj
#         })

