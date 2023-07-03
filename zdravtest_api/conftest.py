import pytest

from pageobject.api.account_client import AccountClient


@pytest.fixture()
def account_client(make_url_from_env):
    _client = AccountClient()
    _client.base_url = make_url_from_env['base_url']
    _client.api_version = make_url_from_env['api_version']
    return _client
