from bardapi import Bard
import requests


class BardAPI:
    def __init__(self):
        self.session = requests.Session()
        self.header = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
        try:
            self.sessionid = input('세션값을 입력해주세요:')
        except Exception as e:
            raise e
        else:
            self.session.cookies.set("__SECURE-1PSID", self.sessionid)

    def getBuzzword(self):
        bard = Bard(token=self.sessionId, session=self.session, timeout=60)
        answer = bard.get_answer("20대, 30대가 많이 사용할 것 같은, 현재 유행하고 있는 인터넷 유행어는 뭐가 있을까? 대통령, 고인 등 혐오단어는 제외해줘. 20개만 알려줘")[
                     'content'].split('\n')[1:-1]
        while '' in answer:
            answer.remove('')
        return answer

    def predictBuzzword(self):
        bard = Bard(token=self.sessionId, session=self.session, timeout=30)
        answer = bard.get_answer("20대, 30대가 사용할 것 같은, 현재는 존재하지 않는 완전히 새로운 유행어를 유추해줄래? 대통령, 고인 등 혐오단어는 제외해줘. 20개만 알려줘")[
                     'content'].split('\n')[1:-1]
        while '' in answer:
            answer.remove('')
        return answer