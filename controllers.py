from fastapi import FastAPI
from starlette.templating import Jinja2Templates #渡された変数を元に動的にページを生成
from starlette.requests import Request
import db
from models import User, Task

app = FastAPI(
    title='FastAPIで作るtoDoアプリケーション',
    description="FastAIPチュートリアル:FastAPI(とstarlette)でシンプルなtodoアプリ作成",
    version="0.9 beta"
)

# テンプレート関連用の設定
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env #Jinja2.Enveronment: filterやglobalの設定用

def index(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})

def admin(reqest: Request):
    #ユーザータスクを取得
    #今はadminのみを取得
    user = db.session.query(User).filter(User.username == "admin").first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()
    return templates.TemplateResponse("admin.html",
                                      {"request": reqest,
                                       "user": user,
                                       "task": task})