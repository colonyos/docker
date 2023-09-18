import os

from pycolonies import Colonies
from pycolonies import func_spec

colonies_server = os.getenv("COLONIES_SERVER_HOST")
colonies_port = os.getenv("COLONIES_SERVER_PORT")
colonies_tls = os.getenv("COLONIES_SERVER_TLS")
colonyid = os.getenv("COLONIES_COLONY_ID")
colony_prvkey = os.getenv("COLONIES_COLONY_PRVKEY")
executorid = os.getenv("COLONIES_EXECUTOR_ID")
executor_prvkey = os.getenv("COLONIES_EXECUTOR_PRVKEY")

if colonies_tls == "true":
  url = "https://" + colonies_server + ":" + colonies_port
  colonies = Colonies(colonies_server, colonies_port, True)
else:
  url = "http://" + colonies_server + ":" + colonies_port
  colonies = Colonies(colonies_server, colonies_port, False)

print("url:", url)
print("colonyid:", colonyid)
print("colony_prvkey:", colony_prvkey)
print("executorid:", executorid)
print("executor_prvkey:", executor_prvkey)

colonies.list_executors(colonyid, "c552e7f91157c1c5b30c84e8b26ef20f44f1f15f3c95454740b6e9ce59e05807")
