import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
        
async def login_cookie(session, url):
    cookie = ''
    login_data = {"username":"company1_operator",
                "password":"05faa4120082731dcedf1afd70795135",
                "clientType":"plant",
                "role":"operator",
                "plantId":"5a411cbf5901f74bcce29731"
    }
    async with session.post(url,data=login_data) as resp:
        respon = await resp.text()
        loaded_json = json.loads(respon,encoding='UTF-8')
        cookie = loaded_json['data']
    return cookie


async def main():
    url = 'http://103.1.209.157:8686/auth'
    async with aiohttp.ClientSession() as session:
        cookie = await login_cookie(session, url)
        print ("Cookie = " , cookie)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())