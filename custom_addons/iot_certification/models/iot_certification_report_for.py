from odoo import models, fields

class ReportFor(models.Model):
    _name = 'iot_certification_report_for'
    _description = 'Report For'

    name = fields.Char(
        string=' ', 
        required=True)
    
    verdict = fields.Boolean(
        string=' ', 
        required=True)
    
    order_name  = fields.Char(
        string='Реєстраційний номер', 
        required=True)