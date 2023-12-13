// https://leetcode.com/problems/power-of-four/

// ugly way
const isPowerOfFourInteractive = function(n) {
  if (n <= 0) return false

  while(n !== 1) {
    if (n % 4 !== 0) return false

    n = n / 4
  }

  return true
};

const isPowerOfFourRecursive = function(n) {
  if (n === 1) return true
  if (n%4 !== 0) return false
  if (n < 4) return false

  return isPowerOfFourRecursive(n / 4)
}

const isPowerOfFourLog = function(n) {
  if (n === 1) return true
  if (n%4 !== 0) return false
  if (n < 4) return false
  
  const log = Math.log(n) / Math.log(4);

  return Math.floor(log) === log
}

console.log(isPowerOfFourLog(4))