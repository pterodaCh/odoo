from odoo import models, fields

class SwHw(models.Model):
    _name = 'iot_certification_sw_hw'
    _description = 'Software / Hardware'

    name = fields.Char(
        string='HW/SW Version', 
        required=True)
    
    part_of_the_equipment_verdict = fields.Selection(
        selection=[
            ('software', "Software"),
            ('hardware', "Hardware"),
        ],
        string="Type",
        required=True)