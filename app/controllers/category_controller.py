from flask import request,jsonify
from app.extensions import db
from app.models import IncidentCategory
from app.controllers.helpers import error,save,delete

def list_categories(): return jsonify({'success':True,'data':[c.to_dict() for c in IncidentCategory.query.order_by(IncidentCategory.id).all()]}),200

def create_category():
    d=request.get_json(silent=True) or {}; name=str(d.get('name','')).strip()
    if not name:return error('name kategori wajib diisi.')
    if IncidentCategory.query.filter_by(name=name).first():return error('Kategori sudah ada.','DUPLICATE',409)
    c=IncidentCategory(name=name,description=d.get('description')); r=save(c)
    if r:return r
    return jsonify({'success':True,'message':'Kategori dibuat','data':c.to_dict()}),201

def get_category(id):return jsonify({'success':True,'data':IncidentCategory.query.get_or_404(id).to_dict()}),200

def update_category(id):
    c=IncidentCategory.query.get_or_404(id); d=request.get_json(silent=True) or {}
    if 'name' in d:
        name=str(d['name']).strip()
        if not name:return error('Nama kategori tidak boleh kosong.')
        duplicate=IncidentCategory.query.filter(IncidentCategory.name==name,IncidentCategory.id!=id).first()
        if duplicate:return error('Kategori sudah digunakan.','DUPLICATE',409)
        c.name=name
    if 'description' in d:c.description=d['description']
    db.session.commit();return jsonify({'success':True,'message':'Kategori diperbarui','data':c.to_dict()}),200

def delete_category(id):
    c=IncidentCategory.query.get_or_404(id)
    if c.incidents:return error('Kategori masih dipakai laporan.','CONFLICT',409)
    r=delete(c)
    if r:return r
    return jsonify({'success':True,'message':'Kategori dihapus'}),200
