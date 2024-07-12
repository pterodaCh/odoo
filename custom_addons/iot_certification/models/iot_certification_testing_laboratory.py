from odoo import models, fields

class TestingLaboratory(models.Model):
    _name = 'iot_certification_testing_laboratory'
    _description = 'ДСТУ'

    name = fields.Char(
        string='Інформація про випробувальну лабораторію', 
        required=True)
    
    order_no = fields.Many2one(
        comodel_name='iot_certification_order',
        inverse_name='safety_laboratory_id',
        string='Номер')
    
    