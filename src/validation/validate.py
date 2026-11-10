
import pandas as pd

def validate_data(users, movies, ratings):

    """
    Validate raw user, movie, and rating datasets.

    Returns a report containing data quality issues.
    """

    report = []

    datasets = {
        "users": users,
        "movies": movies,
        "ratings": ratings
    }

    # Check missing values and duplicates

    for name, df in datasets.items():

        report.append({
            "Dataset": name,
            "Check": "Missing Values",
            "Count": int(df.isnull().sum().sum())
        })

        report.append({
            "Dataset": name,
            "Check": "Duplicate Records",
            "Count": int(df.duplicated().sum())
        })

    # Check invalid ratings

    invalid_ratings = (
        (~ratings["rating"].between(1, 5))
        | ratings["rating"].isnull()
    ).sum()

    report.append({
        "Dataset": "ratings",
        "Check": "Invalid Ratings",
        "Count": int(invalid_ratings)
    })

    # Check invalid timestamps

    invalid_timestamps = pd.to_datetime(
        ratings["timestamp"],
        errors="coerce"
    ).isnull().sum()

    report.append({
        "Dataset": "ratings",
        "Check": "Invalid Timestamps",
        "Count": int(invalid_timestamps)
    })

    # Check invalid user references

    invalid_users = (
        ~ratings["user_id"].isin(users["user_id"])
    ).sum()

    report.append({
        "Dataset": "ratings",
        "Check": "Invalid User References",
        "Count": int(invalid_users)
    })

    # Check invalid movie references

    invalid_movies = (
        ~ratings["movie_id"].isin(movies["movie_id"])
    ).sum()

    report.append({
        "Dataset": "ratings",
        "Check": "Invalid Movie References",
        "Count": int(invalid_movies)
    })

    return pd.DataFrame(report)
