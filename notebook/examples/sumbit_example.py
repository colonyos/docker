import os
import random

from termcolor import cprint 

from pycolonies import Colonies
from pycolonies import colonies_client
from pycolonies import func_spec

colonies, colonyid, colony_prvkey, executorid, executor_prvkey = colonies_client()

snapshotname = str(random.randint(0,9**60))
snapshot = colonies.create_snapshot(colonyid, "src", snapshotname, executor_prvkey)
f = func_spec(func="execute",
              args=[],
              kwargs={
                "cmd":"python3",
                "args":["/tmp/classifier/classifier.py"],
                "keep_snapshots": False
              },
              fs=[ 
                  {
                    "label": "src",
                    "snapshotid": snapshot["snapshotid"],
                    "dir": "/tmp/classifier"
                  }
              ],
              colonyid=colonyid,
              executortype="gpu-mlexecutor",
              priority=0,
              maxexectime=100,
              maxretries=3,
              maxwaittime=-1)

process = colonies.submit(f, executor_prvkey)
colonies.get_process(process["processid"], executor_prvkey)

for l in colonies.get_process_log(process["processid"], 500, -1, executor_prvkey):
    cprint(l["message"], end="")


