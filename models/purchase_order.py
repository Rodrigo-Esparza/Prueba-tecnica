from odoo import api, fields, models, _
from odoo.exceptions import AccessError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    category_id = fields.Many2one(
        "purchase.category",
        string="Categoría de compra",
        tracking=True,
        help="Categoría de compra asignada a esta orden.",
    )

    def write(self, vals):
        if "category_id" in vals and not self.env.su:
            if not self.env.user.has_group("purchase_category_access.group_purchase_categorizer"):
                raise AccessError(_("No tienes permisos para modificar la categoría de compra."))
        return super().write(vals)