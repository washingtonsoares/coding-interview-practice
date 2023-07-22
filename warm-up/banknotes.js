// https://www.beecrowd.com.br/judge/pt/problems/view/1018
// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n');

let n = Number(5000);
console.log(n);

const bankNotes = [100, 50, 20, 10, 5, 2, 1];

for (let i=0; i < bankNotes.length; i++) {
    const bankNote = bankNotes[i];

    if (n >= bankNote) {
        const amountOfBankNotes = Math.floor(n / bankNote);
        console.log(`${amountOfBankNotes} nota(s) de R$ ${bankNote},00`)
        n = n % bankNote;
    } else {
        console.log(`0 nota(s) de R$ ${bankNote},00`)
    }
}