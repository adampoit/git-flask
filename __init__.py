from flask import Flask, request
import git

app = Flask(__name__)

repos = { "adampoit/git-flask": "/home/adampoit/webapps/git/git" }

@app.route("/", methods=["POST"])
def gitpull():
	repo = git.Repo(repos[request.get_json()["repository"]["full_name"]])
	repo.git.pull()
	return "", 204

if __name__ == "__main__":
	app.run()
