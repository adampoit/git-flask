from flask import Flask, request
import git
import subprocess

app = Flask(__name__)

repos = { "git-flask": "/home/adampoit/webapps/git_flask/git_flask" }

@app.route("/", methods=["POST"])
def gitpull():
	path = repos[request.get_json()["repository"]["name"]]
	repo = git.Repo(path)
	repo.git.pull()
	subprocess.call(os.path.dirname(path) + "/deploy.sh")
	return "", 204

if __name__ == "__main__":
	app.run()
