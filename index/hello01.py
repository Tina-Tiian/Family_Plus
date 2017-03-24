from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
	print(request.args)
	return render_template('user.html', name = name)


if __name__ == "__main__":
    app.run(debug = True)	

