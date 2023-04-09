from odoo import api, fields, models



class SulpakSmartphone(models.Model):
    _name = "sulpak.smartphone"
    _description = "Sulpak Smartphone"

    name = fields.Char(string='Name', required=True)
    brand = fields.Char(string='Brand', required=True)
    price = fields.Integer(string='Price', default='100')
    descr = fields.Char(string='Description', required=True)
    pix_of_camera = fields.Integer(string='Main camera', default='16')
    pix_of_front_camera = fields.Integer(string='Front camera', default='12')
    builtin_memory = fields.Integer(string='Built-in memory', default='8')


