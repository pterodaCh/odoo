from odoo import models, fields

class Dstu(models.Model):
    _name = 'iot_certification_dstu'
    _description = 'ДСТУ'

    name = fields.Char(
        string=' ', 
        required=True)
    
    safety = fields.Boolean(
        string='Безпека')
    
    health = fields.Boolean(
        string='Здоров''я')
    
    emc = fields.Boolean(
        string='EMC')
    
    rf_spectrum = fields.Boolean(
        string='Використання РЧР')
    
    