__author__ = 'ajb'

import os, uuid
from werkzeug import secure_filename
from app import app

ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_excel_file_path(file_id):
    file_record = models.UploadedFile.get(models.UploadedFile.id == file_id)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_record.directory, file_record.name)
    return file_path


def save_excel_file(file, directory):
    if file and allowed_file(file.filename):
        filename = "%s.%s" % (uuid.uuid4(), file.filename.split('.')[-1])
        filelocation = os.path.join(app.config['UPLOAD_FOLDER'], directory, filename)
        file.save(filelocation)

        return filelocation

    raise Exception('The file is not valid!')