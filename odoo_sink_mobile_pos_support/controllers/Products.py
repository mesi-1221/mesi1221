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

    @http.route('/addisystems/create/product/data', type='json', methods=['POST', 'GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_create_customer_invoiceseddfgh(self, **kw):
        if request.env.user and request.env.user.id:
            data = json.loads(request.httprequest.data)
            df = data.copy()
            quantity = df.pop("quantity", None)
            data['name'] = data.get('name')
            product_tmpl = request.env['product.template'].sudo().create(df)
            product = request.env['product.product'].search([("product_tmpl_id", "=", product_tmpl.id)])

            stock = request.env["stock.quant"].search([('product_id', '=', product.id)])
            print(stock)
            stock_data = {

                "product_id": product.id,
                "quantity": quantity,
                "location_id": data.get("location_id"),
            }
            if not stock:
                request.env["stock.quant"].create(stock_data)
            else:
                stock.write(stock_data)
            try:
                x = 0
                return {
                    "status": 1,
                }
            except Exception as e:
                return {"status": e}


    @http.route('/update/product/data', type='json', methods=['POST', 'GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_updataswde_products_data(self, **kw):
        if request.env.user and request.env.user.id:
            vals = json.loads(request.httprequest.data)

            stock = request.env["stock.quant"].search([('product_id', '=', vals['product_id'])])
            if not stock:
                request.env["stock.quant"].create(vals)
            else:
                stock.write(vals)
            try:
                x = 0
                return {
                    "status": 1,
                }
            except Exception as e:
                return {"status": e}

    @http.route('/AddisSystems/MPoS/Update/Products/Data', type='json', methods=['POST', 'GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_update_products_data(self,**kw):
        if request.env.user and request.env.user.id:
            data = json.loads(request.httprequest.data)
            return_json = []
            products = request.env['product.template'].search([])
            for product in products:
                quants = request.env['stock.quant'].search([('product_tmpl_id', '=', product.id)])
                product_product = request.env['product.product'].search([("product_tmpl_id", "=", product.id)])
                print(product_product)
                try:
                    quant = quants[0]
                    onhand_qty=quant.quantity
                except:
                    onhand_qty=0

                single_data = {
                        "name": product.name,
                        "product_id": product.id,
                        "product_product": product.id,
                        "internal_reference": product.default_code,
                        "price": product.list_price,
                        "quantity_on_hand": onhand_qty,
                        "cost": product.standard_price,
                        "product_type": product.detailed_type,
                        "product_category": product.categ_id.name,
                        "product_image": product.image_1920,
                        "company_id": product.company_id.id,
                        "invoicing_policy": product.invoice_policy,
                        "can_be_sold": product.sale_ok,
                        "can_be_purchased": product.purchase_ok,
                        "available_in_pos": product.available_in_pos,
                        "customer_taxes": product.taxes_id.name,
                    }
                print("i 'am taried by teybercloaseses",product.id, product.name, product.image_1920)

                return_json.append(single_data)

            return return_json
        else:
            return {'error': 'User authentication failed'}


    @http.route('/AddisSystems/MPoS/Update_Partner_Data', type='json', methods=['POST', 'GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos__update_partner_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            partners = request.env['res.partner'].search([])
            for partner in partners:
                single_data = {}
                single_data["partner_name"] = partner.name
                single_data["partner_phone"] = partner.phone
                single_data["partner_email"] = partner.email
                single_data["partner_website"] = partner.website
                single_data["partner_title"] = partner.title.name
                single_data["partner_tags"] = partner.category_id
                single_data["partner_vat"] = partner.vat
                single_data["partner_id"] = partner.company_id.name
                single_data["partner_state"] = partner.street
                single_data["partner_state2"] = partner.street2
                single_data["partner_city"] = partner.city
                single_data["partner_position"] = partner.function
                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_User_Data', type='json', methods=['GET', 'POST'], auth='user', csrf=False,
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

    @http.route('/AddisSystems/MPoS/Update_Company_Data', type='json', methods=['GET', 'POST'], auth='user', csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_company_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            companys = request.env['res.company'].search([])
            for company in companys:
                single_data = {}
                single_data["company_id"] = company.id
                single_data["company_name"] = company.name
                single_data["company_parent"] = company.partner_id.name
                single_data["company_active"] = company.active
                single_data["company_fiscal year"] = company.fiscalyear_last_day
                single_data["company_Address"] = company.street
                single_data["company_Address2"] = company.street2
                single_data["company_city"] = company.city
                single_data["company_phone"] = company.phone
                single_data["company_mobile"] = company.mobile
                single_data["company_email"] = company.email
                single_data["company_website"] = company.website
                single_data["company_currency"] = company.currency_id
                single_data["company_paper_format"] = company.paperformat_id
                single_data["company_font"] = company.font


                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Sales_Order_Data', type='json', methods=['GET', 'POST'], auth='user',
                csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_sales_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            sales_orders = request.env['sale.order'].search([])
            for sales_order in sales_orders:
                single_data = {}
                single_data["sales_order_number"] = sales_order.name
                single_data["sales_order_creation data"] = sales_order.create_date
                single_data["sales_order_customer"] = sales_order.partner_id.name
                single_data["sales_order_salesperson"] = sales_order.user_id.name
                single_data["sales_order_activities"] = sales_order.activity_ids
                single_data["sales_order_company"] = sales_order.company_id.name
                single_data["sales_order_total"] = sales_order.amount_total
                single_data["sales_order_status"] = sales_order.state
                single_data["sales_order_invoice_status"] = sales_order.invoice_status
                single_data["sales_order_untaxed_amount"] = sales_order.amount_untaxed
                single_data["sales_order_quotation_date"] = sales_order.date_order
                single_data["sales_order_expiration_date"] = sales_order.validity_date
                single_data["sales_order_pricelist"] = sales_order.pricelist_id.name
                single_data["sales_order_payment terms"] = sales_order.payment_term_id.name
                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Purchase_Order_Data', type='json', methods=['GET', 'POST'], auth='user',
                csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_purchase_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            purchase_orders = request.env['purchase.order'].search([])
            for purchase_order in purchase_orders:
                single_data = {}
                single_data["purchase_order_reference"] = purchase_order.name
                single_data["purchase_order_vendor"] = purchase_order.partner_id.name
                single_data["purchase_order_company"] = purchase_order.company_id.name
                single_data["purchase_order_buyer"] = purchase_order.user_id.name
                single_data["purchase_order_order_deadline"] = purchase_order.date_order
                single_data["purchase_order_activities"] = purchase_order.activity_ids
                single_data["purchase_order_source_document"] = purchase_order.origin
                single_data["purchase_order_total"] = purchase_order.amount_total
                single_data["purchase_order_status"] = purchase_order.state
                single_data["purchase_order_untaxed"] = purchase_order.amount_untaxed
                single_data["purchase_order_billing status"] = purchase_order.invoice_status
                single_data["purchase_order_currency"] = purchase_order.currency_id.name
                single_data["purchase_order_expected arrival"] = purchase_order.date_planned

                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Invoice_Order_Data', type='json', methods=['GET', 'POST'], auth='user',
                csrf=False,
                save_session=False)
    def get_addis_systems_mpos_update_invoice_order_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            invoice_orders = request.env['account.move'].search([])
            for invoice_order in invoice_orders:
                single_data = {}
                single_data["invoice_number"] = invoice_order.name
                single_data["invoice_customer"] = invoice_order.invoice_partner_display_name
                single_data["invoice_date"] = invoice_order.invoice_date
                single_data["invoice_due_date"] = invoice_order.invoice_date_due
                single_data["invoice_activities"] = invoice_order.activity_ids
                single_data["invoice_tax_excluded"] = invoice_order.amount_untaxed_signed
                single_data["invoice_total"] = invoice_order.amount_total_signed
                single_data["invoice_total_in_currency"] = invoice_order.amount_total_in_currency_signed
                single_data["invoice_payment_status"] = invoice_order.payment_state
                single_data["invoice_status"] = invoice_order.state
                single_data["invoice_source_document"] = invoice_order.invoice_origin
                single_data["invoice_reference"] = invoice_order.ref
                single_data["invoice_sales_person"] = invoice_order.invoice_user_id.name
                single_data["invoice_sales_team"] = invoice_order.team_id.name
                single_data["invoice_company"] = invoice_order.company_id.name
                single_data["invoice_tax"] = invoice_order.amount_tax_signed
                single_data["invoice_amount_due"] = invoice_order.amount_residual_signed
                single_data["invoice_currency"] = invoice_order.currency_id.name
                single_data["invoice_to_check"] = invoice_order.to_check
                single_data["invoice_electronic_invoicing"] = invoice_order.edi_state
                single_data["invoice_journal"] = invoice_order.journal_id.name
                single_data["invoice_statement"] = invoice_order.statement_line_id.name
                single_data["invoice_payment_term"] = invoice_order.invoice_payment_term_id.name
                single_data["invoice_commercial_partner"] = invoice_order.commercial_partner_id.name
                single_data["invoice_partner_shipping"] = invoice_order.partner_shipping_id.name
                single_data["invoice_sequence_prefix"] = invoice_order.sequence_prefix
                single_data["invoice_access_token"] = invoice_order.access_token
                single_data["invoice_move_type"] = invoice_order.move_type
                single_data["invoice_edi_blocking_level"] = invoice_order.edi_blocking_level
                single_data["invoice_edi_error_message"] = invoice_order.edi_error_message
                single_data["invoice_date"] = invoice_order.date
                single_data["invoice_status"] = invoice_order.invoice_status
                single_data["invoice_payment_reference"] = invoice_order.payment_reference

                return_json.append(single_data)
            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/Update_Payments_Data', type='json', methods=['GET', 'POST'], auth='user', csrf=False,save_session=False)
    def get_addis_systems_mpos_update_payments_data(self, **kw):
        if http.request.env.user and http.request.env.user.id:
            return_json = []
            account_payments = request.env['account.payment'].search([])
            for account_payment in account_payments:
                single_data = {}
                single_data["account_payment_date"] = account_payment.date
                single_data["account_payment_number"] = account_payment.name
                single_data["account_payment_journal"] = account_payment.journal_id.name
                single_data["account_payment_method"] = account_payment.payment_method_line_id.name
                single_data["account_payment_customer"] = account_payment.partner_id.name
                single_data["account_payment_amount_in_currency"] = account_payment.amount_signed
                single_data["account_payment_currency"] = account_payment.currency_id.name
                single_data["account_payment_amount"] = account_payment.amount_company_currency_signed
                single_data["account_payment_status"] = account_payment.state
                single_data["account_payment_internal_transfer"] = account_payment.is_internal_transfer
                single_data["account_payment_type"] = account_payment.payment_type
                single_data["account_payment_amount"] = account_payment.amount
                single_data["account_payment_memo"] = account_payment.ref
                single_data["account_payment_company_bank_account"] = account_payment.partner_bank_id
                return_json.append(single_data)

            return return_json
        else:
            return {'error': 'User authentication failed'}

    @http.route('/AddisSystems/MPoS/get_products_by_company/<int:company_id>', type='json', methods=['POST', 'GET'], auth='user',
                csrf=False, save_session=False)
    def get_products_by_company_id(self,company_id, **kw):
        if request.env.user and request.env.user.id:
            return_json = []
            products = request.env['product.template'].search([('company_id', '=', company_id)])
            for product in products:
                quants = request.env['stock.quant'].search([('product_tmpl_id', '=', product.id)])
                try:
                    quant = quants[0]
                    onhand_qty=quant.quantity
                except:
                    onhand_qty=0
                single_data = {
                    'company_name': product.company_id.name,
                    'product_name': product.name,
                    "product_id": product.id,
                    "quantity_on_hand": onhand_qty,
                    "internal_reference": product.default_code,
                    "price": product.list_price,
                    "cost": product.standard_price,
                    "product_type": product.detailed_type,
                    "product_category": product.categ_id.name,
                    "invoicing_policy": product.invoice_policy,
                    "can_be_sold": product.sale_ok,
                    "can_be_purchased": product.purchase_ok,
                    "available_in_pos": product.available_in_pos,
                    "customer_taxes": product.taxes_id.name,
                    "product_image": product.image_1920,

                }
                return_json.append(single_data)

            return return_json
        else:
            return {'error': 'User authentication failed'}


    @http.route('/create/customer/sales_order/data', type='json', methods=['POST', 'GET'], auth='user', csrf=False,
                save_session=False)
    def addis_systems_mpos_create_customer_invoice(self, **kw):
        if request.env.user and request.env.user.id:
            data = json.loads(request.httprequest.data)
            print(data)
            p = request.env['sale.order'].sudo().create(data)
            required_fields = []
            for field_name, field in request.env["sale.order.line"]._fields.items():
                if field.required:
                    required_fields.append(field_name)
            print((required_fields))
            print(data)
            try:
                return {
                    "status": 1,
                }
            except Exception as e:
                return {"status": e}

    @http.route('/AddisSystems/MPoS/endpoints', type='json', methods=['GET', 'POST'], auth='public', csrf=False,save_session=False)
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
                "invoice_order": "/AddisSystems/MPoS/Update_Invoice_Order_Data",
                "payments": "/AddisSystems/MPoS/Update_Payments_Data",
                "product_company_by_id": "/AddisSystems/MPoS/get_products_by_company/<int:company_id>",
                "create_product": "/create/customer/sales_order/data",
            })
            return return_json
        else:
            return {'error': 'User authentication failed'}
