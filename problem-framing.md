ML Problem Framing Memo
1. Project Title

Customer Churn Prediction Using Machine Learning

2. Business Problem

Customer churn occurs when customers stop using a company's products or services. Losing customers can reduce revenue and increase the cost of acquiring new customers.

The goal of this project is to investigate whether historical customer data can identify customers who are at risk of churning and help the business plan appropriate retention strategies.

3. Decision to Be Supported

The model will support the decision of which customers should be considered for a retention offer or follow-up by the customer support team.

Predictions will be used as decision-support information, not as automatic decisions about customers.

4. Prediction Target

The target variable is the churn label provided in the supplied dataset.

Positive class: Customer churns.
Negative class: Customer does not churn.

The exact target column and its label definitions must be verified against the dataset before model training.

5. Unit of Observation

One row is assumed to represent one customer, subject to confirmation from the dataset documentation.

Duplicate records and missing customer identifiers will be checked before analysis.

6. Prediction Time and Action Window

Predictions should use only information available at the time the prediction is made.

The prediction horizon and churn observation period must be defined using the dataset documentation and business requirements. These periods should not be assumed if they are not provided.

7. Data and Features

The project will use the supplied customer churn training dataset.

Before training, the data will be checked for:

Missing values and duplicate records.
Incorrect data types and inconsistent labels.
Features that directly reveal the churn outcome.
Sensitive or unnecessary personal information.
Features that would not be available at prediction time.
8. Non-ML Baseline

The first baseline will predict the most frequent class in the training data for every customer.

If sufficient historical information is available, a simple business-rule baseline may also be evaluated. The machine learning model must be compared against these baselines using the same test data.

9. Evaluation Metrics

The model will be evaluated using:

Precision: The proportion of predicted churn cases that are actual churn cases.
Recall: The proportion of actual churn cases correctly identified.
F1-score: The balance between precision and recall.
Accuracy: The proportion of all predictions that are correct.
Confusion matrix: The counts of true positives, true negatives, false positives, and false negatives.

Recall and precision will receive particular attention because missed churn cases and unnecessary retention offers have different business costs.

10. Business Costs
False positive: A customer is predicted to churn but does not. The business may spend money on an unnecessary retention offer.
False negative: A customer is predicted not to churn but actually leaves. The business may miss an opportunity to retain that customer.
True positive: A customer at risk of churn is correctly identified.
True negative: A customer who does not churn is correctly identified.

The final decision threshold should be selected based on business costs and validation results, not accuracy alone.

11. Responsible Use and Human Oversight

Customer data must be handled securely and used only for an authorized purpose.

The project will document data provenance, consent where applicable, limitations, missingness, potential bias, and leakage risks. Predictions should support human review rather than automatically trigger high-impact actions.

If a prediction is uncertain or required data is missing, the system should be able to abstain and refer the case for manual review.

12. Monitoring and Rollback

If deployed in the future, the model should be monitored for changes in data quality, churn rates, model performance, and differences in error rates across relevant customer groups where lawful and appropriate.

The model should be suspended or rolled back if performance deteriorates significantly, data leakage is discovered, or privacy and fairness concerns cannot be adequately addressed.

13. Expected Outcome

The project will produce a documented churn prediction baseline, an evaluation using held-out data, a responsible data card, and a risk register. The model's usefulness will be assessed against the non-ML baseline before any deployment is considered.

14. Limitations

The dataset's size, representativeness, feature definitions, and label quality must be verified. Model performance on historical data does not guarantee future performance, and predictive associations do not establish the causes of customer churn.