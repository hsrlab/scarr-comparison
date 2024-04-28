from timeit import default_timer as timer

import random

from lascar import *
import numpy as np
import h5py
import time


def LascarTtest_p1(trace_path0, trace_path1):

    container1 = Hdf5Container(trace_path0,
                           leakages_dataset_name="traces",
                           values_dataset_name="plaintext"
                          )
    container2 = Hdf5Container(trace_path1,
                            leakages_dataset_name="traces",
                            values_dataset_name="plaintext"
                            )
    container1.number_of_traces = 50000
    container2.number_of_traces = 50000


    def partition_function(value,):
        return None
    #!vmtouch -e husky_attack_data.h5

    ttest_engine = TTestEngine(name= "ttest_benchmark", partition_function=partition_function)
    containers = [container1, container2]

    # We choose here to plot the resulting curve
    start = timer()
    results = compute_ttest(*containers, batch_size=5000)
    end = timer()
    print("Lascar Ttest execution time:", end - start)