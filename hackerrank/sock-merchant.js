// https://www.hackerrank.com/challenges/sock-merchant/problem

function sockMerchant(n, colors) {
    const colorByAmount = {};
    let amountOfPairs = 0;

    for (const color of colors) {
        if (!colorByAmount[color]) {
            colorByAmount[color] = 1
        } else {
            colorByAmount[color]++;
        }
    }

    for (const [key, value] of Object.entries(colorByAmount)) {
        const colorPairs = Math.floor(value / 2);
        amountOfPairs += colorPairs;
    }

    return amountOfPairs
}

sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])