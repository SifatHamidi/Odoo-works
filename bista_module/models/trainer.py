# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _


class Trainer(models.Model):
    _name="bista.trainer"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Trainer"
    name=fields.Char(string="Name",compute='_compute_full_name',store=True)
    first_name=fields.Char()
    last_name=fields.Char()
    profile_image=fields.Image(string="Profile Image")

    _sql_constraints = [("name_unique", "unique(name)","The Name should be unique"),]                      

    @api.depends("first_name","last_name")
    def _compute_full_name(self):
        self.name=(self.first_name or '') + ' ' + (self.last_name or '')


class TrainingSubject(models.Model):
    _name="bista.training.subject"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Training Subject"

    name=fields.Char(string="Subject",store=True,required=True)
    description=fields.Html('Description',store=True)
    trainers=fields.Many2many("bista.trainer",string="Trainers",tracking=True)
    topics=fields.One2many("bista.training.topics","subject", string="Topics",tracking=True)
    _sql_constraints = [("name_unique", "unique(name)","The Name should be unique"),]   

class TrainingTopics(models.Model):
    _name="bista.training.topics"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Training Topics"

    name=fields.Char(string="Topic", required=True)
    subject=fields.Many2one("bista.training.subject", string="Subject", readonly=1)