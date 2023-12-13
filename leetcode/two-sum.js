function maxCost(cost, labels, dailyCount) {
  let dailyLaptops = [];
  const costIncurred = [];

  for (let i = 0; i < cost.length; i++) {
    const costItem = cost[i];
    const labelItem = labels[i];

    dailyLaptops.push({ costItem, labelItem });
    console.log(dailyLaptops);
    if (labelItem === "legal") {
      const alreadyLegalManufacured = dailyLaptops.filter(
        ({ labelItem }) => labelItem === "legal"
      );

      if (alreadyLegalManufacured.length === dailyCount) {
        dailyLaptops = [];
        const sumAllManufactured = dailyLaptops.reduce(
          (acc, current) => current.costItem + acc,
          0
        );
        costIncurred.push(sumAllManufactured);
      }
    }
  }

  if (costIncurred.length) {
    return Math.max(...costIncurred);
  }

  return 0;
}

maxCost([2, 5, 3, 11, 1], ["legal", "ilegal", "legal", "ilegal", "legal"], 2);

function twoSum(nums, target) {
  const map = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (map[complement] !== undefined) {
      return [map[complement], i];
    }

    map[nums[i]] = i;
  }
}

function removeDuplicates(nums) {
  if (nums.length == 0) return 0;

  let insertPos = 1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1]) {
      nums[insertPos] = nums[i];
      insertPos++;
    }
  }
  return insertPos;
}

function reverseArray(arr) {
  let reversed = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
  }
  return reversed;
}
