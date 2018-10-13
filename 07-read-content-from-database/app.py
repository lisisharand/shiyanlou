from flask import Flask,render_template
import os
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/shiyanlou',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    ))
class File(db.Model):  #File to Category is many-to-one
    __tablename__ = "files"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.Date)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',uselist=False)
    #uselist use Father one-to-many into one-to-one 
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')
    def __init__(self,name):
        self.name = name
"""def insert_datas():
    java = Category('java')
    python = Category('Python')
    file1 = File('Hello python',datetime.utcnow(),python,'File Content - Python is cool!')
    file2 = File('Hello Java',datetime.utcnow(),java,'File Content - Java is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
"""
    

""" class Files(object):
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

files = Files()"""
@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())
    

@app.route('/files/<file_id>')
def file(file_id):
    file_item  = File.query.get_or_404(file_id)
    if not file_item:
        abort(404)
    return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run()

