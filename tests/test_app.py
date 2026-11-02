from app import app


def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_inventaire():
    response = app.test_client().get('/materiels')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0] == {'id': 1, 'nom': 'PC-ADMIN', 'type': 'ordinateur'}
    assert all({'id', 'nom', 'type'} <= item.keys() for item in data)


def test_route_inconnue():
    assert app.test_client().get('/inconnue').status_code == 404


def test_version(monkeypatch):
    monkeypatch.setenv('APP_VERSION', 'test-commit')
    response = app.test_client().get('/version')
    assert response.status_code == 200
    assert response.get_json() == {'version': 'test-commit'}
