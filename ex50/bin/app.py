import web

urls = (
	'/(.*)', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
	def GET(self, name):
		greeting = "Hello World"
		return render.index(greeting = greeting, name = name)
		#name = 'Bob'
		#return render.index(name)

if __name__ == "__main__":
	app.run()
