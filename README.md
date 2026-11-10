# End-to-End Data Management Pipeline for a Movie Recommendation System

## 1. Project Overview

This project implements an end-to-end data management and machine learning pipeline for a movie recommendation system.

The pipeline covers data ingestion, validation, preparation, feature engineering, transformation, model training, evaluation, and workflow orchestration.

A synthetic movie dataset is used to demonstrate the complete workflow, from raw data ingestion to personalized movie recommendations and model evaluation.

## 2. Dataset

The project uses three synthetic CSV datasets:

- `users.csv`: User information.
- `movies.csv`: Movie information, including titles and genres.
- `ratings.csv`: User-movie interactions and ratings.

**Dataset size:**

- 250 users
- 120 movies
- 15,000 ratings

The data is synthetic and is not sourced from MovieLens.

## 3. Pipeline Architecture

The pipeline consists of eight stages:

1. **Data Ingestion:** Loads raw user, movie, and rating datasets.
2. **Data Validation:** Checks missing values, duplicates, invalid ratings, timestamps, and referential integrity.
3. **Data Preparation:** Cleans the datasets and handles invalid or missing records.
4. **Feature Engineering:** Generates user, movie, and interaction features.
5. **Data Transformation:** Creates user activity summaries, item popularity statistics, and a user-item interaction matrix.
6. **Train-Test Split:** Splits the ratings chronologically into 80% training data and 20% testing data.
7. **Model Training:** Trains popularity-based and collaborative-filtering recommendation models.
8. **Model Evaluation:** Evaluates model performance using rating prediction and recommendation ranking metrics.

Refer to `reports/pipeline_architecture.png` for the pipeline architecture diagram.

## 4. Machine Learning Models

### 4.1 Popularity-Based Recommendation

The popularity-based recommendation model recommends movies based on their popularity in the training dataset.

It uses movie interaction counts and average ratings to rank movies and generate recommendations.

### 4.2 Collaborative Filtering

The collaborative-filtering model uses Truncated Singular Value Decomposition (TruncatedSVD) to learn latent user and movie representations from the user-item interaction matrix.

The learned representations are used to generate predicted ratings and personalized movie recommendations.

## 5. Model Evaluation

The recommendation system is evaluated using both rating prediction metrics and recommendation ranking metrics.

### 5.1 Rating Prediction Metrics

- **RMSE (Root Mean Squared Error):** Measures the square root of the average squared prediction error.
- **MAE (Mean Absolute Error):** Measures the average absolute difference between predicted and actual ratings.

### 5.2 Recommendation Ranking Metrics

- **Precision@10:** Measures the proportion of recommended movies that are relevant among the top 10 recommendations.
- **Recall@10:** Measures the proportion of relevant movies retrieved among the top 10 recommendations.
- **NDCG@10:** Evaluates the ranking quality of recommendations, giving greater importance to relevant movies appearing higher in the list.
- **Coverage:** Measures the proportion of available movies recommended by the system.
- **Diversity:** Measures the diversity of movies within the generated recommendations.

For ranking evaluation, ratings of 4 or above are considered relevant.

### 5.3 Model Comparison Results

The following results were obtained from the final model evaluation:

| Metric | Popularity-Based | Collaborative Filtering |
|---|---:|---:|
| Precision@10 | 0.0514 | 0.0453 |
| Recall@10 | 0.1508 | 0.1279 |
| NDCG@10 | 0.1051 | 0.0932 |
| Coverage | 0.2521 | 1.0000 |
| Diversity | 0.8528 | 0.8295 |
| RMSE | N/A | 2.8151 |
| MAE | N/A | 2.5512 |

The popularity-based model achieves higher Precision@10, Recall@10, NDCG@10, and Diversity in this experiment. Collaborative filtering achieves higher catalogue coverage.

RMSE and MAE are reported for collaborative-filtering rating predictions. The popularity-based model is a ranking-only model, so rating-prediction RMSE and MAE are not applicable.

Detailed evaluation results are available in:

- `reports/final_model_comparison.csv`
- `reports/model_evaluation_results.csv`
- `reports/pipeline_evaluation_results.csv`

## 6. Feature Management

Feature engineering is performed to generate structured datasets for users, movies, and user-movie interactions.

The engineered feature datasets include:

- **Movie Features:** Movie metadata, genre indicators, and release decade.
- **User Features:** User age groups, occupation indicators, and preferred genre indicators.
- **Interaction Features:** User-movie interaction information and temporal features such as rating year, month, and day of the week.

Engineered feature datasets are stored in `data/features/`.

The feature catalog is available at `reports/feature_catalog.csv`.

Transformed datasets, including user activity summaries, item popularity statistics, and the user-item interaction matrix, are stored in `data/processed/transformed/`.

## 7. Data Validation and Preparation

The validation module checks the raw datasets for:

- Missing values
- Duplicate records
- Invalid ratings
- Invalid timestamps
- Invalid user and movie references

The preparation module handles missing and invalid records, removes duplicates, and prepares clean datasets for downstream processing.

The validation report is available at `reports/data_validation_report.csv`.

## 8. Experiment Tracking

MLflow was used during the project to track model experiments and evaluation metrics.

The experiments include popularity-based recommendation and collaborative-filtering models.

Two completed MLflow runs were recorded:

- `Popularity_Based_Model`
- `Collaborative_Filtering_Model`

The local MLflow database is not included in the GitHub repository.

## 9. Workflow Orchestration

The end-to-end pipeline is executed through `dags/run_pipeline.py`.

The orchestration script:

- Executes the complete pipeline.
- Records execution logs.
- Captures pipeline execution status.
- Saves a summary of dataset dimensions and evaluation metrics.

Run the workflow from the project root:

```bash
python dags/run_pipeline.py
```

This implementation uses a manually triggered, structured Python workflow. An external scheduler can be configured for periodic execution.

Execution logs and results are stored in the `reports/` directory:

- `reports/orchestration_run.log`
- `reports/orchestration_results.json`

## 10. Project Structure

```text
Movie_Recommendation_Project/
├── data/
│   ├── raw/
│   │   ├── users.csv
│   │   ├── movies.csv
│   │   └── ratings.csv
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

## 11. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/nitusingh27/DM4ML---Assignment-2.git
cd DM4ML---Assignment-2
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Pipeline

```bash
python dags/run_pipeline.py
```

The script executes all pipeline stages and saves the corresponding outputs, logs, and execution summary.

## 12. Key Deliverables

The repository includes:

- Source code for all pipeline stages.
- Synthetic raw datasets.
- Cleaned and transformed datasets.
- Engineered feature datasets and feature catalog.
- Popularity-based and collaborative-filtering recommendation models.
- Generated recommendation outputs.
- Model evaluation and comparison reports.
- Pipeline architecture diagram.
- Workflow execution script, logs, and results.
- Requirements file and project documentation.
- Final execution evidence report.

---

**Project:** End-to-End Data Management Pipeline for a Movie Recommendation System  
**Repository:** https://github.com/nitusingh27/DM4ML---Assignment-2
