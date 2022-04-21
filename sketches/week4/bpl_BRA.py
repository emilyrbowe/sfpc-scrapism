import requests

cookies = {
    'donation-identifier': 'cedcced797143807186f6e20f0e5093c',
    'abtest-identifier': 'cbd7d051c4d4ab106aa9ee24bd254dbc',
    'PHPSESSID': 'icv8do55oc1p4qfr8qpruq2q1j',
    'collections': 'bplimproperbostonian%2Cbplill%2Cbostonpubliclibrary%2CUSGovernmentDocuments',
}

headers = {
    'authority': 'archive.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'donation-identifier=cedcced797143807186f6e20f0e5093c; abtest-identifier=cbd7d051c4d4ab106aa9ee24bd254dbc; PHPSESSID=icv8do55oc1p4qfr8qpruq2q1j; collections=bplimproperbostonian%2Cbplill%2Cbostonpubliclibrary%2CUSGovernmentDocuments',
    'referer': 'https://archive.org/details/bostonpubliclibrary?and%5B%5D=creator%3A%22boston+redevelopment+authority%22&sort=-week&page=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'and[]': 'creator:"boston redevelopment authority"',
    'sort': '-week',
    'page': '2',
    'headless': '1',
    'facets_xhr': 'facets',
}

response = requests.get('https://archive.org/details/bostonpubliclibrary', headers=headers, params=params, cookies=cookies)

data = response

print(data)