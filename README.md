# Algorithmic Efficiency Analysis: Merge Sort vs Quick Sort for E-Commerce Optimization

## 📋 Project Overview
This project implements and empirically analyzes the performance of Merge Sort and Quick Sort algorithms for optimizing e-commerce product listings. The system sorts products based on sales volume and user ratings across varying dataset sizes (1,000 to 10,000 records), providing concrete data on algorithmic efficiency and scalability.

## 🎯 Project Objectives
- Implement and compare the time complexity of Merge Sort and Quick Sort algorithms
- Develop an efficient multi-criteria sorting system for e-commerce product rankings
- Analyze algorithmic performance scalability across different dataset sizes
- Provide empirical validation of theoretical time complexity (O(n log n))

## 🛠 Technical Implementation

### Core Algorithms
- **Merge Sort**: Divide-and-conquer algorithm with stable O(n log n) performance
- **Quick Sort**: Efficient in-place sorting with O(n log n) average-case complexity
- **Multi-key Comparison**: Custom comparator for (sales_volume, rating) tuple sorting

### Technologies Used
- **Programming Language**: Python 3.x
- **Data Analysis**: Pandas for results tabulation
- **Visualization**: Matplotlib for performance graphing
- **Data Handling**: CSV module for dataset processing

## 🚀 Installation & Usage

### Prerequisites
```bash

### Performance Comparison Table
| Dataset Size | Merge Sort Time (s) | Quick Sort Time (s) |
|--------------|---------------------|---------------------|
| 1,000        | 0.045               | 0.032               |
| 5,000        | 0.215               | 0.148               |
| 10,000       | 0.482               | 0.305               |

### Visualization Graph
![Performance Comparison Chart](results/performance_comparison.png)
*Graph showing execution time scaling with dataset size*

## 📊 Performance Analysis

### Dataset Sizes
- **1,000 product records** - Baseline performance measurement
- **5,000 product records** - Medium-scale testing
- **10,000 product records** - Large-scale scalability analysis

### Key Metrics Measured
- **Execution time** for both algorithms across all dataset sizes
- **Time complexity validation** - Empirical verification of O(n log n) complexity
- **Multi-criteria sorting accuracy** - Correct ordering by (sales_volume, rating) tuples

## 📈 Results & Findings

The empirical analysis revealed:

- **Relative Performance**: Quick Sort demonstrated 25-35% faster execution times across all dataset sizes
- **Scalability**: Both algorithms maintained O(n log n) scaling, with execution times increasing predictably with input size
- **Practical Implications**: Quick Sort's better cache performance makes it more suitable for memory-constrained e-commerce applications
- **Optimal Selection**: For real-time product ranking, Quick Sort provides better performance, while Merge Sort offers stability for consistent results

## 🔬 Academic Significance

This project demonstrates essential computer science competencies:

- **Algorithm Design & Implementation**: Hands-on experience with recursive algorithm implementation
- **Empirical Complexity Analysis**: Practical validation of theoretical time complexities
- **Performance Benchmarking**: Systematic measurement and comparison methodologies
- **Data-Driven Selection Criteria**: Evidence-based algorithm choice for specific application requirements
##
