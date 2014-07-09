from flask import Flask, request
import git
import os

app = Flask(__name__)

repos = { "git-flask": "/home/adampoit/webapps/git_flask/git_flask" }

@app.route("/", methods=["POST"])
def gitpull():
	path = repos[request.get_json()["repository"]["name"]]
	repo = git.Repo(path)
	repo.git.pull()
	touch(os.path.dirname(path) + "/wsgi.py")
	return "", 204
	
def touch(fname, times=None):
	with open(fname, 'a'):
        	os.utime(fname, times)

if __name__ == "__main__":
	app.run()
