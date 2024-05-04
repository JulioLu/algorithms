def calculate_split_cost(string_length, indexes):
    indexes.sort()  # Ensure indexes are sorted in ascending order
    total_cost = string_length  # Cost of the initial split

    for i in range(len(indexes)):
        if i == 0:
            substring_length = indexes[i]
        else:
            substring_length = indexes[i] - indexes[i - 1]

        total_cost += substring_length

    # Add the cost of the substring after the last index
    total_cost += string_length - indexes[-1]

    return total_cost


if __name__ == "__main__":
    string_length = 15
    indexes = [2, 4, 11]
    total_cost = calculate_split_cost(string_length, indexes)
    print("Total cost:", total_cost)