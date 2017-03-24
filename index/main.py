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

		if recipe == "土豆丝鸡蛋饼":
			return render_template('recipe_1.html')

		elif recipe == "葱花鸡蛋饼":
			return render_template('recipe_2.html')

		elif recipe == "盐水虾":
			return render_template('recipe_3.html')

		elif recipe == "韭菜鸡蛋摊饼":
			return render_template('recipe_4.html')

		elif recipe == "香辣虾":
			return render_template('recipe_5.html')

		elif recipe == "蒜香杏鲍菇":
			return render_template('recipe_6.html')

		elif recipe == "蒜蓉蒸虾":
			return render_template('recipe_7.html')

		elif recipe == "土豆烧排骨":
			return render_template('recipe_8.html')

		elif recipe == "双椒煎排骨":
			return render_template('recipe_9.html')

		elif recipe == "耗油杏鲍菇":
			return render_template('recipe_10.html')

		elif recipe == "虾仁豆腐":
			return render_template('recipe_11.html')

		else:
			return "对不起，您要查找的菜谱不在搜索范围内。"


if __name__ == "__main__":
    app.run(debug = True)	

