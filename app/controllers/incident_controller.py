from flask import request,jsonify
from app.extensions import db
from app.models import Incident,IncidentUpdate,User,Asset,IncidentCategory
from app.controllers.helpers import error,save,delete

SEVERITIES=['low','medium','high','critical']
STATUSES=['open','investigating','resolved','closed']

def list_incidents():
    q=Incident.query
    search=request.args.get('search','').strip()
    status=request.args.get('status','').lower()
    severity=request.args.get('severity','').lower()
    if search:q=q.filter(Incident.title.ilike(f'%{search}%'))
    if status:
        if status not in STATUSES:return error('Filter status tidak valid.')
        q=q.filter_by(status=status)
    if severity:
        if severity not in SEVERITIES:return error('Filter severity tidak valid.')
        q=q.filter_by(severity=severity)
    try: page=max(1,int(request.args.get('page',1))); per_page=min(100,max(1,int(request.args.get('per_page',10))))
    except ValueError:return error('page dan per_page harus berupa angka.')
    pagination=q.order_by(Incident.created_at.desc()).paginate(page=page,per_page=per_page,error_out=False)
    return jsonify({'success':True,'data':[i.to_dict() for i in pagination.items],'pagination':{'page':page,'per_page':per_page,'total':pagination.total,'pages':pagination.pages}}),200

def create_incident():
    d=request.get_json(silent=True) or {}; title=str(d.get('title','')).strip(); desc=str(d.get('description','')).strip()
    if not title or not desc:return error('title dan description wajib diisi.')
    severity=str(d.get('severity','medium')).lower(); status=str(d.get('status','open')).lower()
    if severity not in SEVERITIES:return error('severity harus low, medium, high, atau critical.')
    if status not in STATUSES:return error('status tidak valid.')
    for key,model in [('user_id',User),('asset_id',Asset),('category_id',IncidentCategory)]:
        if not d.get(key):return error(f'{key} wajib diisi.')
        if not model.query.get(d[key]):return error(f'{key} tidak ditemukan.', 'REFERENCE_NOT_FOUND',404)
    inc=Incident(title=title,description=desc,severity=severity,status=status,user_id=d['user_id'],asset_id=d['asset_id'],category_id=d['category_id'])
    r=save(inc)
    if r:return r
    return jsonify({'success':True,'message':'Insiden berhasil dilaporkan','data':inc.to_dict()}),201

def get_incident(id):return jsonify({'success':True,'data':Incident.query.get_or_404(id).to_dict()}),200

def update_incident(id):
    inc=Incident.query.get_or_404(id); d=request.get_json(silent=True) or {}
    if 'title' in d:
        title=str(d['title']).strip()
        if not title:return error('title tidak boleh kosong.')
        inc.title=title
    if 'description' in d:
        desc=str(d['description']).strip()
        if not desc:return error('description tidak boleh kosong.')
        inc.description=desc
    if 'severity' in d:
        s=str(d['severity']).lower()
        if s not in SEVERITIES:return error('severity tidak valid.')
        inc.severity=s
    if 'status' in d:
        s=str(d['status']).lower()
        if s not in STATUSES:return error('status tidak valid.')
        inc.status=s
    for key,model in [('user_id',User),('asset_id',Asset),('category_id',IncidentCategory)]:
        if key in d:
            if not model.query.get(d[key]):return error(f'{key} tidak ditemukan.','REFERENCE_NOT_FOUND',404)
            setattr(inc,key,d[key])
    db.session.commit();return jsonify({'success':True,'message':'Insiden diperbarui','data':inc.to_dict()}),200

def delete_incident(id):
    inc=Incident.query.get_or_404(id); r=delete(inc)
    if r:return r
    return jsonify({'success':True,'message':'Insiden dihapus'}),200

def add_update(id):
    inc=Incident.query.get_or_404(id); d=request.get_json(silent=True) or {}; note=str(d.get('note','')).strip(); status=str(d.get('status',inc.status)).lower()
    if not note:return error('note wajib diisi.')
    if status not in STATUSES:return error('status tidak valid.')
    uid=d.get('user_id')
    if not uid or not User.query.get(uid):return error('user_id harus mengacu pada user yang ada.', 'REFERENCE_NOT_FOUND',404)
    inc.status=status; upd=IncidentUpdate(incident_id=id,user_id=uid,status=status,note=note)
    r=save(upd)
    if r:return r
    return jsonify({'success':True,'message':'Update penanganan tercatat','data':upd.to_dict()}),201

def list_updates(id):
    Incident.query.get_or_404(id)
    updates=IncidentUpdate.query.filter_by(incident_id=id).order_by(IncidentUpdate.created_at.desc()).all()
    return jsonify({'success':True,'data':[u.to_dict() for u in updates]}),200
