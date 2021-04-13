# main-wall-street
Main Street vs. Wall Street:
The Geography of Corporate Capital

Authors:
Bretton, Brice, Gunjan, Jeremy, Rawaf

![image](https://user-images.githubusercontent.com/68246130/114586354-6bc3e000-9c39-11eb-8a88-a2263531bf32.png)


Our Story

Is there really such a thing as a National Economy, operating as a single entity and representing the nation as a whole? Or are nations really a collection of many diverse local and regional economies interacting with each other within a national border?

To examine these two narratives, we’ve created an interactive dashboard allowing users to explore geographic concentrations of corporate wealth in the U.S., composed of companies in the S&P 500. 

Our dashboard allows users to compare corporate market capital vs. median household income within the same state. It shows 3 visualizations: 
A US choropleth map of Median Household Income with popups
Hexbin chart of Market Capital with popups
Circle chart of Unemployment Rates with popups
And a Diamond chart of State Revenue with popups

We use PostgreSQL to serve our API. 



Research Questions

How is corporate wealth, as measured by market capital, distributed geographically across the U.S.?
--It seems that Main Street and Wall Street are not representative of each other.

How does corporate wealth compare with median household income (MHI), unemployment rates, and state revenues in the same regions? (Main Street vs. Wall Street comparison)
--While MHI is shows some variation state-to-state (eg. +/- $20k), it is much evenly spread geographically when compared to concentrations of corporate capital.



Datasets & References

Wikipedia S&P 500 / NASDAQ 100 Company headquarter locations (by city)
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
https://en.wikipedia.org/wiki/NASDAQ-100 
https://www.sec.gov/edgar.shtml 

Bureau of Labor Statistics (BLS), for the regional Consumer Price Index (CPI)
https://www.bls.gov/cpi/

Bureau of Labor Statistics (BLS), Unemployment Rates for States
https://www.bls.gov/web/laus/laumstrk.htm

SOI Tax Stats - Gross Collections, by Type of Tax and State - IRS Data Book https://www.irs.gov/statistics/soi-tax-stats-gross-collections-by-type-of-tax-and-state-irs-data-book-table-5

Median Household Income, U.S. Census Bureau, Current Population Survey, Annual Social and Economic Supplements (CPS ASEC)
https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar20.pdf

Financial data - Market Cap
Financial Data - https://www.wsj.com/market-data/quotes/AAPL/financials/annual/income-statement 

Historical Price - https://www.wsj.com/market-data/quotes/AAPL/historical-prices 

HTML5 Up https://html5up.net/

Highcharts https://www.highcharts.com/



Data Science & Visualization Bootcamp Project 2 - Group 6
Heroku deployment of UCSD Bootcamp Project 2
