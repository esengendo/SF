# SF
# Analyzing Business Closures in San Francisco, CA: A Data Science Project

## Project Overview

Welcome to the "Analyzing Business Closures in San Francisco, CA" data science project. In this project, we will leverage data from various sources to gain insights into the factors affecting business closures in the city. We'll use data analysis, machine learning, and geospatial analysis techniques to achieve our goals.

## Project Goals

1. **Business Closure Prediction:** Use historical data to predict which businesses are more likely to close in the near future. We will build a machine learning model that takes into account factors such as business type, location, tax payment history, and economic indicators to predict closures. This prediction can be especially relevant in the context of crime impacts on businesses.

2. **Location-based Insights:** Analyze the dataset to identify areas in San Francisco where businesses are thriving and areas where they are struggling. We will use clustering algorithms to group businesses into categories and then visualize these clusters on a map to provide insights to entrepreneurs and policymakers.

## Data Sources

- [City of San Francisco Business Data (CSV)](https://data.sfgov.org/api/views/g8m3-pdis/rows.csv?accessType=DOWNLOAD&bom=true&format=true)
- [Bay Area Rapid Transport Data (Excel)](http://64.111.127.166/DSE/Daily_Station_Exits.xlsx)
- [City of San Francisco Police Department Data (CSV)](https://data.sfgov.org/api/views/wg3w-h783/rows.csv?accessType=DOWNLOAD&bom=true&format=true)

## Key Steps

The project includes the following key steps:

1. Data Preprocessing and Integration: Collect data from various sources and prepare it for analysis.

2. Data Exploration and Visualization: Explore the datasets to understand the business landscape in San Francisco and identify patterns.

3. Feature Engineering: Create relevant features for the predictive modeling.

4. Machine Learning Model Selection: Choose the appropriate machine learning algorithm (in this case, XGBoost) to predict business closures.

5. Handling Class Imbalance: Use the Synthetic Minority Over-sampling Technique (SMOTE) to balance the dataset.

6. Model Training and Evaluation: Train the XGBoost classifier and evaluate it on F1 Score and ROC AUC.

7. Classification Report and Confusion Matrix: Generate a classification report and confusion matrix to understand model performance.

8. Feature Importance: Identify the top 10 features that influence business closures the most.

## Results and Discussion

- The F1 Score for the model is approximately 0.805, indicating good accuracy.
- The ROC AUC Score is around 0.861, showing strong predictive power.
- The classification report provides a comprehensive view of the model's performance.
- The feature importance analysis reveals the top 10 features affecting business closures.

## Conclusion

This data science project sheds light on business closures in San Francisco, providing valuable insights for policymakers and entrepreneurs. The predictive model can assist in making informed decisions, and the location-based insights can guide entrepreneurs in choosing suitable locations for their businesses.

Please feel free to explore the code and data in this repository and reach out for any questions or collaborations.

## Acknowledgments

We would like to thank the City of San Francisco, the Bay Area Rapid Transport system, and the San Francisco Police Department for providing valuable datasets.

**Contributors:** [Emmanuel Sengendo]

**License:** This project is open-source under the [MIT License](LICENSE).

---

