# 日本語入力で文字化けしないように…
# coding: utf-8

#　必要なモジュールのインポート
from flask import Flask, render_template
# app という変数でFlaskオブジェクトをインスタンス化
app = Flask(__name__)
# --- View側の設定 ---
@app.route('/')
def index():
    #return 'Hello World!'
    return render_template('index.html') #追加

if __name__ == '__main__':
    app.run()