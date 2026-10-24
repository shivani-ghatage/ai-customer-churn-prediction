Risk Register
Project: Customer Churn Prediction Using Machine Learning
1. Risk Assessment
ID	Risk	Likelihood	Impact	Mitigation
R1	Missing data	Medium	Medium	Inspect missing values and apply appropriate imputation using training data only.
R2	Data leakage	Medium	High	Exclude features that reveal the churn outcome or use information unavailable at prediction time.
R3	Class imbalance	Medium	High	Inspect the target distribution and evaluate precision, recall, F1-score, and the confusion matrix.
R4	Biased predictions	Unknown	High	Evaluate error rates across relevant customer groups where appropriate and lawful.
R5	False positives	Medium	Medium	Review the decision threshold and estimate the cost of unnecessary retention offers.
R6	False negatives	Medium	High	Monitor recall and investigate missed churn cases.
R7	Privacy exposure	Low to Medium	High	Restrict access, exclude unnecessary identifiers, and never publish confidential customer data.
R8	Model drift	Unknown	High	Monitor data and performance changes if the model is deployed.
R9	Poor generalization	Medium	High	Evaluate on held-out data and compare performance against a simple baseline.
R10	Incorrect target labels	Unknown	High	Verify the churn definition, label quality, and observation period before training.

Note: Likelihood ratings are preliminary estimates, not measured results. Update them after inspecting the dataset and evaluating the model.

2. False-Positive and False-Negative Risks
False Positives

A false positive occurs when the model predicts that a customer will churn, but the customer does not.

Potential impact:

Unnecessary retention offers.
Increased marketing costs.
Unwanted customer contact.

Mitigation:

Review precision and the confusion matrix.
Set the decision threshold according to business costs.
Ensure retention outreach is appropriate and not excessive.
False Negatives

A false negative occurs when the model predicts that a customer will not churn, but the customer does.

Potential impact:

Missed retention opportunities.
Lost customer revenue.
Incomplete identification of at-risk customers.

Mitigation:

Monitor recall and missed churn cases.
Evaluate alternative thresholds on validation data.
Compare model performance with the non-ML baseline.
3. Data Privacy and Security

Customer data must be used only for authorized purposes.

Mitigation measures:

Remove unnecessary personal identifiers from model inputs.
Restrict access to the dataset.
Do not commit confidential data to a public repository.
Verify permitted use and applicable privacy requirements.
Publish only approved documentation and non-sensitive results.
4. Bias and Fairness

Historical data may reflect unequal treatment, incomplete representation, or other sources of bias.

Mitigation measures:

Inspect relevant data limitations.
Evaluate model errors across suitable customer groups when lawful