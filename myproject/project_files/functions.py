from project_files import app
import os



UPLOAD_FOLDER = '/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_check( file_name):
  if file_name == '':
    return False
  allowed_files = ['jpg', 'jpeg', 'gif', 'png']
  file_type = file_name.split('.')[1]
  if file_type in allowed_files:
    return True
  else:
    return False