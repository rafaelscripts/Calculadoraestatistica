function calcular() {
    const input = document.getElementById('inputData').value;
    const numeros = input.split(',').map(num => parseFloat(num.trim())).filter(num => !isNaN(num));

    const media = calcularMedia(numeros);
    const moda = calcularModa(numeros);
    const mediana = calcularMediana(numeros);

    document.getElementById('media').innerText = `Média: ${media}`;
    document.getElementById('moda').innerText = `Moda: ${moda}`;
    document.getElementById('mediana').innerText = `Mediana: ${mediana}`;
}

function calcularMedia(nums) {
    const soma = nums.reduce((acc, num) => acc + num, 0);
    return (soma / nums.length).toFixed(2);
}

function calcularModa(nums) {
    const frequencia = {};
    let maxFreq = 0;
    let modas = [];

    nums.forEach(num => {
        frequencia[num] = (frequencia[num] || 0) + 1;
        if (frequencia[num] > maxFreq) {
            maxFreq = frequencia[num];
        }
    });

    for (let num in frequencia) {
        if (frequencia[num] === maxFreq) {
            modas.push(num);
        }
    }

    return modas.length > 1 ? `Multimodal: ${modas.join(', ')}` : `Moda: ${modas[0]}`;
}

function calcularMediana(nums) {
    nums.sort((a, b) => a - b);
    const meio = Math.floor(nums.length / 2);

    if (nums.length % 2 === 0) {
        return ((nums[meio - 1] + nums[meio]) / 2).toFixed(2);
    } else {
        return nums[meio].toFixed(2);
    }
}

function reiniciar() {
    document.getElementById('inputData').value = '';
    document.getElementById('media').innerText = 'Média: ';
    document.getElementById('moda').innerText = 'Moda: ';
    document.getElementById('mediana').innerText = 'Mediana: ';
}

function ajuda() {
    alert("Insira os números separados por vírgula para calcular a média, moda e mediana.");
}
