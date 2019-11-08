

from .common import AccountInvoiceCommon


class AccountInvoiceTests(AccountInvoiceCommon):

    def test_001_invoice_fiscal_sequence_id(self):
        """
        Checks invoices gets the right fiscal_sequence_id
        when created
        """

        # Customer invoice (out_invoice)
        invoice_1_id = self.invoice_obj.create({
            'partner_id': self.partner_demo_1,
            'fiscal_type_id': self.fiscal_type_fiscal,
        })
        self.assertEqual(invoice_1_id.fiscal_sequence_id.id,
                         self.seq_fiscal)

        # Vendor bill (in_invoice)
        invoice_2_id = self.invoice_obj.create({
            'partner_id': self.partner_demo_2,
            'fiscal_type_id': self.fiscal_type_informal,
        })
        self.assertEqual(invoice_2_id.fiscal_sequence_id.id,
                         self.seq_informal)

        # Customer refund
        invoice_3_id = self.invoice_obj.create({
            'partner_id': self.partner_demo_3,
            'type': 'out_refund',
        })
        self.assertEqual(invoice_3_id.fiscal_sequence_id.id,
                         self.seq_credit_note)

        # Customer debit note
        invoice_4_id = self.invoice_obj.create({
            'partner_id': self.partner_demo_4,
            'type': 'out_invoice',
            'is_debit_note': True,
        })
        self.assertEqual(invoice_4_id.fiscal_sequence_id.id,
                         self.seq_debit_note)

# Account Invoice Tests

# TODO: an invoice does not get a fiscal sequence if invoice date >= fiscal
#  sequence expiration date

# TODO: invoice fiscal_sequence_status is computed correctly

# TODO: on change journal_id, if not fiscal, invoice fiscal_type_id and
#  fiscal_sequence_id = False

# TODO: when _onchange_fiscal_type(), if fiscal_type_id.journal_id then
#  invoice journal_id = fiscal_type_id.journal_id

# TODO: when _onchange_partner_id, if out_invoice and not fiscal_type_id,
#  invoice fiscal_type_id = partner_id.fiscal_type_id

# TODO: when _onchange_partner_id, if in_invoice,
#  fiscal_type_id = partner_id.fiscal_type_id
#  and expense_type = partner_id.expense_type

# TODO: when out_invoice validate, if not partner_id.sale_fiscal_type_id,
#  partner_id.sale_fiscal_type_id =  invoice.fiscal_type_id

# TODO: when in_invoice validate, if not partner_id.purchase_fiscal_type_id,
#  partner_id.purchase_fiscal_type_id = invoice.fiscal_type_id and if not
#  partner_id.expense_type, partner_id.expense_type = invoice.expense_type

# TODO: when invoice validate, if fiscal_type_id.required_document and
#  not partner_id.vat, raise UserError

# TODO: when out_invoice, out_refund validate,
#  if fiscal_type_id != unico ingreso and amount_total >= 250,000
#  raise UserError

# TODO: a random number of random types invoices always get the
#  right NCF when validate

# TODO: fiscal customer refunds are created with all correct data

# TODO: fiscal vendor refunds are created with all correct data

# TODO: fiscal customer debit notes are created with all correct data

# TODO: fiscal vendor debit notes are created with all correct data
