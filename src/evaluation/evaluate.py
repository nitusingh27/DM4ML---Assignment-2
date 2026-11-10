
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_recommendations(
    actual_ratings,
    predicted_ratings,
    train_ratings,
    k=10
):

    """
    Evaluate rating predictions and recommendation rankings.
    """

    # 1. RMSE and MAE

    actual_values = []
    predicted_values = []

    for row in actual_ratings.itertuples():

        user_id = row.user_id
        movie_id = row.movie_id
        actual_rating = row.rating

        if (
            user_id in predicted_ratings.index
            and movie_id in predicted_ratings.columns
        ):

            actual_values.append(actual_rating)

            predicted_values.append(
                predicted_ratings.loc[user_id, movie_id]
            )

    rmse = np.sqrt(
        mean_squared_error(
            actual_values,
            predicted_values
        )
    )

    mae = mean_absolute_error(
        actual_values,
        predicted_values
    )

    # 2. Precision@K and Recall@K

    precisions = []
    recalls = []

    relevant_threshold = 4.0

    for user_id in actual_ratings["user_id"].unique():

        if user_id not in predicted_ratings.index:
            continue

        user_test = actual_ratings[
            actual_ratings["user_id"] == user_id
        ]

        relevant_movies = set(
            user_test[
                user_test["rating"] >= relevant_threshold
            ]["movie_id"]
        )

        if not relevant_movies:
            continue

        rated_movies = set(
            train_ratings[
                train_ratings["user_id"] == user_id
            ]["movie_id"]
        )

        user_predictions = predicted_ratings.loc[user_id].drop(
            labels=list(rated_movies),
            errors="ignore"
        )

        top_k_movies = set(
            user_predictions.nlargest(k).index
        )

        hits = len(
            top_k_movies.intersection(relevant_movies)
        )

        precisions.append(hits / k)

        recalls.append(
            hits / len(relevant_movies)
        )

    precision_at_k = (
        np.mean(precisions) if precisions else 0
    )

    recall_at_k = (
        np.mean(recalls) if recalls else 0
    )

    return {
        "RMSE": rmse,
        "MAE": mae,
        "Precision@K": precision_at_k,
        "Recall@K": recall_at_k
    }
