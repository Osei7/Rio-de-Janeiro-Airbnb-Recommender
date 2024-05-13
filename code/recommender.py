import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from nltk.corpus import stopwords
import streamlit as st

df = pd.read_csv('./data/df.csv')

features = df['description']

stop_words_en = stopwords.words('english')
stop_words_po = stopwords.words('portuguese')

# create the tf-idf matrix
@st.cache
def create_tfidf_matrix(df):
    stop_words = stop_words_en + stop_words_po
    tfidf = TfidfVectorizer(stop_words=stop_words,max_features = 500)
    tfidf_matrix = tfidf.fit_transform(features)
    #tfidf_df = pd.DataFrame(tfidf_matrix.todense(), index=df.index, columns=tfidf.get_feature_names_out())
    return tfidf_matrix

# calculate the cosine similarity
@st.cache
def calculate_cosine_similarity(tfidf_matrix):
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# recommend the listings
@st.cache
def recommend_listings(cosine_sim, df, id, top_n): # id is the id of the listing
    recommended_listings = [] # create an empty list to store the recommended listings
    idx = id - 1 # get the index of the listing
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False) # get the similarity scores in descending order
    top_n_indexes = list(score_series.iloc[1:top_n+1].index) # get the indexes of the top n similar listings
    for i in top_n_indexes: # append the names of the recommended listings to the list
        recommended_listings.append(list(df['name'])[i]) # append the names of the recommended listings to the list
    return recommended_listings # return the list of recommended listings

# create the web app

# set the page config
st.set_page_config(page_title='Airbnb Rio Listings Recommender', page_icon=':house:', layout='wide', initial_sidebar_state='auto')
    
# set the title of the web app
st.title('Airbnb: Rio De Janeiro')


# show the 5 rows of the data
#st.write(df.head())

# create the tf-idf matrix
tfidf_matrix = create_tfidf_matrix(df)

# calculate the cosine similarity
cosine_sim = calculate_cosine_similarity(tfidf_matrix)

#st.write(cosine_sim)
#st.write(tfidf_matrix)

# create the sidebar
st.sidebar.header('Find your next listing with us...')
# create the user input features
id = st.sidebar.number_input('Enter the listing id here', min_value=1, value=1)

# create the recommendation button
if st.sidebar.button('Recommendations'):
    recommended_listings = recommend_listings(cosine_sim, df, id, 10)
    st.header('We Recommend...')
    for i in recommended_listings:
        st.write(i)

# write the name of the listing
st.header('Listing Name')

st.success(df['name'][id-1])

# write the price of the listing

st.header('Listing Price')

st.success(df['price'][id-1])



# create a subheader
st.subheader('Listing Description')

# show the description of the listing
st.write(df['description'][id-1])

# show the image of the listing
st.image(df['picture_url'][id-1])