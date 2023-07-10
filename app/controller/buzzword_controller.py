import os
from app.llm_buzzword.chatGPT_api import ChatGPT
from app.db.db import PostgreSQL
import ast

class BuzzwordController:
    def __init__(self, chatgptinstance: ChatGPT, postgresinstance: PostgreSQL):
        self.chatGPTInstance = chatgptinstance
        self.postgresInstance = postgresinstance

    def getRecentBuzzword(self) -> list:
        return self.postgresInstance.getRecentData()

    def updateRecentBuzzword(self) -> any or Exception:
        try:
            chatGPTPredictWords = self.chatGPTInstance.getPredictBuzzword('인터넷 커뮤니티에서, 인터넷 방송에서, 게임 방송에서')
            chatGPTPredictList = ast.literal_eval(chatGPTPredictWords)
            for singleList in chatGPTPredictList:
                for singleVal in singleList:
                    singleVal.replace('"','')
                    singleVal.replace("'",'')

            res = self.insertRecentBuzzword("chatGPT",chatGPTPredictList)

        except Exception as e:
            return e
        else:
            return res

    def insertRecentBuzzword(self, llm:str, datalist:list) -> Exception or str:
        try:
            self.postgresInstance.insertData(llm, datalist)
        except Exception as e:
            return e
        else:
            return 'ok'


PostgresInstance = PostgreSQL(os.getenv('POSTGRES_CONNECTION'))
ChatGPTInstance = ChatGPT(os.getenv('OPENAI_API_KEY'))
BuzzwordControllerInstance = BuzzwordController(ChatGPTInstance, PostgresInstance)
