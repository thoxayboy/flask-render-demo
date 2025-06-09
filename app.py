from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào từ Flask chạy trên Render!"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # lấy port từ biến môi trường
    app.run(host="0.0.0.0", port=port)
