import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies=[]
    recommend_movies_poster=[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        # print(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

        recommend_movies.append(movies.iloc[i[0]].title)
        
    # st.write(recommend_movies)
    return recommend_movies,recommend_movies_poster




movies=pickle.load(open('movies.pkl','rb'))
movie_list=movies['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))
# print(movie_list['title'])

st.title("Movie Recommender")

selected_option=st.selectbox('Enter movie name',(movie_list))

if st.button("Recommend"):
    recommended_movie_names,recommended_movie_posters=recommend(selected_option)
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
    # st.color_picker("Color")
