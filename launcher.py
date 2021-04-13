from bot import *

MISCELLANEOUS_ENABLED = True
MAP_ENABLED = True
INVENTORY_ENABLED = True

if INVENTORY_ENABLED:
    from inventory import *

if MAP_ENABLED:
    from map import *

if MISCELLANEOUS_ENABLED:
    from miscellaneous import *

client.run(TOKEN)
