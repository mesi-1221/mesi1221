from datetime import date
from odoo import fields, models, api


class HospitalManagement(models.Model):
    _name = 'hospital.management'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string="Reference", tracking=True)
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True, store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    image = fields.Image(string='Image')

    @api.depends('date_of_birth')
    def _compute_age(self):
        print("self...............................", self)
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1







