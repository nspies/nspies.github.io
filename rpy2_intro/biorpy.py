# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Using the biorpy wrapper

# <codecell>

import collections
import numpy
import pandas
from biorpy import r, plotting

# <codecell>

# converts numpy arrays transparently
x = numpy.arange(10)
y = x + numpy.random.normal(scale=0.5, size=10)
r.plot(x, y)

# <codecell>

result = r["wilcox.test"](range(5), range(5, 10))

# <codecell>

result

# <codecell>

result.names

# <codecell>

result.py

# <codecell>

result.py.pvalue

# <codecell>

result.rx2("p.value")[0]

# <codecell>

# converts DataFrames automatically
df = pandas.DataFrame({"Stanford":numpy.random.normal(loc=56, size=114), "MIT":numpy.random.normal(loc=65, size=114)})

# <codecell>

#r.pdf("temp.pdf")
r.boxplot(df)
#r["dev.off"]()

# <codecell>

r("myfunc = function(x){print(paste('Your input:', x))}")

# <codecell>

r.myfunc("asdf");

# <headingcell level=2>

# biorpy plotting convenience functions

# <codecell>

dataset = []
for i in range(5):
    # each "sample" has mean=i
    dataset.append(numpy.random.normal(loc=i, size=30))
plotting.ecdf(dataset, ["a", "b", "c", "d", "e"], xlab="goodness", main="comparing 5 normals")

# <codecell>

dataset = collections.OrderedDict()
for i, sample in enumerate("ABCDE"):
    dataset[sample] = numpy.random.normal(loc=i)
y_lower = numpy.array(dataset.values()) - 1
y_upper = numpy.array(dataset.values()) + 1
x = plotting.barPlot(dataset, printCounts=False, ylim=[y_lower.min(), y_upper.max()])
plotting.errbars(x=x, y_lower=y_lower, y_upper=y_upper)

# <codecell>

x = numpy.arange(250)
y = x + numpy.random.normal(scale=25, size=250)
z = x + numpy.random.normal(scale=75, size=250)
df = pandas.DataFrame({"x":x, "y":y, "z":z})
plotting.scatterplotMatrix(df, main="Comparing multiple datasets")

# <codecell>

%quickref

# <codecell>


