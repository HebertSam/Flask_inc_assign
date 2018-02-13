import os
from flask import Flask, render_template, redirect, request, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENTIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.secret_key = 'hello'
app.config['images'] = UPLOAD_FOLDER

def allowed_file(filename):
    pass


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    print request.files['picture'].filename
    if 'picture' not in request.files:
        print 'no file'
        return redirect('/')
    file = request.files['picture']
    if file.filename == '':
        print 'no selected file'
        return redirect('/')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['images'], filename))
        session['picture'] = request.files['picture'].filename
        return redirect('/success')

@app.route('/success')
def success():
    print "success"
    print type(session['picture'])
    return render_template('success.html')

app.run(debug=True)