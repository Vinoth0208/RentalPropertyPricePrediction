import pandas as pd
import streamlit
import streamlit as st
import sys

from Preprocess import process
from charts import charts
from predict import predict

sys.path.insert(1,r"C:\Users\Vinoth\PycharmProjects\spotifyrecommendationsystem\venv\Lib\site-packages")
import streamlit_option_menu


st.set_page_config(page_title="Rental price prediction", layout="wide")
selected=streamlit_option_menu.option_menu("Menu", ["About", "Data", "Charts","Predict","Contact"],
                                            icons = ["exclamation-circle", "search", "bar-chart", "globe", 'telephone-forward'],
                                            menu_icon = "cast",
                                            default_index = 0,
                                            orientation = "horizontal",
                                            styles = {"nav-link": {"font-size": "15px", "text-align": "centre",
                                                                   "--hover-color": "#d1798e"},
                                                      "nav-link-selected": {"background-color": "#b30e35"}, "width": "100%"},)
if selected =='About':
    st.header('Title: Smart Predictive Modeling for Rental Property Prices')
    st.subheader('Technology: Cleansing, EDA, Visualization, ML')
    st.markdown('About:')
    st.text("""In the real estate industry, determining the appropriate rental price for a property is crucial for property owners, tenants, and property management companies. 
Accurate rent predictions can help landlords set competitive prices, tenants make informed rental decisions, and property management companies optimize their portfolio management.
The goal of this project is to develop a data-driven model that predicts the rental price of residential properties based on relevant features. 
By analyzing historical rental data and property attributes, the model aims to provide accurate and reliable rent predictions.""")

if selected == 'Data':
    data=pd.read_excel(r'Dataset/House_Rent_Train.xlsx')
    df=process(data)
    streamlit.write(df)
    df.to_csv(r'ProcessedData.csv')

    data = pd.read_csv(r'ProcessedData.csv')
    File = data.to_csv()

    streamlit.download_button(
        label="Download data as CSV",
        data=File,
        file_name='Rental price prediction.csv',
        mime='text/csv', )

if selected == 'Charts':
    charts()
if selected == 'Predict':
    data=pd.read_csv(r'ProcessedData.csv')
    predict(data)
if selected == 'Contact':
    col1, col2 = st.columns([1, 1.5], gap='small')
    with col2:
        st.subheader("Name: :green[Vinoth Palanivel]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")