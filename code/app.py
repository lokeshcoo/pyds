from flask import Flask, render_template,request,redirect,flash, session
from database import User, add_to_db, open_db
app = Flask(__name__)
app.secret_key = 'thisisthesecrectkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('password')
        print("email = ",email)
        print("password ",password)
    return render_template('login.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email') 
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        print(username,email,password,cpassword)

        if len(username) == 0 or len(email)==0 or len(password)==0 or len(cpassword)==0 :
            flash("all feilds are required")
            return redirect('/register')
        user  = User(username=username , email=email, password=password)
        add_to_db(user)    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 