from odoo import models, fields,  api


class PaymentRegistry(models.TransientModel):
    _name = "account.payment.register"
    _inherit = "account.payment.register"

    withholding_amount = fields.Monetary(string='Withholding Amount')
    withholding_checkbox = fields.Boolean(string='Withholding Checkbox', default=False)

    @api.onchange('withholding_checkbox')
    def on_withholding_checkbox_change(self):
        if self.withholding_checkbox:
            print("This is withholding amount")