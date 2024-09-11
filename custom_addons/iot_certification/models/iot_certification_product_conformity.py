from odoo import models, fields


class ProductConformity(models.Model):
    _name = 'iot_certification_product_conformity'
    _description = 'Product conformity'

    name = fields.Char(
        string='Назва регламенту',
        required=True)

    text = fields.Html(
        string='Відповідає',
        required=True
    )
