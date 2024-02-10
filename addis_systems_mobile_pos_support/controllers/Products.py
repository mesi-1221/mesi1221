from odoo import _, http
from odoo.exceptions import AccessError
from odoo.http import request

import json
import time


class AddisSystemsProductPortalController(http.Controller):

    @http.route('/AddisSystems/MPoS/Product/NewProduct', type='json', methods=['POST'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_new_product(self, **kw):

        if http.request.env.user and http.request.env.user.id:
            data = json.loads(request.httprequest.data)
            return_json = {}

            # TODO Data Validation before any process

            auth = data.get("request_data")
            products = data.get("products")

            for product in products:
                is_product_unique = request.env['product.template'].sudo().search([])
                vals = {
                    "name": product.get("name"),
                    "detailed_type": 'product',
                }
                product_id = request.env['product.template'].sudo().create(vals)
                return_json[product.get("name")] = product_id.id

            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update/Products/Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_update_products_data(self):
        if request.env.user and request.env.user.id:
            return_json = []
            products = request.env['product.template'].search([])
            for product in products:
                quants = request.env['stock.quant'].search([('product_tmpl_id', '=', product.id)])
                if quants:
                    quant = quants[0]
                    quant.available_quantity = quant.quantity - quant.reserved_quantity
                    single_data = {
                        "name": product.name,
                        "product_id": product.id,
                        "internal reference": product.default_code,
                        "price": product.list_price,
                        "quantity on hand": quant.quantity,
                        "cost": product.standard_price,
                        "product type": product.detailed_type,
                        "product_category": product.categ_id.name,
                        "product_image": product.image_1920,
                        "company_id": product.company_id.id,
                        "invoicing policy": product.invoice_policy,
                        "can be sold": product.sale_ok,
                        "can be purchased": product.purchase_ok,
                        "available in pos": product.available_in_pos,
                        "customer taxes": product.taxes_id.name,

                    }
                    return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}


    @http.route('/AddisSystems/MPoS/Update_Partner_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos__update_partner_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            partners = request.env['res.partner'].search([])
            for partner in partners:
                single_data = {}
                single_data["partner name"] = partner.name
                single_data["partner phone"] = partner.phone
                single_data["partner email"] = partner.email
                single_data["partner website"] = partner.website
                single_data["partner title"] = partner.title.name
                single_data["partner tags"] = partner.category_id
                single_data["partner vat"] = partner.vat
                single_data["partner id"] = partner.company_id.name
                single_data["partner state"] = partner.street
                single_data["partner state2"] = partner.street2
                single_data["partner city"] = partner.city
                single_data["partner position"] = partner.function
                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_User_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_update_user_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            users = request.env['res.users'].search([])
            for user in users:
                single_data = {}
                single_data["user_name"] = user.name
                single_data["user_id"] = user.id
                single_data["user_login"] = user.login
                single_data["user_password"] = user.password
                single_data["user_language"] = user.lang
                single_data["user_latest_authentication"] = user.login_date
                single_data["user_company"] = user.company_id.name
                single_data["user_status"] = user.state
                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Company_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_company_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            companys = request.env['res.company'].search([])
            for company in companys:
                single_data = {}
                single_data["company name"] = company.name
                single_data["company parent"] = company.partner_id.name
                single_data["company active"] = company.active
                single_data["company fiscal year"] = company.fiscalyear_last_day
                single_data["company Address"] = company.street
                single_data["company Address2"] = company.street2
                single_data["company city"] = company.city
                single_data["company phone"] = company.phone
                single_data["company mobile"] = company.mobile
                single_data["company email"] = company.email
                single_data["company website"] = company.website
                single_data["company currency"] = company.currency_id
                single_data["company paper format"] = company.paperformat_id
                single_data["company font"] = company.font
                single_data["company social twitter"] = company.social_twitter
                single_data["company social facebook"] = company.social_facebook
                single_data["company social github"] = company.social_github
                single_data["company social linkedin"] = company.social_linkedin
                single_data["company social youtube"] = company.social_youtube
                single_data["company social instagram"] = company.social_instagram

                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Sales_Order_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_sales_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            sales_orders = request.env['sale.order'].search([])
            for sales_order in sales_orders:
                single_data = {}
                single_data["sales_order number"] = sales_order.name
                single_data["sales_order creation data"] = sales_order.create_date
                single_data["sales_order customer"] = sales_order.partner_id.name
                single_data["sales_order salesperson"] = sales_order.user_id.name
                single_data["sales_order activities"] = sales_order.activity_ids
                single_data["sales_order company"] = sales_order.company_id.name
                single_data["sales_order total"] = sales_order.amount_total
                single_data["sales_order status"] = sales_order.state
                single_data["sales_order invoice status"] = sales_order.invoice_status
                single_data["sales_order untaxed amount"] = sales_order.amount_untaxed
                single_data["sales_order quotation date"] = sales_order.date_order
                single_data["sales_order expiration date"] = sales_order.validity_date
                single_data["sales_order pricelist"] = sales_order.pricelist_id.name
                single_data["sales_order payment terms"] = sales_order.payment_term_id.name
                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}


    @http.route('/AddisSystems/MPoS/Update_Purchase_Order_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_purchase_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            purchase_orders = request.env['purchase.order'].search([])
            for purchase_order in purchase_orders:
                single_data = {}
                single_data["purchase order reference"] = purchase_order.name
                single_data["purchase order vendor"] = purchase_order.partner_id.name
                single_data["purchase order company"] = purchase_order.company_id.name
                single_data["purchase order buyer"] = purchase_order.user_id.name
                single_data["purchase order order deadline"] = purchase_order.date_order
                single_data["purchase order activities"] = purchase_order.activity_ids
                single_data["purchase order source document"] = purchase_order.origin
                single_data["purchase order total"] = purchase_order.amount_total
                single_data["purchase order status"] = purchase_order.state
                single_data["purchase order untaxed"] = purchase_order.amount_untaxed
                single_data["purchase order billing status"] = purchase_order.invoice_status
                single_data["purchase order currency"] = purchase_order.currency_id.name
                single_data["purchase order expected arrival"] = purchase_order.date_planned

                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Invoice_Order_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_invoice_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            invoice_orders = request.env['account.move'].search([])
            for invoice_order in invoice_orders:
                single_data = {}
                single_data["invoice number"] = invoice_order.name
                single_data["invoice customer"] = invoice_order.invoice_partner_display_name
                single_data["invoice date"] = invoice_order.invoice_date
                single_data["invoice due date"] = invoice_order.invoice_date_due
                single_data["invoice activities"] = invoice_order.activity_ids
                single_data["invoice tax excluded"] = invoice_order.amount_untaxed_signed
                single_data["invoice total"] = invoice_order.amount_total_signed
                single_data["invoice total in currency"] = invoice_order.amount_total_in_currency_signed
                single_data["invoice payment status"] = invoice_order.payment_state
                single_data["invoice status"] = invoice_order.state
                single_data["invoice source document"] = invoice_order.invoice_origin
                single_data["invoice reference"] = invoice_order.ref
                single_data["invoice sales person"] = invoice_order.invoice_user_id.name
                single_data["invoice sales team"] = invoice_order.team_id.name
                single_data["invoice company"] = invoice_order.company_id.name
                single_data["invoice tax"] = invoice_order.amount_tax_signed
                single_data["invoice amount due"] = invoice_order.amount_residual_signed
                single_data["invoice currency"] = invoice_order.currency_id.name
                single_data["invoice to check"] = invoice_order.to_check
                single_data["invoice electronic invoicing"] = invoice_order.edi_state
                single_data["invoice journal"] = invoice_order.journal_id.name
                single_data["invoice statement"] = invoice_order.statement_line_id.name
                single_data["invoice payment term"] = invoice_order.invoice_payment_term_id.name
                single_data["invoice commercial_partner"] = invoice_order.commercial_partner_id.name
                single_data["invoice partner shipping"] = invoice_order.partner_shipping_id.name
                single_data["invoice sequence prefix"] = invoice_order.sequence_prefix
                single_data["invoice access token"] = invoice_order.access_token
                single_data["invoice move type"] = invoice_order.move_type
                single_data["invoice edi blocking level"] = invoice_order.edi_blocking_level
                single_data["invoice edi error message"] = invoice_order.edi_error_message
                single_data["invoice date"] = invoice_order.date
                single_data["invoice status"] = invoice_order.invoice_status
                single_data["invoice payment reference"] = invoice_order.payment_reference

                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Payments_Data', type='json', methods=['GET'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_payments_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            account_payments = request.env['account.payment'].search([])
            for account_payment in account_payments:
                single_data = {}
                single_data["account payment date"] = account_payment.date
                single_data["account payment number"] = account_payment.name
                single_data["account payment journal"] = account_payment.journal_id.name
                single_data["account payment method"] = account_payment.payment_method_line_id.name
                single_data["account payment customer"] = account_payment.partner_id.name
                single_data["account payment amount in currency"] = account_payment.amount_signed
                single_data["account payment currency"] = account_payment.currency_id.name
                single_data["account payment amount"] = account_payment.amount_company_currency_signed
                single_data["account payment status"] = account_payment.state
                single_data["account payment internal transfer"] = account_payment.is_internal_transfer
                single_data["account payment type"] = account_payment.payment_type
                single_data["account payment amount"] = account_payment.amount
                single_data["account payment memo"] = account_payment.ref
                single_data["account payment company bank account"] = account_payment.partner_bank_id
                return_json.append(single_data)

            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/endpoints', type='json', methods=['GET'], auth='public', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_getway(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            return_json.append({
                "products": "/AddisSystems/MPoS/Update/Products/Data",
                "partner": "/AddisSystems/MPoS/Update_Partner_Data",
                "user": "/AddisSystems/MPoS/Update_User_Data",
                "company": "/AddisSystems/MPoS/Update_Company_Data",
                "sales_order": "/AddisSystems/MPoS/Update_Sales_Order_Data",
                "purchase_order": "/AddisSystems/MPoS/Update_Purchase_Order_Data",
                "invoice order": "/AddisSystems/MPoS/Update_Invoice_Order_Data",
                "payments": "/AddisSystems/MPoS/Update_Payments_Data",
            })

            return return_json
        else:
            return {'error': 'User authentication failed'}






