from flask import Flask
from data import questionsdata
from data import userdata

app = Flask(__init__)
quiz = questionsdata.Question.qdata()
user = userdata.Users.authdata()


if __name__ == '__main__':
	app.run(debug = True)