import requests
from pprint import pprint


url="https://youtu.be/6x2Ry40Lqig"
async def GetVideoInfo(video_url):
	if "https://youtu.be/"in video_url:
		video_link=video_url.replace("https://youtu.be/", "")
	elif "http://www.youtube.com/watch?v=" in video_url:
		video_link=video_url.replace("http://www.youtube.com/watch?v=", "")
	url = "https://yt-api.p.rapidapi.com/dl"

	querystring = {"id": video_link}

	headers = {
		"X-RapidAPI-Key": "f577bc3c56mshe02d1cf3dd0ae05p123c0fjsn21dffea739a0",
		"X-RapidAPI-Host": "yt-api.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	data={
		"video_title":response["title"],
		"channel_title":response["channelTitle"],
		"view_count":response["viewCount"],
		"audio":response["adaptiveFormats"][-3]["url"],
		"video":response["formats"],
		"thumbnail":response["thumbnail"][-1]["url"]
	}
	return data
async def GetAudioInfo(video_url):
	video_link=video_url.replace("https://youtu.be/", "")
	url = "https://youtube-mp36.p.rapidapi.com/dl"

	querystring = {"id": video_link}

	headers = {
		"X-RapidAPI-Key": "f577bc3c56mshe02d1cf3dd0ae05p123c0fjsn21dffea739a0",
		"X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	return response

#pprint(GetAudioInfo(url))


