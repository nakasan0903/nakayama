from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template
from flask import send_from_directory
import requests
from flask import jsonify
from datetime import datetime, timedelta


def convert_to_jst(date_str):
    # UTCから日本時間への変換 (UTC +9)
    utc_time = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    jst_time = utc_time + timedelta(hours=9)
    # 日本語の日付形式に変換
    return jst_time.strftime('%Y年%m月%d日 %H:%M')

def get_arsenal_matches(api_key):
    url = 'https://api.football-data.org/v2/teams/57/matches'
    headers = {'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []
    for match in data['matches']:
        match_time_jst = convert_to_jst(match['utcDate'])
        matches.append({
            'date': match_time_jst,
            'homeTeam': match['homeTeam']['name'],
            'awayTeam': match['awayTeam']['name'],
            'competition': match['competition']['name']
        })

    return matches


app = Flask(__name__)
@app.route('/')
def index():
    # 固定のデータを準備
    team_name = "アーセナルFC"
    founded = "1886年"
    current_standing = "現在、プレミアリーグで4位に位置しています。"

    # テンプレートにデータを渡す
    return render_template('index.html', team_name=team_name, founded=founded, current_standing=current_standing)
@app.route('/arsenal-info')
def get_arsenal_info():
    api_key = 'e5f2915e3de24394ae412db32016391c'  # ここにFootball-Data.orgのAPIキーを設定
    url = 'https://api.football-data.org/v2/teams/57'  # アーセナルのチームID
    headers = {'X-Auth-Token': api_key}
    
    response = requests.get(url, headers=headers)
    data = response.json()

    arsenal_info = {
        'name': data.get('name'),
        'shortName': data.get('shortName'),
        'crestUrl': data.get('crestUrl'),
        'website': data.get('website'),
        'founded': data.get('founded'),
        'clubColors': data.get('clubColors'),
        'venue': data.get('venue')
    }

    return jsonify(arsenal_info)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ryouyanaka0903@localhost/flaskapp'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/position/gk')
def goalkeepers():
    
    return render_template('gk.html')

@app.route('/position/df')
def defenders():
    
    return render_template('df.html')

@app.route('/position/mf')
def midfielder():
     
    return render_template('mf.html')

@app.route('/position/fw')
def forward():
     
    return render_template('fw.html')

@app.route('/ramsdale')
def arsenal():
    return send_from_directory('static', 'ramsdale.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            return redirect(url_for('welcome'))
        else:
            flash('ユーザー名またはパスワードが間違っています。')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('このユーザー名は既に使用されています。')
            return redirect(url_for('register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('アカウントが作成されました。ログインしてください。')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/signup_prompt')
def signup_prompt():
    return render_template('signup_prompt.html')

@app.route('/index')
def index():
    api_key = 'e5f2915e3de24394ae412db32016391c'  # ここにFootball-Data.orgのAPIキーを設定

    # アーセナルの試合予定と順位を取得
    matches = get_arsenal_matches(api_key)

    # 必要なデータを準備
    team_name = "アーセナルFC"

    # テンプレートにデータを渡す
    return render_template('index.html', team_name=team_name, matches=matches)

@app.route('/submit-prediction', methods=['POST'])
def submit_prediction():
    # フォームデータの取得
    user_id = request.form.get('user_id')
    match_id = request.form.get('match_id')
    prediction = request.form.get('prediction')

    # 予想をデータベースに保存
    # ...

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)