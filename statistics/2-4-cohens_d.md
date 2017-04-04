[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> An effect size is a summary statistic intended to describe the size of an effect. 

We compute Cohen's D to quantify (or measure) the difference between two groups of data.
It is one of the ways to convey the size of the effect by comparing the difference between groups to the variability within groups ; it is defined

d = 	x_1 − x_2 / s
  
where x_1 and x_2 are the means of the groups and s is the “pooled standard deviation”. Here’s the Python code that computes Cohen’s d:
```
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
    
``` 

Effect Size(totalwgt_lb) = -0.088672927072602
Effect Size(pregnancy length) = 0.028879044654449883

In both the examples, the difference in means is very small relative to the difference in height between men and women(about 1.7 standard deviations)as described in the book.
In case of 'totalwgt_lb' however, there's a slight negative effect in the birth weight which indicates that the mean weight of the first born child is slightly lower than that of the mean weight of other children.

