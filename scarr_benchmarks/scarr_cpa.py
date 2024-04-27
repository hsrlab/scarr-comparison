import numpy as np

import random

from scarr.engines.cpa import CPA as cpa
from scarr.file_handling.trace_handler import TraceHandler as th
from scarr.models.subBytes_weight import SubBytes_weight
from scarr.container.container import Container, ContainerOptions

from timeit import default_timer as timer


def ScarrCPA_p1(trace_path):

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2))

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 1 execution time:", end - start)


def ScarrCPA_p2(trace_path):

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2), byte_positions = [x for x in range(16)])

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 2 execution time:", end - start)


def ScarrCPA_p3(trace_path):

    trace_points = np.arange(0,100_000,2)

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2), Async=True, trace_index=trace_points)

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 3 execution time:", end - start)


def ScarrCPA_p4(trace_path):

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2), Async=True, slice=[48739,57413])

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 4 execution time:", end - start)


def ScarrCPA_p5(trace_path):

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2), Async=True, trace_index=random_index)

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 5 execution time:", end - start)


def ScarrCPA_p6(trace_path):

    
    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    handler2 = th(fileName=trace_path) #, batchSize=10000)#, batchStart=5000)
    model = SubBytes_weight()
    engine2 = cpa(model)
    container2 = Container(options=ContainerOptions(engine=engine2, handler=handler2), Async=True, trace_index=random_index)

    start = timer()
    container2.run()
    end = timer()
    results2 = container2.engine.get_result()

    print("SCARR CPA Profile 6 execution time:", end - start)