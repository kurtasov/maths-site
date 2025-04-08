from proj_maths.views import hello

def test_details(rf):
    request = rf.get('/hello')
    response = hello(request)
    assert "Hello" in response.content.decode("utf-8")
    assert response.status_code == 200


def test_with_unauthenticated_client(client):
    response = client.get('/stats')
    assert "Количество терминов" not in response.content.decode("utf-8")
    assert "Информация недоступна. Необходимо войти в систему." in response.content.decode("utf-8")


def test_with_authenticated_client(client, django_user_model):
    username = "root"
    password = "Django!2025"
    #user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    #client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    response = client.get('/stats')
    assert "Количество терминов" in response.content.decode("utf-8")