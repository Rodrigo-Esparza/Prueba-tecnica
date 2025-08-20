from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    purchase_category_ids = fields.Many2many(
        "purchase.category",
        string="Categorías de compra asignadas",
        help="Categorías de compra a las que este usuario tiene acceso.",
    )