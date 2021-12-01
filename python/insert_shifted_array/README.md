# Insert to Middle of an Array

Function takes in an array and a value as input, then returns a new array with the value inserted at the middle index of the array

## Whiteboard Process

![whiteboard](https://github.com/KimrAndrew/data-structures-and-algorithms/blob/insert-shifted-array/imgs/Insert%20Shift%20Array.png)

## Approach and Efficiency

The algorithm iterates over the given array appending each element to the end of a temporary array, iteration stops to insert the given value at the middle index before resuming iteration until the end of the given array

Time: O(N)
Space: O(N)
