/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let L = 0, R = s.length - 1
    console.log(s, L, R)
    while(L <= R){
        console.log("L: ", L, s[L])
        console.log("R: ", R, s[R])
        if(!s[L].match(/[a-z0-9]/i)){
            L++
            console.log("L is not alphanumeric")
            continue
        }
        if(!s[R].match(/[a-z0-9]/i)){
            R--
            console.log("R is not alphanumeric")
            continue
        }
        if(s[L].toLowerCase() !== s[R].toLowerCase()){
            console.log("string is not alphanumeric")
            return false
        }
        L++
        R--
    }
    return true
};