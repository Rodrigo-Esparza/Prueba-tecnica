{
    "name": "Purchase Category Access",
    "summary": "Categorizar órdenes de compra con control de acceso y reglas de visibilidad.",
    "version": "16.0.1.0.0",
    "author": "Tu Nombre",
    "category": "Purchases",
    "website": "",
    "depends": ["purchase"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "security/purchase_category_rules.xml",
        "views/purchase_category_views.xml",
        "views/purchase_order_views.xml",
    ],
    "license": "LGPL-3",
    "application": False,
    "installable": True
}