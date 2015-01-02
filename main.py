from flask import Flask,url_for,render_template
from flask import request
from flask import redirect,render_template
import nltk

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/frerf')
def frerf():
    return render_template('frerf.html')

@app.route('/ari')
def ari():
    return render_template('ari.html')

@app.route('/clrf')
def clrf():
    return render_template('clrf.html')

@app.route('/fglr')
def fglr():
    return render_template('fglr.html')

@app.route('/gfi')
def gfi():
    return render_template('gfi.html')

@app.route('/lwrf')
def lwrf():
    return render_template('lwrf.html')

@app.route('/srf')
def srf():
    return render_template('srf.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/')
def root():
	print url_for('index')
	return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'	)

if __name__ == '__main__':
	app.debug = True
	app.run()

"""
The Coleman-Liau Readability Formula

L = sum([len[i] for i in word_tokenize(j)[:100]])


"""