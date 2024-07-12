from odoo import models, fields

class Assessment(models.Model):
    _name = 'iot_certification_assessment'
    _description = 'Assessment'

    name = fields.Char(
        string=' ', 
        required=True)
    
    verdict = fields.Boolean(
        string=' ', 
        required=True)
    
    order_name  = fields.Char(
        string='Реєстраційний номер', 
        required=True)