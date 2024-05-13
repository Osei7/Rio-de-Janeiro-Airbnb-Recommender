
# Airbnb Recommender - Rio de Janeiro 

## Project Intro/Objective
The purpose of this project is take a pre-existing inventory of Airbnb listings in Rio De Janeiro, Brazil and build a listing recommender system. Users can search available inventory by ID and select the option to have an additional 10 listings recommended that most match the initially selected listing. 

### Features
- **Data Cleaning**: Scripts to clean and prepare the Airbnb dataset.
- **Exploratory Data Analysis (EDA)**: Notebooks that explore various features and their relationships.
- **Recommender System**: A Python script (`recommender.py`) using TF-IDF and cosine similarity to recommend similar listings.
- **Streamlit Application**: A web application to interact with the recommender system in real-time.

### Technologies
* Cosine Similarity
* Feature Extraction - Tfid Vectorizer
* Folium
* Jupyter 
* Python - Pandas, Matplotlib, Numpy
* Regex
* Streamlit
 

### Repository Structure
```
airbnb-rio-recommender/
│
├── data/ # Dataset directory
│ ├── cleaned_data.csv # Cleaned data file
│ ├── df.csv # Data file used in the recommender
│ ├── rio.csv # Original dataset
│ └── neighbourhoods.geojson # GeoJSON for map visualizations
│
├── notebooks/ # Jupyter notebooks for EDA and preprocessing
│ ├── Cleaning_and_EDA.ipynb
│ └── recommender.ipynb
│ └── recommender.py
│
├── visualizations/ # Generated visualizations directory
│ └── various charts and maps
│
├── .gitignore # Specifies intentionally untracked files to ignore
├── README.md # The top-level README for developers using this project

```

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




