
function createAccount (balance) {
    let balanceAmount = balance

    return {
        deposit : (amount) => {
            return balanceAmount += amount
            },
        withdraw : (amount) => {
            if (amount <= balanceAmount){
                return balanceAmount -= amount
            }else{
                return "Insufficient balance"
            }
        },
        getBalance : () => {
            return balanceAmount
        }
    }
}

const account1 = createAccount(1000)

account1.deposit(500)

console.log(account1.getBalance())

const account2 = createAccount(2000)
console.log(account2.getBalance())

/*

What is a Closure?
A closure occurs when a function is declared inside another function, allowing the inner function to access and 
remember the variables and environment of the outer function, even after the outer function has finished execution. 
This behavior is possible because functions in JavaScript maintain a reference to their lexical environment.

*/