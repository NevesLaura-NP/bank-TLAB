# README

Credit to the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) for this template. To complete this project, delete all template text (save for the headers) and fill in your own information.

## Project Intro/Objective
The purpose of this project is to continue a pipeline in Python to analyse stock data. We aim to integrate it with daily news headline data to measure how reliably sentiment analysis can predict stock prices. Due to stocks being heavily influenced by investors sentiments upon economy and the market, a sentiment analysis could offer new variables of prediction for updated stock prices leading to greater opportunities for profit.

### Methods Used
* Predictive Modeling

### Technologies
* Python
* Jupyter

## Project Description
Our current sample dataset contains 9 weeks of Amazon stock prices. We currently are able to create classes that can measure the mean, median and standart deviation of the stock prices. Due to the first columns of the rows being dates, the StockMetrics code skips the first columns. For the sake of accuracy we also skip the empty values in rows. Once values are transformed into floats we make required caculations for each class and store the final values into a list. At last, we can trace the week in which the prices were most affected through the comparison of the standard deviation with median and mean of prices. 