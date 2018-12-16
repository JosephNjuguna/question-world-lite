from flask import Flask 

app = Flask(__init__)

@app.route('/')
def welcom_message():
	welcome_message ={
		" instructions ": "USE THE FOLLOWING API ENDPOINTS TO INTERACT WITH THE API:",

	 	"/api/v1/auth/signup": "registration",

	 	"/api/v1//auth/login": "user log in",

	 	"/api/v1/questions":"fecth all questions", 

	 	"/api/v1/questions/<string:id>" :"fetch specific question",

	 	"/api/v1/questions" :"post a question",

	 	"/api/v1/category/<string:category>":"get categories of questions",

	 	"/api/v1/questions/<string:id>": "get a specific questions and update it",

	 	"/api/v1/questions/<string:id>" : "delete a specific question"
	}
	return  jsonify ({"Welcome to StackOverFlow API":welcome_message})
	
if __name__ == '__main__':
	app.run(debug = True)