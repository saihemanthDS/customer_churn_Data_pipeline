import pickle

from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods =['GET'] )
def ping():
    return "<H1>Customer Churn Prediction </H1>"

model_pickle = open("churn_classifer.pkl","rb")
clf = pickle.load(model_pickle)

# Building the API End Point
#Data Points Considered - 'Age', 'Gender', 'Usage Frequency','Payment Delay', 'Subscription Type','Contract Length', 'Total Spend', 'Last Interaction'
@app.route("/predict",methods  = ['POST'])
def predictions():
    customer_req = request.json  #Storing the request in the Json Format

    if customer_req['Gender'] == "Male" :
        Gender = 1
    else :
        Gender = 0

    if customer_req['Subscription Type'] == "Basic":
        Subsription = 0
    elif customer_req['Subscription Type'] == "Standard":
        Subsription = 1
    else :
        Subsription = 2

    if customer_req['Contract Length'] == "Monthly":
        Contract = 0
    elif customer_req['Contract Length'] == "Quarterly":
        Contract = 1
    else :
        Contract = 2

    Age = customer_req['Age']
    Usage_frequency = customer_req['Usage Frequency']
    Payment_delay = customer_req['Payment Delay']
    Total_spend = customer_req['Total Spend']
    Last_interaction = customer_req['Last Interaction']

    result = clf.predict([[Age, Gender, Usage_frequency,
        Payment_delay, Subsription,
       Contract, Total_spend,Last_interaction]])

    if result == 0:
        pred = 'Customer may not be churned'
    else:
        pred  =  'Customer will be Churned.'

    return {'Customer Churn Status: ':pred}











if __name__ == "__main__":
    app.run(debug=True)
