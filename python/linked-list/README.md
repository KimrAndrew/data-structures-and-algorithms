# Singly Linked List

## Node

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

## Linked List

- Create a Linked List class
- Within you Linked List class, include a head property
  - Upon instantiation, an empty Linked List should be created
- The class should contain the following methods:
  - insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the `head` of the list with an O(1) Time performance

- includes
  - Arguments: value
  - Returns: Boolean
    - Indicates whether that value exists as a Node's value somewhere within the list.
- to string
  - Arguments: none
  - Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
  - Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
  - Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

## Approach & Efficiency

- Built using TDD workflow of writing the tests before creating the methods being tested
- insert:
  - Time: O(1)
  - Space: O(N)
- includes:
  - Time: O(N)
  - Space: O(N)
- to string:
  - Time: O(N)
  - Space: O(N)

## Linked List Insertions

## Feature Tasks
Write the following methods for the Linked List class:

- append
  - arguments: new value
  - adds a new node with the given value to the end of the list
- insert before
  - arguments: value, new value
  - adds a new node with the given new value immediately before the first node that has the value specified
- insert after
  - arguments: value, new value
  - adds a new node with the given new value immediately after the first node that has the value specified

## Approach & Efficiency

Built using TDD workflow of writing the tests before creating the methods being tested
- append:
  - Time: O(N)
  - Space: O(N)
- insert_before:
  - Time: O(N)
  - Space: O(N)
- insert_after:
  - Time: O(N)
  - Space: O(N)

## Kth_From_End

kth from end

- argument: a number, k, as a parameter.
- Return the node’s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency

- kth_from_end:
  - uses a for loop to push a look ahead k nodes in front of Node who's value will eventually be returned (initialized at the head of the list) then uses a while loop to push the reference to the look ahead node and the reference to the output Node to the end of the list
  - basically uses k to determine how far from the head the look ahead Node needs to be  initialized to
  - Space: O(N)
  - Time: O(N)
