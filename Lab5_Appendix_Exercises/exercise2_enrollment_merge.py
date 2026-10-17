# EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS

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


def merge_sorted_lists(dataset_a, dataset_b):
    i = 0
    j = 0
    merged = []
    comparisons = 0

    # Compare the current values from both datasets.
    while i < len(dataset_a) and j < len(dataset_b):
        comparisons += 1

        if dataset_a[i] <= dataset_b[j]:
            merged.append(dataset_a[i])
            i += 1
        else:
            merged.append(dataset_b[j])
            j += 1

    # Append the remaining records.
    merged.extend(dataset_a[i:])
    merged.extend(dataset_b[j:])

    return merged, comparisons


def main():
    SEED_DIGIT, ID_SUM, NAME_LENGTH, ARTIST_LENGTH, ARTIST_SUM = (
        get_student_inputs()
    )

    # Generate Department A records using SEED_DIGIT and ID_SUM.
    DATASET_A = sorted(
        set(SEED_DIGIT + ID_SUM + (i * 3) for i in range(8))
    )

    # Generate Department B records using ARTIST_LENGTH and NAME_LENGTH.
    DATASET_B = sorted(
        set(ARTIST_LENGTH + NAME_LENGTH + ARTIST_SUM + (i * 4)
            for i in range(7))
    )

    # Merge the two sorted datasets.
    CONSOLIDATED_DATASET, COMPARISON_COUNT = merge_sorted_lists(
        DATASET_A, DATASET_B
    )

    print("\n======================================")
    print("UNIVERSITY ENROLLMENT RECORDS")
    print("======================================")

    print("\nDepartment A Dataset:", DATASET_A)
    print("Department B Dataset:", DATASET_B)

    print("\n--- CONSOLIDATION RESULTS ---")
    print("Consolidated Dataset:", CONSOLIDATED_DATASET)
    print("Department A Record Count:", len(DATASET_A))
    print("Department B Record Count:", len(DATASET_B))

    print(
        "Records Before Consolidation:",
        len(DATASET_A) + len(DATASET_B)
    )
    print("Records After Consolidation:", len(CONSOLIDATED_DATASET))
    print("Comparison Count:", COMPARISON_COUNT)

    # Verify that the merged dataset is sorted.
    ORDERING_VERIFICATION = (
        CONSOLIDATED_DATASET == sorted(CONSOLIDATED_DATASET)
    )

    # Verify that no records were lost.
    RECORD_COUNT_VERIFICATION = (
        len(CONSOLIDATED_DATASET)
        == len(DATASET_A) + len(DATASET_B)
    )

    print("\n--- VERIFICATION ---")
    print("Ordering Verification:", ORDERING_VERIFICATION)
    print("Record Count Verification:", RECORD_COUNT_VERIFICATION)

    print("\n--- COMPLEXITY ANALYSIS ---")
    print("Time Complexity: O(n + m)")
    print("Auxiliary Space Complexity: O(n + m)")
    print("n = number of records in Department A")
    print("m = number of records in Department B")

    print("\n--- FINAL OUTPUT ---")
    print("Department A:", DATASET_A)
    print("Department B:", DATASET_B)
    print("Consolidated Dataset:", CONSOLIDATED_DATASET)
    print("Comparison Count:", COMPARISON_COUNT)
    print("Correctly Ordered:", ORDERING_VERIFICATION)
    print("All Records Retained:", RECORD_COUNT_VERIFICATION)


if __name__ == "__main__":
    main()