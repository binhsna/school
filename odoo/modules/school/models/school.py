# -*- coding: utf-8 -*-
from odoo import api, fields, models


class School(models.Model):
    _name = "school.ql"
    _description = "School Management"
    name = fields.Char(string="Tên trường")
    type = fields.Selection([('private', 'Dân lập'), ('public', 'Công lập')], default='public', string="Loại trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa chỉ")

    phone = fields.Char(string="Số điện thoại")
    hasOnlineClass = fields.Boolean(string="Có lớp online không")
    rank = fields.Integer(string="Xếp hạng")
    establishDay = fields.Date(string="Ngày thành lập")
    document = fields.Binary(string="Tài liệu về trường")
    document_name = fields.Char(string="Tên tài liệu")

    class_list = fields.One2many("class.ql", "school_id", string="Danh sách lớp học")
    tuition = fields.Float(compute="_compute_tuition", string="Học phí 1 kỳ")

    @api.depends("type")
    def _compute_tuition(self):
        for rc in self:
            if rc.type == "private":
                rc.tuition = 2000
            elif rc.type == "public":
                rc.tuition = 500
            else:
                rc.tuition = 0

    def _inverse_one(self):
        for rc in self:
            rc.tuition = 300
