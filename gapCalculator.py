def calculate_gap(result_path: float, optimal_path: float) -> float:
    if optimal_path == 0:
        raise ValueError("Optimal path cannot be zero.")
    
    gap = ((result_path - optimal_path) / optimal_path) * 100
    return gap

if __name__ == "__main__":
    result_path = float(input("Enter the result path length: "))
    optimal_path = float(input("Enter the optimal path length: "))

    try:
        gap = calculate_gap(result_path, optimal_path)
        print(f"The GAP is {gap:.2f}%")
    except ValueError as e:
        print(e)