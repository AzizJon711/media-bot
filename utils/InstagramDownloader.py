import requests
from pprint import pprint

post_link="https://instagram.com/stories/elmurodhaqnazarov/3067319201902515479?utm_source=ig_story_item_share&igshid=MDJmNzVkMjY="
async def GetInstagram(post_link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": post_link}

    headers = {
        "X-RapidAPI-Key": "f577bc3c56mshe02d1cf3dd0ae05p123c0fjsn21dffea739a0",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response


#pprint(GetInstagram(post_link))

#Post-Image, Post-Video, Carousel,Story-Video

