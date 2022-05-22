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
