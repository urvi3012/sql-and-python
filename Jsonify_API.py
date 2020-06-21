from flask import Flask, render_template, url_for, jsonify
#from forms import Reg_Form, Login_Form
import speech_recognition as sr

import re
app = Flask(__name__)

app.config['SECRET_KEY']='5c07f123f5f31a213f742f955f6902e0'

#dummy data of lidt of dictionary with info of posts
posts = [
	{
		'author':'Urvi',
		'title': 'Blog post 1',
		'date': '12/2/2020',
		'content': 'sdc'
	},
	{
		'author':'Prisha',
		'title': 'Blog post 3',
		'date': '9/7/2020',
		'content': 'sdfe'
	},
	{
		'author':'Vishal',
		'title': 'Blog post 6',
		'date': '11/4/2020',
		'content': 'tyj'
	},
	{
		'author':'Sakshi',
		'title': 'Blog post 10',
		'date': '1/2/2020',
		'content': 'abc'
	}
]


@app.route('/')
@app.route('/home')
def home():
	return jsonify(posts) #accessing the list od dictionaries we made (dummy data)

'''
@app.route("/about")
def about():
	return render_template("about.html", title='About')
 

@app.route('/register')
def register():
	form=Reg_Form()
	return render_template('register.html', title='Register', form=form)


@app.route('/login')
def register():
	form=Login_Form()
	return render_template('login.html', title='Login', form=form)

'''

if __name__ == '__main__':
	app.run(debug=True)
