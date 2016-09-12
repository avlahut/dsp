[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
```python
import nsfg
import math
df = nsfg.ReadFemPreg()
firsts = df[df.birthord==1]
others = df[df.birthord>1] 
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
```
```python
print(firsts.totalwgt_lb.mean())
print(others.totalwgt_lb.mean())
print("Cohen's d for weight:",CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
print("Cohen's d for preg length:",CohenEffectSize(firsts.prglngth,others.prglngth))
```
>>7.201094430437772  
>>7.325855614973262  
>>Cohen's d for weight: -0.088672927072602  
>>Cohen's d for preg length: 0.028879044654449883  

>>The mean for first babies is lower than the mean for the others which could lead one to assume that first babies are lighter than others. The Cohen's d value for this (absolute value) is .0886 which is larger than the .0288 value for pregancy length so the differentiation between firsts and others would probably be considered more significant but both seem small to me to draw any conclusion.
