from odoo import models, fields


class Product(models.Model):

    _name = 'iot_certification_product'
    _description = 'Product Details'


    name = fields.Char(string='Назва товару', required=True)
    image = fields.Image(string='image')
    notes = fields.Text(string='Примітки')
    certification_order_ids = fields.One2many(
        comodel_name='iot_certification_order',
        inverse_name='product_id',
        string='Замовлення сертифікації')
