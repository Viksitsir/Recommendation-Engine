## RUN THE JUPYTER NOTEBOOK BEFORE RUNNING THIS FILE
import streamlit as st
import pickle 

movie_opened = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.header("Movie recommender")
movie_names = movie_opened['title'].values
select_value = st.selectbox("Select a movie", movie_names)


def suggest(movie):
    a = movie_opened[movie_opened["title"] == movie].index[0]
    distance_alpha = sorted(list(enumerate(similarity[a])), reverse=True, key= lambda vector:vector[1])
    recommend_list = []
    for i in distance_alpha[1:11]:
        recommend_list.append(movie_opened.iloc[i[0]].title)
    return recommend_list


if st.button("Recommend"):
    suggested_movies = suggest(select_value)
    col1,col2,col3,col4,col5= st.columns(5, gap="medium")
    with col1:
        st.text(suggested_movies[0])
    with col2:
        st.text(suggested_movies[1])
    with col3:
        st.text(suggested_movies[2])
    with col4:
        st.text(suggested_movies[3])
    with col5:
        st.text(suggested_movies[4]) 

    col6,col7,col8,col9,col10 = st.columns(5, gap="medium")
    with col6:
        st.text(suggested_movies[5])
    with col7:
        st.text(suggested_movies[6])
    with col8:
        st.text(suggested_movies[7])
    with col9:
        st.text(suggested_movies[8])
    with col10:
        st.text(suggested_movies[9])