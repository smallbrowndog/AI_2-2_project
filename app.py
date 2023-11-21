from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        data_from_html = request.form['data_from_html']


        return render_template('result.html', result=data_from_html)


if __name__ == '__main__':
    app.run(debug=True)
