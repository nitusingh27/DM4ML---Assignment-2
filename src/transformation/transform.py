import pandas as pd

def transform_data(users, movies, ratings):

    """
    Generate derived datasets for recommendation systems.
    """

    # 1. User activity summary

    user_activity = ratings.groupby("user_id").agg(
        total_ratings=("rating", "count"),
        average_rating=("rating", "mean"),
        minimum_rating=("rating", "min"),
        maximum_rating=("rating", "max"),
        last_interaction=("timestamp", "max")
    ).reset_index()

    # 2. Item popularity summary

    item_popularity = ratings.groupby("movie_id").agg(
        total_ratings=("rating", "count"),
        average_rating=("rating", "mean")
    ).reset_index()

    # 3. User-item interaction matrix

    user_item_matrix = ratings.pivot_table(
        index="user_id",
        columns="movie_id",
        values="rating",
        fill_value=0
    )

    return {
        "user_activity": user_activity,
        "item_popularity": item_popularity,
        "user_item_matrix": user_item_matrix
    }
