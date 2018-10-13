from flask import Flask,render_template
import os
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
class File(db.Model):  
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.Date)
    category_id = db.Column(db.Integer,db.ForeignKey)
    content = db.Column(db.Text)
class Category(db.Model):
    id = db.Column(db.Integer,PrimaryKey=True)
    name = db.Columb(db.String(80))

class Files(object):
    directory  =os.path.join( os.path.abspath(os.path.dirname(__name__)),'..','files')
    def __init__(self):
        self._files = self._read_all_files()
    def _read_all_files(self):
        result ={}
        filenames = os.listdir(self.directory)
        for filename in filenames:
            file_path = os.path.join(self.directory,filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result
    def get_title_list(self):
        return[item['title'] for item in self._files.values() ]

    def get_by_filename(self,filename):
        return self._files.get(filename)

files = Files()
@app.route('/')
def index():
    return render_template('index.html',title_list=files.get_title_list())
    

@app.route('/files/<filename>')
def file(filename):
    file_item  = files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run()

