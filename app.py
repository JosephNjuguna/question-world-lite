from flask import Flask 

app = Flask(__init__)

@app.route('/api/v1/questions/<string:id>',methods=['DELETE'])
def delete_questions(id):
	id = int(id)
	single_quiz = [q for q in quiz if q['id'] == id]
	if not single_quiz:
		return "Id not found"
	quiz.remove(single_quiz[0])
	return jsonify({"deleted data": quiz})
	
if __name__ == '__main__':
	app.run(debug = True)