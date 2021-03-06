from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/gb2606', methods=['GET', 'POST'])
def main():
    return render_template('gb2606.html')

if __name__ == '__main__':
    app.run()
