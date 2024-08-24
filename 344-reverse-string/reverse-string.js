/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    const stack = []

    for(i in s){
        stack.push(s[i])
    }

    for(i in s){
        s[i] = stack.pop()
    }
};