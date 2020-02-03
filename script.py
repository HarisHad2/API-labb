import requests

response = requests.get('https://api.football-data.org/v2/competitions/PL',
    headers = {'X-Auth-Token': 'e46affe63c904205b01f962f12450dbd'}, params={"winner": "Manchester United FC"} )


print(response.text)    

#response.headers["Manchester United FC"]

