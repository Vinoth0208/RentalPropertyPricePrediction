import pandas as pd
import streamlit
import json
def process(df):
    # df=pd.read_excel(r'Dataset/House_Rent_Train.xlsx')
    df=df
    print(df.info())
    print(df.isna().sum())
    df['type'].replace('1BHK1', 'BHK1', inplace=True)
    df['type'].replace('bhk2', 'BHK2', inplace=True)
    df['type'].replace('bhk3', 'BHK3', inplace=True)

    try:
        for i in range(len(df['amenities'])):
            x = json.loads(df['amenities'][i])
            l = []
            for j in x:
                print(x)
                if x[j] == True:
                    l.append(x[j])
            df['amenities'][i] = len(l)
    except:
        pass

    for i in range(len(df['type'])):
        if pd.isna(df['type'][i]) and df['property_size'][i]<500:
            df['type'][i]="RK1"
        elif pd.isna(df['type'][i]) and 500<df['property_size'][i]<1000 :
            df['type'][i]="BHK1"
        elif pd.isna(df['type'][i]) and 1000<df['property_size'][i] <1500 :
            df['type'][i]="BHK2"
        elif pd.isna(df['type'][i]) and 1500 <df['property_size'][i]<2000 :
            df['type'][i]="BHK3"
        elif pd.isna(df['type'][i]) and 2000<df['property_size'][i]<2500 :
            df['type'][i]="BHK4"
        elif pd.isna(df['type'][i]) and 2500<df['property_size'][i]<3000 :
            df['type'][i]="BHK4PLUS"

    print(df['balconies'].value_counts())
    for i in range(len(df['balconies'])):
        if pd.isna(df['balconies'][i]) and df['type'][i]=='RK1':
            df['balconies'][i]=0.0
        elif pd.isna(df['balconies'][i]) and df['type'][i]=='BHK1':
            df['balconies'][i]=1.0
        elif pd.isna(df['balconies'][i]) and df['type'][i]=='BHK2':
            df['balconies'][i]=2.0
        elif pd.isna(df['balconies'][i]) and df['type'][i]=='BHK3':
            df['balconies'][i]=3.0
        elif pd.isna(df['balconies'][i]) and df['type'][i]=='BHK4':
            df['balconies'][i]=4.0
        elif pd.isna(df['balconies'][i]) and df['type'][i]=='BHK4PLUS':
            df['balconies'][i]=10.0

    print(df.groupby(['type', 'building_type','property_size'])['building_type'].value_counts())

    for i in range(len(df['building_type'])):
        if pd.isna(df['building_type'][i]) and df['type'][i]=='RK1':
            df['building_type'][i]='IH'
        elif pd.isna(df['building_type'][i]) and df['type'][i]=='BHK1':
            df['building_type'][i]='AP'
        elif pd.isna(df['building_type'][i]) and df['type'][i]=='BHK2':
            df['building_type'][i]='AP'
        elif pd.isna(df['building_type'][i]) and df['type'][i]=='BHK3':
            df['building_type'][i]='GC'
        elif pd.isna(df['building_type'][i]) and df['type'][i]=='BHK4':
            df['building_type'][i]='IF'
        elif pd.isna(df['building_type'][i]) and df['type'][i]=='BHK4PLUS':
            df['building_type'][i]='IF'

    print(df['lease_type'].unique())
    print(df.groupby(['lease_type','type'])['lease_type'].count())
    for i in range(len(df['lease_type'])):
        if pd.isna(df['lease_type'][i]) and df['type'][i]=='RK1':
            df['lease_type'][i]='ANYONE'
        elif pd.isna(df['lease_type'][i]) and df['type'][i]=='BHK1':
            df['lease_type'][i]='ANYONE'
        elif pd.isna(df['lease_type'][i]) and df['type'][i]=='BHK2':
            df['lease_type'][i]='ANYONE'
        elif pd.isna(df['lease_type'][i]) and df['type'][i]=='BHK3':
            df['lease_type'][i]='FAMILY'
        elif pd.isna(df['lease_type'][i]) and df['type'][i]=='BHK4':
            df['lease_type'][i]='FAMILY'
        elif pd.isna(df['lease_type'][i]) and df['type'][i]=='BHK4PLUS':
            df['lease_type'][i]='ANYONE'

    print(df.groupby(['type'])['total_floor'].agg(pd.Series.mode))
    for i in range(len(df['total_floor'])):
        if pd.isna(df['total_floor'][i]) and df['type'][i]=='RK1':
            df['total_floor'][i]=3.0
        elif pd.isna(df['total_floor'][i]) and df['type'][i]=='BHK1':
            df['total_floor'][i]=2.0
        elif pd.isna(df['total_floor'][i]) and df['type'][i]=='BHK2':
            df['total_floor'][i]=4.0
        elif pd.isna(df['total_floor'][i]) and df['type'][i]=='BHK3':
            df['total_floor'][i]=4.0
        elif pd.isna(df['total_floor'][i]) and df['type'][i]=='BHK4':
            df['total_floor'][i]=1.0
        elif pd.isna(df['total_floor'][i]) and df['type'][i]=='BHK4PLUS':
            df['total_floor'][i]=3.0

    print(df['water_supply'].unique())
    print(df['water_supply'].mode())
    df['water_supply'].fillna('CORP_BORE', inplace=True)

    print(df.groupby(['type'])['floor'].agg(pd.Series.mode))
    for i in range(len(df['floor'])):
        if pd.isna(df['floor'][i]) and df['type'][i]=='RK1':
            df['floor'][i]=2.0
        elif pd.isna(df['floor'][i]) and df['type'][i]=='BHK1':
            df['floor'][i]=1.0
        elif pd.isna(df['floor'][i]) and df['type'][i]=='BHK2':
            df['floor'][i]=1.0
        elif pd.isna(df['floor'][i]) and df['type'][i]=='BHK3':
            df['floor'][i]=1.0
        elif pd.isna(df['floor'][i]) and df['type'][i]=='BHK4':
            df['floor'][i]=0.0
        elif pd.isna(df['floor'][i]) and df['type'][i]=='BHK4PLUS':
            df['floor'][i]=0.0

    print(df.groupby(['type'])['bathroom'].agg(pd.Series.mode))
    for i in range(len(df['bathroom'])):
        if pd.isna(df['bathroom'][i]) and df['type'][i]=='RK1':
            df['bathroom'][i]=1.0
        elif pd.isna(df['bathroom'][i]) and df['type'][i]=='BHK1':
            df['bathroom'][i]=1.0
        elif pd.isna(df['bathroom'][i]) and df['type'][i]=='BHK2':
            df['bathroom'][i]=2.0
        elif pd.isna(df['bathroom'][i]) and df['type'][i]=='BHK3':
            df['bathroom'][i]=3.0
        elif pd.isna(df['bathroom'][i]) and df['type'][i]=='BHK4':
            df['bathroom'][i]=4.0
        elif pd.isna(df['bathroom'][i]) and df['type'][i]=='BHK4PLUS':
            df['bathroom'][i]=4.0

    print(df.groupby(['type'])['property_size'].agg(pd.Series.mode))
    for i in range(len(df['property_size'])):
        if pd.isna(df['property_size'][i]) and df['type'][i]=='RK1':
            df['property_size'][i]=300
        elif pd.isna(df['property_size'][i]) and df['type'][i]=='BHK1':
            df['property_size'][i]=600
        elif pd.isna(df['property_size'][i]) and df['type'][i]=='BHK2':
            df['property_size'][i]=1200
        elif pd.isna(df['property_size'][i]) and df['type'][i]=='BHK3':
            df['property_size'][i]=1200
        elif pd.isna(df['property_size'][i]) and df['type'][i]=='BHK4':
            df['property_size'][i]=2000
        elif pd.isna(df['property_size'][i]) and df['type'][i]=='BHK4PLUS':
            df['property_size'][i]=2500
    df.dropna(inplace=True)
    x=pd.DatetimeIndex(df['activation_date']).year
    for i in range(len(df['activation_date'])):
        df['activation_date'][i]=x[i]

    return df


