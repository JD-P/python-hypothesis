# See file COPYING distributed with python-hypothesis for copyright and 
# license.
import six

if six.PY2:
    from annotation import Annotation
else:
    from .annotation import Annotation
# eof
