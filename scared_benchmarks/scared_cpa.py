from timeit import default_timer as timer

import random

import scared
import numpy as np
import h5py


def ScaredCPA_p1(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    cpa = scared.CPAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths)

    start = timer()
    cpa.run(container)
    end = timer()
    print("Scared CPA Profile 1 execution time:", end - start)


def ScaredCPA_p2(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    cpa = scared.CPAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths)

    start = timer()
    cpa.run(container)
    end = timer()
    print("Scared CPA Profile 2 execution time:", end - start)


def ScaredCPA_p3(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    cpa = scared.CPAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths[::2])

    start = timer()
    cpa.run(container)
    end = timer()
    print("Scared CPA Profile 3 execution time:", end - start)


def ScaredCPA_p4(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    cpa = scared.CPAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths, frame=range(48739,57413))

    start = timer()
    cpa.run(container)
    end = timer()
    print("Scared CPA Profile 4 execution time:", end - start)


def ScaredCPA_p5(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    # Create an analysis CPA
    cpa = scared.CPAAttack(
            selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
            model=scared.HammingWeight(),
            discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths[random_index])

    start = timer()
    cpa.run(container)
    end = timer()
    print("Scared CPA Profile 5 execution time:", end - start)


def ScaredCPA_p6(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    # Create an analysis CPA
    cpa = scared.CPAAttack(
            selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
            model=scared.HammingWeight(),
            discriminant=scared.maxabs)

    # Create a container for your ths
    container = scared.Container(ths[random_index])

    start = timer()
    cpa.run(container)
    end = timer()    
    print("Scared CPA Profile 6 execution time:", end - start)