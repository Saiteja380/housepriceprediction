from flask import Flask, render_template, request
import pickle

app = Flask(_name_)

with open('model_pickle2', 'rb') as file:
    model = pickle.load(file)



@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")



@app.route("/predict", methods = ["POST"])
def predict():
    area =float(request.form['area'])
    bedrooms =float(request.form['bedrooms'])
    age =float(request.form['age'])

    prediction = model.predict([[area,bedrooms,age]])

    return render_template("index.html", prediction = prediction[0])

if _name=="main_":
    app.run(debug=True)
