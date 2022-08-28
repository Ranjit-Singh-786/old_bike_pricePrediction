from flask import Flask , render_template,request,jsonify
import pickle
import numpy 
import warnings
warnings.filterwarnings('ignore')

# import sklearn
# import pymongo    # for deal with the mongodb database
# client = pymongo.MongoClient("mongodb+srv://Ranjit_singh:<password>@learning.a5xc4jg.mongodb.net/?retryWrites=true&w=majority")
# mydb=client['Bikeproject']  # create the database for the project
# colle=mydb['bike_data']      # collection create

model=pickle.load(open('bike_price_prediction.pkl','rb'))
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def Home():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        kms_driven=request.form['Kms_Driven']   # gathering the document
        owner=request.form['owner']
        age=int(request.form['age'])
        power=int(request.form['power'])
        brand=request.form['brand_name']
        # record={'bike':brand,'kilometeres':kms_driven,'handed':owner,'year':age,'power':power}        # create the json document for database
        if (brand=='Royal Enfield'):  # feature scaling string into integer
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
        prediction=model.predict([[kms_driven,owner,age,power,brand]])  # pass value in the model
        output=str(prediction[0])    # change dtype int into string of prediction
        output2=str(output)
        # record['Price']=prediction[0].round(2)       # adding the price into mongodb database
        # colle.insert_one(record)
    return render_template('index.html',prediction_text=f' {output2}')    # return the value on the webpage
if __name__ == "__main__":
    app.run(debug=True)



        #  -----Backend code by using Flask----- 

