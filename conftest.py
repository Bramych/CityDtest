import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture