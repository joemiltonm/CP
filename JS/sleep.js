// https://leetcode.com/problems/sleep/


// async function sleep(millis) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(millis)}, millis)
//     })
// }

// sleep(100).then((res) => console.log(res))

var name2 = {
    first : "ben",
    second : "joe"
}

global.name2 = name2;

function outer(fn) {
    let name = {
        first : "joe",
        second: "milton"
    }

    return function(...args){
        return fn.apply(this,args) // this here refers to the global object. 
    }
}

function greet(a,b){
    return `welcome ${this.name2.first} ${a}, ${b}, ${this.name2.second}` 
}

const result = outer(greet)

console.log(result(5,8))



