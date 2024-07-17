// https://leetcode.com/problems/counter/


/*
Given an integer n, return a counter function. This counter function initially 
returns n and then returns 1 more than the previous value every subsequent time 
it is called (n, n + 1, n + 2, etc).


Example 1:

Input: 
n = 10 
["call","call","call"]
Output: [10,11,12]
Explanation: 
counter() = 10 // The first time counter() is called, it returns n.
counter() = 11 // Returns 1 more than the previous time.
counter() = 12 // Returns 1 more than the previous time.
Example 2:

Input: 
n = -2
["call","call","call","call","call"]
Output: [-2,-1,0,1,2]
Explanation: counter() initially returns -2. Then increases after each sebsequent call.
 

Constraints:

-1000 <= n <= 1000
0 <= calls.length <= 1000
calls[i] === "call"

*/

var a = 0

const counter = (n) => {
    if (n){
        a = a + n
        return a
    }
    else{
        a += 1
        return a
    }
}

console.log(counter(10))
console.log(counter())
console.log(counter())
console.log(counter())

/*
Closures - As I mentioned earlier, closures are an important
concept in JavaScript, and understanding how they work is essential 
for solving the counter function problem. Closures are 
created whenever a function is defined inside another function, and
the inner function has access to the variables and parameters of the 
outer function.
*/