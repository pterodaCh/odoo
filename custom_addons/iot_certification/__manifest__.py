{
    'name': 'IoT Certification',
    'version': '1.0',
    'author': 'Nadiia Melnyk',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'mail'
    ],
    'data': [
        'security/ir_rules.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/iot_certification_partner.xml',
        'views/iot_certification_dstu.xml',
        'views/iot_certification_report_for-view.xml',
        'views/iot_certification_sw_hw.xml',
        'views/iot_certification_assessment.xml',
        'views/iot_certification_order_view.xml',
        'views/iot_certification_menu.xml',
        'views/iot_certification_testing_laboratory.xml',
        'views/iot_certification_additional_order_view.xml',
        'views/iot_certification_enterprise.xml',
        'reports/iot_certification_report.xml'
    ],
    'installable': True,
    'auto_install': True,
}
