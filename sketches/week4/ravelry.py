import requests

cookies = {
    'guest': 'IjY1Y2E5YzIxMzg2NzQwMmI5YTEzYzBmOWZhOTExZjk5Ig%3D%3D--b4aa90853c95cbe1eb2acf5056de06585e0ddd27',
    'radvid': '7d847d7f24528b16e01fdd6656c6b3b7',
    'version': '1',
    'flexworks': '1',
    'timezone': '-14400',
    'disable_dark_mode_switching': '0',
    'ravelry_classic': '0',
    'account': '1',
    'captchaid': '7d847d7f24528b16e01fdd6656c6b3b7',
    'webp_support': '1',
    'theme': 'herdwick',
    'last_inner_width': '590',
    'ravelrys_pocketses': 'eyJ1c2VyX2lkIjo5NjAzMDk1LCJ2ZXJzaW9uIjoxNTk5NjU4MTM5LCJzZXNzaW9uX2lkIjoiZDdlZjNmYWRjYjk1NTdmOGJmOWFjNDM2ZmE3OWMzMWYiLCJfY3NyZl90b2tlbiI6IkZ4OTlrZWQzYjc1b0hFNnVDMjBsVkdLTEZnaE91Q29GL1RqR0ZvTjM1RW89IiwibWluaV9yZWZlcnJlciI6InNlYXJjaC9wYXR0ZXJucyIsImxhc3Rfc2Vlbl9jaGVjayI6MTY0OTc3MjU5NiwidWFfbG9nZ2VkIjp0cnVlLCJnZW9jb2RpbmdfdjIiOls0Mi4zNDk4LC03MS4wNzY1LCJCb3N0b24sIE1hc3NhY2h1c2V0dHMsIFVTIl0sImJ1c2luZXNzX2xvb2t1cCI6dHJ1ZSwiZmxhc2giOnsiZmxhc2hlcyI6e319LCJzZWFyY2hfc2Vzc2lvbl9pZCI6Ijk2MDMwOTUxNjQ5NzcyNjM5In0%3D--49e912110df027102868ba1f22b8ce7c8a726506',
}

headers = {
    'authority': 'www.ravelry.com',
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'guest=IjY1Y2E5YzIxMzg2NzQwMmI5YTEzYzBmOWZhOTExZjk5Ig%3D%3D--b4aa90853c95cbe1eb2acf5056de06585e0ddd27; radvid=7d847d7f24528b16e01fdd6656c6b3b7; version=1; flexworks=1; timezone=-14400; disable_dark_mode_switching=0; ravelry_classic=0; account=1; captchaid=7d847d7f24528b16e01fdd6656c6b3b7; webp_support=1; theme=herdwick; last_inner_width=590; ravelrys_pocketses=eyJ1c2VyX2lkIjo5NjAzMDk1LCJ2ZXJzaW9uIjoxNTk5NjU4MTM5LCJzZXNzaW9uX2lkIjoiZDdlZjNmYWRjYjk1NTdmOGJmOWFjNDM2ZmE3OWMzMWYiLCJfY3NyZl90b2tlbiI6IkZ4OTlrZWQzYjc1b0hFNnVDMjBsVkdLTEZnaE91Q29GL1RqR0ZvTjM1RW89IiwibWluaV9yZWZlcnJlciI6InNlYXJjaC9wYXR0ZXJucyIsImxhc3Rfc2Vlbl9jaGVjayI6MTY0OTc3MjU5NiwidWFfbG9nZ2VkIjp0cnVlLCJnZW9jb2RpbmdfdjIiOls0Mi4zNDk4LC03MS4wNzY1LCJCb3N0b24sIE1hc3NhY2h1c2V0dHMsIFVTIl0sImJ1c2luZXNzX2xvb2t1cCI6dHJ1ZSwiZmxhc2giOnsiZmxhc2hlcyI6e319LCJzZWFyY2hfc2Vzc2lvbl9pZCI6Ijk2MDMwOTUxNjQ5NzcyNjM5In0%3D--49e912110df027102868ba1f22b8ce7c8a726506',
    'origin': 'https://www.ravelry.com',
    'referer': 'https://www.ravelry.com/patterns/search',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'x-newrelic-id': 'VwcOU0VSCwUDVA==',
    'x-prototype-version': '1.5.1_rc2',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'query': 'blue',
    'history': '1',
    'sort': 'best',
    'render_facets': '1',
    'authenticity_token': 'Fx99ked3b75oHE6uC20lVGKLFghOuCoF/TjGFoN35Eo=',
    '_': '',
}

response = requests.post('https://www.ravelry.com/patterns/search', headers=headers, cookies=cookies, data=data)

print(response.text())