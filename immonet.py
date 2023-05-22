import requests as r


get_auth_token = r.get("https://www.immonet.de/immobiliensuche/beta/assets/config/de/prod-configuration.json")

get_auth_token_json = get_auth_token.json()

auth_token = get_auth_token_json["authorizationToken"]


get_token = r.post(url="https://api.immowelt.com/auth/oauth/token", data="grant_type=client_credentials",
                   headers={
                       "Host": "api.immowelt.com",
                       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
                       "Accept": "application/json, text/plain, */*",
                       "Accept-Language": "en-US,en;q=0.5",
                       "Origin": "https://www.immonet.de",
                       "Referer": "https://www.immonet.de/",
                       "Authorization": f"Basic {auth_token}",
                       "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                       "Connection": "keep-alive",
                       "Sec-Fetch-Dest": "empty",
                       "Sec-Fetch-Mode": "cors",
                       "Sec-Fetch-Site": "cross-site"
                   })

get_token_json = get_token.json()
token = get_token_json["access_token"]


search_json = {
    "estateSubtypes": [],
    "excludedFeatureFilters": [],
    "distributionTypes": [
        "LEASE",
        "RENT"
    ],
    "estateType": "APARTMENT",
    "estateGroups": [
        "RESIDENTIAL"
    ],
    "immoItemTypes": [
        "ESTATE",
        "PROJECT"
    ],
    "areas": [
        {
            "areaType": "PLOT_AREA"
        }
    ],
    "featureFilters": [],
    "locations": [
        {
            "type": "LOCATION_ID",
            "id": 125472
        }
    ],
    "primaryPrice": {},
    "primaryArea": {},
    "rooms": {},
    "constructionYear": {},
    "sort": {
        "direction": "DESC",
        "field": "RELEVANCE"
    },
    "paging": {
        "size": 20,
        "page": 0
    }
}

search_header = {
    "Host": "api.immowelt.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://www.immonet.de",
    "Referer": "https://www.immonet.de/",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

search = r.post(url="https://api.immowelt.com/residentialsearch/v2/searches",
                headers=search_header, json=search_json)
print(search.json())
