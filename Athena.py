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

# nlp_en_core_web_sm = spacy.load('en_core_web_sm')

# NER = spacy.load("en_core_web_sm")
# def ner(text):
#   NER = spacy.load("en_core_web_sm")
#   text1 = NER(text)
#   for word in text1.ents:
#     print(word.text,word.label_)
#   #displacy.render(text1,style="ent",jupyter=True)


# def extract_named_ents(text):
#     """Extract named entities, and beginning, middle and end idx using spaCy's out-of-the-box model. 
    
#     Keyword arguments:
#     text -- the actual text source from which to extract entities
    
#     """
#     return [(ent.text, ent.label_) for ent in nlp_en_core_web_sm(text).ents]

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

    if chart_type == 'Scatter plots':
        st.sidebar.subheader("Scatterplot Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            # symbol_value = st.sidebar.selectbox("Symbol",index=length_of_options, options=dropdown_options)
            # size_value = st.sidebar.selectbox("Size", index=length_of_options,options=dropdown_options)
            # hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options,options=dropdown_options)
            # facet_row_value = st.sidebar.selectbox("Facet row",index=length_of_options, options=dropdown_options,)
            # facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
            #                                           options=dropdown_options)
            # marginalx = st.sidebar.selectbox("Marginal X", index=2,options=['rug', 'box', None,
            #                                                              'violin', 'histogram'])
            # marginaly = st.sidebar.selectbox("Marginal Y", index=2,options=['rug', 'box', None,
            #                                                              'violin', 'histogram'])
            # log_x = st.sidebar.selectbox('Log axis on x', options=[True, False])
            # log_y = st.sidebar.selectbox('Log axis on y', options=[True, False])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.scatter(data_frame=df,
                              x=x_values,
                              y=y_values,
                              color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)
            
            # plot = px.scatter(data_frame=df,
            #                   x=x_values,
            #                   y=y_values,
            #                   color=color_value,
            #                   symbol=symbol_value,
            #                   size=size_value,
            #                   hover_name=hover_name_value,
            #                   facet_row=facet_row_value,
            #                   facet_col=facet_column_value,
            #                   log_x=log_x, log_y=log_y,marginal_y=marginaly, marginal_x=marginalx, title=title)

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

    # if chart_type == 'Bar Chart':
    #     st.sidebar.subheader("Bar Settings")

    #     try:
    #         x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
    #         y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
    #         color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
    #         title = st.sidebar.text_input(label='Title of chart')
    #         st.write(sns.barplot(data_frame=df, x=x_values, y=y_values, title=title))
    #     except Exception as e:
    #         print(e)

    if chart_type == 'Histogram':
        st.sidebar.subheader("Histogram Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            nbins = st.sidebar.number_input(label='Number of bins', min_value=2, value=5)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)

            barmode = st.sidebar.selectbox('bar mode', options=['group', 'overlay','relative'], index=2)
            # marginal = st.sidebar.selectbox("Marginal", index=2,options=['rug', 'box', None,
            #                                                              'violin', 'histogram'])
            # barnorm = st.sidebar.selectbox('Bar norm', options=[None, 'fraction', 'percent'], index=0)
            # hist_func = st.sidebar.selectbox('Histogram aggregation function', index=0,
            #                                  options=['count','sum', 'avg', 'min', 'max'])
            # histnorm = st.sidebar.selectbox('Hist norm', options=[None, 'percent', 'probability', 'density',
            #                                                       'probability density'], index=0)
            # hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options,options=dropdown_options)
            # facet_row_value = st.sidebar.selectbox("Facet row",index=length_of_options, options=dropdown_options,)
            # facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
            #                                           options=dropdown_options)
            # cummulative = st.sidebar.selectbox('Cummulative', options=[False, True])
            # log_x = st.sidebar.selectbox('Log axis on x', options=[True, False])
            # log_y = st.sidebar.selectbox('Log axis on y', options=[True, False])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.histogram(data_frame=df,barmode=barmode, x=x_values, y=y_values, color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)
            # plot = px.histogram(data_frame=df,barmode=barmode,histnorm=histnorm,
            #                     marginal=marginal,barnorm=barnorm,histfunc=hist_func,
            #                     x=x_values,y=y_values,cumulative=cummulative,
            #                     color=color_value,hover_name=hover_name_value,
            #                     facet_row=facet_row_value,nbins=nbins,
            #                     facet_col=facet_column_value,log_x=log_x,
            #                     log_y=log_y, title=title)

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
            # hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options, options=dropdown_options)
            # facet_row_value = st.sidebar.selectbox("Facet row", index=length_of_options, options=dropdown_options, )
            # facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
            #                                           options=dropdown_options)
            # log_x = st.sidebar.selectbox('Log axis on x', options=[True, False])
            # log_y = st.sidebar.selectbox('Log axis on y', options=[True, False])
            # notched = st.sidebar.selectbox('Notched', options=[True, False])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.box(data_frame=df, x=x_values,
                          y=y_values, color=color_value,
                          boxmode=boxmode, points=outliers, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)
            # plot = px.box(data_frame=df, x=x_values,
            #               y=y_values, color=color_value,
            #               hover_name=hover_name_value,facet_row=facet_row_value,
            #               facet_col=facet_column_value, notched=notched,
            #               log_x=log_x, log_y=log_y, boxmode=boxmode, points=outliers, title=title)

        except Exception as e:
            print(e)


    if chart_type == 'Pie Charts':
        st.sidebar.subheader('Pie Chart Settings')

        try:
            name_value = st.sidebar.selectbox(label='Name (Selected Column should be categorical)', options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color(Selected Column should be categorical)', options=dropdown_options)
            # value = st.sidebar.selectbox("Value", index=length_of_options, options=dropdown_options)
            # hole = st.sidebar.selectbox('Log axis on y', options=[True, False])
            title = st.sidebar.text_input(label='Title of chart')

            plot = px.pie(data_frame=df,names=name_value, color=color_value, title=title)
            st.subheader("Chart")
            st.plotly_chart(plot)

        except Exception as e:
            print(e)
    # st.subheader("Chart")
    # st.plotly_chart(plot)


    if chart_type == 'Heatmap':
        st.sidebar.subheader("Heatmap Settings")

        try:
            selected_columns=st.sidebar.multiselect("Select Preferred columns",dropdown_options)
            #df1=df[selected_columns]
            #y_values = st.sidebar.selectbox('Y axis', index=length_of_options, options=dropdown_options)
            title = st.sidebar.text_input(label='Title of chart')
            st.write(sns.heatmap(df[selected_columns].corr(), vmax=1, square=True, annot=True,cmap='viridis'))	
            st.subheader("Chart")
            st.pyplot()
            # st.subheader("Chart")
            # st.plotly_chart(plot)

        except Exception as e:
            print(e)
    #st.pyplot()
    # st.subheader("Chart")
    # st.plotly_chart(plot)

chart_types=['scatterplot', 'piechart', 'histogram']

def main():
  st.subheader('1. Upload the dataset')
  if st.checkbox("Upload File"):
    data=st.file_uploader("Upload file",type=['csv', 'excel'])
    #text=st.text_area("Enter the text","Type Here ..")
    # st.markdown("**Named Entity Recognition:**")
    # if st.checkbox("Named Entities of input text"):
    #     entity_result = extract_named_ents(text)
    #     st.markdown(entity_result)
    
    if data is not None:
        df=pd.read_csv(data)
        columns = list(df.columns)
        columns.append(None)
        st.sidebar.subheader("Chart selection")
        chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                                options=['Scatter plots', 'Line Chart', 'Pie Charts',
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
          plot = px.pie(data_frame=df, names=a)
          st.plotly_chart(plot)
        elif len(a)==2:
          b,c=a
          plot = px.pie(data_frame=df, names=b, color=c)
          st.plotly_chart(plot)

      elif Chart_type==['histogram']:
        a= common_elements2(token(text), columns)
        if len(a)==1:
          plot = px.histogram(data_frame=df, x=a)
          st.plotly_chart(plot)
        elif len(a)==2:
          b,c=a
          plot = px.histogram(data_frame=df, x=b, y=c)
          st.plotly_chart(plot)
        elif len(a)==3:
          u,v,w=a
          plot = px.histogram(data_frame=df, x=u, y=v, color=w, barmode='group')
          st.plotly_chart(plot)

      # st.markdown(a)
      # st.markdown(b)

if __name__ == '__main__':
	main()  

