function countingValleys(steps, path) {
    let altitude = 0;
    let valleys = 0;

    for (let i=0; i < steps; i++) {
        const step = path[i] === 'U' ? 1 : -1
        altitude += step;
        if (i > 0 && altitude === 0 && path[i] === 'U') {
            valleys++;
        }
    }

    return valleys;
}

countingValleys(8, 'UDDDUDUU')

