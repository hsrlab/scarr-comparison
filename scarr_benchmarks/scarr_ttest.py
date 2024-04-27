import numpy as np

import random

from scarr.engines.ttest import Ttest as ttest
from scarr.file_handling.trace_handler import TraceHandler as th
from scarr.container.container import Container, ContainerOptions

from timeit import default_timer as timer


def ScarrTtest_p1(trace_path0, trace_path1):

    handler1 = th(fileName=trace_path0, batchSize=5000)
    #handler1 = th(fileName='zarr-converted-tvla0_compressed.zarr', batchSize=5000)
    handler2 = th(fileName=trace_path1, batchSize=5000)
    #handler2 = th(fileName='zarr-converted-tvla1_compressed.zarr', batchSize=5000)

    engine = ttest()
    container = Container(options=ContainerOptions(engine=engine, handler=handler1, handler2=handler2), Async = False)#, stride=10, slice=[0,50000])# byte_positions = [x for x in range(16)])

    start = timer()
    engine.run(container)
    end = timer()
    print("SCARR TVLA Profile 1 execution time:", end - start)