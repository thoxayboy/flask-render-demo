from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào từ Flask chạy trên Render!"

if __name__ == '__main__':
    app.run()
