
import os
import pandas as pd

def load_raw_data(project_path):

    """
    Load raw user, movie, and rating datasets.

    Args:
        project_path: Main project directory.

    Returns:
        Dictionary containing the three raw datasets.
    """

    raw_path = os.path.join(project_path, "data", "raw")

    users = pd.read_csv(
        os.path.join(raw_path, "users.csv")
    )

    movies = pd.read_csv(
        os.path.join(raw_path, "movies.csv")
    )

    ratings = pd.read_csv(
        os.path.join(raw_path, "ratings.csv")
    )

    return {
        "users": users,
        "movies": movies,
        "ratings": ratings
    }
