# Usage of non-relational databases

## Perform calculations

The [Coca Cola Co spreadsheet](CocaColaCo.xlsx) is missing some calculations. Your task is to: 

1. Calculate the Gross profits of FY '15, '16, '17, and '18
    - Gross Profit = Net Operating revenues - Cost of goods sold
1. Calculate the average of all the gross profits. Try to do this with a function.
    - Average = Sum of gross profits divided by the number of fiscal years (10)
    - Documentation on the [AVERAGE function](https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)
1. This is an Excel file, but it should be editable in any spreadsheet platform

[Data source credit to Yiyi Wang](https://www.kaggle.com/yiyiwang0826/cocacola-excel)

## Rubric

Exemplary | Adequate | Needs Improvement
--- | --- | -- |



## 🚀 Model reality


There is a `TwitterData.json` file that you can upload to the SampleDB database. It's recommended that you add it to a separate container. This can be done by:

1. Clicking the new container button in the top right
1. Selecting the existing database (SampleDB) creating a container id for the container
1. Setting the partition key to `/id`
1. Clicking OK (you can ignore rest of the information in this view as this is a small dataset running locally on your machine)
1. Open your new container and upload the Twitter Data file with `Upload Item` button

Try to run a few select queries to find the documents that have Microsoft in the text field. Hint: try to use the [LIKE keyword](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)

