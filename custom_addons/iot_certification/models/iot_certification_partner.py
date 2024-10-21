from odoo import api, fields, models

class PartnerExtension(models.Model):
    _inherit = 'res.partner'

    partner_type = fields.Selection(
        [('applicant', 'Заявник'),
         ('producer', 'Виробник')
        ], 
        string='Тип партнера'
    )
    
    
    enterprise_ids = fields.One2many(
        'iot_certification_enterprise', 
        'partner_id', 
        string='Підприємства'
    )

    duplicated_bank_account_partners_count = fields.Integer(string='Duplicated Bank Account Partner Count', compute='_compute_duplicated_bank_account_partners_count')
    
    @api.model
    def _default_view(self):
        return self.env.ref('view_res_partner_form_extension')

    def _compute_duplicated_bank_account_partners_count(self):
        self.duplicated_bank_account_partners_count = 0