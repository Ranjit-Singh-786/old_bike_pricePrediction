from flask import Flask , render_template,request
import jsonify
import pickle
import numpy 
import sklearn
model=pickle.load(open('bike_price_prediction.pkl','rb'))
app=Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        brand=request.form['brand_name']

        if (brand=='Royal Enfield'):
            brand=1
        elif(brand=='KTM'):
            brand=2
        elif(brand=='Bajaj'):
            brand=3
        elif(brand=='Harley'):
            brand=4
        elif(brand=='Yamaha'):
            brand=5
        elif(brand=='Honda'):
            brand=6
        elif(brand=='Suzuki'):
            brand=7
        elif(brand=='TVS'):
            brand=8
        elif(brand=='Kawasaki'):
            brand=9
        elif(brand=='Hyosung'):
            brand=10
        elif(brand=='Benelli'):
            brand=11
        elif(brand=='Mahindra'):
            brand=12
        elif(brand=='Triumph'):
            brand=13
        elif(brand=='Ducati'):
            brand=14
        elif(brand=='BMW'):
            brand=15
        kms_driven=request.form['Kms_Driven']
        owner=request.form['owner']
        age=int(request.form['age'])
        power=int(request.form['power'])
        
        prediction=model.predict([[kms_driven,owner,age,power,brand]])
        output=str(prediction[0])
        output2=str(output)
    return render_template('index.html',prediction_text=f' {output2}')
    # return render_template('chek.html')
    # return model.predict([[kms_driven,owner,age,power,brand]])






        

        # return render_template('index.html',prediction_text=f'this is bike price :- {output2}')





if __name__ == "__main__":
    app.run(debug=True)