import json


with open('PlayersInfo.json', 'r') as f:
    data = json.load(f)


seasons = {
    '1990': dict(), '1991': dict(), '1992': dict(), '1993': dict(), '1994': dict(),
    '1995': dict(), '1996': dict(), '1997': dict(), '1998': dict(), '1999': dict(),
    '2000': dict(), '2001': dict(), '2002': dict(), '2003': dict(), '2004': dict(),
    '2005': dict(), '2006': dict(), '2007': dict(), '2008': dict(), '2009': dict(),
    '2010': dict(), '2011': dict(), '2012': dict(), '2013': dict(), '2014': dict(),
    '2015': dict(), '2016': dict(), '2017': dict(), '2018': dict(), '2019': dict(),
    '2020': dict()
}


for player in data:
    try:
        birth_year = int(player['BIRTH'].split('/')[0])
        
        for year in player['YEARS']:
            age = year - birth_year

            try:
                seasons[str(year)][age] += 1

            except:
                seasons[str(year)][age] = 1
            
    except:
        continue


with open('SeasonAges.json', 'w') as f:
    json.dump(seasons, f)
