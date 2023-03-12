from odoo import api, fields, models



class StationCustomer(models.Model):
    _name = "station.customer"
    _description = "Station Customer"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    train_id = fields.Many2one('station.train', string='Train')
    ticket_id = fields.Many2many('train.tickets', string='Ticket')
    total = fields.Integer(string='Total', compute='_compute_total')

    @api.depends('ticket_id', 'ticket_id.price')
    def _compute_total(self):
        for rec in self:
            if rec.ticket_id:
                for ticket in rec.ticket_id:
                    rec.total += ticket.price
            else:
                rec.total = 0
