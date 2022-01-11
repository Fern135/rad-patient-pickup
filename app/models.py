from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# pt_DOB     = db.Column(db.DateTime(timezone=True), default=func.now())
# pt_age        = pt_DOB - datetime.datetime.now().year # may change
# Pt_note       = db.Column(db.String(10000)) # in case patient cannot be picked up or something else

class Patient(db.Model):
    __tablename__ = "Patient"
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('User.id')) # connecto to User model
    pt_name       = db.colum(db.String(1000), nullable=False)
    pt_age        = db.Column(db.Integer, nullable=False) # age
    pt_sex        = db.colum(db.String(255), nullable=False)
    pt_DOB        = db.colum(db.DateTime, nullable=False) # date of birth
    visitor_id    = db.colum(db.Integer, unique=True, nullable=False)
    MR_id         = db.colum(db.Integer, unique=True, nullable=False)
    pt_procedure  = db.colum(db.String(1000), unique=True, nullable=False)
    reason_proce  = db.Column(db.String(10000), nullable=False)
    transport     = db.Column(db.String(100), nullable=False) # how to transport the patient
    pt_need_O2    = db.Column(db.Boolean, default=False, nullable=False) # True, or False
    fall_preca    = db.Column(db.Boolean, default=False, nullable=False) # fall precautions True, or False.
    pt_note       = db.Column(db.String(10000)) # in case patient cannot be picked up or something else


    def __init__(self, 
        pt_name, 
        pt_age, 
        pt_sex, 
        pt_DOB, 
        visitor_id, 
        MR_id, 
        pt_procedure, 
        reason_proce, 
        transport, 
        pt_need_O2, 
        fall_preca, 
        pt_note
    ):
        self.pt_name        = pt_name
        self.pt_age         = pt_age
        self.pt_sex         = pt_sex
        self.pt_DOB         = pt_DOB
        self.visitor_id     = visitor_id
        self.MR_id          = MR_id 
        self.pt_procedure   = pt_procedure
        self.reason_proce   = reason_proce
        self.transport      = transport
        self.pt_need_O2     = pt_need_O2
        self.fall_preca     = fall_preca
        self.pt_note        = pt_note


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(150), unique=True)
    full_name   = db.Column(db.String(150))
    password    = db.Column(db.String(150))
    patient     = db.relationship('Patient')