
import pandas as pd
from sklearn.decomposition import TruncatedSVD

def train_recommendation_models(ratings):

    """
    Train popularity-based and collaborative filtering models.
    """

    # 1. Popularity-based model

    popularity_model = (
        ratings.groupby("movie_id")
        .agg(
            total_ratings=("rating", "count"),
            average_rating=("rating", "mean")
        )
        .reset_index()
    )

    popularity_model = popularity_model.sort_values(
        by=["total_ratings", "average_rating"],
        ascending=False
    )

    # 2. Create user-item rating matrix

    user_item_matrix = ratings.pivot_table(
        index="user_id",
        columns="movie_id",
        values="rating"
    ).fillna(0)

    # 3. Train SVD model

    n_components = min(
        20,
        user_item_matrix.shape[0] - 1,
        user_item_matrix.shape[1] - 1
    )

    svd_model = TruncatedSVD(
        n_components=n_components,
        random_state=42
    )

    user_factors = svd_model.fit_transform(user_item_matrix)

    movie_factors = svd_model.components_

    predicted_ratings = user_factors @ movie_factors

    predicted_ratings_df = pd.DataFrame(
        predicted_ratings,
        index=user_item_matrix.index,
        columns=user_item_matrix.columns
    )

    return {
        "popularity_model": popularity_model,
        "svd_model": svd_model,
        "user_item_matrix": user_item_matrix,
        "predicted_ratings": predicted_ratings_df
    }
