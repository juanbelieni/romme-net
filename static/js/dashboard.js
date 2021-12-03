
function renderiza_despesas_mensal(){
    const ctx = document.getElementById('despesas_mensal').getContext('2d');
    /* var cores_despesas_mensal = gera_cor(qtd=12) */
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            datasets: [{
                label: 'Gasto Anual com Ocorrências Corretivas',
                data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
                backgroundColor: ['#396afc'],
                borderColor: "#FFFFFF",
                borderWidth: 0.2
            }]
        },
        
    });
}
