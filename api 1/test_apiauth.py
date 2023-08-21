from pytest import mark


@mark.API
def test_account_get_info(account_client):
    account_client.get_balance()
