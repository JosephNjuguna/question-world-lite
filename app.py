from flask import Flask 
from data import questionsdata

app = Flask(__init__)

quiz = questionsdata.Question.qdata()

@app.route('/api/v1/questions', methods= ['GET'])
def get_all_questions():
	if quiz =='':
		return "no Data"
	return jsonify({"data":quiz})

if __name__ == '__main__':
	app.run(debug = True)