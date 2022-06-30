import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.add_argument('--kiosk')
    return chrome_options