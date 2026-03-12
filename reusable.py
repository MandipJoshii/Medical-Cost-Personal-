
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




def binning(df):
    def bmi_category(bmi):
        if bmi < 18.5:
         return 'underweight'
        elif bmi < 25:   
         return 'normal'   
        elif bmi < 30:
         return 'overweight'
        elif bmi >= 30:
         return 'obese' 

    df['bmi_category'] = df['bmi'].apply(bmi_category) 
    return df



def bmi_category(df):
       if 'bmi_category' in df.columns:
        encoding = pd.get_dummies(df['bmi_category'], drop_first=True,dtype=int)
        df = pd.concat([df,encoding],axis=1)
        df = df.drop(columns=['bmi_category'])
        return df



def flag(df):
   df['high_risks'] = ((df['smoker'] == 1) & (df['bmi'] > 30)).astype(int)
   return df