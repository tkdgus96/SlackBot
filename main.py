import urllib.request
from fastapi import FastAPI
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from bs4 import BeautifulSoup
import os

app = FastAPI()



client = WebClient(token='xoxb-6669740982740-6667189105139-s57zdnFYHgD2fjnSelcP3mvj')
# 홈페이지 주소 가져오기
url_thej = 'https://pf.kakao.com/_QxixlXG'              # 더제이푸드
url_miga = 'https://pf.kakao.com/_yTbHb'                # 미가푸드빌

file_name = '/home/user/Desktop/lunch/test.png'

response = client.conversations_join(channel="C06K6M8FTRD")

@app.get("/")
async def root():
    try:
        req = urllib.request.Request(url_thej)
        res = urllib.request.urlopen(url_thej).read()

        soup = BeautifulSoup(res, 'html.parser')
        # soup = soup.find("div", class_="view_thumb")

        img_src = soup.find("meta",property="og:image")['content']

        os.system("curl " + img_src + " > /tmp/test.jpg")
        response = client.files_upload_v2(
            channel="C06K6M8FTRD",
            file='/tmp/test.jpg',
            title="Test upload",
            initial_comment="Here is the latest version of the file!",
        )
    except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found
    return {"message": img_src}
