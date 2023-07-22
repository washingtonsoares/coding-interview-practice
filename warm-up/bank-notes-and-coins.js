// https://www.beecrowd.com.br/judge/pt/problems/view/1021
// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n');

let n = parseFloat(576.73);

const bankNotes = [100, 50, 20, 10, 5, 2];
const bankCoins = [1, 0.50, 0.25, 0.10, 0.05, 0.01];

console.log('NOTAS:');

for (let i=0; i < bankNotes.length; i++) {
    const bankNote = bankNotes[i];

    if (n >= bankNote) {
        const amountOfBankNotes = Math.floor(n / bankNote);
        console.log(`${amountOfBankNotes} nota(s) de R$ ${bankNote.toFixed(2)}`)
        n = n % bankNote;
        n = parseFloat(n.toFixed(2));
    } else {
        console.log(`0 nota(s) de R$ ${bankNote.toFixed(2)}`)
    }
}
console.log('MOEDAS:');

for (let i=0; i < bankCoins.length; i++) {
    const bankCoin = bankCoins[i];

    if (n >= bankCoin) {
        const amountOfBankNotes = Math.floor(n / bankCoin);
        console.log(`${amountOfBankNotes} moeda(s) de R$ ${bankCoin.toFixed(2)}`)
        n = n % bankCoin;
        n = parseFloat(n.toFixed(2));
    } else {
        console.log(`0 moeda(s) de R$ ${bankCoin.toFixed(2)}`)
    }
}