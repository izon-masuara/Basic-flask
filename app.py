import json
from operator import itemgetter
from flask import Flask , render_template, request ,redirect
app = Flask(__name__)

# Create route access
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "GET":
        readJson = open('data/data.json')
        data = json.loads(readJson.read())
        readJson.close()
        return render_template('student.html',data=data)
    elif request.method == "POST":
        name,physics,chemistry,maths = itemgetter("Name","Physics","Chemistry","Maths")(request.form)
        payload = {
            "name" : name,
            "physics" : physics,
            "chemistry" : chemistry,
            "maths" : maths
        }
        readJson = open('data/data.json')
        data = json.loads(readJson.read())
        data.append(payload)
        dataJson = json.dumps(data,sort_keys=True, indent=4)
        readJson.close()
        writeJson = open('data/data.json','w')
        writeJson.write(dataJson)
        writeJson.close()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,port=5000)