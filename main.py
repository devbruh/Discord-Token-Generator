
# this is a cut from the source #

 with open('CONFIGURATION.json', 'r+', encoding='utf-8') as configfile:
        config = json.load(configfile)
    while True:
        if currenttime_plus_timeout <= int(time()):
            break
        sleep(0.1)
    while True:
        try:
            with Client(transport=SyncProxyTransport.from_url(f'socks4://{getproxies()}')) as client:
                register = client.post(f"https://niggerito.discord.com/api/v{randint(2,3)}/auth/register", 
                    headers={
                        "Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IEVkZy85NC4wLjk5Mi40NyIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAuNDYwNi44MSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAxMzI5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"
                    },
                    json={
                        "captcha_key": bypasscaptcha,
                        "consent": True,
                        "date_of_birth": "1995-04-06",
                        'email': f"{randomstring(5)}@{choice(['blm', 'blm'])}.it", 
                        'password': '#splendit',
                        "fingerprint": null,
                        "gift_code_sku_id": None,
                        "invite": config['SERVER INVITE CODE'],
                        "username": username,
                        
                    }
                ).json()
            tokens_file = open("data/OUATH.txt", "a")
            tokens_file.write(f'{register["token"]}\n')
            tokens_file.close()
            return register["token"]
        except Exception as e: 

                pass
