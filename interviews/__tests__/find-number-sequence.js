const findNumberSequence = require("../find-number-sequence");

describe("Segment Splitter Game", () => {
  test.each([
    ["LRRLLL", [2, 3, 6, 5, 4, 1]],
    
  ])("Given direction %s, the expected output is %j", (input, expected) => {
    expect(findNumberSequence(input)).toEqual(expected);
  });
});
