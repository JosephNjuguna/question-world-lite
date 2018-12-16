from flask import Flask
from data import questionsdata
from data import userdata

app = Flask(__init__)
quiz = questionsdata.Question.qdata()
user = userdata.Users.authdata()

@app.route('/api/v1/questions', methods= ['POST'])
def add_questions():
	questiondata = request.get_json()
	question_added = {}
	question_added['question']= questiondata['question']
	question_added['author']= questiondata['author']
	question_added['id']=questiondata['id']
	quiz.append(question_added)
	return jsonify({"data":quiz})

if __name__ == '__main__':
	app.run(debug = True)