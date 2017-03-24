from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('cover.html')

@app.route('/recipe', methods=['GET','POST'])
def user():
	if request.method == 'POST':
		name = request.form['recipe']
		return render_template('user.html', name = name)
		print(request.args)


if __name__ == "__main__":
    app.run(debug = True)	

