[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
```python
import random
numbers = [random.random() for x in range(1000)]
```
Generate and plot pmf
```python
pmf = thinkstats2.Pmf(numbers)
thinkplot.Pmf(pmf,linewidth=.1)
thinkplot.Show(xlabel='numbers')
```
Generate and plot cdf
```python
cdf = thinkstats2.Cdf(numbers)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='numbers')
```
Because the cdf plots of a straight line, each number has the same probability and thus the distribution is uniform.
