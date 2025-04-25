# 日本語入力で文字化けしないように…
# coding: utf-8

#　必要なモジュールのインポート
from flask import Flask, render_template

# app という変数でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# --- View側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
# def以下がアクセス後の操作
def index():
    #return 'Hello World!'
    return render_template('cdindex.html') #追加

if __name__ == '__main__':
    app.run()