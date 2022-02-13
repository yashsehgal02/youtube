import requests
from urllib.parse import unquote

def unlisted(url):
    request = requests.get(url)
    data = request.text
    url_encoded = data.split("""itag":""")[1].replace('18,"url":"',"").split('","')[0]
    url_encoded = unquote(url_encoded)
    return url_encoded.encode().decode('unicode_escape')
