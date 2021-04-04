import re, sys, os, time, subprocess,discord,ffmpeg,youtube_dl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

main_links = [
"https://www.youtube.com/",
"https://www.nicovideo.jp/"
]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # youtube soundcloud nicovideo
    if message.content.startswith("_d"):
        if message.author.bot:
            return

        url=message.content.split(None,1)
        if any(s in url[1] for s in (main_links)):
            if "https://www.youtube.com/" in url[1] and "list=" in url[1]:
                th_list = url[1].split("list=")[0]
            else:
                th_list = url[1]

            cmd = 'youtube-dl -o ./%(title)s.%(ext)s -i -f mp4 --add-metadata ' + th_list
            await message.channel.send("ダウンロード中です")
            subprocess.check_call(cmd.split())
            await message.channel.send("ダウンロードが完了しました")

            return
        
        else:
            await message.channel.send("正しいurlを入力してください")
            return
    
    if message.content.startswith("_exit"):
        await message.channel.send("終了します")
        sys.exit()

client.run("********************")
