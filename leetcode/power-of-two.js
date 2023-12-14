// https://leetcode.com/problems/power-of-two/description/

const isPowerOfTwoRecursive = function(n) {
  if (n === 1) return true
  if (n % 2 !== 0) return false
  if (n <= 0) return false

  return isPowerOfTwoRecursive(n / 2)
};

const isPowerOfTwoLog1 = function(n) {
  if (n === 1) return true
  if (n % 2 !== 0) return false
  if (n < 2) return false
  
  const result = Math.log2(n)
  
  return Math.floor(result) === result
};

const isPowerOfTwoLog2 = function(n) {
  return Math.log2(n) % 1 === 0
};

console.log(isPowerOfTwoLog2(536870912))