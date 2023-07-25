// https://www.hackerrank.com/challenges/repeated-string/problem

function repeatedStringFast(s, n) {
  function sumAllCharsA(s) {
    let sum = 0;

    for (const c of s) {
      if (c === "a") {
        sum += 1
      }
    }

    return sum;
  }

  const amountCharsAFromInput = sumAllCharsA(s);
  const amountOfAs = Math.floor(n / s.length);
  const nModStrLength = n % s.length;
  let amountOfAsInRestSubstr = sumAllCharsA(s.slice(0, nModStrLength));
  
  const amountOfAllCharsA = (amountOfAs * amountCharsAFromInput) + amountOfAsInRestSubstr;

  return amountOfAllCharsA;
}

console.log(repeatedStringFast("abc", 6))

function repeatedStringSlow(s, n) {
  let repeatedWords = "";
  let amountOfAs = 0;

  function sumAllCharsA(str) {
    let sum = 0;
    for (const s of str) {
      if (s === "a") {
        sum++;
      }
    }
    return sum;
  }

  while (repeatedWords.length < n) {
    const remaining = n - repeatedWords.length;
    let wordsToAppend = "";
    if (remaining < n) {
      wordsToAppend += s.slice(0, remaining);
    } else {
      wordsToAppend += s;
    }
    amountOfAs += sumAllCharsA(wordsToAppend);
    repeatedWords += wordsToAppend;
  }

  return amountOfAs;
}

// console.log(repeatedStringSlow("abc", 6));