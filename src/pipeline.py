
import os
import pandas as pd

from src.ingestion.ingest import load_raw_data
from src.validation.validate import validate_data
from src.preparation.prepare import prepare_data
from src.features.feature_engineering import engineer_features
from src.transformation.transform import transform_data
from src.training.train import train_recommendation_models
from src.evaluation.evaluate import evaluate_recommendations


def run_pipeline(project_path):

    print("Starting movie recommendation pipeline...")

    # Step 1: Data ingestion
    raw_data = load_raw_data(project_path)
    print("\nStep 1: Data ingestion completed.")

    # Step 2: Data validation
    validation_report = validate_data(
        raw_data["users"],
        raw_data["movies"],
        raw_data["ratings"]
    )
    print("\nStep 2: Data validation completed.")

    # Step 3: Data preparation
    cleaned_data = prepare_data(
        raw_data["users"],
        raw_data["movies"],
        raw_data["ratings"]
    )
    print("\nStep 3: Data preparation completed.")

    # Step 4: Feature engineering
    engineered_data = engineer_features(
        cleaned_data["users"],
        cleaned_data["movies"],
        cleaned_data["ratings"]
    )
    print("\nStep 4: Feature engineering completed.")

    # Step 5: Data transformation
    transformed_data = transform_data(
        cleaned_data["users"],
        cleaned_data["movies"],
        cleaned_data["ratings"]
    )
    print("\nStep 5: Data transformation completed.")

    # Step 6: Train-test split
    ratings = cleaned_data["ratings"].copy()
    ratings["timestamp"] = pd.to_datetime(ratings["timestamp"])
    ratings = ratings.sort_values("timestamp")

    split_index = int(len(ratings) * 0.8)

    train_ratings = ratings.iloc[:split_index].copy()
    test_ratings = ratings.iloc[split_index:].copy()

    print("\nStep 6: Train-test split completed.")

    # Step 7: Model training
    trained_models = train_recommendation_models(train_ratings)
    print("\nStep 7: Model training completed.")

    # Step 8: Model evaluation
    evaluation_results = evaluate_recommendations(
        actual_ratings=test_ratings,
        predicted_ratings=trained_models["predicted_ratings"],
        train_ratings=train_ratings,
        k=10
    )
    print("\nStep 8: Model evaluation completed.")

    print("\nMovie recommendation pipeline completed!")

    return {
        "raw_data": raw_data,
        "validation_report": validation_report,
        "cleaned_data": cleaned_data,
        "engineered_data": engineered_data,
        "transformed_data": transformed_data,
        "train_ratings": train_ratings,
        "test_ratings": test_ratings,
        "trained_models": trained_models,
        "evaluation_results": evaluation_results
    }
