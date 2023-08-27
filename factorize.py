import time
import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def parallel_factorize(number):
    num_cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(num_cores) as pool:
        factors = pool.map(factorize, range(1, number + 1))
    return factors

def main():
    numbers = [128, 255, 99999, 10651060]
    results_sync = []
    results_parallel = []

    # Вимірювання часу для синхронної версії
    start_time_sync = time.time()

    for number in numbers:
        result = factorize(number)
        results_sync.append(result)

    end_time_sync = time.time()

    print("Results (Sync):", results_sync)
    print("Time taken (Sync):", end_time_sync - start_time_sync, "seconds")

    # Вимірювання часу для паралельної версії
    start_time_parallel = time.time()

    for number in numbers:
        result = parallel_factorize(number)
        results_parallel.append(result)

    end_time_parallel = time.time()

    print("Results (Parallel):", results_parallel)
    print("Time taken (Parallel):", end_time_parallel - start_time_parallel, "seconds")

if __name__ == "__main__":
    main()