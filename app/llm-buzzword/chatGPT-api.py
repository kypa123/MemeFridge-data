import os
import openai
from dotenv import load_dotenv

load_dotenv()


def getPredictBuzzword():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "현재는 존재하지 않는, 미래에 20, 30대가 사용할만한 친근한 유행어는 뭐가있을지 예측해줘"}
        ]
    )
    return completion


print(answer.encode().decode('utf-8'))
