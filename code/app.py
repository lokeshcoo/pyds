from flask import Flask, render_template,redirect,request, flash, session
from database import User, add_to_db, File, open_db
# file upload 
from werkzeug.utils import secure_filename
from common.files_utils import *
from flask import Flask, render_template, request
import pandas as pd  
from prophet import Prophet 

app = Flask(__name__)
app.secret_key = 'thisissupersecretkeyfornoone'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(session)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("Email =>", email)
        print("Password =>", password)
        try:
            sess = open_db()
            user = sess.query(User).filter_by(email=email,password=password).first()
            if user:
                session['isauth'] = True
                session['email'] = user.email
                session['id'] = user.id
                session['name'] = user.username
                del sess
                flash('login successfull','success')
                return redirect('/')
            else:
                flash('email or password is wrong','danger')
        except Exception as e:
            flash(e,'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        print(username, email, password, cpassword)
        # logic
        if len(username) == 0 or len(email) == 0 or len(password) == 0 or len(cpassword) == 0:
            flash("All fields are required", 'danger')
            return redirect('/register') # reload the page
        user = User(username=username, email=email, password=password)
        add_to_db(user)
    return render_template('register.html')

@app.route('/file/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        name = secure_filename(file.filename)
        if not is_file_allowed(name):
            flash('Please upload file in csv format only','danger')
            return redirect('/file/upload')
        path = upload_file(file, name)
        file = File(path=path, user_id=1)
        add_to_db(file)
        flash("File uploaded successfully", 'success')
    return render_template('upload.html')

@app.route('/file/list', methods=['GET', 'POST'])
def file_list():
    db = open_db()
    files = db.query(File).all()
    return render_template('display_list.html', files=files)


#@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        n_days = int(request.form['n_days'])
        
        # Fetch stock data (you'll need to implement this part)
        # Example:
        # stock_data = fetch_stock_data(stock_symbol)
        
        # For demonstration purposes, let's create a dummy DataFrame
        dates = pd.date_range(start='2022-01-01', periods=100)
        dummy_data = {'Date': dates, 'Close': range(100)}
        stock_data = pd.DataFrame(dummy_data)
        
        # Preprocess data
        stock_data = stock_data.rename(columns={'Date': 'ds', 'Close': 'y'})
        
        # Initialize and train Prophet model
        model = Prophet()
        model.fit(stock_data)
        
        # Make future predictions
        future = model.make_future_dataframe(periods=n_days)
        forecast = model.predict(future)
        predictions = forecast[['ds', 'yhat']].tail(n_days)
        
        return render_template('prediction.html', predictions=predictions.to_html())
    return render_template('prediction.html')

@app.route('/file/<int:id>/view/')
def file_view(id):
    try:
        value = open_db().query(File).get(id)
        path = value.path
        df = pd.read_csv(path)
        table = df.head(100).reset_index(drop=True).to_html(classes='table table-hovered tabled-striped table-responsive vw-100 ')
        return render_template('view_file.html', table=table)
    except Exception as e:
        value=None

    return render_template('view_file.html')

@app.route('/logout')
def logout():
    if session.get('isauth'):
        session.clear()
        flash('you have been logged out','warning')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
     