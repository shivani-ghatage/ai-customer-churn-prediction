# AI Customer Churn Prediction

## 1. Project Overview

AI Customer Churn Prediction is a machine learning project that explores whether a customer is likely to stop using a service. It uses customer data, including subscription tenure, support tickets, monthly spending, recent login activity, and plan type, to predict customer churn.

The project compares a simple baseline model with a Logistic Regression classifier and evaluates their performance using common classification metrics.

## 2. Project Objectives

- Understand and define a customer churn prediction problem.
- Inspect and prepare a dataset for machine learning.
- Train a Logistic Regression classification model.
- Compare the model with a majority-class baseline.
- Evaluate predictions using accuracy, precision, recall, and F1-score.
- Document responsible data use, limitations, and potential risks.

## 3. Dataset Description

The dataset is stored in `customer_churn.csv` and contains 12 customer records and 7 columns.

| Column | Description |
|---|---|
| `customer_id` | Unique customer identifier |
| `tenure_months` | Number of months the customer has subscribed |
| `support_tickets` | Number of support tickets |
| `monthly_spend_inr` | Monthly customer spending in INR |
| `last_login_days` | Number of days since the last login |
| `plan_type` | Customer subscription plan |
| `churned` | Target variable: 1 = churned, 0 = not churned |

### Target Distribution

- Not churned (`0`): 7 records
- Churned (`1`): 5 records

The dataset is small and is intended for learning and experimentation. It should not be treated as sufficient evidence for making real-world customer decisions.

## 4. Technologies Used

- **Python** — programming language
- **Pandas** — data loading and analysis
- **Scikit-learn** — preprocessing, model training, and evaluation
- **Jupyter Notebook** — interactive data exploration
- **Visual Studio Code** — development environment
- **Git and GitHub** — version control and project hosting

## 5. Machine Learning Workflow

### Step 1: Data Inspection

The dataset is loaded and examined to understand its structure, data types, class distribution, and missing values.

### Step 2: Feature Preparation

The `customer_id` field is excluded from model features because it is an identifier rather than a meaningful predictive feature. Numeric and categorical columns are processed using suitable preprocessing steps.

### Step 3: Model Training

Two models are evaluated:

1. **Majority-Class Baseline:** Provides a simple reference by predicting the most frequent class in the training data.
2. **Logistic Regression:** A supervised machine learning algorithm used for binary classification.

### Step 4: Model Evaluation

The models are evaluated on a held-out test set using:

- Accuracy
- Weighted precision
- Weighted recall
- Weighted F1-score
- Confusion matrix

## 6. Model Evaluation Results

The following results were obtained in the current evaluation run.

| Model | Accuracy | Weighted Precision | Weighted Recall | Weighted F1-score |
|---|---:|---:|---:|---:|
| Majority-Class Baseline | 66.67% | 0.00 | 66.67% | 53.33% |
| Logistic Regression | 100.00% | 1.00 | 1.00 | 1.00 |

### Interpretation

In this particular test split, Logistic Regression correctly classified all 3 test records, while the majority-class baseline did not identify the churned test example.

**Important limitation:** The dataset contains only 12 records, and the test set contains only 3 records. Therefore, the 100% accuracy is a preliminary result and does not demonstrate that the model will achieve similar performance on new customers. A larger dataset and more robust validation are required.

## 7. Project Structure

```text
ML-Problem-Framing-Responsible-Data-Card/
├── customer_churn.csv
├── baseline_model.py
├── baseline-model.ipynb
├── model_results.csv
├── problem-framing.md
├── responsible-data-card.md
├── risk-register.md
└── README.md
```

## 8. Installation and Setup

### Prerequisites

Install Python and Visual Studio Code. Open a terminal in the project directory.

Install the required Python libraries:

```bash
python -m pip install pandas scikit-learn
```

### Run the Model

Execute the following command from the project directory:

```bash
python baseline_model.py
```

The script loads the dataset, trains and evaluates the models, displays evaluation metrics, and saves the results to `model_results.csv`.

### Explore the Notebook

Open `baseline-model.ipynb` in VS Code to inspect the dataset and perform interactive analysis.

## 9. Responsible Data Use

This project includes supporting documentation for problem framing, responsible data considerations, and risk assessment.

Key considerations include:

- Protecting customer privacy and limiting unnecessary data collection.
- Checking data quality and potential bias.
- Avoiding unsupported claims about model accuracy.
- Reviewing predictions before making decisions that affect customers.
- Validating the model on larger and more representative data before deployment.

The model is an educational prototype and is not intended for automated real-world customer decisions.

## 10. Future Improvements

- Use a larger and more representative dataset.
- Apply suitable cross-validation techniques.
- Evaluate class-specific precision, recall, and confusion matrices.
- Investigate possible data leakage and overly simple patterns.
- Compare additional classification algorithms.
- Add visualizations to explain the model's results.
- Develop a simple interface to demonstrate churn predictions.

## 11. Conclusion

This project demonstrates a basic machine learning workflow for customer churn prediction, including data inspection, feature preparation, model training, evaluation, and responsible data documentation.

It provides a foundation for further learning in machine learning and predictive analytics. Additional data, testing, and validation are necessary before considering real-world use.
