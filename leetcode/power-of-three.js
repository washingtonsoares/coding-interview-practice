// https://leetcode.com/problems/power-of-three/

const isPowerOfThreeRecursive = function(n) {
    if (n === 1) return true
    if (n % 3 !== 0) return false
    if (n < 3) return false

    return isPowerOfThreeRecursive(n / 3)
};

const isPowerOfThreeLog = function(n) {
  if (n === 1) return true
  if (n % 3 !== 0) return false
  if (n < 3) return false

  const result = Math.log(n) / Math.log(3);
  const tolerance = 1e-10;

  return Math.abs(result - Math.round(result)) < tolerance;
};

console.log(isPowerOfThreeLog(27))