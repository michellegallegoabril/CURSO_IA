from flask import Flask, request, render_template
import pickle
import pandas as pd
import os
app = Flask(__name__,template_folder='../templates')
modelo=pickle.load(open(os.path.join(os.path.dirname(__file__),'../modelo/modelo.pkl'),'rb'))
columna=pickle.load(open(os.path.join(os.path.dirname(__file__),'../modelo/columna.pkl'),'rb'))

@app.route('/',methods=['GET'])
def formulario():
    return render_template('formulario.html')
@app.route('/predecir',method=['POST'])
def predecir():
    datos={
        'ubicacion':request.form['ubicacion'],
        'tamano_hogar':request.form['tamano_hogar'],
        'costo_instalacion':request.form['costo_instalacion'],
        'energia_generada':request.form['energia_generada'],
    }
    df =pd.DataFrame([datos])
    df_encoded=pd.get_dummies(df)
    for col in columna:
        if col not in df_encoded:
            df_encoded[col]=0
    prediccion = modelo.predict(df_encoded[columna])[0]
    return render_template('resultao.html',prediccion=roun(prediccion,2))
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)