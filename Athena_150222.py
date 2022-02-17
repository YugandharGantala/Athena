import streamlit as st

PAGE_CONFIG = {"page_title":"Athena","layout":"centered"}
#st.set_page_config(layout="wide")

st.set_page_config(**PAGE_CONFIG)
 
from PIL import Image
import pandas as pd
import re
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
import os
import re
import numpy as np

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#stop_words = stopwords.words('english')
stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# import spacy
# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
# from collections import OrderedDict
from pprint import pprint
# import itertools


st.title('Athena')
st.markdown('<style>h1{color: orange; text-align: center}</style>', unsafe_allow_html=True)
st.markdown('<style>p{color: black;}</style>', unsafe_allow_html=True)
st.markdown('<style>h3{color: blue;}</style>', unsafe_allow_html=True)
image = Image.open('CI ORPHEUS LOGO+TEXT.png')
#st.sidebar.image('CI ORPHEUS LOGO+TEXT.png',width=200)
#st.sidebar.subheader('**Athena**')
#st.sidebar.write('eMail configurator helps you to classify given eMail to specific category. Each category is assigned to concern department in the organisation. The application provides automated solution  to route eMails to the concern department with minimal human intervention')
st.set_option('deprecation.showPyplotGlobalUse', False)
# col1, col2, col3 = st.sidebar.columns([1,1,1])
# with col1:
#   st.image("CIAI LOGO_Original-01.png")
#   st.sidebar.markdown('[Read more about CIAI](https://www.customerinsights.ai/)')
# with col2:
#   st.write("")
# with col3:
#   st.write("")

import streamlit as st
import plotly.express as px

def token(text):
  nltk_tokens = nltk.word_tokenize(text)
  filtered_sentence = [w for w in nltk_tokens if not w.lower() in stop_words]
 
  filtered_sentence = []
 
  for w in nltk_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
  return filtered_sentence

def common_elements1(list1, list2):
    #result = []
    for element in list1:
        if element in list2:
          return element

def common_elements2(list1, list2):
  return [x for x in list1 if x in list2]

