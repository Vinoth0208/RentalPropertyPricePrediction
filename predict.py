import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from Preprocess import process


def predict(df):
    tab1, tab2=st.tabs(['Given data', 'User Data' ])
    with tab1:
        df = df
        df.drop(columns=['Unnamed: 0', 'id', 'locality','latitude', 'longitude','cup_board'], inplace=True)
        model = LabelEncoder()
        for col in ['type', 'activation_date', 'lease_type', 'furnishing', 'facing', 'parking', 'water_supply','building_type']:
            df[col] = model.fit_transform(df[col])

        x = df.drop(columns=['rent'])
        y = df['rent']
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
        modelpredict = LinearRegression()
        modelpredict.fit(x_train,y_train)
        train_pred = modelpredict.predict(x_train)
        test_pred = modelpredict.predict(x_test)
        st.write("Train error: ",mean_absolute_percentage_error(y_train,train_pred))
        st.write("Test error: ",mean_absolute_percentage_error(y_test,test_pred))

        data = pd.read_excel(r'Dataset/House_Rent_Test.xlsx')
        df = process(data)
        dt=df
        df.drop(columns=['id', 'locality','latitude', 'longitude','cup_board'], inplace=True)
        model = LabelEncoder()
        for col in ['type', 'activation_date', 'lease_type', 'furnishing', 'facing', 'parking', 'water_supply',
                    'building_type']:
            df[col] = model.fit_transform(df[col])
        x_test=df
        test_pred = modelpredict.predict(x_test)
        rent=pd.DataFrame(test_pred)
        rent.columns=['Rent']
        rent.to_csv(r'Submission.csv')
        df=pd.concat([dt,rent], axis=1, join='outer')
        st.write(df)

        File = df.to_csv()
        st.download_button(
            label="Download data as CSV",
            data=File,
            file_name='Test Data Rental price prediction.csv',
            mime='text/csv', )
    with tab2:
        with st.form("my_form"):
            col1, col2, col3=st.columns([1,1,1])
            with col1:
                type=st.selectbox('Select Type',options=['RK1', 'BHK1', 'BHK2','BHK3','BHK4','BHK4PLUS'])
                lease_type=st.selectbox('Select Lease_Type',options=['FAMILY', 'ANYONE', 'BACHELOR', 'COMPANY'])
                furnishing=st.selectbox('Select Furnishing',options=['SEMI_FURNISHED', 'FULLY_FURNISHED', 'NOT_FURNISHED'])
                parking=st.selectbox('Select Parking',options=['BOTH', 'TWO_WHEELER', 'NONE', 'FOUR_WHEELER'])
                facing=st.selectbox('Select Facing', options=['E', 'NE', 'S', 'N', 'SE', 'W', 'NW', 'SW'])
                water_supply=st.selectbox('Select Water Supply', options=['CORP_BORE', 'CORPORATION', 'BOREWELL'])
                building_type=st.selectbox('Select Building Type', options=['AP', 'IH', 'IF', 'GC',])

            with col2:
                activation_year=st.selectbox('Select Activation Year', options=[2018,2017])
                gym=st.selectbox('Select Gym Availablity (0 for No, 1 for Yes)', options=[0, 1])
                lift=st.selectbox('Select Lift Availablity (0 for No, 1 for Yes)', options=[0, 1])
                swimming_pool=st.selectbox('Select Swimming Pool Availablity (0 for No, 1 for Yes)', options=[0, 1])
                negotiable=st.selectbox('Select Negotiable (0 for No, 1 for Yes)', options=[0, 1])

            with col3:
                property_size=st.slider('Select Property Size', max_value=3000, min_value=300)
                property_age=st.slider('Select Property age', max_value=400.00, min_value=0.0)
                bathroom=st.slider('Select Bathroom', max_value=21.0, min_value=1.0, step=1.0)
                floor=st.slider('Select Floor', max_value=25.0, min_value=1.0, step=1.0)
                total_floor=st.slider('Select Total Floor', max_value=26.0, min_value=1.0, step=1.0)
                amenities=st.slider('Select Amenities', max_value=19, min_value=0, step=1)
                balconies=st.slider('Select Balconies', max_value=13.0, min_value=0.0, step=1.0)
            submitted = st.form_submit_button("predict")

        if submitted:
            df = {"type": type, 'activation_date':activation_year, "lease_type": lease_type,'gym':gym,'lift':lift,
                  'swimming_pool':swimming_pool,'negotiable':negotiable,"furnishing": furnishing,"parking": parking,
                  'property_size':property_size,'property_age':property_age, 'bathroom':bathroom, "facing": facing,
                  'floor':floor,'total_floor':total_floor,'amenities':amenities, "water_supply": water_supply,
                  'building_type': building_type,'balconies':balconies}
            df = pd.DataFrame(df, index=[0])
            model = LabelEncoder()
            for col in ['type', 'activation_date', 'lease_type', 'furnishing', 'facing', 'parking', 'water_supply',
                        'building_type']:
                df[col] = model.fit_transform(df[col])
            x_test = df
            test_pred = modelpredict.predict(x_test)
            st.write('Preiction Rent:',test_pred[0])
