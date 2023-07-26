// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

while( i < length) {
    if (clouds[i] === 1) {
        i++;
        continue
    }
    if (clouds[i+2] === 0) {
        i += 2;
        jumps++;
        continue;
    }
    if (clouds[i+1] === 0) {
        i += 1;
        jumps++;
        continue;
    } 
    
    i++;
}


console.log(jumpingOnClouds([0,0 ,0 ,0 ,1 ,0]))