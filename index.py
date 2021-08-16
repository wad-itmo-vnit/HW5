from flask import Flask, render_template, send_file, request, redirect, make_response

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/login'), 301
def auth(request):
    token = request.coookies.get('login-info')
    try:
        user, pwd = token.split(':')
    except:
        return False
    if (user == 'admin' and pwd == 'admin'):
        return True
    else: 
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get("uname")
        pwd = request.form.get("pwd")
        if (user == 'admin' and pwd == 'admin'):
            token = user + ":" + pwd
            resp = make_response(redirect('/index'))
            resp.set_cookie('login_info', token)
            return render_template('index.html')
        else:
            return redirect('/login'), 403



@app.route('/index')
def open_web():
    if auth(request):
        return render_template('index.html')
    else:
        return redirect('/')



@app.route('/img/get/<number>')
def serve_img(number):
    file_name = './static/' + number + '.jpg'
    return send_file(file_name)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)