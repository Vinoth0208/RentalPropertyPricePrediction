import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt


def charts():
    df=pd.read_csv(r'ProcessedData.csv')

    image = px.box(df, y='type', x='rent', color='type', title='Type vs rent')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, x='rent', y='amenities', color='type', title='amenities vs rent')
    st.plotly_chart(image, use_container_width=True)

    image=px.bar(df, x='type', y='property_size', color='type', title='Type vs Property_size')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, x='property_age', y='rent', color='type', title='rent vs property_age')
    st.plotly_chart(image, use_container_width=True)

    image = px.bar(df, x='furnishing', y='rent', color='type',barmode='group', title='rent vs furnishing')
    st.plotly_chart(image, use_container_width=True)

    image = px.pie(df, names='type', values='property_age', color='property_age',  title='Type vs property_age')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, x='type', y='bathroom', color='type', title='Type vs bathroom')
    st.plotly_chart(image, use_container_width=True)

    image = px.bar(df, x='water_supply', y='type', color='water_supply', title='Type vs water_supply')
    st.plotly_chart(image, use_container_width=True)

    image = px.violin(df, y='type', x='property_size', color='type', title='Type vs property_size')
    st.plotly_chart(image, use_container_width=True)

    image = px.bar(df, x='type', y='lease_type', color='lease_type', barmode='group', title='Type vs lease_type')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, x='activation_date', y='rent', color='type', title='rent vs activation_date')
    st.plotly_chart(image, use_container_width=True)

    img = px.scatter_geo(df, lat='latitude', lon='longitude', geojson='geometry',
                         scope='asia', hover_data=['rent', 'bathroom', 'type', 'gym', 'swimming_pool'], size='rent', color='type')
    img.update_geos(
        showland=True, landcolor="wheat",
        showocean=True, oceancolor="powderblue", )
    img.update_layout(geo=dict(projection_scale=3))
    st.plotly_chart(img, use_container_width=True)

    image = px.bar(df, x='total_floor', y='rent', color='type', barmode='group', title='total_floor vs rent')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, x='floor', y='rent', color='type', title='floor vs rent')
    st.plotly_chart(image, use_container_width=True)

    image = px.bar(df, x='negotiable', y='rent', color='lease_type', barmode='group',title='rent vs negotiable')
    st.plotly_chart(image, use_container_width=True)

    image = px.violin(df, x='balconies', y='rent', color='type', title='balconies vs rent')
    st.plotly_chart(image, use_container_width=True)

    image = px.pie(df, values='balconies', names='facing',  title='balconies vs facing')
    st.plotly_chart(image, use_container_width=True)

    image = px.scatter(df, y='water_supply', x='rent', color='type', title='water_supply vs rent')
    st.plotly_chart(image, use_container_width=True)

    plt.figure(figsize=(20, 10))
    dx=df.drop(columns=['Unnamed: 0','id', 'latitude', 'longitude'])
    img=sns.heatmap(dx.corr(numeric_only=True), annot=True)
    st.title('Correlation')
    st.pyplot(img.get_figure(), use_container_width=True)



