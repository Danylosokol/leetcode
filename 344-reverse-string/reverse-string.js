/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let L = 0, R = s.length - 1

    while(L < R){
        const temp = s[L]
        s[L] = s[R]
        s[R] = temp
        L += 1
        R -= 1
    }
};