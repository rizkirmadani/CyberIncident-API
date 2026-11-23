def test_health_ok(client):
    res=client.get('/api/v1/health')
    assert res.status_code==200
    assert res.json['success'] is True

def test_user_create_and_validation(client):
    good=client.post('/api/v1/users',json={'name':'Test User','email':'test@example.com','role':'reporter'})
    assert good.status_code==201
    bad=client.post('/api/v1/users',json={'name':'Missing Email'})
    assert bad.status_code==400

def test_incident_create_requires_fields(client):
    res=client.post('/api/v1/incidents',json={'title':'No refs','description':'Missing linked IDs'})
    assert res.status_code==400
    assert res.json['success'] is False

def test_incident_list_pagination(client):
    res=client.get('/api/v1/incidents?page=1&per_page=5')
    assert res.status_code==200
    assert 'pagination' in res.json
