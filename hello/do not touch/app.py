from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Change 'your_script.py' to the name of the script you want to run
        result = subprocess.run(['python', 'english.py'], capture_output=True, text=True)
        return f"<center><h1>Script Output:</h1><pre>{result.stdout}</pre><h2>Error (if any):</h2><pre>{result.stderr}</pre>"
    except Exception as e:
        return f"<h1>Error:</h1><pre>{str(e)}</pre>"

if __name__ == '__main__':
    app.run(debug=True)