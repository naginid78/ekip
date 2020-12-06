from flask import Flask, render_template
import sys, os,json

app = Flask(__name__)

maisons = json.load(open("data/maison.json"))
#Route index
@app.route('/',methods=["GET"])
def index():
	#retourn les maisons sur la page d'accueil
	return render_template('index.html', maisons=maisons)

@app.route("/maison/<int:id>", methods=["GET"])
def get_house_id(id):
# permet d'obtenir une par id (on pourrait faire la meme chose par nom) et l'afficher dans un template
	maison = None
	for val in maisons:
		if val.get("id") == id :
			maison=val
			break
	return render_template("maison.html", maison=maisons)
if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = os.environ.get("PORT", 5000), debug=True)
