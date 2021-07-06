import wget
import praw
import time
from instabot import Bot
import random
import os
import shutil
from PIL import Image

isExist = os.path.exists("config")
if isExist:
    shutil.rmtree("config", ignore_errors=True)

#instagram login
bot = Bot()
bot.login (username = "your-username", password = "your-password")

#reddit login
reddit = praw.Reddit(client_id='reddit-script-client-id', client_secret='reddit-script-secret', user_agent='reddit-script-user-agent')

def get_post_meme():
    hot_posts = reddit.subreddit('dankmemes').hot(limit=48)
    tags_for_post = ["#meme", "#memes", "#funny", "#dankmemes", "#memesdaily", "#funnymemes", "#lol", "#follow", "#humor", "#like", "#dank", "#love", "#instagram", "#memepage", "#dankmeme", "#tiktok", "#comedy", "#lmao", "#fun", "#anime", "#lol", "#dailymemes", "#edgymemes", "#offensivememes", "#memestagram", "#bhfyp", "#instagood", "#funnymeme", "#memer",
                     "#reddit", "#shitpost", "#funnyvideos", "#explorepage", "#followforfollowback", "#jokes", "#viral", "#haha", "#likeforlikes", "#art", "#f", "#youtube", "#memesespa" "#memeita", "#explore", "#gaming", "#covid", "#minecraft", "#likes", "#memez", "#laugh", "#followme", "#edgy", "#trending", "#life", "#music", "#india", "#dankmemesdaily", 
                     "#gamer", "#cute",]
    for post in hot_posts:
       tagstring = ""
       for i in range(15):
           rand_tag = random.choice(tags_for_post)
           tagstring = tagstring + rand_tag + " "
       post_url = post.url
       file_ext = post_url[post_url.rindex("."):]
       wget.download(post_url, 'meme' + file_ext)
       try:
           im = Image.open("meme"+file_ext)  
           newsize = (1080, 1080) 
           im = im.resize(newsize) 
           im.save('meme'+file_ext)
       except:
           print("couldn't resize image; possible cause: unsupported file format")
       try:
           bot.upload_photo("meme"+file_ext,
                        caption = post.title + "(posted on r/dankmemes)" + "\n \n \n" + tagstring)
       except:
           print("error. possible cause: unsupported file format")
       time.sleep(15)
       if os.path.exists("meme"+file_ext):
           os.remove ("meme"+file_ext)
       time.sleep(1800)
       
while True:
    get_post_meme()
    time.sleep(360)