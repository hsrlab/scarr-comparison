from timeit import default_timer as timer

import random

import scared
import numpy as np
import h5py


def ScaredTtest_p1(trace_path0, trace_path1):

    ths0 = scared.traces.read_ths_from_ets_file(trace_path0)
    ths1 = scared.traces.read_ths_from_ets_file(trace_path1)

    tcontainer = scared.TTestContainer(ths_1=ths0, ths_2=ths1)

    # Create a container for your ths
    ttest = scared.TTestAnalysis(precision='float32')

    start = timer()
    ttest.run(tcontainer)
    end = timer()
    print("Scared TVLA Profile 1 execution time:", end - start)
