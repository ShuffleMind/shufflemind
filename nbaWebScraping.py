from bs4 import BeautifulSoup
import requests
import pandas as pd
def getPlayerStats(years):
    #funcao para recuperar dados danba na web
    url = 'https://www.fantasypros.com/nba/stats/overall.php?'
    getUrl = url + str("year=") + str(years)
    response = requests.get(getUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    team = []
    player = []
    #loop para adicionar o campo team
    for j in df['Player']:
        j = j.split('(')
        player.append(j[0])
        team.append(j[1])
    team = pd.Series(team).str.replace(')', '')
    team = pd.Series(team)
    df['Player'] = player
    df['Team'] = team.str[0:3]
    df['Year']= years
    return df

def getHist(time):
    #funcao para fazer a carga dos dados historicos
    dfIn = pd.DataFrame()
    for getData in range(len(time)):
        temp = getPlayerStats(time[getData])
        dfIn = dfIn.append(temp, ignore_index=True)
    return dfIn
path = '/Users/rlchagas/Downloads/NBA1.csv'
dado = getHist(['2016','2015','2014','2013'])
dado.to_csv(path)
