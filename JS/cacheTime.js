class TimeLimitedCache{
    constructor(){
        this.cache = new Map()
    }

    set(key, value, duration){
        const now = Date.now()
        const expiry = now + duration

        const alreadyExistsUnexpired = this.cache.has(key) && this.cache.get(key).expiry > now

        this.cache.set(key, {value, expiry})
        return alreadyExistsUnexpired      

    }

    get(key){
        const now = Date.now()
        if(this.cache.has(key)){
            const value = this.cache.get(key)
            if (value.expiry > now){
                return value.value
            }
            else{
                this.cache.delete(key)
            }
        }else{
            return -1
        }
    }

    count(){

        const now = Date.now()
        let count = 0

        this.cache.forEach((value,key) => {
            if (value.expiry > now ){
                count++
            }else{
                this.cache.delete(key)
            }
        })
        return count
    }
}


var test = new TimeLimitedCache()

console.log(test.set(1,42,0))
console.log(test.set(2, 55, 3000))
console.log(test.set(3,50,2000))
console.log(test.set(1,42,1000))


console.log(test.get(3))

console.log(test.count())



