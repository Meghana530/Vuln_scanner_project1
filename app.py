# app.py
from flask import Flask, render_template, request
import scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        target_url = request.form['url']
        if target_url:
            xss_found = scanner.scan_xss(target_url)
            sqli_found = scanner.scan_sqli(target_url)
            result = {
                "url": target_url,
                "xss": xss_found,
                "sqli": sqli_found
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
