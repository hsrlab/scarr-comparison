from timeit import default_timer as timer

import random

import scared
import numpy as np
import h5py


def ScaredMIA_p1(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths, frame=slice(0, 5000))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 1 execution time:", end - start)


def ScaredMIA_p2(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths, frame=slice(0, 5000))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 2 execution time:", end - start)



def ScaredMIA_p3(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths[::2], frame=slice(0, 5000))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 3 execution time:", end - start)


def ScaredMIA_p4(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths, frame=range(0,8674))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 4 execution time:", end - start)


def ScaredMIA_p5(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths[random_index], frame=range(0,5000))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 5 execution time:", end - start)


def ScaredMIA_p6(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    mia = scared.MIAAttack(
        selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(words=[0]),
        model=scared.HammingWeight(),
        discriminant=scared.maxabs,
        bins_number=9)
        #convergence_step=5000)

    container = scared.Container(ths[random_index], frame=range(0,5000))

    start = timer()
    mia.run(container)
    end = timer()
    print("Scared MIA Profile 6 execution time:", end - start)

