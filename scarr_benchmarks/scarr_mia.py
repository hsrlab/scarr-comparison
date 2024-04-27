import numpy as np

import random

from scarr.engines.mia import MIA as mia
from scarr.file_handling.trace_handler import TraceHandler as th
from scarr.models.subBytes_weight import SubBytes_weight
from scarr.container.container import Container, ContainerOptions

from timeit import default_timer as timer


def ScarrMIA_p1(trace_path):

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,5000])

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 1 execution time:", end - start)


def ScarrMIA_p2(trace_path):

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,5000], byte_positions = [x for x in range(16)])

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 2 execution time:", end - start)


def ScarrMIA_p3(trace_path):

    trace_points = np.arange(0,100_000,2)

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,5000], trace_index=trace_points)

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 3 execution time:", end - start)


def ScarrMIA_p4(trace_path):

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,8674])

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 4 execution time:", end - start)


def ScarrMIA_p5(trace_path):

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,5000], trace_index=random_index)

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 5 execution time:", end - start)


def ScarrMIA_p6(trace_path):

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    handler3 = th(fileName=trace_path)#, batchStart=5000)
    model = SubBytes_weight()
    bin_num = 9
    engine3 = mia(model, bin_num)
    container3 = Container(options=ContainerOptions(engine=engine3, handler=handler3), slice=[0,5000], trace_index=random_index)

    start = timer()
    container3.run()
    end = timer()
    results3 = container3.engine.get_result()

    print("SCARR MIA Profile 6 execution time:", end - start)