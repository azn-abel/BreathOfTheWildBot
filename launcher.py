from bot import *

MISCELLANEOUS_ENABLED = True
MAP_ENABLED = True


if MISCELLANEOUS_ENABLED:
    from miscellaneous import *

if MAP_ENABLED:
    from map import *

client.run(TOKEN)
