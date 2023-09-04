import json

from odoo import http
from odoo.http import request
import werkzeug


class ClassController(http.Controller):
    @http.route(['/qlsv/classes', '/link2'], type='http', auth='none', methods=["GET"])
    def class_check(self):
        classes = request.env['class.ql'].sudo().search([])
        html_result = '<html><body><ul>'
        for c in classes:
            html_result += "<li> %s </li>" % c.name
        html_result += '</ul></body></html>'
        return html_result

    # Ví dụ truyền biến trên url
    @http.route('/pra/<int:id>', type='http', auth='none', methods=["GET"])
    def pra1(self, id):
        return "Ví dụ về biến %s đầu tiên" % str(id)

    # Ví dụ về chuyển hướng
    @http.route('/redirect', type='http', auth='none')
    def redirect01(self):
        return werkzeug.utils.redirect('https://www.google.com')

    # Ví dự về render ra template web.login -> Xuất ra form login
    @http.route('/render', auth='none')
    def render01(self):
        return request.render("web.login")

    # Ví dụ trả về dữ liệu dạng json
    @http.route('/json_example', auth='none')
    def json_ex(self):
        return json.dumps({
            'name': 'Nguyễn Công Bình',
            'address': 'Hà Nội'
        })

    # Ví dụ về hàm tạo đối tượng lớp
    @http.route('/class/create', auth='none')
    def create_class_school(self):
        c = request.env['class.ql'].sudo().create({
            'name': 'test thêm lớp 1'
        })
        return "Lớp đã được thêm"
