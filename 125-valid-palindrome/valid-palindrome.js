/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let L = 0, R = s.length - 1
    while(L <= R){
        if(!s[L].match(/[a-z0-9]/i)){
            L++
            continue
        }
        if(!s[R].match(/[a-z0-9]/i)){
            R--
            continue
        }
        if(s[L].toLowerCase() !== s[R].toLowerCase()){
            return false
        }
        L++
        R--
    }
    return true
};