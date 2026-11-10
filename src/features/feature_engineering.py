
import pandas as pd

def engineer_features(users, movies, ratings):

    """
    Generate user, movie, and interaction features.
    """

    # 1. Movie features

    movie_features = movies[
        ["movie_id", "title", "release_year"]
    ].copy()

    genre_series = (
        movies["genres"]
        .fillna("")
        .str.replace(",", "|", regex=False)
    )

    genre_features = genre_series.str.get_dummies(
        sep="|"
    )

    genre_features.columns = (
        genre_features.columns.str.strip()
    )

    genre_features.index = movies.index

    movie_features = pd.concat(
        [movie_features, genre_features],
        axis=1
    )

    movie_features["release_decade"] = (
        (movie_features["release_year"] // 10) * 10
    )

    # 2. User features

    user_features = users[
        ["user_id", "age"]
    ].copy()

    user_features["age_group"] = pd.cut(
        user_features["age"],
        bins=[0, 25, 35, 50, 100],
        labels=["18-25", "26-35", "36-50", "50+"]
    )

    occupation_features = pd.get_dummies(
        users["occupation"],
        prefix="occupation",
        dtype=int
    )

    user_features = pd.concat(
        [user_features, occupation_features],
        axis=1
    )

    preferred_genres = (
        users["preferred_genres"]
        .fillna("")
        .str.get_dummies(sep="|")
    )

    preferred_genres.columns = [
        "preferred_genre_" + col
        for col in preferred_genres.columns
    ]

    preferred_genres.index = users.index

    user_features = pd.concat(
        [user_features, preferred_genres],
        axis=1
    )

    # 3. Interaction features

    interaction_features = ratings.copy()

    interaction_features["timestamp"] = pd.to_datetime(
        interaction_features["timestamp"],
        errors="coerce"
    )

    interaction_features = interaction_features.dropna(
        subset=["timestamp"]
    )

    interaction_features["rating_year"] = (
        interaction_features["timestamp"].dt.year
    )

    interaction_features["rating_month"] = (
        interaction_features["timestamp"].dt.month
    )

    interaction_features["rating_day_of_week"] = (
        interaction_features["timestamp"].dt.dayofweek
    )

    return {
        "movie_features": movie_features,
        "user_features": user_features,
        "interaction_features": interaction_features
    }
