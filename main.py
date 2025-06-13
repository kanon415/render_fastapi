from typing import Optional

from fastapi import FastAPI
import random
from fastapi.responses import HTMLResponse #インポート


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    message_list = [
        "大吉！素晴らしい幸運が舞い込むでしょう。"
        "中吉！努力が実を結び、良い結果が待っています。"
        "小吉！ちょっとした幸運があなたの元にやってきます。"
        "吉！安定した幸せな日々が続くでしょう。"
        "末吉！努力が実り始め、良い方向に進む時期です。"
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。"
        "小凶。注意が必要な日です。慎重に行動しましょう。"
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]
    #messages{"":""}
    #for i in range(0:len(omikuji_list)):
    #    messages  = {omikujiList(i):messageList(i)}
    #fortune = omikuji_list[random.randrange(10)]
    #message = messages.get(fortune)
    return omikuji_list[random.randrange(10)]


### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <h2>I'm hungry...</h2>
            <a url="https://www.keishicho.metro.tokyo.lg.jp/">check me</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)