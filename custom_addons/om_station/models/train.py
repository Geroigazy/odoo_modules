from odoo import api, fields, models


class StationTrain(models.Model):
    _name = "station.train"
    _description = "Station Train"

    train_name = fields.Char(string='Train name')
    destination = fields.Char(string="Destination")
    customer_ids = fields.One2many('station.customer', 'train_id', string='Customers')

