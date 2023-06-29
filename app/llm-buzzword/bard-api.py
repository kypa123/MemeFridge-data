from bardapi import Bard
from dotenv import load_dotenv
import os
import requests

load_dotenv()
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }

session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

bard = Bard(token=os.getenv("_BARD_API_KEY"), session=session, timeout=30)
print(bard.get_answer("20대, 30대가 많이 사용할 것 같은, 현재 존재하지 않는 미래의 유행어가 뭐가 있을까? 완전히 새로운 단어를 말해줄래?")['content'])
# print(answer)
# Continued conversation without set new session
print(bard.get_answer("What is my last prompt??")['content'])