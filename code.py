import pandas as pd
import os

data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,34,37],
    'City':['Los Angeles','Chicago','New York']
}

df=pd.DataFrame(data)
new_row_loc={'Name':'rahul','Age':20,'City':'Banglore'}
df.loc[len(df.index)]=new_row_loc
new_row_loc={'Name':'megh','Age':30,'City':'surat'}
df.loc[len(df.index)]=new_row_loc
data_dir = "data"
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"csv file saved to path {file_path}")
