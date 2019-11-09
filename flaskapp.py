from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)    