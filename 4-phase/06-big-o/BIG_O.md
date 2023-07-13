# Big O Notation

- https://www.bigocheatsheet.com/

What is Big O? What does the O stand for?
- The Total number of OPERATIONS that an algo will execute

Every function/method/algorithm, we can determine the total number of operations for each individual line of code, then group them together given these rules below

## **TIME COMPLEXITY**

### *Constant Time => O(1) => O of One*
Any Operation that is applied once.

*Examples:*
- Variable Assignment
- print/console.log
- All the rudimentry Math ops
  - +, -, *, /


### *Linear Time => O(N)*
Any Operation that is applied to EVERY element in an array/list
The *N* is the length of the list/array

*Examples:*
- ANY LOOP
  - for, while, until
  - .forEach, .map, .filter, .find, etc..
- Any PARALLEL LOOPS

### *Quadratic Time => O(N^2)* ! DANGER ZONE
Any operation that is applied to every COMBINATION of every element together

*Examples:*
- Nested Loops
- Matrix

### *Cubic Time => O(N^3)* ! END OF THE WORLD ZONE

*Examples:*
- DOUBLE Nested Loops


## How to Calulate Big O?

to calc the big o, we needt o go line by line and add each big o 
O(1 + 1 + 1 + 1 + n + n + n) => O(4 + 3n)
n = 1     => O(4 + 3) => O(7)
n = 10    => O(4 + 30) => O(34)
n = 100    => O(4 + 300) => O(304)
n = 100000000000000000    => O(4 + 300000000000000000) => O(3000000000000000004)
n = ♾    => O(1 + 3*♾) => Can drop the CONSTANT 
  => O(3 * ♾) => Can ALSO DROP THE COEFFICENT of N
The resulting Big O is just O(N)

O(3 + 5n + 4n^2) => O(n^2)


### Other Times 
#### O(log(n))
For Binary Search and Binary Search Trees

#### O(n * log(n))
For the general sorting algorithms

#### O(2^n)
Recursion

#### O(n!)
A mystery that will crash yoiur computer, probably

---
## Big O Ground Rules

### Rule 1 => ALWAYS THE WORST CASE
### Rule 2 => Remove the Constants
### Rule 3 => Different Terms for different inputs
### Rule 4 => Drop NonDominants

--- 

## **SPACE COMPLEXITY**
How much MEMORY is being used in an operation

### **Constant Space O(1)**
Only uses the data provided by the inputs
Does not add any additional data
Solving the algo without creating an output array


### **Linear Space O(N)**
Creating additional data for each element in our array
EX: Creating an output array