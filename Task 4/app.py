from flask import Flask,request,render_template

from src.predict_pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application



@app.route('/',methods=['GET','POST'])

def predict_datapoint():                                # Getting data and prediction
    
    if request.method == 'GET':
        return render_template('home.html')
    
    else:
        data = CustomData(
            quantity=float(request.form.get('quantity')),
            temperature=float(request.form.get('temperature')),
            category=request.form.get('category'),
            unit_price=float(request.form.get('unit_price')),
            day_of_month=int(request.form.get('day_of_month')),
            hour=int(request.form.get('hour'))
        )

        pred_df = data.get_data_as_DataFrame()
        print(pred_df)

        predict_pipeline= PredictPipeline()
        result = predict_pipeline.predict(pred_df)
       
        result = result[0].round(2)*100

        print(result)

        return render_template('home.html',result=result)
        # return "The Expected Stock Level pct is " + "  "+  str(result[0].round(2)*100)+"%"


    

if __name__ == '__main__':
   
    app.run(host = "0.0.0.0")
