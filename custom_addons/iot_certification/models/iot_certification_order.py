from odoo import api, fields, models, SUPERUSER_ID, exceptions, _
from babel.dates import format_date
import datetime


class IoTCertificationOrder(models.Model):
    _name = "iot_certification_order"
    _inherit = ['mail.thread']
    _description = "IoT Certification Order"
    _track = 1  # Enable tracking for this model

    additional_order_ids = fields.One2many('iot_certification_additional_order', 'order_id', string='Additional Orders')

    name = fields.Char(
        string='Реєстраційний номер',
        readonly=True,
        default=lambda self: _('New')
    )

    certificate_name = fields.Char(string="Номер сертифікату", readonly=True)
    
    date_of_commencement_of_work = fields.Date(
        string='Дата початку')
    
    date_of_report = fields.Date(
        string='Дата закінчення')
    
    report_for_ids = fields.One2many(
        comodel_name='iot_certification_report_for',
        inverse_name='order_name',
        string='Звіт за:')
    
    assessment_ids = fields.One2many(
        comodel_name='iot_certification_assessment',
        inverse_name='order_name',
        string='Оцінювання:')
    
    responsible_person = fields.Many2one(
        comodel_name='res.users',
        string="Відповідальна особа",
        default=lambda self: self.env.user,
        change_default=True)
    
    status = fields.Selection(
        selection=[
            ('draft', "Чернетка"),
            ('readyforapproval', "Готовий до перевірки"),
            ('inprogress', "На перевірці"),
            ('needchanges', "Потребує доопрацювання"),
            ('approved', " Підтверджено"),
        ],
        default='draft',
        string="Статус",
        tracking=True)

    approved_cert_status = fields.Boolean(
        string='Сертифікацію підтверджено', default=False)

    approved_report_status = fields.Boolean(
        string='Звітування підтверджено', default=False)

    conducted_an_assessment = fields.Many2one(
        comodel_name='res.users',
        string="Оцінювання проведено",
        change_default=True)
    
    conducted_an_analysis_and_made_a_decision_on_certification = fields.Many2one(
        comodel_name='res.users',
        string='Аналізування проведено та прийнято рішення щодо видачі Сертифікату експертизи типу',
        change_default=True)
    
    order_application_form_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    order_application_form_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='order_application_form_attachment_relation',
        string='Коментар'
    )
    
    order_application_form_remarks = fields.Html(
        string="Remarks")
    
    appliciant_id = fields.Many2one(
        comodel_name='res.partner',
        string="Заявник",
        domain="[('partner_type', '!=', 'producer')]")
    
    product_id = fields.Many2one(
        comodel_name='iot_certification_product',
        string="Продукт")
    
    producer_id = fields.Many2one(
        comodel_name='res.partner',
        string="Виробник",
        domain="[('partner_type', '=', 'producer')]")
    
    enterprise_ids = fields.Many2many(
        comodel_name='iot_certification_enterprise',
        relation='order_enterprise_relation',
        column1='order_id',
        column2='enterprise_id',
        string="Підприємства",
        #domain="['|', ('partner_id', '=', applicant_id), ('partner_id', '=', producer_id)]"
        )

    presence_of_sample_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")

    presence_of_sample_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='power_of_attorney_attachment_relation',
        string='Коментар'
    )

    presence_of_sample_remarks = fields.Html(
        string="Remarks")
    
    power_of_attorney_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    power_of_attorney_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='power_of_attorney_attachment_relation',
        string='Коментар'
    )
    
    power_of_attorney_remarks = fields.Html(
        string="Remarks")
    
    product_specification_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    product_specification_1 = fields.Boolean(
        string="Широкосмуговий радіодоступ")
    
    product_specification_1_1 = fields.Boolean(
        string="IEEE 802.11 b/g")
    
    product_specification_1_2 = fields.Boolean(
        string="IEEE 802.11а")
    
    product_specification_1_3 = fields.Boolean(
        string="IEEE 802.11n")
    
    product_specification_1_4 = fields.Boolean(
        string="IEEE 802.11 ас")
    
    product_specification_1_5 = fields.Boolean(
        string="IEEE 802.11 ах")
    
    product_specification_1_6 = fields.Boolean(
        string="IEEE 802.16")
    
    product_specification_1_7 = fields.Boolean(
        string="Bluetooth")
    
    product_specification_1_8 = fields.Boolean(
        string="ZigBee")

    product_specification_1_9 = fields.Boolean(
        string="2400 МГц")
    
    product_specification_2 = fields.Boolean(
        string="Цифровий стільниковий радіозв'язок")
    
    product_specification_2_1 = fields.Boolean(
        string="GSM 900/1800")
    
    product_specification_2_2 = fields.Boolean(
        string="LTE")
    
    product_specification_2_3 = fields.Boolean(
        string="ІМТ-2000 (UMTS)")
    
    product_specification_2_4 = fields.Boolean(
        string="CDMA-800")
    
    product_specification_3 = fields.Boolean(
        string="Пристрої короткого радіусу дії")
    
    product_specification_3_1 = fields.Boolean(
        string="433 МГц")
    
    product_specification_3_2 = fields.Boolean(
        string="868 МГц")
    
    product_specification_3_3 = fields.Boolean(
        string="2400 МГц")
    
    product_specification_3_4 = fields.Boolean(
        string="5800 МГц")

    product_specification_3_5 = fields.Boolean(
        string="6,7 МГц")

    product_specification_3_6 = fields.Boolean(
        string="13 МГц")
    
    product_specification_4 = fields.Boolean(
        string="Індуктивні застосування")

    product_specification_4_1 = fields.Boolean(
        string="NFC")

    product_specification_4_2 = fields.Boolean(
        string="RFID")
    
    product_specification_5 = fields.Boolean(
        string="Приймач")
    
    product_specification_5_1 = fields.Boolean(
        string="GNSS")
    
    product_specification_5_2 = fields.Boolean(
        string="FM/AM")
    
    product_specification_5_3 = fields.Boolean(
        string="КХ/УКХ")

    product_specification_5_4 = fields.Boolean(
        string="433 МГц")
    
    product_specification_5_5 = fields.Boolean(
        string="Інший")
    
    product_specification_5_6 = fields.Text(
        string="Інший (вказати)")

    product_specification_5_7 = fields.Boolean(
        string="DAB")

    product_specification_5_8 = fields.Boolean(
        string="TV/DBV")
    
    product_specification_6 = fields.Boolean(
        string="УКХ радіозв'язок")
    
    product_specification_7 = fields.Boolean(
        string="Радіолокаційні вимірювання")
    
    product_specification_8 = fields.Boolean(
        string="Супутниковий радіозв'язок")
    
    product_specification_9 = fields.Boolean(
        string="Радіорелейний зв'язок")
    
    product_specification_10 = fields.Boolean(
        string="Інше")
    
    product_specification_10_1 = fields.Text(
        string="Інше (вказати)")
    
    product_specification_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='product_specification_attachment_relation',
        string='Коментар'
    )
    
    product_specification_remarks = fields.Html(
        string="Remarks")
    
    the_scheme_of_power_supply_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    the_scheme_of_power_supply_1 = fields.Boolean(
        string="БАТАРЕЯ")
    
    the_scheme_of_power_supply_2 = fields.Boolean(
        string="МЕРЕЖА")
    
    the_scheme_of_power_supply_2_1 = fields.Boolean(
        string="Змінний струм")
    
    the_scheme_of_power_supply_2_1_1 = fields.Boolean(
        string="- шнур живлення")
    
    the_scheme_of_power_supply_2_1_2 = fields.Boolean(
        string="- безпосереднє приєднання")
    
    the_scheme_of_power_supply_2_1_3 = fields.Boolean(
        string="- перетворювач")
    
    the_scheme_of_power_supply_2_1_4 = fields.Text(
        string="- перетворювач (вказати)")
    
    the_scheme_of_power_supply_2_2 = fields.Boolean(
        string="Постійний струм")
    
    the_scheme_of_power_supply_2_2_1 = fields.Boolean(
        string="- шнур живлення")
    
    the_scheme_of_power_supply_2_2_2 = fields.Boolean(
        string="- безпосереднє приєднання")
    
    the_scheme_of_power_supply_2_2_3 = fields.Boolean(
        string="- перетворювач")
    
    the_scheme_of_power_supply_2_2_4 = fields.Text(
        string="- перетворювач (вказати)")
    
    the_scheme_of_power_supply_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='the_scheme_of_power_supply_attachment_relation',
        string='Коментар'
    )
    
    the_scheme_of_power_supply_remarks = fields.Html(
        string="Remarks")
    
    model_line_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    model_line_model = fields.Text(
        string="Модель")
    
    model_line_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='model_line_attachment_relation',
        string='Коментар'
    )
    
    model_line_remarks = fields.Html(
        string="Remarks")
    
    part_of_the_equipment_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    part_of_the_equipment = fields.Html(
        string="Склад обладнання")
    
    part_of_the_equipment_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='part_of_the_equipment_attachment_relation',
        string='Коментар'
    )
    
    part_of_the_equipment_remarks = fields.Html(
        string="Remarks")
    
    information_regarding_freq_bands_eirp_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    information_regarding_freq_bands_eirp_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='information_regarding_freq_bands_eirp_attachment_relation',
        string='Коментар'
    )
    
    information_regarding_freq_bands_eirp_remarks = fields.Html(
        string="Remarks")
    
    illustrations_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    illustrations_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='illustrations_relation',
        string='Фотографії та ілюстрації'
    )
    
    illustrations_remarks = fields.Html(
        string="Remarks")
    
    hw_sw_version_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    sw_id = fields.Many2one(
        comodel_name='iot_certification_sw_hw',
        string="Software",
        domain="[('part_of_the_equipment_verdict', '=', 'software')]")
    
    hw_id = fields.Many2one(
        comodel_name='iot_certification_sw_hw',
        string="Hardware",
        domain="[('part_of_the_equipment_verdict', '=', 'hardware')]")
    
    hw_sw_version_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='hw_sw_version_relation',
        string='Коментар'
    )
    
    hw_sw_version_remarks = fields.Html(
        string="Remarks")
    
    user_manual_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    user_manual_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='user_manual_relation',
        string='Коментар'
    )
    
    user_manual_remarks = fields.Html(
        string="Remarks")
    
    compliance_documents_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    compliance_documents_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='compliance_documents_relation',
        string='Коментар'
    )
    
    compliance_documents_remarks = fields.Html(
        string="Remarks")
    
    diagrams_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    diagrams_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='diagrams_relation',
        string='Схеми'
    )
    
    diagrams_remarks = fields.Html(
        string="Remarks")
    
    risk_assessment_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    risk_assessment_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='risk_assessment_relation',
        string='Коментар'
    )
    
    risk_assessment_remarks = fields.Html(
        string="Remarks")
    
    label_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    label_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='label_relation',
        string='Коментар'
    )
    
    label_remarks = fields.Html(
        string="Remarks")
    
    safety_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    safety_details = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='safety_details',
        string='Деталі',
        domain="[('safety', '=', True)]"
    )
    
    safety_protocol_no = fields.Char(
        string='ПРОТОКОЛ №',
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
        relation='safety_relation',
        string='Коментар'
    )
    
    safety_remarks = fields.Html(
        string="Remarks")
    
    health_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    health_details = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='health_details',
        string='Деталі',
        domain="[('health', '=', True)]"
    )
    
    health_protocol_no = fields.Char(
        string='ПРОТОКОЛ №',
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
        relation='health_relation',
        string='Коментар'
    )
    
    health_remarks = fields.Html(
        string="Remarks")
    
    emc_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    emc_details = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='emc_details',
        string='Деталі',
        domain="[('emc', '=', True)]"
    )
    
    emc_protocol_no = fields.Char(
        string='ПРОТОКОЛ №',
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
        relation='emc_relation',
        string='Коментар'
    )
    
    emc_remarks = fields.Html(
        string="Remarks")
    
    spectrum_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    spectrum_details = fields.Many2many(
        comodel_name='iot_certification_dstu',
        relation='spectrum_details',
        string='Деталі',
        domain="[('rf_spectrum', '=', True)]"
    )
    
    spectrum_protocol_no = fields.Char(
        string='ПРОТОКОЛ №',
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
        relation='spectrum_relation',
        string='Коментар'
    )
    
    spectrum_remarks = fields.Html(
        string="Remarks")
    
    product_reassessment_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")

    product_reassessment_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='power_of_attorney_attachment_relation',
        string='Коментар'
    )

    product_reassessment_remarks = fields.Html(
        string="Remarks")
    
    subpart_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    subpart_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='subpart_relation',
        string='Коментар'
    )
    
    subpart_attachment_remarks = fields.Html(
        string="Remarks")
    
    subpart_notes = fields.Html(
        string='Notes'
    )
    conditions_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    conditions_remarks = fields.Html(
        string="Remarks")

    product_conformity_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")

    product_conformity_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='subpart_relation',
        string='Коментар'
    )

    product_conformity_remarks = fields.Html(
        string="Remarks")

    product_conformity = fields.Many2one("iot_certification_product_conformity", "Відповідає")

    operation_basis_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")

    operation_basis_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='subpart_relation',
        string='Коментар'
    )

    operation_basis_remarks = fields.Html(
        string="Remarks")

    operation_basis = fields.Selection([
        ("option1", "не потребує внесення до реєстру присвоєнь радіочастот загальних користувачів"),
        ("option2", "на бездозвільній основі"),
    ], "Порядок використання")
    
    for i in range(1, 21):
        show_field_name = f"show_condition_{i}"
        verdict_field_name = f"condition_{i}_verd"
        notes_field_name = f"condition_{i}_notes"
        attachment_field_name = f"condition_{i}_attachment_ids"
        
        
        locals()[show_field_name] = fields.Boolean(
        string='Show Condition {i}')
        
        locals()[verdict_field_name] = fields.Selection(
            selection=[
                ('yes', "Так"),
                ('no', "Ні"),
            ],
            string=f"Verdict {i}"
        )
        
        locals()[notes_field_name] = fields.Html(
            string=f'Condition {i}'
        )
        
        locals()[attachment_field_name] = fields.Many2many(
            comodel_name='ir.attachment',
            relation=f'condition_{i}_relation',
            string=f'Коментар'
        )
    
    type_examination_certificate_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    type_examination_number = fields.Text(
        string="№")
    
    type_examination_date = fields.Date(
        string="Термін дії:")
    
    type_examination_certificate_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='type_examination_certificate_attachment_relation',
        string='Коментар'
    )
    
    type_examination_certificate_remarks = fields.Html(
        string="Remarks")
    
    declaration_of_conformity_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    declaration_of_conformity_number = fields.Text(
        string="№")
    
    declaration_of_conformity_date = fields.Date(
        string="Термін дії:")
    
    declaration_of_conformity_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='declaration_of_conformity_attachment_relation',
        string='Коментар'
    )
    
    declaration_of_conformity_remarks = fields.Html(
        string="Remarks")
    
    certification_agrement_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    certification_agrement_number = fields.Text(
        string="№")
    
    certification_agrement_date = fields.Date(
        string="Термін дії:")
    
    certification_agrement_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='certification_agrement_relation',
        string='Коментар'
    )
    
    certification_agrement_remarks = fields.Html(
        string="Remarks")
    
    contract_verdict = fields.Selection(
        selection=[
            ('ok', "Ok"),
            ('remark', "See remark"),
        ],
        string="Рішення")
    
    contract_number = fields.Text(
        string="№")
    
    contract_date = fields.Date(
        string="Термін дії:")
    
    contract_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='contract_relation',
        string='Коментар'
    )
    
    contract_remarks = fields.Html(
        string="Remarks")
    
    general_notes_subpart_notes = fields.Html(
        string='Notes'
    )
    
    general_notes_subpart_notes_editability = fields.Boolean(
        string='Notes'
    )
    
    @api.onchange('product_specification_1')
    def _onchange_product_specification_1(self):
        if not self.product_specification_1:
            self.product_specification_1_1 = False
            self.product_specification_1_2 = False
            self.product_specification_1_3 = False
            self.product_specification_1_4 = False
            self.product_specification_1_5 = False
            self.product_specification_1_6 = False
            self.product_specification_1_7 = False
            self.product_specification_1_8 = False
            self.product_specification_1_9 = False

    @api.onchange('product_specification_2')
    def _onchange_product_specification_2(self):
        if not self.product_specification_2:
            self.product_specification_2_1 = False
            self.product_specification_2_2 = False
            self.product_specification_2_3 = False
            self.product_specification_2_4 = False
    
    @api.onchange('product_specification_3')
    def _onchange_product_specification_3(self):
        if not self.product_specification_3:
            self.product_specification_3_1 = False
            self.product_specification_3_2 = False
            self.product_specification_3_3 = False
            self.product_specification_3_4 = False
            self.product_specification_3_5 = False
            self.product_specification_3_6 = False


    @api.onchange('product_specification_4')
    def _onchange_product_specification_4(self):
        if not self.product_specification_4:
            self.product_specification_4_1 = False
            self.product_specification_4_2 = False

    @api.onchange('product_specification_5')
    def _onchange_product_specification_5(self):
        if not self.product_specification_5:
            self.product_specification_5_1 = False
            self.product_specification_5_2 = False
            self.product_specification_5_3 = False
            self.product_specification_5_4 = False
            self.product_specification_5_5 = False
            self.product_specification_5_6 = ""
    
    @api.onchange('product_specification_5_5')
    def _onchange_product_specification_5_5(self):
        if not self.product_specification_5_5:
            self.product_specification_5_6 = ""
    
    # @api.onchange('product_specification_10')
    # def _onchange_product_specification_10(self):
    #     if not self.product_specification_10:
    #         self.product_specification_10_1 = ""
    
    @api.onchange('the_scheme_of_power_supply_2')
    def _onchange_the_scheme_of_power_supply_2(self):
        if not self.the_scheme_of_power_supply_2:
            self.the_scheme_of_power_supply_2_1 = False
            self.the_scheme_of_power_supply_2_2 = False
            self.the_scheme_of_power_supply_2_1_1 = False
            self.the_scheme_of_power_supply_2_1_2 = False
            self.the_scheme_of_power_supply_2_1_3 = False
            self.the_scheme_of_power_supply_2_1_4 = ""
            self.the_scheme_of_power_supply_2_2_1 = False
            self.the_scheme_of_power_supply_2_2_2 = False
            self.the_scheme_of_power_supply_2_2_3 = False
            self.the_scheme_of_power_supply_2_2_4 = ""
    
    @api.onchange('the_scheme_of_power_supply_2_1')
    def _onchange_the_scheme_of_power_supply_2_1(self):
        if not self.the_scheme_of_power_supply_2_1:
            self.the_scheme_of_power_supply_2_1_1 = False
            self.the_scheme_of_power_supply_2_1_2 = False
            self.the_scheme_of_power_supply_2_1_3 = False
            self.the_scheme_of_power_supply_2_1_4 = ""
    
    @api.onchange('the_scheme_of_power_supply_2_2')
    def _onchange_the_scheme_of_power_supply_2_2(self):
        if not self.the_scheme_of_power_supply_2_2:
            self.the_scheme_of_power_supply_2_2_1 = False
            self.the_scheme_of_power_supply_2_2_2 = False
            self.the_scheme_of_power_supply_2_2_3 = False
            self.the_scheme_of_power_supply_2_2_4 = ""
    
    @api.onchange('the_scheme_of_power_supply_2_1_3')
    def _onchange_the_scheme_of_power_supply_2_1_3(self):
        if not self.the_scheme_of_power_supply_2_1_3:
            self.the_scheme_of_power_supply_2_1_4 = ""
    
    @api.onchange('the_scheme_of_power_supply_2_2_3')
    def _onchange_the_scheme_of_power_supply_2_2_3(self):
        if not self.the_scheme_of_power_supply_2_2_3:
            self.the_scheme_of_power_supply_2_2_4 = ""
        
     
    def action_show_next_condition(self):
        for index in range(1, 21):
            show_condition_field = getattr(self, f'show_condition_{index}')
            if not show_condition_field:
                setattr(self, f'show_condition_{index}', True)
                return
   
    def delete_last_condition(self):
        for index in range(1, 21):
            index2 = 21 - index
            show_condition_field = getattr(self, f'show_condition_{index2}')
            if show_condition_field:
                setattr(self, f'condition_{index2}_verd', 'no')
                setattr(self, f'condition_{index2}_notes', '')
                setattr(self, f'condition_{index2}_attachment_ids', False)
                setattr(self, f'show_condition_{index2}', False)
                return
            
    def action_modify_notes(self):
        self.general_notes_subpart_notes_editability = True
        
    def action_save_notes(self):
        self.general_notes_subpart_notes_editability = False

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            last_record = self.search([], order='id desc', limit=1)
            if last_record:
                last_number = int(last_record.name.split('-')[-1])
                next_number = last_number + 1
            else:
                next_number = 1
            vals['name'] = f'УЧН-{next_number}'
        return super(IoTCertificationOrder, self).create(vals)

    def write(self, vals):
        if 'status' in vals and vals.get('status') == 'approved' and not self.certificate_name:
            last_record = self.search([], order='id desc', limit=1)
            if last_record and last_record.certificate_name:
                last_number = int(last_record.certificate_name.split('-')[-1])
                next_number = last_number + 1
            else:
                next_number = 1
            vals['certificate_name'] = f'УЧН-{next_number}'

        return super(IoTCertificationOrder, self).write(vals)
        
    def open_or_create_additional_order(self):
        additional_order = self.env['iot_certification_additional_order'].search([('order_id', '=', self.id)], limit=1)
        
        if additional_order:
            # Open the existing additional order
            return {
                'name': 'Additional Order',
                'type': 'ir.actions.act_window',
                'res_model': 'iot_certification_additional_order',
                'res_id': additional_order.id,
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'current',
            }
        else:
            # Create a new additional order with the same name
            additional_order = self.env['iot_certification_additional_order'].create({
                'order_id': self.id,
                'name': self.name
            })
            return {
                'name': 'Additional Order',
                'type': 'ir.actions.act_window',
                'res_model': 'iot_certification_additional_order',
                'res_id': additional_order.id,
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'current',
            }
    
    
    
    # @api.onchange('status')
    # def _onchange_status(self):
    #     for record in self:
    #         if record.status == 'approved' or record.status == 'readyforapproval':
    #             verdict_fields = [field_name for field_name in record._fields if 'verdict' in field_name]
    #             for field_name in verdict_fields:
    #                 if record[field_name] != 'Ok':
    #                     raise exceptions.ValidationError('Помилка: є поля зі значенням "See remark". Статус не може бути змінений. Виправте всі ремарки і повторіть запит знову. Поле, що спричинило помилку: "{}"'.format(field_name))

                    
    def copy_record_and_update_name(self):
        for record in self:
            copied_record = record.copy()
            copied_record.write({'name': record.name + ' (КОПІЯ)'})

    def action_ready_for_approval(self):
        for record in self:
            if record.status == 'readyforapproval':
                raise exceptions.ValidationError('Помилка: заявку вже надіслано на перевірку')
            elif record.status == 'inprogress':
                raise exceptions.ValidationError('Помилка: заявка перевіряється. На цьому етапі статус заявки змінити неможливо')
            elif record.status == 'approved':
                raise exceptions.ValidationError('Помилка: заявку підтверджено. На цьому етапі статус заявки змінити неможливо')
            else:
                record.status = 'readyforapproval'

    def action_accept_for_approval(self):
        for record in self:
            if record.status == 'readyforapproval':
                record.status = 'inprogress'
            elif record.status == 'approved':
                raise exceptions.ValidationError('Помилка: заявку підтверджено. На цьому етапі статус заявки змінити неможливо')
            else:
                raise exceptions.ValidationError('Помилка: заявка не готова до перевірки')

    def action_submit_for_revision(self):
        for record in self:
            if record.status == 'inprogress':
                record.status = 'needchanges'
            elif record.status == 'approved':
                raise exceptions.ValidationError('Помилка: заявку підтверджено. На цьому етапі статус заявки змінити неможливо')
            else:
                raise exceptions.ValidationError('Помилка: неможливо надіслати на доопрацювання. Заявка не перевіряється')

    def action_submit(self):
        for record in self:
            if record.status != 'inprogress':
                if record.status == 'approved':
                    if record.approved_cert_status or record.approved_report_status:
                        record.approved_report_status = True
                        record.approved_cert_status = True
                else:
                    raise exceptions.ValidationError('Помилка: неможливо підтвердити. Заявка не перевіряється')
            else:
                if self.env.user.has_group('iot_certification.group_certification_report_manager'):
                    record.approved_report_status = True
                if self.env.user.has_group('iot_certification.group_certification_cert_manager'):
                    record.approved_cert_status = True
            if record.approved_cert_status or record.approved_report_status:
                record.status = 'approved'

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    # def print_options(self):
    #     return {
    #         'res_model': 'res.partner',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'view_id': self.env.ref('base.view_empty_form').id
    #     }

    def print_application(self):
        return self.env.ref('iot_certification.iot_application_report_action').report_action(self)

    def print_report(self):
        for record in self:
            if not record.approved_report_status:
                raise exceptions.ValidationError('Помилка: звіт неможливо надрукувати. Заявку не підтверджено відповідним керівником')
            else:
                 return self.env.ref('iot_certification.action_report').report_action(self)

    def print_cert(self):
        for record in self:
            if not record.approved_cert_status:
                raise exceptions.ValidationError('Помилка: сертифікат неможливо надрукувати. Заявку не підтверджено відповідним керівником')
            else:
                 return self.env.ref('iot_certification.iot_certification_certification_report_action').report_action(self)

    def get_formatted_date(self):
        if self.date_of_commencement_of_work:
            return format_date(self.date_of_commencement_of_work, format='d MMMM yyyy', locale='uk_UA')
        else:
            return ""

    def get_equipment_description(self) -> str:
        result = str()
        result += "IEEE 812 "
        ieee_letters: list[str] = list()

        if self.product_specification_2_1:
            result += "GSM 900/1800" + "; "
        if self.product_specification_2_2:
            result += "LTE" + "; "
        if self.product_specification_2_3:
            result += "ІМТ-2000 (UMTS)" + "; "
        if self.product_specification_2_4:
            result += "CDMA-800" + "; "

        if self.product_specification_1_2:
            ieee_letters.append("a")
        if self.product_specification_1_1:
            ieee_letters.append("b/g")
        if self.product_specification_1_3:
            ieee_letters.append("n")
        if self.product_specification_1_4:
            ieee_letters.append("ac")
        if self.product_specification_1_5:
            ieee_letters.append("ax")
        result += "/".join(ieee_letters) + "; "

        if self.product_specification_1_6:
            result += "IEEE 802.16" + "; "
        if self.product_specification_1_7:
            result += "Bluetooth" + "; "
        if self.product_specification_1_6:
            result += "ZigBee" + "; "
        if self.product_specification_1_6:
            result += "2400 МГц" + "; "

        if self.product_specification_4_1:
            result += "NFC" + "; "
        if self.product_specification_4_2:
            result += "RFID" + "; "

        receivers: list[str] = list()

        if self.product_specification_5_1:
            receivers.append("GNSS")
        if self.product_specification_5_2:
            receivers.append("FM/AM")
        if self.product_specification_5_3:
            receivers.append("КХ/УКХ")
        if self.product_specification_5_4:
            receivers.append("433 МГц")
        if self.product_specification_5_7:
            receivers.append("DAB")
        if self.product_specification_5_8:
            receivers.append("TV/DBV")
        if self.product_specification_5_5 and self.product_specification_5_6:
            receivers.append(self.product_specification_5_6)

        result += ", ".join(receivers) + " приймачі"

        return result
