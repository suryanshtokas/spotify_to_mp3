import base64
import json
from requests import post, get

from dotenv import load_dotenv
import os

load_dotenv()



class Spotify:
    def __init__(self):
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")

        self.token = self.get_token()

    def get_token(self):
        auth_string = self.CLIENT_ID + ":" + self.CLIENT_SECRET
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
                "Authorization": "Basic " + auth_base64,
                "Content-Type": "application/x-www-form-urlencoded"
            }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(self):
        return {"Authorization": "Bearer " + self.token}

    def get_playlist_songs(self, playlist_id):
        url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
        headers = self.get_auth_header()
        result = get(url, headers=headers)
        json_result = json.loads(result.content)

        items = json_result["tracks"]["items"]

        songs_list = []
        for i in range(0, len(items)):
           songs_list.append(items[i]["track"]["name"] + " by " + items[i]["track"]["artists"][0]["name"])

        return songs_list




