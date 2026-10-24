
# Customer Churn Prediction - Baseline Model
# RabTech Academy Project

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

DATA_FILE = "customer_churn.csv"
TARGET_COLUMN = "churned"

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(
        f"Dataset '{DATA_FILE}' was not found. "
        "Place your actual dataset in the same folder "
        "as baseline_model.py and update DATA_FILE if needed."
    )

df = pd.read_csv(DATA_FILE)

print("\n--- Dataset Overview ---")
print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

# --------------------------------------------------
# 2. Validate the target
# --------------------------------------------------

if TARGET_COLUMN not in df.columns:
    raise ValueError(
        f"Target column '{TARGET_COLUMN}' was not found. "
        f"Available columns: {df.columns.tolist()}. "
        "Update TARGET_COLUMN to match your dataset."
    )

df = df.dropna(subset=[TARGET_COLUMN]).copy()

# Remove rows with invalid target labels only after
# confirming that the remaining labels are usable.
if df[TARGET_COLUMN].nunique() < 2:
    raise ValueError("The target must contain at least two classes.")

X = df.drop(columns=[TARGET_COLUMN]).copy()
y = df[TARGET_COLUMN].copy()

# Exclude common direct identifiers when present.
# Review these columns before using the model.
identifier_names = {
    "customerid", "customer_id", "customer id",
    "accountid", "account_id", "account id"
}

identifier_columns = [
    col for col in X.columns
    if col.strip().lower() in identifier_names
]

if identifier_columns:
    print("\nExcluding identifier columns:", identifier_columns)
    X = X.drop(columns=identifier_columns)

# --------------------------------------------------
# 3. Inspect target distribution
# --------------------------------------------------

print("\n--- Target Distribution ---")
print(y.value_counts())
print("\nTarget proportions:")
print(y.value_counts(normalize=True).round(3))

# --------------------------------------------------
# 4. Split data into training and test sets
# --------------------------------------------------

class_counts = y.value_counts()

if class_counts.min() < 2:
    raise ValueError(
        "At least one target class has fewer than two records. "
        "A stratified train/test split is not possible."
    )

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# --------------------------------------------------
# 5. Prepare numerical and categorical features
# --------------------------------------------------

numeric_features = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_features = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features),
])

# --------------------------------------------------
# 6. Define the models
# --------------------------------------------------

models = {
    "Majority-Class Baseline": DummyClassifier(
        strategy="most_frequent"
    ),
    "Logistic Regression": Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
        )),
    ]),
}

# --------------------------------------------------
# 7. Train and evaluate
# --------------------------------------------------

results = []

for name, model in models.items():
    print(f"\n{'=' * 55}")
    print(name)
    print("=" * 55)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions, average="binary",
        pos_label="Yes" if "Yes" in y_test.unique() else 1,
        zero_division=0,
    ) if y_test.nunique() == 2 and (
        "Yes" in y_test.unique() or 1 in y_test.unique()
    ) else precision_score(
        y_test, predictions, average="weighted",
        zero_division=0,
    )

    # Weighted metrics work with common string or numeric labels.
    recall = recall_score(
        y_test, predictions, average="weighted",
        zero_division=0,
    )
    f1 = f1_score(
        y_test, predictions, average="weighted",
        zero_division=0,
    )

    print(f"Accuracy:  {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall:    {recall:.3f}")
    print(f"F1-score:  {f1:.3f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(classification_report(
        y_test, predictions, zero_division=0
    ))

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision_weighted": precision,
        "Recall_weighted": recall,
        "F1_weighted": f1,
    })

# --------------------------------------------------
# 8. Compare models and save results
# --------------------------------------------------

results_df = pd.DataFrame(results)

print("\n--- Model Comparison ---")
print(results_df.to_string(index=False))

results_df.to_csv("model_results.csv", index=False)

print("\nResults saved to model_results.csv")
print("Baseline evaluation completed.")
