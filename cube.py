#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# Automatic Discord notification when adding a new quest with cube on Layer3
# A script by TRTtheSalad
# Discord : https://discord.com/invite/szXyZSgSYg
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json
#!/usr/bin/python3

# API URL to query
api_url = "https://app.layer3.xyz/api/trpc/questSearch.search,collection.search,community.getCommunities?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%7D"

headers = {
    'authority': 'app.layer3.xyz',
    'method': 'GET',
    'path': '/api/trpc/questSearch.search,collection.search,community.getCommunities?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22searchQuery%22%3Anull%2C%22filter%22%3A%7B%22sort%22%3A%22last_added%22%2C%22chainIds%22%3A%5B%5D%2C%22tab%22%3A%22quests%22%2C%22difficulties%22%3A%5B%5D%2C%22types%22%3A%5B%5D%2C%22rewards%22%3A%5B%5D%2C%22hideCompleted%22%3Afalse%2C%22hideUncompleted%22%3Afalse%2C%22hideExpired%22%3Atrue%2C%22communitySort%22%3A%22name%22%2C%22isCubeEnabled%22%3Atrue%7D%7D%7D%7D',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'fr-FR,fr;q=0.6',
    'Cache-Control': 'max-age=0',
    'Cookie': '__cf_bm=wM4T1auXz46k58zMVfC.oMsZ1_gElKAPnCSB2kDtS.A-1715936352-1.0.1.1-09swgOT2jdJLC7JoOXRaHd6kVtnJgYDZvA_1HfCGPw6_rMjrakzQulBS5h1LYFP2F_PJHuPJtSzNbHf5cBoxwA',
    'Priority': 'u=0, i',
    'Sec-Ch-Ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-Gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:

    all_slugs = []
    data=response.json()
    
    for entry in data:
        # Extract slugs from elements for each entry
        slugs = [item['slug'] for item in entry['result']['data']['json']['items']]

        # Add the extracted slugs to the all_slugs list
        all_slugs.extend(slug for slug in slugs if slug)
        for item in entry['result']['data']['json']['items']:
            for quest in item.get('quests', []):
                if quest['slug']:
                    all_slugs.append(quest['slug'])
 
    # Load slugs from text file
    with open("slugs_quetes.txt", "r") as file:
        slugs_quetes = [line.strip() for line in file]

    # Find slugs that are not in the text file
    slugs_absents = list(set(all_slugs) - set(slugs_quetes))

    with open("slugs_quetes.txt", "w") as file:
        for slugs in all_slugs:
            file.write(str(slugs) + "\n")
    
    # Discord webhook URL
    discord_webhook_url = "YOUR_DISCORD_WEB_HOOK"

    for slug_absent in slugs_absents:
    # Creating the Discord webhook payload
        formatted_slug = ' '.join(word.capitalize() for word in slug_absent.split('-'))
        content = {
            "embeds": [
                {
                    "title": "🧊 Nouveau CUBE Layer3 🧊",
                    "fields": [
                        {
                            "name": formatted_slug,
                            "value": "🌐 "+"[Lien vers quête]("+"https://app.layer3.xyz/quests/"+ slug_absent+")",
                            "inline": True
                        }
                        ],
            "color": 15767615  
        }
    ]
}
        # Sending POST request to Discord webhook
        requests.post(discord_webhook_url, data=json.dumps(content), headers={"Content-Type": "application/json"})

else:
    print("La requête API a échoué avec le code d'état", response.status_code)


