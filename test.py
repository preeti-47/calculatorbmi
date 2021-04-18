import json
import pandas as pd
import numpy as np





class BMI():

    

    def bmi_cal(self,data=None):
        
    
        if data is None:
            print("Data is Empty")
        else:
            try:
                for idx,person_data in data.iterrows():
                    p_weight_m=person_data[2]
                    p_height_m=float(person_data[1] / 100)
                    bmi_value=round(float(p_weight_m/(p_height_m**2)),1)
            
                    data.loc[idx,'BMI_range']=bmi_value
                    if bmi_value < 18.5:
                        data.loc[idx,'BMI_category']='Underweight'
                        data.loc[idx,'Health_risk']='Malnutrition risk'

                    elif bmi_value>=18.5 and bmi_value < 25:
                        data.loc[idx,'BMI_category']='Normal weight'
                        data.loc[idx,'Health_risk']='Low risk'

                    elif bmi_value>=25 and bmi_value < 30:
                        data.loc[idx,'BMI_category']='Overweight'
                        data.loc[idx,'Health_risk']='Enhanced risk'

                    elif bmi_value>=30 and bmi_value < 35:
                        data.loc[idx,'BMI_category']='Moderately obese'
                        data.loc[idx,'Health_risk']='Medium risk'
                
                    elif bmi_value>=35 and bmi_value < 40:
                        data.loc[idx,'BMI_category']='Severely obese'
                        data.loc[idx,'Health_risk']='High risk'

                    elif bmi_value>=40:
                        data.loc[idx,'BMI_category']='Very severely obese'
                        data.loc[idx,'Health_risk']='Very high risk'
            except:
                print("Error Occur")            
     


        return data

    def count(self,data=None,col_name=None,value=None):

        if data is None or col_name is None or value is None:
            print("Data or Column name  is empty")
        else:
            try:
                val_count=data[col_name].value_counts()[value]
            except:
                print("Error occur for counting values")  

        return val_count          

                
    
ob=BMI()
df=pd.read_json('data.json')
df['BMI_category']=None
df['BMI_range']=None
df['Health_risk']=None


df=ob.bmi_cal(df)
print(df)

col_name='BMI_category'
value='Overweight'
count_val=ob.count(df,col_name,value)

print("Total Number of "+value+" people is "+str(count_val))




      

