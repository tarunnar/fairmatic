Instacart Data Analysis
Instacart has open-sourced sample data about user purchases on its platform. Use their dataset to generate a report that shows the most popular Departments purchased from, segmented by the hour for every day of the week.
Example report output:
Day 0:
Hour 0:
1. Frozen (20%)
2. Bakery (15%)
...
21. Pets (0%)
Hour 1:
1. Bakery (19%)
...
Hour 23:
1. Bakery (19%)
...
Day 1:
Hour 0:
1. Frozen (19%)
...
...
Day 6:
Hour 0:
1. Alcohol (20%)
Dataset: https://www.dropbox.com/s/1ao72uiciov4uxc/instacart_online_grocery_shopping_2017_05_01.tar.gz?dl=0
Definitions: https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b
Instacart’s data is a set of CSVs. You should inspect them and determine how each table is related to each other in order to generate the report.
Additionally, any given user shouldn’t inflate the data for a given hour, say “User A” buys from the Frozen department multiple times in hour 10, then it shouldn’t inflate the Frozen department percentage for that hour.
Considerations:
You can use any programming language. You can use any open-source libraries, however, any computations and logic must be performed by your code (i.e. no use of SQL, pandas etc)
Your program should be written in a way where you can easily demonstrate that it works correctly.
Make sure to check out the data definitions in the link above that describes CSV files
Free to use any resources or references online.
