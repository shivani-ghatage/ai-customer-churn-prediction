Responsible Data Card
1. Dataset Overview
Dataset Name: Customer Churn Training Data
Source: RabTech Academy task resources
Purpose: Educational experimentation with customer churn prediction.
Data Type: Structured customer data.
Target Variable: Churn label provided in the dataset.
Status: Dataset details and column definitions must be verified before model training.
2. Data Provenance

The dataset was provided through the RabTech Academy project resources.

The original data collection source, collection date, collection method, and data processing history have not yet been independently verified. These details should be documented when the information is available.

The dataset must not be used for purposes outside its authorized scope.

3. Consent and Privacy

Before processing the data, verify that its use for educational analysis is permitted.

Do not publish customer names, contact details, account identifiers, or other personal information.
Remove or exclude direct identifiers from model features when they are not required.
Store the dataset securely and restrict access to authorized users.
Do not upload confidential customer data to public repositories.
Document applicable consent, legal basis, and data-retention requirements where relevant.
4. Sensitive Attributes and Fairness

Inspect the dataset for sensitive attributes and potential proxies for protected characteristics.

Determine whether these attributes are necessary for the stated purpose. Avoid using sensitive information for prediction unless its use is specifically justified and authorized.

Where suitable data and permissions are available, evaluate model performance and error rates across relevant customer groups. Do not assume that removing sensitive attributes alone eliminates bias.

5. Missing Values

Inspect each column for missing values and calculate the percentage of missing entries.

Document the chosen treatment for each affected feature. Depending on the data type, options may include median imputation for numerical variables, mode imputation for categorical variables, or an explicit missing category.

Fit imputation steps using training data only. Do not automatically remove rows or columns without assessing the potential impact.

6. Data Quality

Perform the following checks before training:

Identify duplicate records.
Verify column names and data types.
Check invalid values and inconsistent categories.
Inspect unusual numerical values and outliers.
Confirm the meaning and encoding of the churn target.
Check for inconsistent customer records and class imbalance.

Record significant data-quality issues and the actions taken to address them.

7. Data Leakage

Review all features to ensure they would be available at the intended prediction time.

Exclude information that directly reveals the outcome, such as a confirmed cancellation recorded after the prediction date, if present.

Separate training and test data before fitting preprocessing steps. Use an appropriate validation strategy and ensure that repeated customer records do not create unintended leakage between data splits.

8. Intended Use

The dataset is intended for educational experimentation and evaluation of a baseline customer churn prediction model.

The model may help explore which customers could benefit from retention support. Predictions must not be treated as confirmed statements about customer intentions.

The project does not establish that the model is suitable for production deployment.

9. Prohibited or Inappropriate Uses

The model should not be used to:

Deny customers essential services or ordinary support.
Make consequential decisions solely from a churn score.
Infer sensitive personal characteristics without authorization.
Publish identifiable customer records or predictions.
Claim that predictive associations prove why customers churn.
10. Dataset Limitations

The dataset size, representativeness, collection