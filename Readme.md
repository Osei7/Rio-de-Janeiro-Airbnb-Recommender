
# Airbnb Recommender - Rio de Janeiro 

## Project Intro/Objective
The purpose of this project is take a pre-existing inventory of Airbnb listings in Rio De Janeiro, Brazil and build a listing recommender system. Users can search available inventory by ID and select the option to have an additional 10 listings recommended that most match the initially selected listing. 

### Methods Used
* Data Visualization
* Inferential Statistics
* Machine Learning
* Natural Learning Processing
* Recommender Systems

* etc.

### Technologies
* Cosine Similarity
* Feature Extraction - Tfid Vectorizer
* Folium
* Jupyter 
* Python - Pandas, Matplotlib, Numpy
* Regex
* Streamlit

* etc. 

## Project Description
This project initially began with a hypothesis I could accurately predict what a property in Rio De Janeiro would list for on Airbnb. From there I would use streamlit to create a web hosted app allowing people to input the features of their property to generate a price. After doing a quick glance at the key features of the data, the data was messy. there was less than 8% correlation with the highest correlated feature.

Data cleaning consisted of removing special characters and spaces from key categories such as price, then reformatting those features from objects to integers, floats, or categorical. In addition there were several null vales. Numerical features were imputed with a linear regression (later in the recommender notebook these will be replaced with the mean or mode of each individual column depending on type). Columns with object values were replaced with missing. 

From there After attempting several versions of a regression model using Polynomial Features, Feature Selection, PCA, One Hot Encoding Neighborhoods, the best Accuracy score produced on the test set was 0.002.
At this point I pivoted to building an interactive recommender system that suggests additional airbnb options to clients based on a selected listing. The model uses TfidVectorizer to analyze the description, accounting for Potuguese and English stop words to match closely described listings. 

## Folders
1. Code: contains the jupyter lab notebooks for cleaning, Exploratory Data Analysis, and the recommender model.
2. Data: the sources of data for the project
3. Visualizations & Presentation: the visual representations of data from EDA and presentation slides of the project


### Credits & Resources:
1. Hank Butler, GA Assembly DSI
* Lesson 7.05 - Recommender Systems
* Lesson 9.06 - Streamlit

2. Marcello Dichiera, Data Scientist / Medium Contributer
* https://medium.com/geekculture/step-by-step-guide-to-build-personalized-airbnb-recommendation-app-with-streamlit-a41d5514d534
* https://medium.com/geekculture/web-page-content-analysis-made-easy-with-streamlit-a-step-by-step-guide-d5051ed6c3b7

3. Soner Yildirim, Data Scientist 
* https://towardsdatascience.com/data-cleaning-and-eda-on-airbnb-dataset-with-python-pandas-and-seaborn-7c276116b650

4. Liam Connors, Data Science Student
* https://towardsdatascience.com/creating-a-simple-map-with-folium-and-python-4c083abfff94

5. Mikey Ling, Data Scientist at Veeya Systems
* https://medium.com/analytics-vidhya/folium-and-choropleth-weird-names-cool-graph-4f9b99b99190

6. Jingwen Zheng, Data Scientist in Retail
* https://jingwen-z.github.io/how-to-draw-a-variety-of-maps-with-folium-in-python/

7. Ferhat Metin
https://www.kaggle.com/code/ferhatmetin34/stanbul-airbnb-data-visualization-with-folium-map/notebook

### Data:
http://insideairbnb.com/get-the-data/

### Would like to explore:
Regression Model: Further exploring  correlation between features and pricing in Rio. Feature extraction, engineering and predictive pricing.

Recommender system: better organization and naming of listings both for searching and recommending. In addition, recommending based on features. Price range first and foremost, as well as beds, baths, and neighborhood, and accomodates, better cleaning / eda on desciption in Portuguese


