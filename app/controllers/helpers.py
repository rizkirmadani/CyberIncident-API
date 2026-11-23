from flask import jsonify
from app.extensions import db

def error(message, code='VALIDATION_ERROR', status=400):
    return jsonify({'success':False,'error':{'code':code,'message':message}}), status

def save(model):
    try:
        db.session.add(model)
        db.session.commit()
        return None
    except Exception:
        db.session.rollback()
        return error('Data gagal disimpan. Pastikan input valid dan tidak duplikat.', 'DATABASE_ERROR', 400)

def delete(model):
    try:
        db.session.delete(model)
        db.session.commit()
        return None
    except Exception:
        db.session.rollback()
        return error('Data tidak dapat dihapus karena masih digunakan atau terjadi kesalahan.', 'DATABASE_ERROR', 409)
