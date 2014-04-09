# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Vanilla RPy2

# <codecell>

from rpy2 import robjects as ro

# <codecell>

ro.r.plot(range(10))

# <codecell>

ro.r.plot(ro.FloatVector(range(10)))

# <codecell>

result = ro.r["wilcox.test"](ro.FloatVector(range(5)), ro.FloatVector(range(15,20)))

# <codecell>

print result

# <codecell>

print result.names

# <codecell>

print result.rx2("p.value")

# <headingcell level=2>

# RPy2 with numpy

# <codecell>

import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()

# <codecell>

import numpy

# <codecell>

ro.r.plot(numpy.random.normal(size=6))

# <codecell>

ro.r.plot(ro.r.ecdf(numpy.arange(5)), main="", **{"do.points":False})

# <codecell>

result = ro.r["wilcox.test"](numpy.random.normal(size=6), numpy.random.normal(loc=10, size=6))

# <codecell>

print result

# <codecell>

print result.names

# <codecell>

print result[2][0]

# <codecell>

print result.rx2("p.value")

# <codecell>


# <codecell>


