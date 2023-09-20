import os.path

import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'

response = requests.get(url)

with open('selenium_logo_square_green.png', 'wb').write(response.content) as file:
    file.write(response.content)

with open('selenium_logo_square_green.png', 'rb') as file:
    selenium_png = file.read()
    print(len(selenium_png))
    assert len(selenium_png) == 30803

print(os.path.getsize('selenium_logo_square_green.png'))

