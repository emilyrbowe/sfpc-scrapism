# Sam downloaded from Stack Overflow

import requests
from bs4 import BeautifulSoup

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

response = requests.get("https://nytimes.com", "html.parser")
soup = BeautifulSoup(response.text)
images = soup.select("img")
for i in images:
    image_url = i.attrs.get("src")
    if image_url:
        download_file(image_url)


# image_url = "https://resource.logitech.com/w_900,h_900,c_limit,q_auto,f_auto,dpr_1.0/d_transparent.gif/content/dam/logitech/en/products/mice/mx-anywhere-3-for-mac/gallery/mx-anywhere-3-for-mac-product-gallery-pale-gray-top.png?v=1"

# download_file(image_url)

