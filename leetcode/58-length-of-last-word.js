// https://leetcode.com/problems/length-of-last-word/

const lengthOfLastWord = function(s) {
    const words = s.trim().split(" ");
    const lastWord = words[words.length - 1];

    return lastWord.length
};