import pytest


@pytest.mark.django_db
def test_openapi_root_path_open_to_all(client, settings):
    settings.FEATURE_DIRECTORY_CMS_OPENAPI_ENABLED = True
    response = client.get(
        '/openapi/'
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_openapi_ui_path_closed_to_user(client, settings):
    settings.FEATURE_DIRECTORY_CMS_OPENAPI_ENABLED = True
    response = client.get(
        '/openapi/ui/'
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_openapi_ui_path_open_to_admin(admin_client, settings):
    settings.FEATURE_DIRECTORY_CMS_OPENAPI_ENABLED = True
    response = admin_client.get(
        '/openapi/ui/'
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_openapi_redoc_path_closed_to_user(client, settings):
    settings.FEATURE_DIRECTORY_CMS_OPENAPI_ENABLED = True
    response = client.get(
        '/openapi/ui/redoc/'
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_openapi_redoc_path_open_to_admin(admin_client, settings):
    settings.FEATURE_DIRECTORY_CMS_OPENAPI_ENABLED = True
    response = admin_client.get(
        '/openapi/ui/redoc/'
    )
    assert response.status_code == 200
