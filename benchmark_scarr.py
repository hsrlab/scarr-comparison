from scarr_benchmarks.scarr_snr import *
from scarr_benchmarks.scarr_cpa import *
from scarr_benchmarks.scarr_mia import *
from scarr_benchmarks.scarr_ttest import *
from evict_file import *


def run_snr_benches(trace_path):
    evict_file(trace_path)
    ScarrSNR_p1(trace_path)
    evict_file(trace_path)
    ScarrSNR_p2(trace_path)
    evict_file(trace_path)
    ScarrSNR_p3(trace_path)
    evict_file(trace_path)
    ScarrSNR_p4(trace_path)
    evict_file(trace_path)
    ScarrSNR_p5(trace_path)
    evict_file(trace_path)
    ScarrSNR_p6(trace_path)


def run_cpa_benches(trace_path):
    evict_file(trace_path)
    ScarrCPA_p1(trace_path)
    evict_file(trace_path)
    ScarrCPA_p2(trace_path)
    evict_file(trace_path)
    ScarrCPA_p3(trace_path)
    evict_file(trace_path)
    ScarrCPA_p4(trace_path)
    evict_file(trace_path)
    ScarrCPA_p5(trace_path)
    evict_file(trace_path)
    ScarrCPA_p6(trace_path)


def run_mia_benches(trace_path):
    evict_file(trace_path)
    ScarrMIA_p1(trace_path)
    evict_file(trace_path)
    ScarrMIA_p2(trace_path)
    evict_file(trace_path)
    ScarrMIA_p3(trace_path)
    evict_file(trace_path)
    ScarrMIA_p4(trace_path)
    evict_file(trace_path)
    ScarrMIA_p5(trace_path)
    evict_file(trace_path)
    ScarrMIA_p6(trace_path)


def run_ttest_benches(trace_path0, trace_path1):
    evict_file(trace_path0)
    evict_file(trace_path1)
    ScarrTtest_p1(trace_path0, trace_path1)


if __name__ == "__main__":
    # uncompressed trace
    uncompressed_trace = 'traces/benchmark_medium_sw_aes128.zarr'
    # compressed trace
    compressed_trace = 'traces/benchmark_medium_sw_aes128_compressed.zarr'
    # TVLA uncompressed
    uncompressed_trace_path0 = 'traces/benchmark_medium_sw_aes128-tvla0.zarr'
    uncompressed_trace_path1 = 'traces/benchmark_medium_sw_aes128-tvla1.zarr'
    # TVLA compressed
    compressed_trace_path0 = 'traces/benchmark_medium_sw_aes128-tvla0_compressed.zarr'
    compressed_trace_path1 = 'traces/benchmark_medium_sw_aes128-tvla1_compressed.zarr'
    
    print(">>> Uncompressed SCARR Benchmarks")
    # run uncompressed TVLA
    run_ttest_benches(uncompressed_trace_path0, uncompressed_trace_path1)
    # run uncompressed SNR
    run_snr_benches(uncompressed_trace)
    # run uncompressed CPA
    run_cpa_benches(uncompressed_trace)
    # run uncompressed MIA
    run_mia_benches(uncompressed_trace)

    print(">>> Compressed SCARR Benchmarks")
    # run compressed TVLA
    run_ttest_benches(compressed_trace_path0, compressed_trace_path1)
    # run compressed SNR
    run_snr_benches(compressed_trace)
    # run compressed CPA
    run_cpa_benches(compressed_trace)
    # run compressed MIA
    run_mia_benches(compressed_trace)
