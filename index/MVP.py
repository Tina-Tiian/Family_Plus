from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('cover.html')

@app.route('/recipe', methods=['GET','POST'])
def user():
	if request.method == 'POST':
		name = request.form['recipe']
		print(request.args)
		return render_template('recipe.html', name = name, pic = pic, pic1 = pic1, pic2 = pic2, pic3 = pic3, text1 = text1, text2 = text2, text3 = text3)
		

name = ["土豆饼", "鸡蛋饼", "小龙虾"]
pic = ['/static/A1-01.jpg', '/static/A2-01.jpg', '/static/B3-01.jpg']
pic1 = ['/static/A1-02.jpg', '/static/A2-02.jpg', '/static/B3-02.jpg']
pic2 = ['/static/A1-03.jpg', '/static/A2-03.jpg', '/static/B3-03.jpg']
pic3 = ['/static/A1-04.jpg', '/static/A2-04.jpg', '/static/B3-04.jpg']
text1 = ['取一个新鲜土豆，洗净去皮', '打2-3个鸡蛋并搅拌，放入适量面粉。随后搅拌至均匀', '将一斤虾洗净']
text2 = ['土豆切丝、放入少量面粉，并取一个鸡蛋黄', '放入少许葱花', '葱、姜、蒜准备好']
text3 = ['将土豆丝、面粉、鸡蛋加入少量油和水放入锅中翻炒', '放入锅中制成蛋饼', '放入锅中翻炒']



if __name__ == "__main__":
    app.run(debug = True)	