def graph_controls(chart_type, df, dropdown_options):
    """
    Function which determines the widgets that would be shown for the different chart types
    :param chart_type: str, name of chart
    :param df: uploaded dataframe
    :param dropdown_options: list of column names
    :param template: str, representation of the selected theme
    :return:
    """
    length_of_options = len(dropdown_options)
    length_of_options -= 1

    #plot = px.scatter()
    if chart_type == 'None':
        st.subheader("Select chart")

    if chart_type == 'Scatter plots':
        st.sidebar.subheader("Scatterplot Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.scatter(data_frame=df,
                              x=x_values,
                              y=y_values,
                              color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_type == 'Line Chart':
        st.sidebar.subheader("Line Chart Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_type == 'Histogram':
        st.sidebar.subheader("Histogram Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            nbins = st.sidebar.number_input(label='Number of bins', min_value=2, value=5)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            barmode = st.sidebar.selectbox('bar mode', options=['group', 'overlay','relative'], index=2)
  
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.histogram(data_frame=df,barmode=barmode, x=x_values, y=y_values, color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_type == 'Box plots':
        st.sidebar.subheader('Box plot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options, options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis', index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options, options=dropdown_options)
            boxmode = st.sidebar.selectbox('Violin mode', options=['group', 'overlay'])
            outliers = st.sidebar.selectbox('Show outliers', options=[False, 'all', 'outliers', 'suspectedoutliers'])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.box(data_frame=df, x=x_values,
                          y=y_values, color=color_value,
                          boxmode=boxmode, points=outliers, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)

        except Exception as e:
            print(e)


    if chart_type == 'Pie Charts':
        st.sidebar.subheader('Pie Chart Settings')

        try:
            name_value = st.sidebar.selectbox(label='Name (Selected Column should be categorical)', options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color(Selected Column should be categorical)', options=dropdown_options)
            title = st.sidebar.text_input(label='Title of chart')

            plot = px.pie(data_frame=df,names=name_value, color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_type == 'Heatmap':
        st.sidebar.subheader("Heatmap Settings")

        try:
            selected_columns=st.sidebar.multiselect("Select Preferred columns",dropdown_options)
            title = st.sidebar.text_input(label='Title of chart')
            st.write(sns.heatmap(df[selected_columns].corr(), vmax=1, square=True, annot=True,cmap='viridis'))	
            st.subheader("Chart")
            st.pyplot()

        except Exception as e:
            print(e)

chart_types=['scatterplot', 'piechart', 'histogram']

def main():
  st.subheader('1. Upload the dataset')
  if st.checkbox("Upload File"):
    data=st.file_uploader("Upload file",type=['csv', 'excel'])

    if data is not None:
        df=pd.read_csv(data)
        if st.checkbox("Show Columns"):
          show_columns=df.columns.to_list()
          st.markdown(show_columns)
        columns = list(df.columns)
        columns.append(None)
        st.sidebar.subheader("Chart selection")
        chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                                options=['None', 'Scatter plots', 'Line Chart', 'Pie Charts',
                                                        'Histogram', 'Box plots', 'Heatmap'])  # 'Line plots',
        graph_controls(chart_type=chart_type, df=df, dropdown_options=columns)
  st.subheader('2. Enter text')
  if st.checkbox("Input text"):
    text=st.text_area("Enter the text","Type Here ..")
    
    if st.button("Visualization"):
      st.subheader(text)
      Chart_type= common_elements2(token(text), chart_types)
      if Chart_type==['scatterplot']:
        a= common_elements2(token(text), columns)
        if len(a)==1:
          plot = px.scatter(data_frame=df, x=a)
          st.plotly_chart(plot)
        elif len(a)==2:
          b,c=a
          plot = px.scatter(data_frame=df, x=b, y=c)
          st.plotly_chart(plot)
        elif len(a)==3:
          d,e,f=a
          plot = px.scatter(data_frame=df, x=d, y=e, color=f)
          st.plotly_chart(plot)

      elif Chart_type==['piechart']:
        a= common_elements2(token(text), columns)
        if len(a)==1:
          #plot = px.pie(data_frame=df, names=a)
          plot = df[a].value_counts().plot.pie(autopct="%1.1f%%")
          st.write(plot)
          st.pyplot()
        elif len(a)==2:
          b,c=a
          plot = px.pie(data_frame=df, names=b, color=c)
          st.plotly_chart(plot)

      elif Chart_type==['histogram']:
        a= common_elements2(token(text), columns)
        if len(a)==1:
          plot = px.histogram(data_frame=df, x=a, barmode='group')
          st.plotly_chart(plot)
        elif len(a)==2:
          b,c=a
          plot = px.histogram(data_frame=df, x=b, y=c, barmode='group')
          st.plotly_chart(plot)
        elif len(a)==3:
          u,v,w=a
          plot = px.histogram(data_frame=df, x=u, y=v, color=w, barmode='group')
          st.plotly_chart(plot)
      elif Chart_type==[]:
        a= common_elements2(token(text), columns)
        if len(a)==1:
          text = ' '.join(a)
          a1=df[text].nunique()
          if a1>=15:
            plot = px.scatter(data_frame=df, x=a)
            st.plotly_chart(plot)
          elif a1<15:
            plot = df[a].value_counts().plot.pie(autopct="%1.1f%%")
            st.write(plot)
            st.pyplot()
        elif len(a)==2:
          b,c=a
          plot = px.scatter(data_frame=df, x=b, y=c)
          st.plotly_chart(plot)
        elif len(a)==3:
          d,e,f=a
          plot = px.scatter(data_frame=df, x=d, y=e, color=f)
          st.plotly_chart(plot)

      # st.markdown(a)
      # st.markdown(b)

if __name__ == '__main__':
	main()  
