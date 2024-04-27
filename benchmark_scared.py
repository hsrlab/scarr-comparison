from scared_benchmarks.scared_snr import *
from scared_benchmarks.scared_cpa import *
from scared_benchmarks.scared_mia import *
from scared_benchmarks.scared_ttest import *
from evict_file import *


def run_snr_benches(trace_path):
    evict_file(trace_path)
    ScaredSNR_p1(trace_path) 
    evict_file(trace_path)
    ScaredSNR_p2(trace_path)
    evict_file(trace_path)
    ScaredSNR_p3(trace_path)
    evict_file(trace_path)
    ScaredSNR_p4(trace_path)
    evict_file(trace_path)
    #ScaredSNR_p5(trace_path)
    print("Profile 5 skipped: see paper for details")
    evict_file(trace_path)
    print("Profile 6 skipped: see paper for details")
    #ScaredSNR_p6(trace_path) 


def run_cpa_benches(trace_path):
    evict_file(trace_path)
    ScaredCPA_p1(trace_path) 
    evict_file(trace_path)
    ScaredCPA_p2(trace_path)
    evict_file(trace_path)
    ScaredCPA_p3(trace_path)
    evict_file(trace_path)
    ScaredCPA_p4(trace_path)
    evict_file(trace_path)
    #ScaredCPA_p5(trace_path)
    print("Profile 5 skipped: see paper for details")
    evict_file(trace_path)
    print("Profile 6 skipped: see paper for details")
    #ScaredCPA_p6(trace_path) 


def run_mia_benches(trace_path):
    evict_file(trace_path)
    ScaredMIA_p1(trace_path)
    evict_file(trace_path)
    ScaredMIA_p2(trace_path) 
    evict_file(trace_path)
    ScaredMIA_p3(trace_path)
    evict_file(trace_path)
    ScaredMIA_p4(trace_path)
    evict_file(trace_path)
    #ScaredMIA_p5(trace_path) 
    print("Profile 5 skipped: see paper for details")
    evict_file(trace_path)
    print("Profile 6 skipped: see paper for details")
    #ScaredMIA_p6(trace_path)  


def run_tvla_benches(trace_path0, trace_path1):
    evict_file(trace_path0)
    evict_file(trace_path1)
    ScaredTtest_p1(trace_path0, trace_path1)


if __name__ == "__main__":
    # uncompressed trace
    uncompressed_trace_path = 'traces/benchmark_medium_sw_aes128.ets'
    # compressed trace
    compressed_trace_path = 'traces/benchmark_medium_sw_aes128.zets'
    # TVLA uncompressed traces
    uncompressed_trace_path0 = 'traces/benchmark_medium_sw_aes128-tvla0.ets'
    uncompressed_trace_path1 = 'traces/benchmark_medium_sw_aes128-tvla1.ets'
    # TVLA compressed traces
    compressed_trace_path0 = 'traces/benchmark_medium_sw_aes128-tvla0.zets'
    compressed_trace_path1 = 'traces/benchmark_medium_sw_aes128-tvla1.zets'

    print(">>> Uncompressed SCARED Benchmarks")
    # run TVLA uncompressed
    run_tvla_benches(uncompressed_trace_path0, uncompressed_trace_path1)
    # run SNR uncompressed
    run_snr_benches(uncompressed_trace_path)
    # run CPA uncompressed
    run_cpa_benches(uncompressed_trace_path)
    # run MIA uncompressed
    run_mia_benches(uncompressed_trace_path)

    print(">>> Compressed SCARED Benchmarks")
    # run TVLA compressed
    run_tvla_benches(compressed_trace_path0, compressed_trace_path1)
    # run SNR compressed
    run_snr_benches(compressed_trace_path)
    # run CPA compressed
    run_cpa_benches(compressed_trace_path)
    # run MIA compressed
    run_mia_benches(compressed_trace_path)

