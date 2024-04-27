from timeit import default_timer as timer

import random

import scared
import numpy as np
import h5py


def ScaredSNR_p1(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    @scared.selection_function(words=[0]) # word = byte-position
    #@scared.selection_function()
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths)

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 1 execution time:", end - start)


def ScaredSNR_p2(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    @scared.selection_function() # word = byte-position
    #@scared.selection_function()
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths)

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 2 execution time:", end - start)


def ScaredSNR_p3(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    @scared.selection_function(words=[0]) # word = byte-position
    #@scared.selection_function()
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths[::2])

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 3 execution time:", end - start)


def ScaredSNR_p4(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    @scared.selection_function(words=[0]) # word = byte-position
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths, frame=range(48739,57413))

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 4 execution time:", end - start)


def ScaredSNR_p5(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 60000)
    random_index.sort()

    @scared.selection_function(words=[0]) # word = byte-position
    #@scared.selection_function()
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths[random_index])

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 5 execution time:", end - start)


def ScaredSNR_p6(trace_path):

    ths = scared.traces.read_ths_from_ets_file(trace_path)

    random.seed(3141)

    random_index = random.sample(range(1, 100_000), 80000)
    random_index.sort()

    @scared.selection_function(words=[0]) # word = byte-position
    #@scared.selection_function()
    def identity(plaintext):
        return plaintext

    snr = scared.SNRReverse(selection_function=identity,
                            model=scared.Value())

    container = scared.Container(ths[random_index])

    start = timer()
    snr.run(container)
    end = timer()
    print("Scared SNR Profile 6 execution time:", end - start)