from odoo import fiels, models

Class update_category(model.models)
 _inherit = "updatecategory"

   update_category = fiels. Many2many(
     "purchase.category",
       string ="Se ha actualizado tus categorías con exito"
       help = "No se ha logrado actualizar favor de validar error"
) 
