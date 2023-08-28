from flask import Flask,render_template,request
import pickle
import numpy as np
import xgboost as xgb


model= pickle.load(open('CCmodel.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def index():
       return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_Default():
    LIMIT_BAL = int(request.form.get('LIMIT_BAL'))
    SEX = int(request.form.get('SEX'))
    EDUCATION = int(request.form.get('EDUCATION'))
    MARRIAGE = int(request.form.get('MARRIAGE'))
    AGE = int(request.form.get('AGE'))
    PAY_0  = int(request.form.get('PAY_0 '))
    PAY_2  = int(request.form.get('PAY_2 '))
    PAY_3  = int(request.form.get('PAY_3 '))
    PAY_4  = int(request.form.get('PAY_4 '))
    PAY_5  = int(request.form.get('PAY_5 '))
    PAY_6 = int(request.form.get('PAY_6 '))
    April_Bill = int(request.form.get('April_Bill '))
    May_Bill = int(request.form.get('May_Bill '))
    June_Bill  = int(request.form.get('June_Bill '))
    July_Bill  = int(request.form.get('July_Bill '))
    Aug_Bill  = int(request.form.get('Aug_Bill '))
    Sep_Bill  = int(request.form.get('Sep_Bill '))
    Sep_Pay  = int(request.form.get('Sep_Pay '))
    Aug_Pay  = int(request.form.get('Aug_Pay '))
    July_Pay  = int(request.form.get('July_Pay '))
    June_Pay  = int(request.form.get('June_Pay '))
    May_Pay  = int(request.form.get('May_Pay '))
    April_Pay  = int(request.form.get('April_Pay '))



    #prediction
    result = model.predict(np.array([LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,
                                    April_Bill,May_Bill,June_Bill,July_Bill,Aug_Bill,Sep_Bill,
                                     Sep_Pay,Aug_Pay,July_Pay,June_Pay,May_Pay,April_Pay]).reshape(1,23))
    if result[0]==1:
        result = "The customer is Defaulter"
    else:
        result = 'The customer is  non Defaulter'



    return render_template('index.html', result =result)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)