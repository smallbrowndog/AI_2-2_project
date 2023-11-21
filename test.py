from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/save_singer', methods=['POST'])
def save_singer():
    singer_input = request.form['singer']

    # 가수 이름을 사용하여 원하는 작업을 수행
    # 여기서는 간단히 가수 이름을 출력하는 예시를 보여줍니다.
    print('가수:', singer_input)

    response_data = {
        'success': True,
        'message': '가수 이름을 성공적으로 받았습니다.'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
