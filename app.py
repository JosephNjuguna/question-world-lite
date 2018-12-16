from flask import Flask 

app = Flask(__init__)

def update_question(id):
	id = int(id)
	quiz_json = request.get_json()
	single_quiz = [q for q in quiz if q['id'] == id]
	if not single_quiz:
		return "Invalid id"
	single_quiz[0]['question'] = quiz_json['question']
	return jsonify({"updated data":quiz})
	
if __name__ == '__main__':
	app.run(debug = True)