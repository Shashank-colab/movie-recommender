import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=afb841b88f4f09b06e4499e9b8c918da&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path

def recommend(movie):
     movie_index = movies_list[movies_list['title'] == movie].index[0]
     distance = similarity[movie_index]
     movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
     recommended_movies = []
     recommended_movies_posters = []
     for i in movie_list:
          movie_id = movies_list.iloc[i[0]].movie_id
          recommended_movies.append(movies_list.iloc[i[0]].title)
          # fetch poster from api
          recommended_movies_posters.append(fetch_poster(movie_id))
     return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))
movies = movies_list['title'].values


similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
'Movies Names',movies)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
