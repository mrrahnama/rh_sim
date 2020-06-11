welcome to this repp..
you should install mesa 
pip install mesa

then run server.py

if you have python 3.8 on windows you will see some error about asyncio 
Change the end part of the file %USERNAME%\AppData\Local\Programs\Python\Python38\Lib\asyncio\__init__.py

From
-----------------------------------------------
if sys.platform == 'win32':  # pragma: no cover
    from .windows_events import *
    __all__ += windows_events.__all__
else:
    from .unix_events import *  # pragma: no cover
    __all__ += unix_events.__all__
-----------------------------------------------
TO
-----------------------------------------
import asyncio

if sys.platform == 'win32':
    from .windows_events import *
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    __all__ += windows_events.__all__
else:
    from .unix_events import *  # pragma: no cover
    __all__ += unix_events.__all__
----------------------------------------------