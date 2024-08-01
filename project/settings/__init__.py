# from .production import *

try:
    from .local import *

except:
    pass

#this is to handle local and production files