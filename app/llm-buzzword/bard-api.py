from bardapi import Bard
from dotenv import load_dotenv
import os
import requests
load_dotenv()



# def setSession():
#     session = requests.Session()
#     session.headers = {
#             "Host": "bard.google.com",
#             "X-Same-Domain": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#             "Origin": "https://bard.google.com",
#             "Referer": "https://bard.google.com/",
#         }
#     try:
#         sessionId = input('세션값을 입력해주세요:')
#         session.cookies.set("__SECURE-1PSID", sessionId)
#         return [session, sessionId]
#     except:
#         return 'error occured. no session key input'
#
#
# def getBuzzword(session, sessionId):
#     bard = Bard(token=sessionId, session=session, timeout=60)
#     answer = bard.get_answer("20대, 30대가 많이 사용할 것 같은, 현재 유행하고 있는 인터넷 유행어는 뭐가 있을까? 완전히 새로운 단어를 말해줄래?")['content'].split('\n')[1:-1]
#     while '' in answer:
#         answer.remove('')
#     for a in answer:
#         print(a)
#     return answer
#
#
# def predictBuzzword(session, sessionId):
#     bard = Bard(token=sessionId, session=session, timeout=30)
#     answer = bard.get_answer("20대, 30대가 사용할 것 같은, 현재는 존재하지 않는 완전히 새로운 유행어를 유추해줄래? 대통령의 이름같은 것들은 제외해줘. 20개만 알려줘")['content'].split('\n')[1:-1]
#     while '' in answer:
#         answer.remove('')
#     for a in answer:
#         print(a)
#     return answer
#
#
# session, sessionId = setSession()
# predictBuzzword(session, sessionId)


session = requests.Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", 'YQiXXgLs5L6QWLco-FNnoUYleoSBjxJa9jRNpBy6YLaX84A_ltqfSzIvjEYzjUASKxMvCg.')

bard = Bard(token='YQiXXgLs5L6QWLco-FNnoUYleoSBjxJa9jRNpBy6YLaX84A_ltqfSzIvjEYzjUASKxMvCg.', session=session, timeout=30)
answer = bard.get_answer("20대, 30대가 사용할 것 같은, 현재는 존재하지 않는 완전히 새로운 유행어를 유추해줄래? 대통령의 이름같은 것들은 제외해줘. 20개만 알려줘")['content'].split('\n')[1:-1]
answer2 = bard.get_answer("미안한데 너의 대답은 이미 존재하는 단어들이잖아. 미래에 사용할 것 같은, 현재는 없는 유행어들을 알려줘. 20개 알려줘")['content'].split('\n')[1:-1]