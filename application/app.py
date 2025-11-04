"""
Simple REST API application
"""
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

ALLOWED_EXTENSIONS = ["xml","txt"]

@app.route("/")
def hello():
  return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/health/")
def health():
  return"<h1>Health check passes</h1>"
if __name__ == "__main__":
    app.run(host='0.0.0.0')

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=['GET', 'POST'])
def upload():
  if request.method == "POST":
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join('UPLOAD_FOLDER', filename))
      return redirect(url_for("/"))
  return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>

   '''

if __name__ == "__main__": app.run()