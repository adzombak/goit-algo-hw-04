import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

small_array = [random.randint(0, 10_000) for _ in range(1_000)]
medium_array = [random.randint(0, 100_000) for _ in range(10_000)]
big_array = [random.randint(0, 100_000) for _ in range(20_000)]

insertion_time_small = timeit.Timer(lambda: insertion_sort(small_array)).timeit(number=3)
merge_time_small = timeit.Timer(lambda: merge_sort(small_array)).timeit(number=3)
timsorted_time_small = timeit.Timer(lambda: sorted(small_array[:])).timeit(number=3)
timsort_time_small = timeit.Timer(lambda: small_array[:].sort()).timeit(number=3)

insertion_time_medium = timeit.Timer(lambda: insertion_sort(medium_array)).timeit(number=3)
merge_time_medium = timeit.Timer(lambda: merge_sort(medium_array)).timeit(number=3)
timsorted_time_medium = timeit.Timer(lambda: sorted(medium_array[:])).timeit(number=3)
timsort_time_medium = timeit.Timer(lambda: medium_array[:].sort()).timeit(number=3)

insertion_time_big = timeit.Timer(lambda: insertion_sort(big_array)).timeit(number=3)
merge_time_big = timeit.Timer(lambda: merge_sort(big_array)).timeit(number=3)
timsorted_time_big = timeit.Timer(lambda: sorted(big_array[:])).timeit(number=3)
timsort_time_big = timeit.Timer(lambda: big_array[:].sort()).timeit(number=3)

print(f"| {'Algorithm':<20} | {'Time of small array':<20} | {'Time of medium array':<20} | {'Time of big array':<20} | "
      f"{'Relation to Timsort (Big array)':<35} |")
print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*35} |")
print(f"| {'Insertion sort':<20} | {insertion_time_small:20.5f} | {insertion_time_medium:20.5f} | "
      f"{insertion_time_big:20.5f} | {insertion_time_big / timsort_time_big:35.5f} |")
print(f"| {'Merge sort':<20} | {merge_time_small:20.5f} | {merge_time_medium:20.5f} | {merge_time_big:20.5f} | "
      f"{merge_time_big / timsort_time_big:35.5f} |")
print(f"| {'Timsorted':<20} | {timsorted_time_small:20.5f} | {timsorted_time_medium:20.5f} | "
      f"{timsorted_time_big:20.5f} | {timsorted_time_big / timsort_time_big:35.5f} |")
print(f"| {'Timsort':<20} | {timsort_time_small:20.5f} | {timsort_time_medium:20.5f} | {timsort_time_big:20.5f} | "
      f"{timsort_time_big / timsort_time_big:35.5f} |")
