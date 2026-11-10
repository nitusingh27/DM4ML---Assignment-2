# End-to-End Data Management Pipeline for a Movie Recommendation System

## 1. Project Overview

This project implements an end-to-end data management and machine learning pipeline for a movie recommendation system.

The pipeline covers data ingestion, validation, preparation, feature engineering, transformation, model training, evaluation, and workflow orchestration.

A synthetic movie dataset is used to demonstrate the complete workflow.

## 2. Dataset

The project uses three synthetic CSV datasets:
- `users.csv`: User information.
- `movies.csv`: Movie information, including titles and genres.
- `ratings.csv`: User-movie interactions and ratings.

Dataset size:
- 250 users
- 120 movies
- 15,000 ratings

The data is synthetic and is not sourced from MovieLens.

## 3. Pipeline Architecture

The pipeline consists of eight stages:
1. Data ingestion
2. Data validation
3. Data preparation
4. Feature engineering
5. Data transformation
6. Chronological 80:20 train-test split
7. Model training
8. Model evaluation

Refer to `reports/pipeline_architecture.png` for the architecture diagram.

## 4. Machine Learning Models

### Popularity-Based Recommendation

Recommends movies based on their popularity in the training dataset.

### Collaborative Filtering

Uses Truncated Singular Value Decomposition (TruncatedSVD) to learn latent user and movie representations and generate personalized recommendations.

## 5. Evaluation Metrics

Rating prediction metrics:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

Recommendation ranking metrics:
- Precision@10
- Recall@10
- NDCG@10
- Coverage
- Diversity

The popularity-based model is evaluated using ranking metrics. RMSE and MAE are reported for collaborative-filtering rating predictions.

Detailed results are available in `reports/final_model_comparison.csv`.

## 6. Feature Management

Engineered feature datasets are stored in `data/features/`.
The feature catalog is available at `reports/feature_catalog.csv`.
Transformed datasets are stored in `data/processed/transformed/`.

## 7. Experiment Tracking

MLflow was used during the project to track model experiments and evaluation metrics.
The local MLflow database is not included in the GitHub repository.

## 8. Workflow Orchestration

The pipeline is executed through `dags/run_pipeline.py`.
The script runs the end-to-end pipeline, records execution logs, and saves execution results.

Run from the project root:

```bash
python dags/run_pipeline.py
```

This is a manually triggered Python workflow. An external scheduler can be configured for periodic execution.

Execution logs and results are stored in `reports/`.

## 9. Project Structure

```text
Movie_Recommendation_Project/
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── transformed/
│   └── features/
├── src/
│   ├── ingestion/
│   ├── validation/
│   ├── preparation/
│   ├── transformation/
│   ├── features/
│   ├── training/
│   ├── evaluation/
│   └── pipeline.py
├── models/
├── reports/
├── dags/
│   └── run_pipeline.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 10. Installation and Execution

Clone the repository:

```bash
git clone https://github.com/nitusingh27/DM4ML---Assignment-2.git
cd DM4ML---Assignment-2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python dags/run_pipeline.py
```

## 11. Key Deliverables

- Source code for all pipeline stages
- Synthetic raw datasets
- Cleaned and transformed datasets
- Engineered feature datasets and feature catalog
- Recommendation model outputs
- Model evaluation and comparison reports
- Pipeline architecture diagram
- Workflow execution script, logs, and results
- Requirements and project documentation
