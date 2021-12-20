from flask import Flask, request,jsonify,render_template
import numpy as np
import pickle
import os


BASEDIR = "c:/JupyterNotebook/PROJECT/PredictDiabetes/"
os.chdir(BASEDIR)


MODELDIR = "models/"
model = pickle.load(open(MODELDIR+'StackingClassifier.pickle','rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

# def predict():
#     cgpa = request.form.get('cgpa')
#     iq = request.form.get('iq')
#     profile_score = request.form.get('profile_score')
#     input_query = np.array([[cgpa,iq,profile_score]])
#     result = model.predict(input_query)[0]
#     return jsonify({'placement':str(result)})


@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        #access the data from form
        T_AGE = int(request.form["T_AGE"])
        T_INCOME = int(request.form["T_INCOME"])
        T_MARRY = int(request.form["T_MARRY"])
        T_HEIGHT = int(request.form["T_HEIGHT"])
        T_WEIGHT = int(request.form["T_WEIGHT"])
        T_BMI = int(request.form["T_BMI"])
        T_DM = int(request.form["T_DM"])
        T_GLU0 = int(request.form["T_GLU0"])
        T_DRINK = int(request.form["T_DRINK"])
        T_DRDU = int(request.form["T_DRDU"])
        T_TAKFQ = int(request.form["T_TAKFQ"])
        T_TAKAM = int(request.form["T_TAKAM"])
        T_RICEFQ = int(request.form["T_RICEFQ"])
        T_RICEAM = int(request.form["T_RICEAM"])
        T_WINEFQ = int(request.form["T_WINEFQ"])
        T_WINEAM = int(request.form["T_WINEAM"])
        T_SOJUFQ = int(request.form["T_SOJUFQ"])
        T_SOJUAM = int(request.form["T_SOJUAM"])
        T_BEERFQ = int(request.form["T_BEERFQ"])
        T_BEERAM = int(request.form["T_BEERAM"])
        T_HLIQFQ = int(request.form["T_HLIQFQ"])
        T_HLIQAM = int(request.form["T_HLIQAM"])
        T_SMOKE = int(request.form["T_SMOKE"])
        T_SMDUYR = int(request.form["T_SMDUYR"])
        T_SMDUMO = int(request.form["T_SMDUMO"])
        T_SMAM = int(request.form["T_SMAM"])
        T_PSM = int(request.form["T_PSM"])
        T_EXER = int(request.form["T_EXER"])

        
        #get prediction
        input_cols = [[T_AGE,T_INCOME,T_MARRY,T_HEIGHT,T_WEIGHT,T_BMI,T_DM,T_GLU0,T_DRINK,T_DRDU,T_TAKFQ,T_TAKAM,T_RICEFQ,T_RICEAM,T_WINEFQ,T_WINEAM,T_SOJUFQ,T_SOJUAM,T_BEERFQ,T_BEERAM,T_HLIQFQ,T_HLIQAM,T_SMOKE,T_SMDUYR,T_SMDUMO,T_SMAM,T_PSM,T_EXER]]
        prediction = model.predict(input_cols)
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_text='Your predicted annual Healthcare Expense is $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

