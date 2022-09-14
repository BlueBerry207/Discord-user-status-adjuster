import requests
import time
import random

token = input('Token : ')
delay = input('Delay (only number) : ')
text = input('Text : ')
# guild_id = input('Guild ID : ')
# nick = input('Nick : ')

status_list = ['online', 'dnd', 'idle']
emoji_list = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣']
recent_status = None
recent_emoji = None

def nick(guild_id, nick):
  headers = {
        'authorization': token,
        'content-type': 'application/json',
        'cookie': '__dcfduid=fe8b3880499e11eca0b7a3a83b2e1d34; __sdcfduid=fe8b3881499e11eca0b7a3a83b2e1d348a3bf901949f280fcb9654c18258eef74e71a941e5d63891efc7e9911619fccc; __stripe_mid=940a619c-9732-4724-85c9-8d90f35bdc7a1a2423; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+22+2022+21%3A43%3A53+GMT%2B0800+(%EC%A4%91%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false; locale=en-US; __cf_bm=BdCVAhg237uVNGJZ11YM_uRL_ULpEYQUvNI0v5AQRf0-1645537727-0-Af72aIr44rZI+IadB5lltHPY4FDw2cVSzJ9K0A5yTqaPghWjIPFbUxovtZwbfcbp1S5jx5dlWjApSiyf3JoMRQUaCMwWiMnNW7GnhaBSNVSgz49RhmohGmy/XW5pVAyg9A==',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'x-fingerprint': '945666638852812850.u4vklrnz07XYBtH6o1Z6NQui6zc',
        'x-super-properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJrby1LUiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OC4wLjQ3NTguMTAyIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5OC4wLjQ3NTguMTAyIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMTU2MzMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }

  payload = {'nick': nick}
  
  r = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me", json=payload)
  #print(r.text)
  print(f"Changed to {nick}")
  

def change(status, emoji, text):
    headers = {
        'authorization': token,
        'content-type': 'application/json',
        'cookie': '__dcfduid=fe8b3880499e11eca0b7a3a83b2e1d34; __sdcfduid=fe8b3881499e11eca0b7a3a83b2e1d348a3bf901949f280fcb9654c18258eef74e71a941e5d63891efc7e9911619fccc; __stripe_mid=940a619c-9732-4724-85c9-8d90f35bdc7a1a2423; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+22+2022+21%3A43%3A53+GMT%2B0800+(%EC%A4%91%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false; locale=en-US; __cf_bm=BdCVAhg237uVNGJZ11YM_uRL_ULpEYQUvNI0v5AQRf0-1645537727-0-Af72aIr44rZI+IadB5lltHPY4FDw2cVSzJ9K0A5yTqaPghWjIPFbUxovtZwbfcbp1S5jx5dlWjApSiyf3JoMRQUaCMwWiMnNW7GnhaBSNVSgz49RhmohGmy/XW5pVAyg9A==',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'x-fingerprint': '945666638852812850.u4vklrnz07XYBtH6o1Z6NQui6zc',
        'x-super-properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJrby1LUiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OC4wLjQ3NTguMTAyIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5OC4wLjQ3NTguMTAyIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMTU2MzMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }

    payload = {
        'status': status,
        'custom_status' : {
            'emoji_name': emoji,
            'text': text
        }
    }

    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print(f"Changed to : {status} | {emoji} | {text}")

def get_unused_status():
    global recent_status
    while True:
        status = random.choice(status_list)
        if status != recent_status:
            recent_status = status
            return status
        else:
            pass

def get_unused_emoji():
    global recent_emoji
    while True:
        emoji = random.choice(emoji_list)
        if emoji != recent_emoji:
            recent_emoji = emoji
            return emoji
        else:
            pass

while True:
    chars = ""
    for i in range(len(text)):
        status = get_unused_status()
        emoji = get_unused_emoji()
        chars += text[i]
        change(status, emoji, chars)
        #nick(guild_id, nick)
        time.sleep(float(delay))