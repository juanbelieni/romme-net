const canvas = document.querySelector('#grafico-gasto-mensal canvas');
const meses = [
  'Jan',
  'Fev',
  'Mar',
  'Abr',
  'Mai',
  'Jun',
  'Ago',
  'Set',
  'Out',
  'Nov',
  'Dez',
];

let chart = new Chart(canvas, {
  type: 'line',
  data: {
    labels: meses,
    datasets: [
      {
        label: 'Gasto Anual com Ocorrências Corretivas',
        data: [14, 21, 30, 17, 37, 33, 24, 19, 8, 0, 0],
        backgroundColor: ['#396afc'],
      },
    ],
  },
});
