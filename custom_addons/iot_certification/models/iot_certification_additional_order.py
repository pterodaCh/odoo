from odoo import api, models, fields


class IoTCertificationAdditionalOrder(models.Model):
    _name = "iot_certification_additional_order"
    _description = "IoT Certification Additional Order"

    order_id = fields.Many2one('iot_certification_order', string='Order')

    name  = fields.Char(
        string='Реєстраційний номер',
        readonly=True)

    safety_verdict = fields.Selection(
        selection=[
            ('none', "відсутній"),
            ('full', "Повністю застосовані вимоги стандарту"),
            ('part', "НЕ повністю застосовані вимоги стандарту"),
            ('other', "інше"),
        ],
        string="Рішення")

    safety_details_1 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='safety_details_1',
        string='Деталі',
        domain="[('safety', '=', True)]"
    )


    safety_details_2 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='safety_details_2',
        string='Деталі',
        domain="[('safety', '=', True)]"
    )
    safety_protocol_no = fields.Char(
        string='TEST REPORT №',
    )

    safety_protocol_date = fields.Date(
        string='від',
    )

    safety_laboratory_id = fields.Many2one(
        comodel_name='iot_certification_testing_laboratory',
    # relation='safety_laboratory_id',
        string='Випробувальна лабораторія:')

    safety_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='safety_relation_additional',
        string='Коментар'
    )

    safety_result = fields.Html(
        string='Висновок'
    )

    health_verdict = fields.Selection(
        selection=[
            ('none', "відсутній"),
            ('full', "Повністю застосовані вимоги стандарту"),
            ('part', "НЕ повністю застосовані вимоги стандарту"),
            ('other', "інше"),
        ],
        string="Рішення")

    health_details_1 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='health_details_1',
        string='Деталі',
        domain="[('health', '=', True)]"
    )

    health_details_2 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='health_details_2',
        string='Деталі',
        domain="[('health', '=', True)]"
    )

    health_protocol_no = fields.Char(
        string='TEST REPORT №',
    )

    health_protocol_date = fields.Date(
        string='від',
    )

    health_laboratory_id = fields.Many2one(
        comodel_name='iot_certification_testing_laboratory',
    # relation='health_laboratory_id',
        string='Випробувальна лабораторія:')

    health_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='health_relation_additional',
        string='Коментар'
    )

    health_result = fields.Html(
        string='Висновок'
    )

    emc_verdict = fields.Selection(
        selection=[
            ('none', "відсутній"),
            ('full', "Повністю застосовані вимоги стандарту"),
            ('part', "НЕ повністю застосовані вимоги стандарту"),
            ('other', "інше"),
        ],
        string="Рішення")

    emc_details_1 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='emc_details_1',
        string='Деталі',
        domain="[('emc', '=', True)]"
    )

    emc_details_2 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='emc_details_2',
        string='Деталі',
        domain="[('emc', '=', True)]"
    )

    emc_protocol_no = fields.Char(
        string='TEST REPORT №',
    )

    emc_protocol_date = fields.Date(
        string='від',
    )

    emc_laboratory_id = fields.Many2one(
        comodel_name='iot_certification_testing_laboratory',
    # relation='emc_laboratory_id',
        string='Випробувальна лабораторія:')

    emc_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='emc_relation_additional',
        string='Коментар'
    )

    emc_result = fields.Html(
        string='Висновок'
    )

    spectrum_verdict = fields.Selection(
        selection=[
            ('none', "відсутній"),
            ('full', "Повністю застосовані вимоги стандарту"),
            ('part', "НЕ повністю застосовані вимоги стандарту"),
            ('other', "інше"),
        ],
        string="Рішення")

    spectrum_details_1 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='spectrum_details_1',
        string='Деталі',
        domain="[('rf_spectrum', '=', True)]"
    )

    spectrum_details_2 = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='spectrum_details_2',
        string='Деталі',
        domain="[('rf_spectrum', '=', True)]"
    )

    spectrum_protocol_no = fields.Char(
        string='TEST REPORT №',
    )

    spectrum_protocol_date = fields.Date(
        string='від',
    )

    spectrum_laboratory_id = fields.Many2one(
        comodel_name='iot_certification_testing_laboratory',
    # relation='spectrum_laboratory_id',
        string='Випробувальна лабораторія:')

    spectrum_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='spectrum_relation_additional',
        string='Коментар'
    )

    spectrum_result = fields.Html(
        string='Висновок'
    )

    @api.depends('order_id.status')
    def _compute_status(self):
        for record in self:
            record.status = record.order_id.status
