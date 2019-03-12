# NYC Rent Analyzer: Predicting Aparment Pricing in NYC
This is a project for Introduction to Machine Learning course in CCNY by Erik Grimmelmann.

## Introduction
### Goal
To predict where to rent an apartment in NYC by asking the user's budget and needs.

### Motivation
In this project, we will utilize Machine Learning algorithms to help consumers decide where to find their next apartment by predicting their prices. The user can input features such as # of bathrooms, # of bedrooms, price, and size. Then, the algorithm can narrow down their search by outputting which borough they should start looking. With the use of Machine Learning, we can also see how each borough differs from one another in terms of pricing.

## Data Collection
Before starting the project, we must know what kind of data that we can use. Tons of data are available online but some of them are not updated. Therefore, scraping recent apartment listings from [StreetEasy](https://streeteasy.com) was the solution. By using BeautifulSoup and Python, I went through all the listings in NYC and gathered these features:
* Number of bedrooms
* Number of bathrooms
* Size in sqft.
* Price
* Borough

[rent.csv](./rent.csv) shows how the dataset looks like.

### Potential Problems with the dataset
* By observing the data I gathered, the algorithm might favor other boroughs since they have more listings, therefore I limited each to have 100 entries each. [rent_bak.csv](./rent_bak.csv) shows the raw data gathered.
* There was not enough listings in Staten Island so I removed the borough.

## Applying Machine Learning Algorithms to the Dataset
By showing the accuracy of each algorithm, we can have an idea on how well they can predict the fed data. Each algorithm will have 70% train data and 30% test data. I will be using these:
* Linear Regression
* Logistic Regression
* SVM
* Decision Tree with AdaBoost
* Random Forests

[Project.ipynb](./Project.ipynb) shows the code and exact results. There are also figures that are helpful in visualizing the data. 

## Conclusion and Findings
### Linear Regression
* As expected, Linear Regression performed poorly since most of our data are not really correlated with each other.
* It is interesting to see that SVR performed better (22%) than others (6%)
* The accuracy that we got is very low. Therefore, we cannot use Linear Regression (22% highest accuracy).

### Logistic Regression
* I expected Logistic Regression to have better results than linear regression since our dataset is categorical in nature. (Bronx, Brooklyn, Manhattan, Queens)
* Without scaling, the algorithm actually gives correct prediction 67% of the time. Although it is recommended to use StandardScaler() for Logistic Regression.

### SVM
* For SVM, I used three kernels: linear (80%), RBF (79%), and Sigmoid (20%)
* I expected SVM to also do well since we can use the correct kernel and adjust the parameters (gamma) to get better results.

### Decision Tree with AdaBoost
* AdaBoosting had a score of 74% which is better than I expected. The algorithm does not learn the data completely (25% error)
* Without AdaBoosting, Decision Trees performed 73%

### Random Forests
* The way Random Forests work is very similar to decision trees. However, I expected it to be a little better since DT tend to over fit. Random forests prevents overfitting by combining series of subsets with DT.
* However, we adjusted our data beforehand and it’s not overfitting. Therefore it showed similar score of 74%

## Other things that I learned
* In addition to ML, I learned a lot of things about Data Science and importance of having the right data. Without the right data, our Machine Learning algorithms will yield bad results or worse, it won’t even be applied. I understand now what my mentor from an internship told me: “Data is hard to find. We would pay a good amount of money to get useful data.”
* I also learned that applying Scikit Learn basic Machine Learning algorithms is not tedious after optimizing your data.
