from proj_maths.views import hello

def test_details(rf, admin_user):
    request = rf.get('/hello')
    response = hello(request)
    assert response.status_code == 200