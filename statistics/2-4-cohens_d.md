[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> An effect size is a summary statistic intended to describe the size of an effect. For example, to describe the difference between two groups, one obvious choice is the difference in the means.

Mean pregnancy length for first babies is 38.601; for other babies it is 38.523. The difference is 0.078 weeks, which works out to 13 hours. As a fraction of the typical pregnancy length, this difference is about 0.2%.

If we assume this estimate is accurate, such a difference would have no practical consequences. In fact, without observing a large number of pregnancies, it is unlikely that anyone would notice this difference at all.

Another way to convey the size of the effect is to compare the difference between groups to the variability within groups. Cohen’s d is a statistic intended to do that; it is defined
```
d = 	x_1 − x_2 / s
  
where x_1 and x_2 are the means of the groups and s is the “pooled standard deviation”. Here’s the Python code that computes Cohen’s d:
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

