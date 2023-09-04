# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Subject(models.Model):
    _name = "subject.ql"
    _description = "Subject Management"

    name = fields.Char(string="Tên môn học")
    author = fields.Char(string="Tác giả")
