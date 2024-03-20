from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    print("Button clicked on the server!")
    # Perform any desired server-side action here
    return "Button clicked!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20013, debug=True)
