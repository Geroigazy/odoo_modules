from odoo import api, fields, models



class StationCustomer(models.Model):
    _name = "station.customer"
    _description = "Station Customer"

    name = fields.Char(String='Name')
    age = fields.Integer(String='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
