import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from pydub import AudioSegment
from analysis import queue_analyze_video
import constants
import string
import random

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['mp4'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = constants.BASE_PATH + "UploadedVideos/"
app.secret_key = 'sdafhwofasdgeryteu6457a89234ryshdfkawr39r'

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/showAnalyzed', methods=['GET'])
def show_analyzed():
	f = open("database/analyzed.json")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if not allowed_file(file.filename):
			flash('Invalid extension')
			return redirect(request.url)
		if file:
			filename = secure_filename(file.filename)
			print filename
			if ".mp4" in filename:
				temp_file = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
				temp_file += ".mp4"
				temp_file = os.path.join(app.config['UPLOAD_FOLDER'], temp_file)
				file.save(temp_file)
				queue_analyze_video(temp_file, filename)
				flash('Done')
			else:
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				flash('Done')
			return redirect(request.url)
	print "here5"
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=submit value=Upload>
	</form>
	'''

app.run(host = "0.0.0.0", port = 5000)
