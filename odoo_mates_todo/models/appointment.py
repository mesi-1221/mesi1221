from odoo import fields, models, api


class HospitalManagement(models.Model):
    _name = 'hospital.appointment'
    _order = "id desc"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.management', string="Patient")
    gender = fields.Selection(related='patient_id.gender', readoly=False)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    refer = fields.Char(string="Reference", tracking=True, help="reference from patient record")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default="draft",  required=True, string="Status")
    doctor_id = fields.Many2one('res.users', string="Doctor")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='pharmacy_line')
    hide_sales_price = fields.Boolean(string="Hide Sale price")

    @api.onchange('patient_id', 'hide_sales_price')
    def onchange_patient_id(self):
        print(self.hide_sales_price)
        print("this appointment model", self.patient_id)
        self.refer = self.patient_id.ref

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_test(self):
        print("Button clicked!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfully',
                'type': 'rainbow_man',
            }
        }


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price', string="price")
    qty = fields.Integer(string="Quantity", default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')











