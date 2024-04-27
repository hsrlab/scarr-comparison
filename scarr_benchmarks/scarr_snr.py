import numpy as np

import random

from scarr.engines.snr import SNR as snr
from scarr.file_handling.trace_handler import TraceHandler as th
from scarr.container.container import Container, ContainerOptions

from timeit import default_timer as timer


def ScarrSNR_p1(trace_path):

    handler = th(fileName=trace_path)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True)

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()

    print("SCARR SNR Profile 1 execution time:", end - start)


def ScarrSNR_p2(trace_path):
    handler = th(fileName=trace_path)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True, byte_positions = [x for x in range(16)])

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()

    print("SCARR SNR Profile 2 execution time:", end - start)


def ScarrSNR_p3(trace_path):
    trace_points = np.arange(0,100_000,2)

    handler = th(fileName=trace_path)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True, trace_index=trace_points)

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()
    print("SCARR SNR Profile 3 execution time:", end - start)


def ScarrSNR_p4(trace_path):
    handler = th(fileName=trace_path)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True, slice=[48739,57413])

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()
    print("SCARR SNR Profile 4 execution time:", end - start)


def ScarrSNR_p5(trace_path):
    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    handler = th(fileName=trace_path)#, batchStart=5000)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True, trace_index=random_index)

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()
    print("SCARR SNR Profile 5 execution time:", end - start)


def ScarrSNR_p6(trace_path):
    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    handler = th(fileName=trace_path)#, batchStart=5000)
    engine = snr()
    container = Container(options=ContainerOptions(engine=engine, handler=handler), Async=True, trace_index=random_index)

    start = timer()
    engine.run(container)
    end = timer()
    results = engine.get_result()
    print("SCARR SNR Profile 6 execution time:", end - start)
