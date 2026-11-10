
import os
import sys
import json
import logging

# Identify the project directory
PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Add project directory to Python path
sys.path.insert(0, PROJECT_PATH)

from src.pipeline import run_pipeline

# Create reports directory if it does not exist
reports_path = os.path.join(PROJECT_PATH, "reports")
os.makedirs(reports_path, exist_ok=True)

# Configure execution logging
log_path = os.path.join(reports_path, "orchestration_run.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    logging.info("Starting movie recommendation workflow.")

    try:
        # Execute the complete pipeline
        results = run_pipeline(PROJECT_PATH)

        # Collect execution summary
        summary = {
            "status": "SUCCESS",
            "train_records": len(results["train_ratings"]),
            "test_records": len(results["test_ratings"]),
            "transformed_datasets": {
                name: list(data.shape)
                for name, data in results["transformed_data"].items()
            },
            "evaluation_metrics": {
                name: float(value)
                for name, value in results["evaluation_results"].items()
            }
        }

        # Save execution results
        results_path = os.path.join(
            reports_path, "orchestration_results.json"
        )

        with open(results_path, "w") as file:
            json.dump(summary, file, indent=4)

        logging.info("Pipeline executed successfully.")
        logging.info("Execution results saved.")

        print("ORCHESTRATION COMPLETED SUCCESSFULLY")
        print(json.dumps(summary, indent=4))

    except Exception as error:
        logging.exception("Pipeline execution failed.")
        raise error

if __name__ == "__main__":
    main()
