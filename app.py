import json
from flask import Flask,render_template,request,redirect,flash
from werkzeug.utils import secure_filename
import os 
from extraction_model import *
import config as cfg


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
STATIC_FOLDER = 'static'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp','bmp'])
check_files = [files for files in os.listdir(app.config['UPLOAD_FOLDER']) if files.lower().endswith(('.jpg','.png', '.jpg', '.jpeg', '.webp','.bmp'))] 
for file in check_files:
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
def allowed_file(filepath):
    return '.' in filepath and filepath.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    check_files = [files for files in os.listdir(app.config['UPLOAD_FOLDER']) if files.lower().endswith(('.jpg','.png', '.jpg', '.jpeg', '.webp','.bmp'))] 
    for file in check_files:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        random_filename = generate_name(filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        new_path = os.path.join(app.config['UPLOAD_FOLDER'],random_filename)
        file.save(path)
        rename_file(path,new_path)

        prediction_op = get_predict(new_path)

        data = {
                'Prediction': prediction_op
                }
        # printjsn = json.dumps(data)
        print('',type(data))

        try:
            del_dir(cfg.PRED_TXT_PATH)
        except Exception:
            pass
        # try:
        #     clear_image(new_path)
        # except:
        #     pass
        return render_template('result.html', image=random_filename, data=data)
        
    else:
        #flash('Allowed image types are - png, jpg, jpeg')
        #return redirect(request.url)
        error ={}
        error['Message'] = 'Allowed image types are - png, jpg, jpeg, webp, bmp'
        return json.dumps(error)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)