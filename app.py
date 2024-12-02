from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import requests
from io import BytesIO
import os
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)
logging.basicConfig(level=logging.INFO)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

PIC_EXTENSIONS_ALLOWED = {'png', 'jpg', 'jpeg'}

REMOVE_BG_API_KEY = "ADD_YOUR_API_KEY"
REMOVE_BG_API_URL = "https://api.remove.bg/v1.0/removebg"

def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in PIC_EXTENSIONS_ALLOWED

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request', 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        
        if not file_allowed(file.filename):
            flash('Invalid file format. Only PNG, JPG, and JPEG are allowed.', 'danger')
            return redirect(request.url)

        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)

        try:
            # Call Remove.bg API
            response = requests.post(
                REMOVE_BG_API_URL,
                files={'image_file': file.stream},
                data={'size': 'auto'},
                headers={'X-Api-Key': REMOVE_BG_API_KEY},
            )
            
            if response.status_code == requests.codes.ok:
                img_io = BytesIO(response.content)
                img_io.seek(0)
                return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='image_rmbg.png')
            else:
                logging.error(f"Remove.bg API Error: {response.status_code}, {response.text}")
                flash(f"API Error: {response.json().get('errors', 'Unknown error')}", 'danger')
                return redirect(request.url)

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            flash('Unexpected error occurred. Please try again later.', 'danger')
            return redirect(request.url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5100)
