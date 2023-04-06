Hello all! This is my first post-Codeup project, and I've decided I want to go back through every project we did there and make them better. Without further adieu, here's:

# Telecom Churn - Remixed

# Project Description

The goal of this project is to, using various pieces of customer data, predict when a customer will leave the company, or churn, and to then use that to find some reasons why people are leaving in order to come up with actionable business recommendations and conclusions.

# Project Goals

- Discovers the biggest drivers of customer churn.

- Use those drivers to develpo machine learning models to accurately classify customers as either churned or not churned.

- Deliver a report that a non-techincal person can read and understand what steps were taken, why they were taken, and the outcomes from those steps.

- Beat my old project, which had a 79% accuracy rating from it's best model.

# Intial Hypothesis and Questions

**From my initial sweep through this project:**

My initial hypothesis is that the biggest drivers of churn will be their contract type, whether or not they have internet and phone services, and what type of internet they have.

My main questions to determine this:

- Is whether or not a customer churns independent of their internet service type?

- Are contract type and churn status related?

- What is the relationship between phone service and churn?

- Does gender factor into churn?

- Do monthly charges differ for different contract types?

**This Iteration**

Now I know the following:

- Internet service type, and contract type are huge when it comes to importance.

- Monthly charges are also important, though not as important as the two above.

- Phone service, age, and gender didn't play much into churn status.

- Customers with fiber optic internet churned way more than the other categories.

I want to look further into:

- 

# Data Dictionary

For each entry below: 

- A 0 means 'No', and a 1 means 'Yes'.

- Most of the categorical columns include either a yes or no, as well as a 'No internet/phone service' option

    - An example for this would be 'Multiple Lines', there are three categories in this column - yes, no, and no phone service

| **Feature** | **Definition** |
|:--------|:-----------|
|**Gender** | If a customer is male or female|
|**Senior** Citizen | If a customer has senior citizen status|
|**Partner** | If someone has a partner|
|**Dependents** | If someone has dependents|
|**Tenure** | The length a customer (in months) has been with the company|
|**Phone Service** | If a customer has phone service through the company|
|**Paperless Billing** | If a customer has paperless billing or not|
|**Monthly Charges** | A customers monthly bill|
|**Total Charges** | The total a customer has paid the company|
|**Churn** (Target Variable) | Whether or not a customer has left the company|
|**Payment Type** | The customers payment type (0 for manual and 1 for automatic)|
|**Multiple Lines** | If a customer has multiple lines or not|
|**Online Security** | If a customer has online security services|
|**Online Backup** | If a customer has online backup services with the company|
|**Device Protection** | If a customer has device protection|
|**Tech Support** | If a customer has tech support included in their plan|
|**Streaming TV** | If a customer has TV streaming included|
|**Streaming Movies** | If a customer has movie streaming included|
|**Contract Type** | The customers contract type (Month to month, 1 year, or 2 years)|
|**Internet Service Type** | The customers internet service type (fiber optic, dsl, or no internet)|

# Libraries Used

| **Library** | **Documentation** |
|:-------|:-----------|
|**Pandas**| (https://pandas.pydata.org/docs/) |
|**NumPy**| (https://numpy.org/doc/) |
|**Matplotlib**| (https://matplotlib.org/stable/index.html) |
|**Seaborn**| (https://seaborn.pydata.org/) |
|**SciPy**| (https://docs.scipy.org/doc//scipy/index.html) |
|**Scikit-learn**| (https://scikit-learn.org/stable/user_guide.html) |
|**XGBoost**| (https://xgboost.readthedocs.io/en/stable/index.html) |

# My Plan Going Forward

# Steps to Reproduce this notebook

# Conclusions

## Takeaways

- Roughly 1/4 of customers churn.

- The biggest driver of churn seems to be the customers contract type; When a customer has a month-to-month contract, churn is just over 40%, or 2/5.

- Internet service type also plays a significant role in churn, though not as large as their contract type.

- Customers with fiber optic internet churned much more than those with either no internet or DSL.

- Whether or not a customer has phone service doesn't play a significant role in churn.

- Neither age or gender have much of an effect on whether or not someone will churn.

- Monthly charges also seem to play a role in churn.

- The final model beats the baseline accuracy for predicting whether someone will churn by about 8%.

# Recommendations


## Next Steps