from flask import *
from database import *
import speech_recognition





from model import *

global logged_in



app = Flask(__name__)
@app.route("/")
def home():
	global current_user
	return render_template("home.html")


@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")


@app.route("/speak")
def speak():
	return render_template("speak.html")

@app.route("/post", methods = [ "GET" , "POST"])
def post():
	if request.method == "GET":
		return render_template("post.html")

	else:
		text = request.form['text']
		topic = request.form['topic']
		add_post(text, topic)
		return redirect("notes")





@app.route("/signup", methods = [ "GET" , "POST"])
def start():
	if request.method == "GET":
		return render_template("signup.html")
	else: 
		add_user(username = request.form["username"], password = request.form['password'], name = request.form["name"])
		return render_template("home.html",users = query_all())

	if get_user_by_username(username) == None:
		add_user(username, password, name)
		return render_template('home.html', users=query_all())
	else:
		print("Username already taken, try a diffrent one")
		return render_template('signup.html')


error_mes1 = None
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username1 = request.form['username1']
		password1 = request.form['password1']


		userlog = get_user_by_username(username1)

		if userlog == None:
			error_mes1 ="We couldn't find a user with that username"
			return render_template('login.html', error_mes1 = error_mes1)
		else:
			if password1 == userlog.password:
				current_user = username1
				logged_in = True
				return render_template('home.html',usernamelog = username1,current_user = current_user, logged_in = logged_in)
			else:
				error_mes2 = "The password is incorrect, try again."
				return render_template('login.html', error_mes2 = error_mes2)
			return render_template('login.html',current_user)





@app.route("/notes")
def notes():
	posts_list = query_all()
	return render_template("notes.html", posts_list = posts_list)



if __name__ == '__main__':
	app.run(host = "localhost", port= 5000, debug = True)



