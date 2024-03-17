from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderReportWizard(models.TransientModel):
    _name = 'sale.order.report.wizard'
    _description = 'Sale Order Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def print_sale_orders(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start Date must be less than End Date')

        # filter the sale data with date
        sale_orders = self.env['sale.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date)
        ])
        report_data = []
        for data in sale_orders:
            report_data.append({
                'id': data.id,
                'partner_id': data.partner_id.name,
                'created_on': data.create_date,
                'name': data.name,
                'total_amount': data.amount_total,
                'order_line': [{
                    'product_id': items.product_id.name,
                    'description': items.name,
                    'quantity': items.product_uom_qty,
                    'unit_price': items.price_unit,
                    'amount': items.price_subtotal,
                } for items in data.order_line],
            })

        data = {'form_data': self.read()[0],
                'report_data': report_data}

        return self.env.ref('zinfog_task.sales_wise_report').report_action(self, data=data)



