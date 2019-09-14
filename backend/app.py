from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from zipfile import ZipFile
from werkzeug.utils import secure_filename
import os
import pydicom

app = Flask(__name__)
CORS(app)

##
# API routes
##

@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description})
    response.status_code = 400
    return response

@app.route('/upload', methods=['POST'])
def items():
    if 'file' not in request.files:
        return abort(400, 'File not included')
    file = request.files['file']
    file.save(secure_filename(file.filename))

    if file:
        filename = file.filename
    else:
        return abort(400, 'Invalid file')

    if filename.split('.')[1] == 'zip':
        with ZipFile(file.filename, 'r') as zip:
            zip.extractall()
            foldername = filename.split('.')[0]
    else:
        return abort(400, 'Please submit a .zip file')
    
    
    dicom_array = []
    for filename in os.listdir(foldername):
        print(filename)
        if filename.endswith(".dcm"):
            ds = pydicom.dcmread(os.path.join(foldername, filename))            

    return jsonify([{'title': 'A'}, {'title': 'B'}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)