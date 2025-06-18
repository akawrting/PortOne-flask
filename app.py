from flask import Flask, render_template ,request
from basket_example import total_price

app = Flask(__name__)  # Flask 애플리케이션 생성

@app.route('/payment')  # 기본 경로 설정
def home():
    pay_amount = total_price
    return render_template('payment.html', pay_amount=pay_amount)  # 클라이언트에게 반환할 내용

@app.route('/payment_success')
def payment_success():
    paid_amount = request.args.get('paid_amount', '0')  # 기본값은 '0'
    merchant_uid = request.args.get('merchant_uid', 'unknown')  # 기본값은 'unknown'
    return render_template('payment_success.html', paid_amount=paid_amount, merchant_uid=merchant_uid)
    
@app.route('/payment_failed')
def payment_failed():
    return render_template('payment_failed.html')

if __name__ == '__main__':
    app.run(debug=True)  # 애플리케이션 실행