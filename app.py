from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bom_info')
def info():
    df = pd.read_excel('bom.xls')
    return df.to_html()

if __name__ == '__main__':
    app.run()
