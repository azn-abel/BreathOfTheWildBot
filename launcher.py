from bot import *

MISCELLANEOUS_ENABLED = True
MAP_ENABLED = True
INVENTORY_ENABLED = True
SHOP_ENABLED = True
CHEATS_ENABLED = True

if INVENTORY_ENABLED:
    from inventory import *

if SHOP_ENABLED:
    from shop import *

if MAP_ENABLED:
    from map import *

if MISCELLANEOUS_ENABLED:
    from miscellaneous import *

if CHEATS_ENABLED:
    from cheats import *

client.run(TOKEN)
