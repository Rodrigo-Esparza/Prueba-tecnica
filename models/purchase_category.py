from odoo import fields, models

class PurchaseCategory(models.Model):
    _name = "purchase.category"
    _description = "Purchase Category"
    _order = "name"

    name = fields.Char(required=True, index=True)
    description = fields.Text()

    _sql_constraints = [
        ("purchase_category_name_uniq", "unique(name)", "El nombre de la categoría debe ser único."),
    ]