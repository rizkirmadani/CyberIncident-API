from flask import request, jsonify
from app.extensions import db
from app.models import User
from app.controllers.helpers import error, save, delete


def list_users():
    return jsonify({'success':True,'data':[u.to_dict() for u in User.query.order_by(User.id).all()]}),200

def create_user():
    data=request.get_json(silent=True) or {}
    name=str(data.get('name','')).strip(); email=str(data.get('email','')).strip().lower(); role=str(data.get('role','reporter')).strip().lower()
    if not name or not email: return error('Field name dan email wajib diisi.')
    if '@' not in email or '.' not in email.split('@')[-1]: return error('Format email tidak valid.')
    if role not in ['reporter','analyst','admin']: return error('Role harus reporter, analyst, atau admin.')
    if User.query.filter_by(email=email).first(): return error('Email sudah terdaftar.', 'DUPLICATE_EMAIL',409)
    user=User(name=name,email=email,role=role); result=save(user)
    if result: return result
    return jsonify({'success':True,'message':'User berhasil dibuat','data':user.to_dict()}),201

def get_user(id):
    user=User.query.get_or_404(id); return jsonify({'success':True,'data':user.to_dict()}),200

def update_user(id):
    user=User.query.get_or_404(id); data=request.get_json(silent=True) or {}
    if 'name' in data:
        name=str(data['name']).strip()
        if not name: return error('Name tidak boleh kosong.')
        user.name=name
    if 'email' in data:
        email=str(data['email']).strip().lower()
        if '@' not in email or '.' not in email.split('@')[-1]: return error('Format email tidak valid.')
        duplicate=User.query.filter(User.email==email,User.id!=id).first()
        if duplicate: return error('Email sudah digunakan user lain.','DUPLICATE_EMAIL',409)
        user.email=email
    if 'role' in data:
        role=str(data['role']).lower()
        if role not in ['reporter','analyst','admin']: return error('Role tidak valid.')
        user.role=role
    db.session.commit(); return jsonify({'success':True,'message':'User diperbarui','data':user.to_dict()}),200

def delete_user(id):
    user=User.query.get_or_404(id)
    if user.incidents: return error('User masih memiliki laporan; data tidak dapat dihapus.','CONFLICT',409)
    result=delete(user)
    if result: return result
    return jsonify({'success':True,'message':'User berhasil dihapus'}),200
