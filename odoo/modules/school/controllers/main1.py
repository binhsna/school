from modules.school.controllers.main import ClassController
from odoo import http


class ChildClassController(ClassController):

    # Ví dụ về kế thừa
    @http.route('/qlsv/classes', type='http', auth='none', methods=["GET"])
    def class_check(self):
        super(ChildClassController, self).class_check()
        return "inherit"
