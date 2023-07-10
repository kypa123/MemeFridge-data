import openai


class ChatGPT:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def getPredictBuzzword(self, query: str) -> list:
        openai.api_key = self.api_key
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f'현재는 존재하지 않는, 미래에 한국의 20, 30대가 {query} 사용할만한 유행어는 뭐가있을지 예측해줘. 설명은 최대한 짧고 간결하게 부탁할게. 그리고 해당 유행어를 나타낼 수 있는, 간결한 태그를 붙여서 알려줘. 20개만 알려줘'}
            ]
        )
        return completion.choices[0].message.content.encode().decode('utf-8').split("\n")