import openai


def get_open_ai_api_chat_response(prompt):
    # 輸入open api key
    # openai.api_key = "你的api key"
    # 範列：openai.api_key = "sdfdsfasdfaewfgegerfvb"
    openai.api_key = "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"

    # 範例文件
    # openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
    #   messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": "Who won the world series in 2020?"},
    #         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #         {"role": "user", "content": "Where was it played?"}
    #     ]
    # )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=50,
        # stream=True, ???
        messages=[
            {"role": "assistant", "content": "你是一位碳排放和碳盤查專家"},
            {"role": "user", "content": prompt},
        ],
    )

    # response的範例
    #   {
    #  'id': 'chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve',
    #  'object': 'chat.completion',
    #  'created': 1677649420,
    #  'model': 'gpt-3.5-turbo',
    #  'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
    #  'choices': [
    #    {
    #     'message': {
    #       'role': 'assistant',
    #       'content': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'},
    #     'finish_reason': 'stop',
    #     'index': 0
    #    }
    #   ]
    # }
    # 服務身上菜了，我們開始吃想要吃的菜，這邊想要吃的菜就是傳回來的答案
    ai_answer = response["choices"][0]["message"]["content"].replace("\n", "<br>")
    print(ai_answer)
    # 把答案返迴給呼叫這個方程的地方
    return ai_answer
