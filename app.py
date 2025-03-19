from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'mri-file' not in request.files:
        return redirect(url_for('upload'))
    file = request.files['mri-file']
    if file.filename == '':
        return redirect(url_for('upload'))
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    # Add your tumor detection logic here
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)