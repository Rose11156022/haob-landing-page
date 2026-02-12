from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    """一頁式網站 - HABO 冷暖智慧風扇"""
    return render_template('index.html')

if __name__ == '__main__':
    # 生產環境使用環境變數設定 port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

