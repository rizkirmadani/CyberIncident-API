from app import create_app
from app.extensions import db
from app.models import User, Asset, IncidentCategory, Incident

app=create_app()
with app.app_context():
    db.create_all()
    demo_user=User.query.filter_by(email='analyst@example.com').first()
    if not demo_user:
        demo_user=User(name='Demo Analyst',email='analyst@example.com',role='analyst'); db.session.add(demo_user)
    demo_asset=Asset.query.filter_by(asset_name='Demo Web Server').first()
    if not demo_asset:
        demo_asset=Asset(asset_name='Demo Web Server',asset_type='server',ip_address='192.0.2.10',description='Alamat IP dokumentasi untuk simulasi'); db.session.add(demo_asset)
    demo_category=IncidentCategory.query.filter_by(name='Phishing').first()
    if not demo_category:
        demo_category=IncidentCategory(name='Phishing',description='Simulasi email atau tautan phishing'); db.session.add(demo_category)
    db.session.commit()
    if not Incident.query.filter_by(title='Simulasi email phishing').first():
        db.session.add(Incident(title='Simulasi email phishing',description='Laporan simulasi email mencurigakan untuk keperluan demo.',severity='medium',status='open',user_id=demo_user.id,asset_id=demo_asset.id,category_id=demo_category.id)); db.session.commit()
    print('Seed berhasil. User, asset, kategori, dan contoh incident tersedia.')
