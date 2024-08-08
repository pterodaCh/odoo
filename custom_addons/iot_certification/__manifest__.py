{
    'name': 'IoT Certification',
    'version': '1.0',
    'author': 'Nadiia Melnyk',
    'depends': [
        'base',
        'product'
    ],
    'data': [
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

        # iot application report related
        'reports/iot_application_report/iot_application_report_style.xml',
        'reports/iot_application_report/iot_application_report_header_style.xml',
        'reports/iot_application_report/iot_application_report_header_html_document.xml',
        'reports/iot_application_report/iot_application_report_html_document.xml',
        'reports/iot_application_report/iot_application_report.xml',
    ],
    'installable': True,
    'auto_install': True,
}
