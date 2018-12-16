from flask import Flask 
from data import userdata

app = Flask(__init__)
user = userdata.Users.authdata()

@app.route('/api/v1/auth/signup',methods=['POST'])
def user_registration():
	data = request.get_json()
	if data == {}:
		return "Empty Json"
	for key in data:
		if data[key] == '':
			return "empty"
	add_user = {}
	add_user['name'] = data['name']
	add_user['email'] = data['email']
	add_user['password'] = data['password']
	add_user['passwordconfirm'] = data['passwordconfirm']
	add_user['admin'] = False
	user.append(add_user)
	return jsonify({"updated users": user})


if __name__ == '__main__':
	app.run(debug = True)