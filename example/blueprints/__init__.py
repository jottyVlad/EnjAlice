from .blueprint1 import bp as bp1
from .blueprint2 import bp as bp2

bps = [bp1, bp2]

# or you can use
bp = bp1 + bp2

# or similarly
# bp = bp1.add(bp2)
