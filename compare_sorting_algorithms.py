import time
import pandas as pd  # I'm using pandas to create nice tables for the results
import matplotlib.pyplot as plt  # I need matplotlib to visualize the execution times in a graph
import csv  # I forgot to import the csv module earlier

# Function to load data from a CSV file, it's straightforward and handles the data parsing
def load_data_from_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['sales_volume'] = int(row['sales_volume'])  # I'm converting sales volume to integer
            row['rating'] = float(row['rating'])  # I also convert rating to float
            dataset.append(row)
    return dataset

# Merge Sort algorithm implementation
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])  # I recursively split the data to sort the left part
    right = merge_sort(data[mid:])  # Similarly, I sort the right part
    return merge(left, right)  # I then merge the sorted halves

# Helper function to merge two sorted halves together
def merge(left, right):
    result = []
    while left and right:
        if (left[0]['sales_volume'], left[0]['rating']) > (right[0]['sales_volume'], right[0]['rating']):
            result.append(left.pop(0))  # I compare the first element of both lists and append the larger one
        else:
            result.append(right.pop(0))
    result.extend(left or right)  # After merging, I add any remaining elements from the left or right list
    return result

# Quick Sort algorithm implementation
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]  # I pick the first element as the pivot (this can be optimized later)
    left = [x for x in data[1:] if (x['sales_volume'], x['rating']) > (pivot['sales_volume'], pivot['rating'])]
    right = [x for x in data[1:] if (x['sales_volume'], x['rating']) <= (pivot['sales_volume'], pivot['rating'])]
    return quick_sort(left) + [pivot] + quick_sort(right)  # I recursively sort the left and right parts

# Function to measure the time it takes for Merge Sort to run
def measure_merge_sort_time(dataset):
    start_time = time.time()
    merge_sort(dataset)
    return time.time() - start_time  # I return the time it took to sort the dataset

# Function to measure the time it takes for Quick Sort to run
def measure_quick_sort_time(dataset):
    start_time = time.time()
    quick_sort(dataset)
    return time.time() - start_time  # Similar to Merge Sort, I measure how long Quick Sort takes

# Main function to compare the sorting algorithms
def compare_sorting_algorithms():
    dataset_files = [
        "large_product_dataset_1000.csv",
        "large_product_dataset_5000.csv",
        "large_product_dataset_10000.csv"
    ]
    
    results = []
    
    for file in dataset_files:
        dataset = load_data_from_csv(file)  # I'm loading the data from each dataset file
        
        # I'm measuring the execution times of both algorithms
        merge_sort_time = measure_merge_sort_time(dataset)
        quick_sort_time = measure_quick_sort_time(dataset)
        
        print(f"\nTop 5 Sorted Products (Merge Sort) - {file}:")
        sorted_merge = merge_sort(dataset)  # I'm sorting the dataset with Merge Sort
        for product in sorted_merge[:5]:  # Printing the top 5 products
            print(f"ID: {product['id']}, Sales Volume: {product['sales_volume']}, Rating: {product['rating']}")
        
        print(f"\nTop 5 Sorted Products (Quick Sort) - {file}:")
        sorted_quick = quick_sort(dataset)  # Now, I'm sorting the dataset with Quick Sort
        for product in sorted_quick[:5]:  # Printing the top 5 products from Quick Sort
            print(f"ID: {product['id']}, Sales Volume: {product['sales_volume']}, Rating: {product['rating']}")
        
        # I store the results (dataset size and execution times) for further analysis
        dataset_size = len(dataset)
        results.append([dataset_size, merge_sort_time, quick_sort_time])

    # Now, I display the comparison results in a table
    df = pd.DataFrame(results, columns=["Dataset Size", "Merge Sort Time (s)", "Quick Sort Time (s)"])
    print("\nExecution Time Comparison (in seconds):")
    print(df)
    
    # Plotting the execution times for both algorithms in a graph
    plt.plot(df["Dataset Size"], df["Merge Sort Time (s)"], label="Merge Sort", marker='o')
    plt.plot(df["Dataset Size"], df["Quick Sort Time (s)"], label="Quick Sort", marker='x')
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Merge Sort vs Quick Sort Execution Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    compare_sorting_algorithms()  # Running the main function when the script is executed
