# EXERCISE 3: E-COMMERCE ORDER PROCESSING

import random
import time


def get_student_inputs():
    LAST_NAME = input("Enter your last name: ").strip()
    STUDENT_ID = input("Enter your student ID: ").strip()
    FAVORITE_ARTIST = input("Enter your favorite artist: ").strip()

    digits = [int(d) for d in STUDENT_ID if d.isdigit()]

    if not LAST_NAME or not digits or not FAVORITE_ARTIST:
        raise ValueError("Please enter valid student information.")

    SEED_DIGIT = digits[-1]
    ID_SUM = sum(digits)
    NAME_LENGTH = len(LAST_NAME.replace(" ", ""))
    ARTIST_LENGTH = len(FAVORITE_ARTIST.replace(" ", ""))

    ARTIST_SUM = sum(
        ord(letter.upper()) - ord("A") + 1
        for letter in FAVORITE_ARTIST
        if letter.isalpha() and letter.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    print("\n--- STUDENT-SPECIFIC INPUTS ---")
    print("LAST_NAME:", LAST_NAME)
    print("STUDENT_ID:", STUDENT_ID)
    print("FAVORITE_ARTIST:", FAVORITE_ARTIST)
    print("SEED_DIGIT:", SEED_DIGIT)
    print("ID_SUM:", ID_SUM)
    print("NAME_LENGTH:", NAME_LENGTH)
    print("ARTIST_LENGTH:", ARTIST_LENGTH)
    print("ARTIST_SUM:", ARTIST_SUM)

    return SEED_DIGIT, ID_SUM, NAME_LENGTH, ARTIST_LENGTH, ARTIST_SUM


# BUBBLE SORT
def bubble_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0
    n = len(arr)

    for end in range(n - 1, 0, -1):
        swapped = False

        for i in range(end):
            comparisons += 1

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                movements += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, movements


# SELECTION SORT
def selection_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0
    n = len(arr)

    for i in range(n - 1):
        minimum = i

        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[minimum]:
                minimum = j

        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
            movements += 1

    return arr, comparisons, movements


# INSERTION SORT
def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                movements += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        movements += 1

    return arr, comparisons, movements


# MEASURE EXECUTION TIME
def measure_sorting(algorithm, data):
    start_time = time.perf_counter()

    sorted_data, comparisons, movements = algorithm(data)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return sorted_data, comparisons, movements, execution_time


def main():
    SEED_DIGIT, ID_SUM, NAME_LENGTH, ARTIST_LENGTH, ARTIST_SUM = (
        get_student_inputs()
    )

    # Generate the original order dataset using student inputs.
    base_orders = [
        ID_SUM + ARTIST_SUM + SEED_DIGIT + (i * 2)
        for i in range(12)
    ]

    # Use student-specific values to make the random dataset reproducible.
    random_seed = (
        ID_SUM + ARTIST_SUM + SEED_DIGIT
        + NAME_LENGTH + ARTIST_LENGTH
    )
    rng = random.Random(random_seed)

    # Create the three input conditions from the same orders.
    sorted_orders = sorted(base_orders)
    reverse_orders = sorted(base_orders, reverse=True)
    random_orders = rng.sample(base_orders, len(base_orders))

    datasets = {
        "SORTED INPUT": sorted_orders,
        "REVERSE-ORDERED INPUT": reverse_orders,
        "RANDOM INPUT": random_orders,
    }

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
    }

    print("\n======================================")
    print("E-COMMERCE ORDER PROCESSING")
    print("======================================")
    print("Generated Order Dataset:", base_orders)

    results = []

    for condition, data in datasets.items():
        print("\n======================================")
        print(condition)
        print("Input:", data)

        for algorithm_name, algorithm in algorithms.items():
            sorted_data, comparisons, movements, elapsed = (
                measure_sorting(algorithm, data)
            )

            verified = sorted_data == sorted(data)

            print("\nAlgorithm:", algorithm_name)
            print("Sorted Output:", sorted_data)
            print("Comparisons:", comparisons)
            print("Movements:", movements)
            print(f"Execution Time: {elapsed:.8f} seconds")
            print("Sorting Verification:", verified)

            results.append(
                (
                    condition,
                    algorithm_name,
                    comparisons,
                    movements,
                    elapsed,
                    verified,
                )
            )

    print("\n======================================")
    print("PERFORMANCE SUMMARY")
    print("======================================")
    print(
        f"{'Input Condition':<22}"
        f"{'Algorithm':<20}"
        f"{'Comparisons':<14}"
        f"{'Movements':<12}"
        f"{'Time (seconds)':<16}"
    )

    for condition, algorithm, comparisons, movements, elapsed, verified in results:
        print(
            f"{condition:<22}"
            f"{algorithm:<20}"
            f"{comparisons:<14}"
            f"{movements:<12}"
            f"{elapsed:<16.8f}"
        )

    print("\n======================================")
    print("BIG O ANALYSIS")
    print("======================================")
    print("Bubble Sort:")
    print("Best Case: O(n)")
    print("Average Case: O(n^2)")
    print("Worst Case: O(n^2)")

    print("\nSelection Sort:")
    print("Best Case: O(n^2)")
    print("Average Case: O(n^2)")
    print("Worst Case: O(n^2)")

    print("\nInsertion Sort:")
    print("Best Case: O(n)")
    print("Average Case: O(n^2)")
    print("Worst Case: O(n^2)")

    print("\nAuxiliary Space:")
    print("Each algorithm uses O(n) space here because it sorts a copy.")
    print("The sorting operations themselves use O(1) extra space.")

    print("\nAll sorting results verified:",
          all(result[5] for result in results))


if __name__ == "__main__":
    main()