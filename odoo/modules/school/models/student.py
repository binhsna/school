# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Student(models.Model):
    _name = "student.ql"
    _description = "Student Management"
    name = fields.Char(string="Họ và tên")
    birthday = fields.Date(string="Ngày sinh")
    class_id = fields.Many2one("class.ql", string="Lớp")
    subject_list = fields.Many2many("subject.ql", "rel_subject_student_qlsv", "student_id", "subject_id",
                                    string="Mối quan hệ học sinh với môn học")
    school_id = fields.Many2one(related="class_id.school_id", string="Trường học")
    # Học phí 1 kỳ
    fee_per_semester = fields.Float(related="school_id.tuition", string="Học phí 1 kỳ")
    # khối học
    grade = fields.Char(related="class_id.grade", string="Khối")
    # Số học kỳ
    semester = fields.Integer(compute="_compute_semester", string="Số học kỳ")
    tuition = fields.Float(compute="_compute_tuition", string="Tổng số học phí")
    # Tính học phí cho sinh viên (tuition)
    currency_id = fields.Many2one("res.currency", string="Đơn vị")
    tuition = fields.Monetary(compute="_compute_tuition", string="Tổng số học phí")

    @api.depends("grade")
    def _compute_semester(self):
        for rc in self:
            if rc.grade == "10":
                rc.semester = 2
            elif rc.grade == "11":
                rc.semester = 4
            else:
                rc.semester = 6

    @api.depends("semester", "fee_per_semester")
    def _compute_tuition(self):
        for rc in self:
            rc.tuition = rc.semester * rc.fee_per_semester

    # Hàm kiểm tra nhập môn học
    def write(seft, value):
        rtn = super(Student, seft).write(value)
        if not seft.subject_list:
            raise UserWarning("Bạn cần chọn môn học")
        return rtn
