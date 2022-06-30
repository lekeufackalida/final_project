import pandas as pd 
from preprocessing import preprocess
from fastapi import FastAPI,  Depends, HTTPException, status
import joblib
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


security = HTTPBasic()
users_db = {
    'alice': 'wonderland',
    'bob': 'builder',
    'clementine': 'mandarine'
}



api = FastAPI()

class Item(BaseModel):
    seniorcitizen: str
    dependents: str
    tenure: float
    phoneservice: str
    mutliplelines: str
    internetservice:  str
    onlinesecurity: str
    onlinebackup: str
    techsupport: str
    streamingtv: str
    streamingmovies: str
    contract: str
    paperlessbilling: str
    PaymentMethod: str
    monthlycharges: float
    totalcharges: float


class Models(BaseModel):
    model: str

def get_current_username(credentials: HTTPBasicCredentials=Depends(security)):
    try:
        correct_password = secrets.compare_digest(credentials.password, users_db[credentials.username])
    except:
        correct_password = False
    if not (correct_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return credentials.username					

@api.get("/")
def read_current():
	"""
	return welcome url
	"""
	return "Hello"

@api.post("/permissions")
def permissions(username: str = Depends(get_current_username)):
    return {"username": username}
	
@api.post("/performance")
def performance(model: Models, username: str = Depends(get_current_username)):
   
    data = {
        "v1" : 0.63,
        "v2": 0.72
        }
    choix = model.model    
    
    if choix in data.keys():
        score = data[choix]
        return f'the score(accuracy) of {choix} model is : {score}'
    else:
        return "Ce model n'existe pas"




@api.post("/predict/v1")
def predictions1(item:Item, username: str = Depends(get_current_username)):
    
    model = joblib.load(r"model_nb.sav")

    seniorcitizen = item.seniorcitizen
    dependents = item.dependents
    tenure = item.tenure
    phoneservice = item.phoneservice
    mutliplelines = item.mutliplelines
    internetservice =  item.internetservice
    onlinesecurity = item.onlinesecurity
    onlinebackup = item.onlinebackup
    techsupport = item.techsupport
    streamingtv = item.streamingtv
    streamingmovies = item.streamingmovies
    contract = item.contract
    paperlessbilling = item.paperlessbilling
    PaymentMethod = item.PaymentMethod
    monthlycharges = item.monthlycharges
    totalcharges = item.totalcharges
                    
    data = {
        'SeniorCitizen': seniorcitizen,
        'Dependents': dependents,
        'tenure':tenure,
        'PhoneService': phoneservice,
        'MultipleLines': mutliplelines,
        'InternetService': internetservice,
        'OnlineSecurity': onlinesecurity,
        'OnlineBackup': onlinebackup,
        'TechSupport': techsupport,
        'StreamingTV': streamingtv,
        'StreamingMovies': streamingmovies,
        'Contract': contract,
        'PaperlessBilling': paperlessbilling,
        'PaymentMethod':PaymentMethod, 
        'MonthlyCharges': monthlycharges, 
        'TotalCharges': totalcharges
                    
                    }
    features_df = pd.DataFrame.from_dict([data])


    #Preprocess inputs
    preprocess_df = preprocess(features_df, 'Online')

    prediction = model.predict(preprocess_df)
    prediction_proba = model.predict_proba(preprocess_df)
    score =  max(prediction_proba[0])
    #score = str(prediction)
    
    if prediction == 1:
        return 'Yes, the customer will terminate the service.'
    else:
        return f'No, the customer is happy with Telco Services. the probability is : {score}'
   


@api.post("/predict/v2")
def predictions2(item:Item, username: str = Depends(get_current_username)):
    
    model = joblib.load(r"model.sav")

    seniorcitizen = item.seniorcitizen
    dependents = item.dependents
    tenure = item.tenure
    phoneservice = item.phoneservice
    mutliplelines = item.mutliplelines
    internetservice =  item.internetservice
    onlinesecurity = item.onlinesecurity
    onlinebackup = item.onlinebackup
    techsupport = item.techsupport
    streamingtv = item.streamingtv
    streamingmovies = item.streamingmovies
    contract = item.contract
    paperlessbilling = item.paperlessbilling
    PaymentMethod = item.PaymentMethod
    monthlycharges = item.monthlycharges
    totalcharges = item.totalcharges
                    
    data = {
        'SeniorCitizen': seniorcitizen,
        'Dependents': dependents,
        'tenure':tenure,
        'PhoneService': phoneservice,
        'MultipleLines': mutliplelines,
        'InternetService': internetservice,
        'OnlineSecurity': onlinesecurity,
        'OnlineBackup': onlinebackup,
        'TechSupport': techsupport,
        'StreamingTV': streamingtv,
        'StreamingMovies': streamingmovies,
        'Contract': contract,
        'PaperlessBilling': paperlessbilling,
        'PaymentMethod':PaymentMethod, 
        'MonthlyCharges': monthlycharges, 
        'TotalCharges': totalcharges
                    
                    }
    features_df = pd.DataFrame.from_dict([data])


    #Preprocess inputs
    preprocess_df = preprocess(features_df, 'Online')

    prediction = model.predict(preprocess_df)
    prediction_proba = model.predict_proba(preprocess_df)
    #clf.predict_proba(X_test_std)[:, 1]
    score =  max(prediction_proba[0])
    #score = model.predict_proba(preprocess_df)[:, 1]
    
    if prediction == 1:
        return 'Yes, the customer will terminate the service.'
    else:
        return f'No, the customer is happy with Telco Services. the score is : {score}'
   