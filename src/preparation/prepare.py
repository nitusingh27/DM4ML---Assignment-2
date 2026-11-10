
import pandas as pd

def prepare_data(users, movies, ratings):

    """
    Clean user, movie, and rating datasets.

    Returns:
        Dictionary containing cleaned datasets.
    """

    users_clean = users.copy()
    movies_clean = movies.copy()
    ratings_clean = ratings.copy()

    # Handle missing values

    users_clean["age"] = users_clean["age"].fillna(
        users_clean["age"].median()
    )

    movies_clean = movies_clean.dropna(
        subset=["title"]
    )

    ratings_clean = ratings_clean.dropna(
        subset=["rating"]
    )

    # Remove duplicate records

    users_clean = users_clean.drop_duplicates()
    movies_clean = movies_clean.drop_duplicates()
    ratings_clean = ratings_clean.drop_duplicates()

    # Remove invalid ratings

    ratings_clean = ratings_clean[
        ratings_clean["rating"].between(1, 5)
    ]

    # Convert timestamps and remove invalid dates

    ratings_clean["timestamp"] = pd.to_datetime(
        ratings_clean["timestamp"],
        errors="coerce"
    )

    ratings_clean = ratings_clean.dropna(
        subset=["timestamp"]
    )

    # Remove invalid foreign key references

    ratings_clean = ratings_clean[
        ratings_clean["user_id"].isin(
            users_clean["user_id"]
        )
    ]

    ratings_clean = ratings_clean[
        ratings_clean["movie_id"].isin(
            movies_clean["movie_id"]
        )
    ]

    return {
        "users": users_clean,
        "movies": movies_clean,
        "ratings": ratings_clean
    }
