from odoo import models, fields

class Enterprise(models.Model):
    _name = 'iot_certification_enterprise'
    _description = 'Виробництво'

    partner_id = fields.Many2one('res.partner', string='Партнер', required=True)
    name = fields.Text(string='Адреса підприємства')