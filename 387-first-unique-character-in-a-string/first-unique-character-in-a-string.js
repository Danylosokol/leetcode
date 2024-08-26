/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    for (let idx = 0; idx < s.length; idx++) {
        if (s.indexOf(s[idx]) === s.lastIndexOf(s[idx])) {
            return idx
        }
    }
    return -1
};