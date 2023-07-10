import openai


class ChatGPT:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def getPredictBuzzword(self, query: str) -> str:
        openai.api_key = self.api_key
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "넌 한국의 유행에 민감하고, 단어 하나로 사람을 웃길 수 있는 유쾌한 존재야."},
                {"role": "user",
                 "content": f'현재는 존재하지 않는, 미래에 한국의 20, 30대가 {query} 사용할만한 유행어는 무엇일지 예측해줘. 설명은 짧고 간결하게 알려줘. 유행어를 나타낼 수 있는 간결한 태그를 붙여서 알려줘. 주제에 대해 각각 5개만 알려줘.'
                            f'알려줄 때, 어떤 설명이나 맺음말을 포함하지 마. 배열에 담긴 string 형태로 돌려줘. 아래의 예시에서 어떤 편차도 없이 그대로 해줘.'
                            f'[["유행어이름","유행어에 대한 설명","유행어에 대한 태그 1 유행어에 대한 태그 2"],["유행어이름","유행어에 대한 설명","유행어에 대한 태그 1 유행어에 대한 태그 2"]]'}
            ]
        )
        return completion.choices[0].message.content.encode().decode('utf-8')