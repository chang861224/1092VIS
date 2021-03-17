import requests
import json
from bs4 import BeautifulSoup as bs

teams = list()

f = open('TeamID.txt', 'r')
for line in f.readlines():
    teams.append({
            'id': line.split()[0],
            'pages': int(line.split()[1])
            })
f.close()
#print(teams)

f = open('AllPlayers.csv', 'w')

for team in teams:
    for page in range(team['pages']):
        url = 'http://www.cpbl.com.tw/players.html?&offset={}&status=&teamno={}'.format(str(page * 20), team['id'])
        req = requests.get(url)

        soup = bs(req.text, 'html.parser')
        items = soup.select('div.gap_b20 table.std_tb.mix_.gap_t20 tr')

        for item in items:
            try:
                TEAM = item.find_all('td')[0].text
                NAME = item.find_all('td')[1].text
                LINK = item.find_all('td')[1].find('a')['href']
                f.write(','.join([TEAM, NAME, LINK]) + '\n')
                print(','.join([TEAM, NAME]), 'Done!!')

            except:
                continue

f.close()


f = open('AllPlayers.csv', 'r')

players = list()

for line in f.readlines():
    link = line.split(',')[-1][:-1]

    url = 'http://www.cpbl.com.tw' + link
    req = requests.get(url)

    soup = bs(req.text, 'html.parser')

    birth = soup.select('table.player_info_other tr td')
    print(birth[4].text.split(':')[1])

    items = soup.select('table.std_tb.mix_x')

    years = list()

    for x in items:
        for item in x.find_all('td'):
            try:
                if int(item.text) >= 1990 and int(item.text) <= 2020 and int(item.text) not in years:
                    years.append(int(item.text))

            except:
                continue

    years.sort()
    player = {'BIRTH': birth[4].text.split(':')[1], 'YEARS': years}
    players.append(player)

f.close()


with open('PlayersInfo.json', 'w') as f:
    json.dump(players, f)

print('Process Done!!')
