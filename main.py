from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lottery')
def showlottery():
    url = 'http://www.taiwanlottery.com.tw/'
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    data1 = sp.select("#rightdown")
    data2 = data1[0].find_all('div', {'class':'contents_box02'})
    data3 = data2[2].find_all('div', {'class':'ball_tx ball_yellow'})
    data2 = data2[2].find('div', {'class':'ball_red'})
    return render_template('Show.html',data2 = data2, data3 = data3 )

if __name__ == '__main__':
    app.run(debug = True)
    
