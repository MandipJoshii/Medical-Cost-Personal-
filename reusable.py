
import pandas as pd
from sklearn.preprocessing import LabelEncoder
health = pd.read_csv('insurance.csv')

df = pd.DataFrame(health)

def label_Encoder(df):
    encoder = LabelEncoder()

    
    df['sex'] = encoder.fit_transform(df['sex'])
    df['smoker'] = encoder.fit_transform(df['smoker'])
    # print(df[['sex','smoker']].sample(20))
    return df

def oneHot_encoder(df):
    
    
    df = pd.get_dummies(df,columns=['region'],drop_first=True,dtype=int)
    return df


def cleaning(df):
    df = df.drop_duplicates()
    return df
