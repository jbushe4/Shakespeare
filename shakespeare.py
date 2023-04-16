from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import glob, nltk, os, re
from nltk.corpus import stopwords 
import plotly.express as px


st.set_option('deprecation.showPyplotGlobalUse', False)

# Importing the StringIO module.
from io import StringIO 


st.markdown('''
# Analyzing Shakespeare Texts
''')

#Create a dictionary (not a list)
books = {' ':' ',"A Mid Summer Night's Dream":'summer.txt',"The Merchant of Venice":'merchant.txt',"Romeo and Juliet":'romeo.txt' }

#Create a sidebar
st.sidebar.header('Word Cloud Settings')

max_word = st.sidebar.slider('Max Words', min_value=10,max_value=200,value=100,step = 10)    
large_word = st.sidebar.slider('Size of Largest World', min_value=50,max_value=350,value=100,step = 10) 
image_word = st.sidebar.slider('Image Width', min_value=200,max_value=400,value=300,step = 10) 
Random_State = st.sidebar.slider('Random State', min_value=20,max_value=200,value=100,step = 10) 
remove_stop_words = st.sidebar.checkbox('Remove Stopwords?',value=True)

st.sidebar.header('Word Count Settings')
count_word = st.sidebar.slider('Minimum Count of Words', min_value=50,max_value=350,value=100,step = 10) 




#Select the text files
Image = st.selectbox('Choose a text file', books.keys())

# Get the Value
Image = books.get(Image)

if Image != ' ':
     stop_words = []
     raw_text = open(Image,'r').read().lower()
     nltk_stop_words = stopwords.words('english')
     if remove_stop_words:
        stopwords = set(nltk_stop_words)
        stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came','thou'])
        # These are all lowecase
     tokens = nltk.word_tokenize(raw_text)
    


tab1, tab2, tab3 = st.tabs(['Word Cloud','Bar Chart','View Text'])

with tab1:
    raw_text = open(Image,'r').read().lower()
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          max_words=max_word,
                          width=image_word,height=200,
                         ).generate(raw_text)
    plt.clf()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    st.pyplot()
   
with tab2:
    st.write('')
    raw_text = open(Image,'r').read().lower()
    stopwords = STOPWORDS
    filtered_text = [w for w in raw_text if not w in stopwords]
    fdist_filtered = nltk.FreqDist(filtered_text)
    fdist_filtered.plot(large_word)
    st.bar_chart(fdist_filtered)






with tab3:
    if Image !=' ':
        raw_text = open(Image,'r').read().lower()
        st.write(raw_text)










