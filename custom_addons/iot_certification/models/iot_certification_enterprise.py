from odoo import models, fields

class Enterprise(models.Model):
    _name = 'iot_certification_enterprise'
    _description = 'Виробництво'

    partner_id = fields.Many2one('res.partner', string='Партнер', required=True)
    name = fields.Text(string='Адреса підприємства')


    def __str__(self):
        # for application report

        result = ""
        if self.partner_id.is_company:
            result += '"' + self.partner_id.name + '", '
        else:
            result += '"' + self.partner_id.parent_id.name + '", '

        return result + self.name