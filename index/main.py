# -*- coding = utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('cover.html')


@app.route('/recipe', methods=['GET','POST'])
def recipe():
	if request.method == 'POST':
		recipe = request.form['recipe']

		if recipe == "土豆饼":
			return render_template('recipe_1.html')

		elif recipe == "鸡蛋饼":
			return render_template('recipe_2.html')

		elif recipe == "小龙虾":
			return render_template('recipe_3.html')
		else:
			return "对不起，没有您要的菜谱"


if __name__ == "__main__":
    app.run(debug = True)	

