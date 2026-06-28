import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("movies.csv")

cv = CountVectorizer()
vectors = cv.fit_transform(movies['genre'])

similarity = cosine_similarity(vectors)

def recommend(movie_name):
    
    movie_index = movies[movies['title'].str.lower() == movie_name.lower()].index

    if len(movie_index) == 0:
        print("Movie not found!")
        return

    movie_index = movie_index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    print("\nRecommended Movies:\n")

    count = 0

    for movie in movie_list[1:]:
        print(movies.iloc[movie[0]].title)
        count += 1

        if count == 5:
            break

print("🎬 Movie Recommendation System")

movie_name = input("Enter movie name: ")

recommend(movie_name)