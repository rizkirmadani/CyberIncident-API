from app.extensions import db
from datetime import datetime, timezone


def utcnow():
    return datetime.now(timezone.utc)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(30), nullable=False, default='reporter')
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)
    incidents = db.relationship('Incident', back_populates='reporter', lazy=True)
    updates = db.relationship('IncidentUpdate', back_populates='author', lazy=True)
    def to_dict(self):
        return {'id':self.id,'name':self.name,'email':self.email,'role':self.role,'created_at':self.created_at.isoformat()}

class Asset(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(120), nullable=False)
    asset_type = db.Column(db.String(50), nullable=False)
    ip_address = db.Column(db.String(45))
    description = db.Column(db.Text)
    incidents = db.relationship('Incident', back_populates='asset', lazy=True)
    def to_dict(self):
        return {'id':self.id,'asset_name':self.asset_name,'asset_type':self.asset_type,'ip_address':self.ip_address,'description':self.description}

class IncidentCategory(db.Model):
    __tablename__ = 'incident_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    incidents = db.relationship('Incident', back_populates='category', lazy=True)
    def to_dict(self):
        return {'id':self.id,'name':self.name,'description':self.description}

class Incident(db.Model):
    __tablename__ = 'incidents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), nullable=False, default='medium')
    status = db.Column(db.String(20), nullable=False, default='open')
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('incident_categories.id'), nullable=False)
    reporter = db.relationship('User', back_populates='incidents')
    asset = db.relationship('Asset', back_populates='incidents')
    category = db.relationship('IncidentCategory', back_populates='incidents')
    updates = db.relationship('IncidentUpdate', back_populates='incident', cascade='all, delete-orphan', lazy=True)
    def to_dict(self, include_relations=True):
        result={'id':self.id,'title':self.title,'description':self.description,'severity':self.severity,'status':self.status,'created_at':self.created_at.isoformat(),'user_id':self.user_id,'asset_id':self.asset_id,'category_id':self.category_id}
        if include_relations:
            result['reporter']=self.reporter.name if self.reporter else None
            result['asset']=self.asset.asset_name if self.asset else None
            result['category']=self.category.name if self.category else None
        return result

class IncidentUpdate(db.Model):
    __tablename__ = 'incident_updates'
    id = db.Column(db.Integer, primary_key=True)
    incident_id = db.Column(db.Integer, db.ForeignKey('incidents.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    note = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)
    incident = db.relationship('Incident', back_populates='updates')
    author = db.relationship('User', back_populates='updates')
    def to_dict(self):
        return {'id':self.id,'incident_id':self.incident_id,'user_id':self.user_id,'author':self.author.name if self.author else None,'status':self.status,'note':self.note,'created_at':self.created_at.isoformat()}
