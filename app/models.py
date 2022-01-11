from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

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

    #region not being used
    # def __init__(self, pt_name, pt_age, pt_sex, pt_DOB, visitor_id, MR_id, pt_procedure, reason_proce, transport, pt_need_O2, fall_preca, pt_note):
    #     self.pt_name        = pt_name 
    #     self.pt_age         = pt_age  
    #     self.pt_sex         = pt_sex  
    #     self.pt_DOB         = pt_DOB  
    #     self.visitor_id     = visitor_id  
    #     self.MR_id          = MR_id   
    #     self.pt_procedure   = pt_procedure  
    #     self.reason_proce   = reason_proce  
    #     self.transport      = transport  
    #     self.pt_need_O2     = pt_need_O2  
    #     self.fall_preca     = fall_preca  
    #     self.pt_note        = pt_note

    #endregion  

    #region setters
    def setNote(self, pt_note):
        self.pt_note = pt_note

    def setFallPrecautions(self, fall_preca):
        self.fall_preca = fall_preca

    def setO2Need(self, pt_need_O2):
        self.pt_need_O2 = pt_need_O2

    def setTransport(self, transport):
        self.transport = transport

    def setReasonProcedure(self, reason_proce):
        self.reason_proce = reason_proce
        
    def setProcedure(self, pt_procedure):
        self.pt_procedure = pt_procedure

    def setMRID(self, MR_id):
        self.MR_id = MR_id

    def setVisitorId(self,visitor_id):
        self.visitor_id = visitor_id    

    def setDOB(self, pt_DOB):
        self.pt_DOB = pt_DOB

    def setPtSex(self, pt_sex):
        self.pt_sex = pt_sex

    def setPtAge(self, pt_age):
        self.pt_age = pt_age

    def setPtName(self, pt_name):
        self.pt_name = pt_name

    #endregion

    #region getters
    def getNote(self):
        return self.pt_note

    def getFallPrecautions(self):
        return self.fall_preca

    def getNeedO2(self):
        return self.pt_need_O2

    def getTransport(self):
        return self.transport

    def getReasonProcedure(self):
        return self.reason_proce

    def getProcedure(self):
        return self.pt_procedure

    def getMRID(self):
        return self.MR_id

    def getVisitorId(self):
        return self.visitor_id

    def getDob(self):
        return self.pt_DOB

    def getSex(self):
        return self.pt_sex

    def getAge(self):
        return self.pt_age

    def getName(self):
        return self.pt_name

    #endregion


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(150), unique=True)
    full_name   = db.Column(db.String(150))
    password    = db.Column(db.String(150))
    api_key     = db.Column(db.String(500)) # to access all the pt information
    patient     = db.relationship('Patient')