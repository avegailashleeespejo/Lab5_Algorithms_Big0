# EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH

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

    return SEED_DIGIT, ID_SUM, ARTIST_SUM


def binary_search_rotated(data, target):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2

        comparisons += 1
        if data[mid] == target:
            return mid, comparisons

        comparisons += 1
        if data[left] <= data[mid]:
            comparisons += 1
            if data[left] <= target < data[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            comparisons += 1
            if data[mid] < target <= data[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1, comparisons


def linear_search(data, target):
    comparisons = 0

    for index in range(len(data)):
        comparisons += 1

        if data[index] == target:
            return index, comparisons

    return -1, comparisons


def main():
    SEED_DIGIT, ID_SUM, ARTIST_SUM = get_student_inputs()

    # Generate unique incident records in ascending order.
    ORIGINAL_DATASET = sorted(
        set(
            ID_SUM + ARTIST_SUM + SEED_DIGIT + (i * 7)
            for i in range(12)
        )
    )

    # Determine the rotation point using SEED_DIGIT.
    ROTATION_POINT = SEED_DIGIT % len(ORIGINAL_DATASET)

    ROTATED_DATASET = (
        ORIGINAL_DATASET[ROTATION_POINT:]
        + ORIGINAL_DATASET[:ROTATION_POINT]
    )

    # Generate the target using ID_SUM and ARTIST_SUM.
    TARGET_INDEX = (ID_SUM + ARTIST_SUM) % len(ORIGINAL_DATASET)
    TARGET_INCIDENT = ORIGINAL_DATASET[TARGET_INDEX]

    # Search using rotated binary search.
    binary_index, binary_comparisons = binary_search_rotated(
        ROTATED_DATASET, TARGET_INCIDENT
    )

    # Search using linear search.
    linear_index, linear_comparisons = linear_search(
        ROTATED_DATASET, TARGET_INCIDENT
    )

    print("\n======================================")
    print("EMERGENCY DISPATCH RECORD SEARCH")
    print("======================================")

    print("\nOriginal Dataset:", ORIGINAL_DATASET)
    print("Rotation Point:", ROTATION_POINT)
    print("Rotated Dataset:", ROTATED_DATASET)
    print("Target Incident:", TARGET_INCIDENT)

    print("\n--- ROTATED BINARY SEARCH ---")

    if binary_index != -1:
        print("Target found at index:", binary_index)
    else:
        print("Target incident was not found.")

    print("Comparison Count:", binary_comparisons)

    print("\n--- LINEAR SEARCH ---")

    if linear_index != -1:
        print("Target found at index:", linear_index)
    else:
        print("Target incident was not found.")

    print("Comparison Count:", linear_comparisons)

    print("\n--- SEARCH COMPARISON ---")

    if binary_comparisons < linear_comparisons:
        print("Rotated Binary Search used fewer comparisons.")
    elif binary_comparisons > linear_comparisons:
        print("Linear Search used fewer comparisons.")
    else:
        print("Both algorithms used the same number of comparisons.")

    print("\n--- COMPLEXITY ANALYSIS ---")
    print("Rotated Binary Search:")
    print("Time Complexity: O(log n) typical case, O(n) worst case")
    print("Auxiliary Space: O(1)")

    print("\nLinear Search:")
    print("Time Complexity: O(n)")
    print("Auxiliary Space: O(1)")

    print("\n--- FINAL OUTPUT ---")
    print("Original Dataset:", ORIGINAL_DATASET)
    print("Rotated Dataset:", ROTATED_DATASET)
    print("Target Incident:", TARGET_INCIDENT)
    print("Binary Search Comparisons:", binary_comparisons)
    print("Linear Search Comparisons:", linear_comparisons)


if __name__ == "__main__":
    main()