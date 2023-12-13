function findTheSequence(direction) {
  const segments = [{
    start: 0,
    end: Math.pow(2, direction.length),
    number: 0,
  }]

  for (let i = 0; i < direction.length; i++) {
    const currentSegment = segments[i];
    
    const mid = Math.floor((currentSegment.start + currentSegment.end) / 2);

    if (direction[i] === 'L') {
      segments.push({
        start: currentSegment.start,
        end: mid,
        number: i + 1
      })
    } 

    if (direction[i] === 'R') {
      segments.push({
        start: mid,
        end: currentSegment.end,
        number: i + 1
      })
    }
  }

  console.log({ segments })
  segments.sort((a, b) => a.start - b.start);
  console.log({ segmentsSorted: segments })
  let result = segments.map(segment => segment.number);
  console.log({ result })
  return result;
}

console.log(findTheSequence("LRRLLL")); // [2, 4, 5, 6, 3, 1]

module.exports = findTheSequence;