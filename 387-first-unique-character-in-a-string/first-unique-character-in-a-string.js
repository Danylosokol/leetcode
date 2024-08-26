/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const unique = new Map()
    for(i in s){
        let prevVal = 0
        if(unique.has(s[i])){
            prevVal = unique.get(s[i])
        }
        unique.set(s[i], prevVal + 1)
    }
    for(i in s){
        if(unique.get(s[i]) === 1){
            return i
        }
    }
    return -1
};