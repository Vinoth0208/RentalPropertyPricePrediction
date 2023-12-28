import pandas as pd
from sklearn.preprocessing import LabelEncoder

from Preprocess import process

data=pd.read_excel(r'Dataset/House_Rent_Test.xlsx')
df=process(data)
model = LabelEncoder()
for col in ['type', 'activation_date', 'locality', 'lease_type', 'furnishing', 'facing', 'parking', 'water_supply',
            'building_type']:
    df[col] = model.fit_transform(df[col])
