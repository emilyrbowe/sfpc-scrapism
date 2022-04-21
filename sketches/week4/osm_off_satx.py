import requests

cookies = {
    '_osm_session': '052a7d08852f8a09524490214fe55977',
    '_osm_totp_token': '545510',
    '_pk_id.1.cf09': '7d7d1bc6f66464fe.1649776789.',
    '_pk_ref.1.cf09': '%5B%22%22%2C%22%22%2C1649776789%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.1.cf09': '1',
    '_osm_welcome': 'hide',
    '_osm_location': '-98.5280|29.4538|11|M',
}

headers = {
    'authority': 'www.openstreetmap.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_osm_session=052a7d08852f8a09524490214fe55977; _osm_totp_token=545510; _pk_id.1.cf09=7d7d1bc6f66464fe.1649776789.; _pk_ref.1.cf09=%5B%22%22%2C%22%22%2C1649776789%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.cf09=1; _osm_welcome=hide; _osm_location=-98.5280|29.4538|11|M',
    'if-none-match': 'W/"217fb1a10adfce5969918285f74814e8-gzip"',
    'referer': 'https://www.openstreetmap.org/history',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'x-csrf-token': 'RtPLK7H-GzKmYiuvAYJNY05_c_w7eHYHCtjOA5YfuUFRT3H_2kd5zxVRUMud6CAEzIcEjZ7U9FB82YBKKWwOIw',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'list': '1',
    'bbox': '-98.76629322767258,29.196688649909046,-98.2897612452507,29.71028204492455',
}

response = requests.get('https://www.openstreetmap.org/history', headers=headers, params=params, cookies=cookies)

print(response.text)