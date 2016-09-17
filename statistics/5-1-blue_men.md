[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```
In order to determine the distribution of men between 5'10 and 6'1, subtract the cumulative prob of 5'10 from cumlative prob of 6'1 to get the probability of a male between the two heights.
```python
dist.cdf(185.4)-dist.cdf(177.8)
```
Answer: 0.34209468294595308

Approximately 34%.
