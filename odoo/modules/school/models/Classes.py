# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ClassQl(models.Model):
    _name = "class.ql"
    _description = "Class Management"
    name = fields.Char(string="Tên lớp")
    grade = fields.Char(compute="_auto_compute_grade", string="Khối")
    mainTeacher = fields.Text(string="GVCN")

    school_id = fields.Many2one("school.ql", string="Trường")
    student_list = fields.One2many("student.ql", "class_id", string="Danh sách học sinh")
    address = fields.Text(related="school_id.address", string="Địa chỉ trường", store=True)

    @api.depends("name")
    def _auto_compute_grade(self):
        for re in self:
            if re.name == False:
                re.grade = ''
            else:
                re.grade = ''.join(list(re.name)[0:2])
