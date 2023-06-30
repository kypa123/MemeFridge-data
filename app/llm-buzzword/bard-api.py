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




def getBuzzword():
    bard = Bard(token=os.getenv("_BARD_API_KEY"), session=session, timeout=60)
    answer = bard.get_answer("20대, 30대가 많이 사용할 것 같은, 현재 유행하고 있는 인터넷 유행어는 뭐가 있을까? 완전히 새로운 단어를 말해줄래?")['content'].split('\n')[1:-1]
    while '' in answer:
        answer.remove('')
    for a in answer:
        print(a)
    return answer

# getBuzzword()

def predictBuzzword():
    bard = Bard(token=os.getenv("_BARD_API_KEY"), session=session, timeout=60)
    answer = bard.get_answer("20대, 30대가 사용할 것 같은, 현재는 존재하지 않는 완전히 새로운 유행어를 유추해줄래? 대통령의 이름같은 것들은 제외해줘")['content'].split('\n')[1:-1]
    while '' in answer:
        answer.remove('')
    for a in answer:
        print(a)
    return answer

# predictBuzzword()