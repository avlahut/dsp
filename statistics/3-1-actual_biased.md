[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Read in the response data
```python
%matplotlib inline
import chap01soln
resp = chap01soln.ReadFemResp()
```
Create pmf of the kids under 18 (`numkdhh`)
```python
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh,label='kids actual')
```
Plot the pmf
```python
import thinkplot
thinkplot.Pmfs([pmf])
thinkplot.Show(xlabel='Num Of Kids', ylabel='prob')
```
Given Bias PMF function
```python
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.
    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.
    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.
     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf
```
Compute bias pmf 
```python
bias_pmf = BiasPmf(pmf, label = 'bias pmf')
thinkplot.Pmfs([bias_pmf])
thinkplot.Show(xlabel='Num Of Kids Biased', ylabel='prob')
```
Plot two pmfs together
```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,bias_pmf])
thinkplot.Show(xlabel='kids', ylabel='PMF')
```
Calculate the means of the two distributions
```python
print(pmf.Mean())
print(bias_pmf.Mean())
```
