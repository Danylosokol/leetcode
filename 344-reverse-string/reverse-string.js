/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    function helper(L, R){
        if(L >= R){
            return 
        }
        const temp = s[L]
        s[L] = s[R]
        s[R] = temp
        helper(++L, --R)
    }

    helper(0, s.length - 1)
};