from flask import request,jsonify
from app.extensions import db
from app.models import Asset
from app.controllers.helpers import error,save,delete

def list_assets(): return jsonify({'success':True,'data':[a.to_dict() for a in Asset.query.order_by(Asset.id).all()]}),200

def create_asset():
    d=request.get_json(silent=True) or {}; name=str(d.get('asset_name','')).strip(); typ=str(d.get('asset_type','')).strip()
    if not name or not typ: return error('asset_name dan asset_type wajib diisi.')
    a=Asset(asset_name=name,asset_type=typ,ip_address=d.get('ip_address'),description=d.get('description')); r=save(a)
    if r:return r
    return jsonify({'success':True,'message':'Asset berhasil dibuat','data':a.to_dict()}),201

def get_asset(id): return jsonify({'success':True,'data':Asset.query.get_or_404(id).to_dict()}),200

def update_asset(id):
    a=Asset.query.get_or_404(id); d=request.get_json(silent=True) or {}
    for field in ['asset_name','asset_type','ip_address','description']:
        if field in d:
            if field in ['asset_name','asset_type'] and not str(d[field]).strip(): return error(f'{field} tidak boleh kosong.')
            setattr(a,field,d[field])
    db.session.commit(); return jsonify({'success':True,'message':'Asset diperbarui','data':a.to_dict()}),200

def delete_asset(id):
    a=Asset.query.get_or_404(id)
    if a.incidents:return error('Asset masih terkait laporan insiden.','CONFLICT',409)
    r=delete(a)
    if r:return r
    return jsonify({'success':True,'message':'Asset dihapus'}),200
