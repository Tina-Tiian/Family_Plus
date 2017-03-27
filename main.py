# -*- coding = utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('cover.html')

@app.route('/Mother_category')
def Mother_category():
	print(request.args)
	return render_template('Mother_category.html')

@app.route('/Father_category')
def Father_category():
	print(request.args)
	return render_template('Father_category.html')

@app.route('/Meat_category')
def Meat_category():
	print(request.args)
	return render_template('Meat_category.html')


@app.route('/recipe', methods=['GET','POST'])
def recipe():
	if request.method == 'POST':
		recipe = request.form['recipe']

		if recipe == "土豆丝鸡蛋饼":
			print(request.args)
			return render_template('Potatoegg.html')

		elif recipe == "葱花鸡蛋饼":
			return render_template('Springonion.html')

		elif recipe == "盐水虾":
			return render_template('Saltshrimp.html')

		elif recipe == "韭菜鸡蛋摊饼":
			return render_template('Omelette.html')

		elif recipe == "香辣虾":
			return render_template('Spicyshrimp.html')

		elif recipe == "蒜香杏鲍菇":
			return render_template('Garlicpleurotus.html')

		elif recipe == "蒜蓉蒸虾":
			return render_template('Garlicshrimp.html')

		elif recipe == "土豆烧排骨":
			return render_template('Potatorib.html')

		elif recipe == "双椒煎排骨":
			return render_template('Doublepepper.html')

		elif recipe == "蚝油杏鲍菇":
			return render_template('Pleurotus.html')

		elif recipe == "虾仁豆腐":
			return render_template('Tofu.html')

		else:
			return "对不起，您要查找的菜谱不在搜索范围内。"

	else:
		print(request.args)
		print(request.args.get("recipe"))
		recipe = request.args.get("recipe")

		if recipe == "土豆丝鸡蛋饼":
			print(request.args)
			return render_template('Potatoegg.html')

		elif recipe == "葱花鸡蛋饼":
			return render_template('Springonion.html')

		elif recipe == "盐水虾":
			return render_template('Saltshrimp.html')

		elif recipe == "韭菜鸡蛋摊饼":
			return render_template('Omelette.html')

		elif recipe == "香辣虾":
			return render_template('Spicyshrimp.html')

		elif recipe == "蒜香杏鲍菇":
			return render_template('Garlicpleurotus.html')

		elif recipe == "蒜蓉蒸虾":
			return render_template('Garlicshrimp.html')

		elif recipe == "土豆烧排骨":
			return render_template('Potatorib.html')

		elif recipe == "双椒煎排骨":
			return render_template('Doublepepper.html')

		elif recipe == "蚝油杏鲍菇":
			return render_template('Pleurotus.html')

		elif recipe == "虾仁豆腐":
			return render_template('Tofu.html')

		else:
			return "对不起，您要查找的菜谱不在搜索范围内。"


if __name__ == "__main__":
    app.run(debug = True)	

