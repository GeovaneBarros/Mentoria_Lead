import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import Normalizer, LabelEncoder



def pre_processing(passenger):
    df = {}
    
    df['Pclass'] = int(passenger.pClass)
    if passenger.sex == 'male':
        df['Sex'] = 1
    else:
        df['Sex'] = 0
    df['Age'] = passenger.age
    df['SibSp'] = passenger.sibSp
    df['Parch'] = passenger.parch

    return df 


def perform_prediction(passenger):
    df = pre_processing(passenger)
    X_test = pd.DataFrame(df, index=[0])
    model_load = joblib.load('./results/titanic.pkl')
    predict = model_load.predict(X_test)
    if predict == 1:
        return 'Survived'
    else:
        return 'Not survived'




