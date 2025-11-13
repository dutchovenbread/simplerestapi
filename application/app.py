"""
Simple REST API application
"""
import logging, os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
# Prefer SECRET_KEY from the environment for production; fall back to a default for dev/test.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "This is a secret key.")

file_handler = logging.FileHandler('app_errors.log')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

ALLOWED_EXTENSIONS = ["xml","txt","json"]

@app.route("/")
def hello():
  return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/health")
def health():
  return"<h1>Health check passes</h1>"


def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=['GET', 'POST'])
def upload():
  try:
    print(request)
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
        return redirect(url_for("upload"))
    return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
      </form>

    '''
  except Exception as e:
    app.logger.exception(f"An error occurred during request processing. [{e}]")
    raise e

if __name__ == "__main__": app.run()