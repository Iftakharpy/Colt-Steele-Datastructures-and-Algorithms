# [JavaScript Algorithms and Data Structures Masterclass - Colt Steele's courses resources and solutions](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/)


>#### For many exercises I could not find the question so I saved the provided solutions in "SQX\_\*.js" file.("\*" means anything)
>#### These files are prefixed with "SQX_"(Solutions without questions exercise)

&nbsp;

## Problem solving approach for challanging problems(programming problems usually)

>1. Understand the problem
>2. Explore concrete examples
>3. Break it down
>4. Solve/Simplify
>5. Lookback and refactor
## Simplified 

>1. Understand
>2. Plan
>3. Solve
>4. Check

&nbsp;

# Topics 
- [Recursion](#recursion)
- [Short description of sorting algorithms](#sorting-algorithms)
  - [Bubble Sort](#1-bubble-sort)
  - [Seletion Sort](#2-selection-sort)
  - [Insertion Sort](#3-insertion-sort)
  - [Merge Sort](#4-merge-sortdivide-and-conquer)
  - [Quick Sort](#5-quick-sortdivide-and-conquer)
  - [Radix Sort](#6-radix-sort)
- [Graphs](#big-o-graphs)
  - [Datastructures](#big-o-for-datastructures)
  - [Algorithms](#big-o-for-sorting-algorithms)

&nbsp;

# Recursion

## Recursion means calling a function inside it's definition.

>Tree datastructures are usually treversed using recursion.

>When a function calls are stored(pushed) in callstack(Stack datastructure-LIFO(Last in first out)).
>When return is called in the runction this function is popped out of the call statck.

## Essential parts of recrusive functions.
1. Base Case (Condition(s) to stop the recursive function.)
2. Changing the argument (Changing the argument value so that the recursive calls gradually apporatches to the base case.)
### Example:

```Python
#This function will hit the recursion limit or Recursion Error.
def sequence_printer(start=1, increment):
    # printing the start value
    print(start)

    #calling the function inside it's definition and increasing the start value each time the function is called
    sequence_printer(start+increment, increment)

#This function will stop when it hits recursion limit
def get_recursion_depth(count=1):
    try:
        get_recursion_depth(count+1) #increasing the argument value
    except RecursionError:
        print(count)
```

#### Proper recursion example
```python
def sum_range(number):
    if number==0: #base case
        return 0
    elif number>0:
        #changing the argument so that the function gradually approatches to the base case
        return number + sum_range(number-1)
    else: # if numer is smaller than 0. Example: -10
        #changing the argument so that the function gradually approatches to the base case
        return number + sum_range(number+1)
```

&nbsp;

___

&nbsp;

# Sorting Algorithms
## 1. Bubble Sort
    In Bubble sort only one number is sorted after each itteration.
    
    We look at two numbers while looping over the array(index "i" and index "i+1")
    We start from the beginning of the array. If value of index i > index i+1 we swap the value of the indexes.
    We do this for each numbers in the array.

## 2. Selection Sort
    Seletion sort is similar to bubble sort.Here we look for smallest number in the array.
    We swap the values of smallest number index and the first index.

    Note: After each swap we increment our smallest index by 1.
          Otherwise it will ony bring the smallest number to at index 0 everytime and won't sort the array.

## 3. Insertion Sort
    In Insertion sort an unsorted element gets placed in the correct place after each iteration.

    We start by assuming that first number in the list/array is already sorted.
    We start iterating from the index 1 and continue to the last index.
    We bring the value of index in the right place by comparing the numbers before the current index(if current index is 5 we start comparing from 4 and go all the way to the beginning).
    If the number is smaller than the number we continue exploring behind. In each step we push the values to the right so that we can insert the number in the right place.
    If we find an number that is either smaller or equals to the current index's number we consider that index is the right place for the number.
    We continue doing this for each element in the array. After each iteration we our target index increases by 1.

## 4. Merge Sort(Divide and conquer)
    In Merge Sort we keep breaking the array in half recursively one is left half and other is right half untill we get down to the simplest form of the array.
    Simplest form means an array with a single element or an empty array.
    Then we start marging the left and right arrays together.
    After merging the array we return the array the we merge the array with the next sorted half.
    the we repeat the process.

## 5. Quick Sort(Divide and conquer)
    In Quick Sort we select a pivot. Pivot is a value which should be placed in the correct place after an iteration over an array. Pivot can be selected in many ways(randomly/first element/last element/middle element). After selecting the pivot we place the selected pivot in the correct place and return the index. Here by placing the pivot in the correct place means we put the smaller elements to the left of the pivot and larger elements to the right of the pivot.

    Then we reucrisvely call the quick sort function on the left half and the right half to sort the array.

# 6. Radix Sort
    In Radix Sort we sort the nubmers without comparing the numbers to each other. We sort the number by comparing the digits of the numbers.

___

&nbsp;

# Big O Graphs

## Big O is used to analyze the time and space complexity of algorithms. It's also known as asymptotic analyzation of algorithms

![Runtime compared with Big O notations.](media/images/big_O_chart.PNG)

&nbsp;

# Big O for Datastructures
![big_O_for_data_structures.PNG](media/images/big_O_for_data_structures.PNG)

&nbsp;

# Big O for Sorting Algorithms
![big_O_of_sorting_algorithms.PNG](media/images/big_O_of_sorting_algorithms.PNG)

&nbsp;


### [Charts credit](https://www.bigocheatsheet.com/)
### [Markdown documentation reference](https://www.markdownguide.org/extended-syntax/)

## Todos
1. KNP string search
2. More recursion porblem solving