from flask import Flask, render_template, request
import pickle
import numpy as np

from flask import Flask, render_template, request
import pickle
import numpy as np
from PIL import Image
import os
app = Flask(__name__)

# Load models
heart_model = pickle.load(open("heart_model.pkl", "rb"))
disease_model = pickle.load(open("disease_model.pkl", "rb"))
ecg_model = pickle.load(open("ecg_model.pkl", "rb"))

image_model = pickle.load(open("image_model.pkl","rb"))
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")


# Heart Risk Prediction
# @app.route("/heart", methods=["POST"])
# def heart():

#     age = float(request.form["age"])
#     bp = float(request.form["bp"])
#     chol = float(request.form["chol"])
#     hr = float(request.form["hr"])

#     data = np.array([[float(age), float(bp), float(chol), float(hr)]])

#     result = heart_model.predict(data)

#     if result[0] == 1:
#         output = "High Heart Disease Risk"
#     else:
#         output = "Low Risk"

#     return render_template("index.html", heart_result=output,age=age,bp=bp,chol=chol,hr=hr)

@app.route('/heart', methods=['POST'])
def heart():

    age = request.form['age']
    bp = request.form['bp']
    chol = request.form['chol']
    hr = request.form['hr']

    data = [[int(age), int(bp), int(chol), int(hr)]]

    prediction = heart_model.predict(data)

    if prediction[0] == 1:
        result = "High Heart Disease Risk"
    else:
        result = "Low Heart Disease Risk"

    return render_template(
        "index.html",
        heart_result=result,
        age=age,
        bp=bp,
        chol=chol,
        hr=hr
    )
# Disease Prediction
@app.route("/disease", methods=["POST"])
def disease():

    fever = float(request.form["fever"])
    cough = float(request.form["cough"])
    fatigue = float(request.form["fatigue"])

    data = np.array([[fever, cough, fatigue]])

    result = disease_model.predict(data)

    return render_template("index.html",
                            disease_result=result, 
                            fever=fever,
                            cough=cough,
                            fatigue=fatigue)



# ECG Analyzer
@app.route("/ecg", methods=["POST"])
def ecg():

    ecg_value = float(request.form["ecg"])

    data = np.array([[ecg_value]])

    result = ecg_model.predict(data)

    return render_template("index.html", ecg_result=result,ecg=ecg_value)

@app.route("/image", methods=["POST"])
def image_diagnosis():

    file = request.files["image"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    from PIL import Image
    import numpy as np

    img = Image.open(filepath)

    img = img.convert("L")

    img_array = np.array(img)

    brightness = np.mean(img_array)

    data = np.array([[brightness]])

    prediction = image_model.predict(data)

    result = prediction[0]

    return render_template("index.html", image_result=result)


if __name__ == "__main__":
    app.run(debug=True)