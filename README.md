# Election_Analysis
### Background
#### We were tasked with analyzing election audit results. Specifically, we were to determine the winner of an election using voter information including: the ballot id, the county, and the candidate receiving the vote. We analyzed and presented this data in text files using python. We also determined the voter turnout by county, the percentage of votes from each county, the county with the greatest voter turnout, and we created a visualization showing the votes per candidate per county.
### Election Audit Analysis
![votes](https://github.com/shaneabbley/Election_Analysis/blob/main/ElectionResults.png)
#### We counted a total of 369,711 ballots in three counties for three candidates.
#### * Counties
   * Jefferson County had 38,855 ballots for 10.5% of the total votes.
   * Arapahoe County had 24,801 ballots for 6.7% of the total votes.
   * Denver County had the most voters. They cast 306,055 ballots for 82.8% of the total votes.
#### * Candidates
   * Raymon Anthony Doane received 11,606 votes for 3.1% of the total votes.
   * Charles Casper Stockham received 85,213 votes for 23.0% of the total votes.
   * Diana Degette received the most votes! She had 272,892 or 73.8% of the total votes.
### Discussion
#### As seen in the results above, this script is ready to be utilized to simplify the audits of other elections. In order to make this happen, I would make a few small modifications. First, I would decrease the number of looping statements to make this script run even faster for larger data sets. At the moment there are multiple loops that can most likely be simplified or optimized. I would also attempt to make the visualization generate from any desired election data. At the moment the visualization only works for this specific data.
