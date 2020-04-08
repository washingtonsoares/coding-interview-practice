/**
  Write a function that reverses a string. The input string is given as an array of characters char[].
  Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
  
  Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
 * 
 * 
 * 
 * 
 * 
 * 
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(str) {
    const strLen = str.length;
    const iterations = parseInt(strLen / 2);

    for (let i = 0; i < iterations; i++) {
        const aux = str[i];
        str[i] = str[strLen-(i+1)];
        str[strLen-(i+1)] = aux;
    }

    return str;
};