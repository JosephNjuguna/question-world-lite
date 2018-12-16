from flask import Flask 
from data import userdata

app = Flask(__init__)

user = userdata.Users.authdata()

@app.route('/api/v1/auth/login',methods=['POST', 'GET'])
def user_log_in():
	data = request.get_json()
	if data == {}:
		return "Empty Json"
	user_name = data['name']
	user_auth_password = data['password']
	info_check = [info for info in user if info['name'] == user_name or info['password'] == user_auth_password]
	if not info_check:
		return "Check your Auth details"
	return jsonify({"user": info_check})


if __name__ == '__main__':
	app.run(debug = True)