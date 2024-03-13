# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, AccessError, RedirectWarning
from odoo.tools.misc import formatLang


class AccountInvoice(models.Model):
    _inherit = "account.move"

    withholding_boolean = fields.Boolean(default=False)
    withholding_amount = fields.Char(string="Withholding", compute='_compute_withholding_amount', store=True)

    @api.depends('withholding_boolean', 'invoice_line_ids')
    def _compute_withholding_amount(self):
        for invoice in self:
            if invoice.withholding_boolean:
                invoice.withholding_amount = str(-1*sum((line.quantity * line.price_unit * 2) / 100 for line in invoice.invoice_line_ids)) + " Br"
            else:
                invoice.withholding_amount = str(0.0)+" Br"

    @api.constrains('withholding_boolean')
    def _onchange_active_withhold(self):
        if self.withholding_boolean:
            company_record = self.env['res.currency'].search([('symbol', '=', 'Br')], limit=1)
            print("kzhkjds", self.withholding_amount, company_record.symbol)
            line_ids = self.line_ids.ids
            print(line_ids)
            ids = self.line_ids.search([('display_type', '=', 'product'), ('id', 'in', line_ids)]).ids
            print("hugewquryigjhgwqueffdsagsadgwregwqg", ids)
            for id in ids:
                wityh = self.env['account.tax'].search([('description', '=', 'tax02')]).ids
                if not wityh:
                    raise ValidationError("There is no withholding tax labeled 'tax02'. Please create the tax or update it to make it unique.")
                normaltaxes = self.line_ids.browse(id).tax_ids.ids
                print(normaltaxes)
                print("yes",self.env['account.tax'].search([('id', 'in', wityh + normaltaxes)]))
                withhold =  self.line_ids.browse(id).tax_ids = self.env['account.tax'].search([('id', 'in', wityh + normaltaxes)])
                print(withhold)
        else:
            line_ids = self.line_ids.ids
            ids = self.line_ids.search([('display_type', '=', 'product'), ('id', 'in', line_ids)]).ids
            for id in ids:
                wityh = self.env['account.tax'].search([('description', '=', 'tax02')]).ids
                if not wityh:
                    raise ValidationError(
                        "There is no withholding tax labeled 'tax02'. Please create the tax or update it to make it unique.")
                normaltaxes = self.line_ids.browse(id).tax_ids.ids
                print("ww",self.env['account.tax'].search([('id', 'in', list(set(normaltaxes) - set(wityh)))]))
                self.line_ids.browse(id).tax_ids = self.env['account.tax'].search([('id', 'in', list(set(normaltaxes) - set(wityh)))])



