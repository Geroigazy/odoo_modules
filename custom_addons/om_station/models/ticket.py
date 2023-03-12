from odoo import api, fields, models


class StationTrainTicket(models.Model):
    _name = "train.tickets"
    _description = "Train Ticket"

    train_id = fields.Many2one('station.train', string='Train')
    price = fields.Integer(string='Price')
    sit = fields.Selection([('ground floor', 'Ground floor'), ('top floor', 'Top floor')], string='Sit')
