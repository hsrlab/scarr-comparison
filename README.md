# SCARR CHES 2024 Artifact (Benchmarks)

This repository contains the benchmarks for the archival version of our corresponding CHES 2024 artifact.

* The archival/artifact version of our software SCARR can be found [here](https://github.com/hsrlab/scarr).
* The active development version of our software SCARR can be found [here](https://github.com/decryptofy/scarr).

To run these benchmarks, we assume Ubuntu 22.04 LTS as host OS which enjoys support until April 2032 (standard security maintenance). Additionally, the following software must be installed:

```
sudo apt install build-essential python3.10 python3-virtualenv python-is-python3 git vmtouch
```

# Usage Warning

Some benchmarks can push your hardware to its limits and beyond. Caution is advised when running sustained compute loads as many consumer-grade hardware is not made for this.

# Install CHES 2024 Artifact (Benchmarks)

Simply clone this repository:

```
git clone https://github.com/hsrlab/scarr-comparison.git
```

# Getting Started

Please download all trace files individually from [here](https://oregonstate.box.com/s/hxfhekjpgxyoc5ce3e0cy93l8lrcc5wo) and store them in the subdirectory 'traces'. Zarr data sets are directories and must be extracted from the .zarr.tar files first. All traces combined are approx. 120 GB and you may choose to only download the trace files needed for a particular software framework.

# Running a Benchmark

To run a benchmark, take a look at the Makefile. The main targets for running the benchmark are: lascar, scarr, scared. In other words:

```
make lascar
```

will run the benchmark for Lascar. Whereas:

```
make scared
```

and

```
make scarr
```

will run the benchmarks for these frameworks.

# Benchmark Profiles

These benchmarks enable reproducibility of the results in the paper. More precisely:

* Lascar
    * TVLA (Profile 1)
    * SNR (all profiles)
* SCARED
    * TVLA (Profile 1)
    * SNR (all profiles)
    * CPA (all profiles)
    * MIA (all profiles)
* SCARR
    * TVLA (Profile 1)
    * SNR (all profiles)
    * CPA (all profiles)
    * MIA (all profiles)

A description of these profiles is included in our paper. In the paper, you can also find the explanation as to why Profile 5 and Profile 6 for SCARED are not performed. Once you familiarized yourself with the specifics of these profiles, and executed the benchmark once, you may adjust the benchmark such that multiple iterations of these tests are performed.

Before each profile is executed, the corresponding file is evicted from memory to ensure that data is indeed read from disk. In addition, before/after each test, there is a 60s sleep delay to allow for heat to dissipate.

Running the benchmarks for a single framework, e.g., SCARED, can easily take up to 1h.
