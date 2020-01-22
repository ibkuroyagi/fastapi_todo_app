# 今後触ることなく、サーバーを立ち上げるだけの関数
from urls import  app
import uvicorn

if __name__ == "__main__":
    # コンソールで [$ uvicorn run:app --reload]でも可
    uvicorn.run(app=app)
    # uvicorn.run(app=app, port=8888)ぽーと変更可能