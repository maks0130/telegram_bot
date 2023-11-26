import requests
import re

def get_quardian():
    headers = {
        'authority': 'api.nextgen.guardianapps.co.uk',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
        'origin': 'https://www.theguardian.com',
        'referer': 'https://www.theguardian.com/football',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'dcr': 'true',
    }

    response = requests.get(
        'https://api.nextgen.guardianapps.co.uk/football/show-more/d972-2641-c242-f3ac.json',
        params=params,
        headers=headers,
    ).json()

    for i in response:
        id = i['properties']['maybeContent']['metadata']['id']
        name = [j['fields']['altText'] for j in i['properties']['maybeContent']['trail']['trailPicture']['allImages']]
        #url_foto = [j['url'] for j in i['properties']['maybeContent']['trail']['trailPicture']['allImages']]
        url_foto = i['properties']['maybeContent']['trail']['thumbnailPath']
        title = re.sub(r'\<[^>]*\>','', i['properties']['maybeContent']['fields']['body'])
        url = i['properties']['maybeContent']['metadata']['webUrl']
        #return i['properties']['maybeContent']['trail']['thumbnailPath']
        return [str(*name), title, url_foto, url, 'Guardian', id]
        break

#print(get_quardian())
#print(response)


def get_allfootball():
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://m.allfootballapp.com/news',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {

        'page': '1',
    }

    response = requests.get('https://m.allfootballapp.com/m/app/tabs/1.json', params=params, headers=headers).json()

    for i in response['articles']:
        if i['top'] == False:
            name = i['title']
            title = i['share_title']
            url_foto = i['thumb']
            url = i['url']
            foto_post =  '/'.join(url_foto.split('/')[:7])+'/' + ''.join(url_foto.split('/')[-1])
            #print(name, i['id'])
            return [name, title, foto_post, url, 'Allfootbal', i['id']]
            break
        else:
            continue
#print(get_allfootball())



#print(response)

