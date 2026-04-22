from flask import Flask, render_template, request, jsonify, session
from config import Config
from models import db, User, DivinationRecord, Donation
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config.from_object(Config)

# 初始化資料庫
db.init_app(app)

@app.route('/')
def index():
    """首頁渲染"""
    return render_template('index.html')

# ===============================
# 會員認證 API
# ===============================

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'error': '該 Email 已被註冊'}), 400
        
    hashed_pw = generate_password_hash(data.get('password'))
    user = User(email=data.get('email'), password_hash=hashed_pw)
    db.session.add(user)
    db.session.commit()
    
    session['user_id'] = user.id
    return jsonify({'message': '註冊成功'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get('email')).first()
    if user and check_password_hash(user.password_hash, data.get('password')):
        session['user_id'] = user.id
        return jsonify({'message': '登入成功'})
    return jsonify({'error': '信箱或密碼錯誤'}), 401

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': '登出成功'})

@app.route('/api/auth/me', methods=['GET'])
def get_me():
    user_id = session.get('user_id')
    if user_id:
        user = db.session.get(User, user_id)
        if user:
            return jsonify({'logged_in': True, 'email': user.email, 'balance': user.balance})
    return jsonify({'logged_in': False})

# ===============================
# 歷史紀錄 API
# ===============================

@app.route('/api/history', methods=['GET'])
def get_history():
    """獲取歷史抽籤紀錄"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登入'}), 401
    
    records = DivinationRecord.query.filter_by(user_id=user_id).order_by(DivinationRecord.created_at.desc()).all()
    results = [{'date': r.created_at.strftime('%Y-%m-%d %H:%M'), 'poem_id': r.poem_id} for r in records]
    return jsonify(results)

@app.route('/api/history/donations', methods=['GET'])
def get_donations_history():
    """獲取歷史儲值紀錄"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登入'}), 401
    
    records = Donation.query.filter_by(user_id=user_id).order_by(Donation.created_at.desc()).all()
    results = [{'date': r.created_at.strftime('%Y-%m-%d %H:%M'), 'amount': r.amount, 'status': r.status} for r in records]
    return jsonify(results)

# ===============================
# 結帳與抽籤 API
# ===============================

@app.route('/api/divination/record', methods=['POST'])
def save_divination_record():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登入'}), 401
        
    data = request.json
    record = DivinationRecord(user_id=user_id, question=data.get('question', ''), poem_id=data.get('poem_id'))
    db.session.add(record)
    db.session.commit()
    return jsonify({'message': '紀錄已儲存'}), 200

@app.route('/api/donate', methods=['POST'])
def donate():
    """模擬添香油錢並存入餘額"""
    user_id = session.get('user_id') 
    data = request.json
    amount = data.get('amount')
    
    # 儲值入帳邏輯
    if user_id:
        user = db.session.get(User, user_id)
        if user:
            user.balance += amount
    
    # 建立訂單紀錄
    donation = Donation(
        user_id=user_id, amount=amount,
        status='SUCCESS', paid_at=datetime.datetime.utcnow()
    )
    db.session.add(donation)
    db.session.commit()
    
    return jsonify({'message': f'成功儲值 NT$ {amount} 元！香火餘額已更新。'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
