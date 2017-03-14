- 欢迎界面是templates文件中的cover.html，请忽略test.html
- Bootstrap的所有格式都在static文件中，需要一并下载才可以正常显示页面。



- 注意：由于我没有使用flask主程序调用来启动欢迎界面，所以为了显示图片，cover.html中line62,line73,line84中的图片条用是使用的决定路径。
小明写好主程序后，请记得把图片的路径分别改为src="/static/01.jpg", src="/static/02.jpg", src="/static/03.jpg"，应该才可以调用到图片
