from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b5f51bbfe46e889454386a9176644786'

posts = [
    {
        'author': 'Muawiya Assali',
        'title': 'Social Media Post 1',
        'content': 'This is a post to test python flask',
        'date_posted': 'May 1, 1990'
    },
    {
        'author': 'Super Man',
        'title': 'Social Media Post 2',
        'content': 'This is a post to test python flask',
        'date_posted': 'June 1, 1995'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created For {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='REGISTER', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@test.com" and form.password.data == "password":
            flash("You have been successfully logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Pleas check username and data!', 'danger')
    return render_template('login.html', title='LOGIN', form=form)

if __name__ == '__main__':
    app.run(debug=True)    