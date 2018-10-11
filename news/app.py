from flask import Flask,render_template
import os
app = Flask()
class Files(object):
    directory  =os.path.join( os.path.abspath('__name__'),'..','files')
    def _read_all_files(self):
        result ={}
        filenames = os.listdir(self.directory)
        for filename in filenames:
            file_path = os.path.join(self.directory,filename)
            with open(file) as f:
                result[filename[:-5]] = json.load(f)

    return result
    def __init__(self):
    
    def get_title_list():
        return[item['title'] for item in self._fiels.values() ]

    def get_by_filename(self,filename):
        return self._files.get(filename)

files = Files()
@app.route('/')
def index():
    return render_template('index.html',title_list=files.get_title_list())
    

@app.route('/files/<filename>')
def file(filename):
    file_item  = files.get_by_filename(filename)
    if not file_item
        abort(404)
    return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
if __name__ == '__main__'
    app.run()

