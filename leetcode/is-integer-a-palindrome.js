/**
 Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const numAsList = String(x).split('');
    const len = numAsList.length;
          
    for(let i=0, j = len - 1; i < len; i++, j--) {
        if(numAsList[i] !== numAsList[j]) {
          return false;
        }
    }
    
    return true;
};