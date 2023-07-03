from pytest import mark

@mark.Api
def test_product_detail(zdrav_api):
    zdrav_api.product_detail()