# Breadth First Traversal

## Whiteboard Process

## Approach and Efficiency

- Algorithm uses a queue to deconstruct the tree in the correct order
  - Parent Node gets enqueued
  - Parent Node gets dequeued
  - Parent value gets appended to output list
  - Children of parent get enqueued

### Big O

Time: Every node in the tree needs to be touched to get its value so time effieciency is **O(N)**

Space: The value of every node in the tree gets copied to a list that will eventually be the functions output. Space usuage increases linearly with size of the input tree. **O(N)**
