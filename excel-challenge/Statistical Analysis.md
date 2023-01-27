# Statistical Analysis - Excel Challenge
by Nathon Burwick

Created 1/22/2023 

## Crowdfunded Campaigns


### Three (3) Take Aways from the Data 

1. The most popular type of fundraiser are for 'Theater' productions accounting for 34.4% of the data sample. 'Theater' Productions also had one of the top 3 percentage of success per category at 54.4%, which was not too far behind 'Film & Video' (57.3% Qualitiatively) and 'Music' (56.6% Qualitatively). While the quality of success per its individual category was marginally lower than 'Film & Video' and 'Music', 'Theater' campaigns account for nearly a third (33.1%) of the overall successfull campaigns within the dataset.  

2. Diving a little deeper into the data subcategories, it appears that the sub-category Plays is the only category within the 'Theater' Parent Category. Whereas, the other top categories above have six (6) sub-categories. I believe this could possibly skew the data for 'Theater' within the set.

3. The majority of the successful campaigns had goals between '1000 to 4999' (19.4%) and the least failed (3.9%) or canceled (0.2%) campaigns overall. This goal was closely followed by '5000 to 9999' (16.6%, 12.8%, and 2.5% respectively) and 'Greater than or equal to 50000' (11.6%, 16.5%, 2.8% respectively). This is interesting because of the lower goal value may become more successful because it is likely the smaller goal is completed faster than a larger or even lofty fundraising goal. 

4. We see that the summer months (especially July) tend to be the more popular times to run a campaign, and are more likely to be successful. More research would need to be conducted on this to find out why.

### Limitations of the Data
\
Some of the limitations this data has are: 

* The size of the sample may not be completely representitive of all crowdfunded campaigns.
* Not all currency values are necessarily equal. Therefore, we cannot use this variable for a comparison between currency values without conversions being calculated first, or only compare the different categories equally by country/currency.
* There also isn't a variable to say where the platform was for the campaign. This assumes all platforms are equal in performance.
* The information within this particular data set lends itself particularly to measuring statistics with counts and percentages compared to other units of measure.
* There was no indication as to what kind of organization was running the campaign. For example, a non-profit youth summer theater camp or a for-profit technology start up.

### Other Possible Tables or Graphs and Insight

* We could make a table where we group the sub-categories within their respective parent categories to further separate potenial duplicate labels within sub-categories creating a slightly more accurate bar chart. (See Parent Category (2) in my xlsx workbook)
* Depending on the purpose of the information, we could make some of these pie charts to find what part of a categorical variable makes up the whole. For example the Parent Category to the Sub-Category, or percentage (%) of successful campaigns to the whole data set (or specific category).
* We could also create a stacked bar chart (or unstacked depending on the emphasis) for a clearer display of our data displayed by the monthly PivotTable. (See my workbook)
* We could create a stacked bar chart for the goals analysis too instead of a line graph because it provides more clear insights as too comparing the various goals and outcomes. We could even hide the lower categories and focus on the top 3-4 most common goals within the intervals of the data set. (See my workbook)

## Selecting Mean vs Median as a Data Summary Statisic

When determining the best way to summarize the data of backers_count between successful crowdfunding campaigns and failed campaigns, we must consider how the data is distributed. I see there is a high variance in the data which leads me to believe the data may contain real outliers for the size of each successful and failed tables. This could possibly cause the data to be skewed which usually leads us to believe the best summary of the data is the median (middle of the data). However, I still do not believe this particular set of data should be summarized by using the median; I would use the mean instead. While the medians of both tables are similar in their value, the count of rows in the data suggests that there is no real middle of the failed table. We can confirm this by seeing the value being the average of the two median values in the result 114.5. The average in this case would be a better summary of the data due to the difference in data size the average would help us explain the differences at scale and would lead to better decision making by the end user of our analysis. The average crowdfunded campaign which was successful had 851 people backing the campaign, while the average failed campaing had 586 backers. The difference of nearly 300 people backing the campaign would be more likely to explain what led to a successful campaign. There are limitations to consider with this analysis as well. These tables talk about the average campaign overall, and not by campaign category or sub-category. These pieces of information could lead us to a more specific analysis on predicting what attributes to a successful campaign as well.


