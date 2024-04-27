from lascar_benchmarks.lascar_snr import * 
from lascar_benchmarks.lascar_ttest import * 

from evict_file import *

def run_snr_benches(trace_path):
    evict_file(trace_path)
    LascarSNR_p1(trace_path) 
    evict_file(trace_path)
    LascarSNR_p2(trace_path)
    evict_file(trace_path)
    LascarSNR_p3(trace_path)
    evict_file(trace_path)
    LascarSNR_p4(trace_path)
    evict_file(trace_path)
    LascarSNR_p5(trace_path)
    evict_file(trace_path)
    LascarSNR_p6(trace_path) 


def run_ttest_benches(trace_path0, trace_path1):
    LascarTtest_p1(trace_path0, trace_path1) 


if __name__ == "__main__":
    # uncompressed traces
    trace_path = 'traces/benchmark_medium_sw_aes128.h5'
    # TVLA uncompressed traces
    trace_path0 = 'traces/benchmark_medium_sw_aes128-tvla0.h5'
    trace_path1 = 'traces/benchmark_medium_sw_aes128-tvla1.h5'
    
    print(">>> Uncompressed LASCAR Benchmarks")
    # run SNR uncompressed
    run_snr_benches(trace_path)
    # run TVLA uncompressed
    run_ttest_benches(trace_path0, trace_path1)