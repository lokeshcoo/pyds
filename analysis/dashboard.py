import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
st.title("Smoker  Dashboard")
st.markdown("The Dashboard will help a researchers to get to know more about the the given dataset and it's output")

st.sidebar.title("Selct visiual chart")
st.sidebar.markdown("Select the Charts/Plots accordingly")

#Reading the dataset
data=pd.read_csv(r"C:\Users\ASUS\Downloads\demo_data_set.csv")

chart_visual=st.sidebar.selectbox("select the charts/plots",('Line Chart','Bar Chart','Bubble Chart'))

st.sidebar.checkbox("show analysis by smoking status", True, key=1)
selected_status=st.sidebar.selectbox("Selct smoking Status",options=['formerly_smoked','Smokes','Never_smoked','unknown'])

fig=go.Figure()

if chart_visual == 'Line Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,mode="lines", name="formerly_smoked"))

    if selected_status == 'Smokes':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,mode="lines", name="Smokes"))

    if selected_status == 'Never Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Never_smokes,mode="lines", name="Never_smokes"))  

    if selected_status == 'unknown':
        fig.add_trace(go.Scatter(x=data.Country,y=data.unknown,mode="lines", name="unknown"))    


elif chart_visual == 'Bar Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.bar(x=data.Country,y=data.formerly_smoked,mode="lines", name="formerly_smoked"))

    if selected_status == 'Smokes':
        fig.add_trace(go.bar(x=data.Country,y=data.Smokes,mode="lines", name="Smokes"))

    if selected_status == 'Never Smoked':
        fig.add_trace(go.bar(x=data.Country,y=data.Never_smokes,mode="lines", name="Never_smokes"))  

    if selected_status == 'unknown':
        fig.add_trace(go.bar(x=data.Country,y=data.unknown,mode="lines", name="unknown"))    


elif chart_visual == 'Bubble Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,mode="lines", name="formerly_smoked"))

    if selected_status == 'Smokes':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,mode="lines", name="Smokes"))

    if selected_status == 'Never Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Never_smokes,mode="lines", name="Never_smokes"))  

    if selected_status == 'unknown':
        fig.add_trace(go.Scatter(x=data.Country,y=data.unknown,mode="lines", name="unknown"))    
        
st.plotly_chart(fig,use_container_width=True) 


 





    