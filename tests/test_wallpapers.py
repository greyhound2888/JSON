import json
import requests

def test_highlights():
    try:
        with open('news.json', mode='r') as f:
            data = json.load(f)
            for lit_data in data['wallpapers']:
                url = lit_data['image']
                r = requests.get(url)
                assert r.status_code == 200, 'Broken url ' + url
    except IOError as e:
        assert False, 'Failed to open news.json'
