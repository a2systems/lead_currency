# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _, api

class CrmLead(models.Model):
    _inherit = "crm.lead"

    def _default_currency(self):
        return self.env.ref('base.USD').id

    currency_id = fields.Many2one('res.currency',string='Moneda oportunidad',default=_default_currency)
