from timeit import default_timer as timer

import random

from lascar import *
import numpy as np
import h5py
import time

# "husky_attack_data.h5"

def LascarSNR_p1(trace_path):

    container = Hdf5Container(trace_path,
                           leakages_dataset_name="traces",
                           values_dataset_name="metadata"
                          )

    def partition_function(
        value,
    ):  # partition_function must take 1 argument: the value returned by the container at each trace
        return value["plaintext"][3] # here we partition on the value of the 3rd plaintext byte

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engine = SnrEngine(
        partition_function, range(number_of_partitions), name="snr_benchmark"
    )

    # We choose here to plot the resulting curve
    session = Session(
        container, engine=snr_engine, progressbar=True
    )

    start = timer()
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 1 execution time:", end - start)


def LascarSNR_p2(trace_path):

    container = Hdf5Container(trace_path,
                           leakages_dataset_name="traces",
                           values_dataset_name="metadata"
                          )
    # container.number_of_traces = 100000

    def get_partition_function(byte):
        def partition_function(
            value,
        ):  # partition_function must take 1 argument: the value returned by the container at each trace
            return value["plaintext"][
                byte
            ]  # here we partition on the value of the 3rd plaintext byte

        return partition_function

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engines = [
        SnrEngine(
            get_partition_function(i), range(number_of_partitions), name="snr_plaintext_%d" % i
        )
        for i in range(16)
    ]

    # We choose here to plot the resulting curve
    session = Session(
        container,
        engines=snr_engines,
        output_method=DictOutputMethod(*snr_engines),
    )

    start = timer()
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 2 execution time:", end - start)


def LascarSNR_p3(trace_path):

    container = Hdf5Container(trace_path,
                           leakages_dataset_name="traces",
                           values_dataset_name="metadata")#,
                           
                          #leakage_section=poi)
    # container.number_of_traces = 100000

    def partition_function(
        value,
    ):  # partition_function must take 1 argument: the value returned by the container at each trace
        return value["plaintext"][3] # here we partition on the value of the 3rd plaintext byte

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engine = SnrEngine(
        partition_function, range(number_of_partitions), name="snr_benchmark"
    )

    # We choose here to plot the resulting curve


    start = timer()
    session = Session(
        container[::2], engine=snr_engine, output_method=DictOutputMethod(snr_engine)
    )
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 3 execution time:", end - start)


def LascarSNR_p4(trace_path):

    poi = np.arange(48739,57413,1)

    container = Hdf5Container(trace_path,
                            leakages_dataset_name="traces",
                            values_dataset_name="metadata",
                            leakage_section=poi)
    # container.number_of_traces = 100000

    def partition_function(
        value,
    ):  # partition_function must take 1 argument: the value returned by the container at each trace
        return value["plaintext"][3] # here we partition on the value of the 3rd plaintext byte

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engine = SnrEngine(
        partition_function, range(number_of_partitions), name="snr_benchmark"
    )

    # We choose here to plot the resulting curve


    start = timer()
    session = Session(
        container[::2], engine=snr_engine, output_method=DictOutputMethod(snr_engine)
    )
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 4 execution time:", end - start)


def LascarSNR_p5(trace_path):

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    #poi = np.arange(48739,57413,1)

    container = Hdf5Container(trace_path,
                            leakages_dataset_name="traces",
                            values_dataset_name="metadata")#,
                            #leakage_section=poi)
                            
    # container.number_of_traces = 100000

    def partition_function(
        value,
    ):  # partition_function must take 1 argument: the value returned by the container at each trace
        return value["plaintext"][3] # here we partition on the value of the 3rd plaintext byte

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engine = SnrEngine(
        partition_function, range(number_of_partitions), name="snr_benchmark"
    )

    # We choose here to plot the resulting curve


    start = timer()
    session = Session(
        container[random_index], engine=snr_engine, output_method=DictOutputMethod(snr_engine)
    )
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 5 execution time:", end - start)


def LascarSNR_p6(trace_path):
    
    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    #poi = np.arange(48739,57413,1)

    container = Hdf5Container(trace_path,
                            leakages_dataset_name="traces",
                            values_dataset_name="metadata")#,
                            #leakage_section=poi)
    # container.number_of_traces = 100000

    def partition_function(
        value,
    ):  # partition_function must take 1 argument: the value returned by the container at each trace
        return value["plaintext"][3] # here we partition on the value of the 3rd plaintext byte

    #!vmtouch -e husky_attack_data.h5

    number_of_partitions = 256  # number of possible classes (~output of the partiton_function) for the partition_function
    snr_engine = SnrEngine(
        partition_function, range(number_of_partitions), name="snr_benchmark"
    )

    # We choose here to plot the resulting curve


    start = timer()
    session = Session(
        container[random_index], engine=snr_engine, output_method=DictOutputMethod(snr_engine)
    )
    session.run(batch_size=5000)
    end = timer()
    print("Lascar SNR Profile 6 execution time:", end - start)