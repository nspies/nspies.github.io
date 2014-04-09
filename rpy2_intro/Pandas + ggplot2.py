# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import rpy2.robjects
from collections import OrderedDict
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()

py2ri_orig = rpy2.robjects.conversion.py2ri
def conversion_pydataframe(obj):
    if isinstance(obj, pandas.core.frame.DataFrame):
        od = OrderedDict()
        for name, values in obj.iteritems():
            if values.dtype.kind == 'O':
                od[name] = rpy2.robjects.vectors.StrVector(values)
            else:
                od[name] = rpy2.robjects.numpy2ri.numpy2ri(values.values)
        return rpy2.robjects.vectors.DataFrame(od)
    elif isinstance(obj, pandas.core.series.Series):
        # converted as a numpy array
        res = py2ri_orig(obj) 
        # "index" is equivalent to "names" in R
        if obj.ndim == 1:
            res.names = ListVector({'x': ro.conversion.py2ri(obj.index)})
        else:
            res.dimnames = ListVector(ro.conversion.py2ri(obj.index))
        return res
    else:
        return py2ri_orig(obj) 
rpy2.robjects.conversion.py2ri = conversion_pydataframe

# <codecell>

import pandas

# <codecell>

import rpy2.robjects.lib.ggplot2 as ggplot2

# <codecell>

df = pandas.DataFrame({"a":range(10), "b":range(10,20)})

# <codecell>

pp = ggplot2.ggplot(df) + ggplot2.aes_string(x="a", y="b") + ggplot2.geom_point()
pp.plot()

# <codecell>


