from flask import Flask,request,jsonify
import numpy as np
import pickle
from sklearn import preprocessing

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)


@app.route('/predict',methods=['POST'])
def predict():

    sym1=request.form.get('sym1')
    sym2=request.form.get('sym2')
    sym3=request.form.get('sym3')
    sym4=request.form.get('sym4')
    sym5=request.form.get('sym5')
    list = [sym1,sym2,sym3,sym4,sym5]

    print(list)
    from  sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    li = le.fit_transform(list)

    result = model.predict([li])[0]

    return jsonify({'disease': str(result)})

if __name__ == '__main__':
    app.run(debug=True)
