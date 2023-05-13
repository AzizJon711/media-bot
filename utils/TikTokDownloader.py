import requests
from pprint import pprint

video_link="https://www.tiktok.com/@wasupitsraf/video/7214544333142265094?is_from_webapp=1&sender_device=mobile&sender_web_id=7198985344847119877"
async def TikTokVideo_info(video_link):
	url = "https://tiktok-download-without-watermark.p.rapidapi.com/analysis"

	querystring = {"url":video_link,"hd":"0"}

	headers = {
		"X-RapidAPI-Key": "f577bc3c56mshe02d1cf3dd0ae05p123c0fjsn21dffea739a0",
		"X-RapidAPI-Host": "tiktok-download-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	result={
		"nickname":response["data"]["author"]["nickname"],
		"comment_count":response["data"]["comment_count"],
		"download_count": response["data"]["download_count"],
		"music":response["data"]["music"],
		"video":response["data"]["play"],
		"region":response["data"]["region"],
		"title": response["data"]["title"],
		"share_count": response["data"]["share_count"],
		"play_count": response["data"]["play_count"],
	}
	return result
