from models import *
import db
import os

if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        #テーブルを作成
        Base.metadata.create_all(db.engine)

    #サンプルユーザ(admin)を作成
    admin = User(username="admin", password="fastpath", mail="hoge@gmail.com")
    db.session.add(admin)#追加
    db.session.commit()#コミット

    #サンプルタスク
    task = Task(
        user_id=admin.id,
        content="課題やる",
        deadline=datetime(2020,1,22,18,00,00),
    )

    print(task)
    db.session.add(task)
    db.session.commit()

    db.session.close()#セッションを閉じる
