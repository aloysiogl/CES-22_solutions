from flask import Flask, make_response, request, render_template, send_file, redirect, session, url_for
from config.working_files import IGNORED, ICON_TYPES, DATA_TYPES
from werkzeug import secure_filename
import os

app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.secret_key = 'yano'
root = os.path.dirname(os.path.abspath(__file__)) + '/files'
login_key = "yano"


@app.template_filter('data_fmt')
def data_fmt(filename):
    """Checking if the file format is supported"""
    current_type = 'unknown'
    for type, exts in DATA_TYPES.items():
        if filename.split('.')[-1] in exts:
            current_type = type
    return current_type


@app.route('/', methods=['POST', 'GET'])
def index():
    """Open enter session page"""
    if request.method == 'GET':
        # If the session is open go to files page
        if 'verified' in session and session['verified']:
            return redirect(url_for('files'))
        # If not show the enter session page
        else:
            return render_template('index.html', message="Enter the secret key")
    if request.method == 'POST':
        # If the key is correct log in
        if request.form['username'] == login_key:
            session['verified'] = True
            return redirect(url_for('files'))
        # In other case reload the page
        else:
            return render_template('index.html', message="Wrong key")


@app.route('/logout')
def logout():
    """Logging out the session"""
    session['verified'] = False
    return redirect(url_for('index'))


@app.route('/setcookieshow')
def setCookieShowAll():
    """Set cookie to show all files"""
    resp = make_response(redirect(url_for('files')))
    resp.set_cookie('showall', "yes")
    return resp


@app.route('/setcookieshownot')
def setCookieShowAllNot():
    """Set cookie to hide unsupported formats"""
    resp = make_response(redirect(url_for('files')))
    resp.set_cookie('showall', "no")
    return resp


@app.route('/files', methods=['POST', 'GET'])
def files():
    """Returning the files stored and uploading files"""

    # Handling get files list
    if request.method == 'GET':
        contents = []
        for filename in os.listdir(root):
            # Hide ignored files
            if filename in IGNORED:
                continue
            # Hide non supported formats if a cookie is set
            showall = request.cookies.get('showall')
            if data_fmt(filename) in ['unknown', 'archive'] and showall == 'no':
                continue
            contents.append({'name': filename})

        page = render_template('files.html', contents=contents, showall=showall)

        return page

    # Handling uploading files
    elif request.method == 'POST':
        path = root
        if os.path.isdir(path):
            request_files = request.files.getlist('files[]')
            for file in request_files:
                filename = secure_filename(file.filename)
                file.save(os.path.join(path, filename))

        return redirect('/')


@app.route('/files/<path:p>')
def download(p):
    """Download route for the files"""
    path = os.path.join(root, p)

    # Verifying if the file exists in the filesystem
    if os.path.isfile(path):
        res = send_file(path)
        res.headers.add('Content-Disposition', 'attachment')
    else:
        res = make_response('Not found', 404)
    return res


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
