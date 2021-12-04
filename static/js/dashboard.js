
/* function renderiza_despesas_mensal(){
    const ctx = document.getElementById('despesas_mensal').getContext('2d');
    /* var cores_despesas_mensal = gera_cor(qtd=12) 
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
} */

function renderiza_despesa_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('despesas_mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Despesa Mensal com Ocorrências',
                    data: data.data,
                    backgroundColor: ['#396afc'],
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }]
            }
        });


    })

}

function renderiza_total_gasto(url){  
  fetch(url, {
      method: 'get',
  }).then(function(result){
      return result.json()
  }).then(function(data){
      document.getElementById('gasto_total').innerHTML = data.total
  })

}

function renderiza_ultimo_mes(url){  
  fetch(url, {
      method: 'get',
  }).then(function(result){
      return result.json()
  }).then(function(data){
      document.getElementById('ultimo_mes').innerHTML = data.total
  })

}

function renderiza_ultima_semana(url){  
  fetch(url, {
      method: 'get',
  }).then(function(result){
      return result.json()
  }).then(function(data){
      document.getElementById('ultima_semana').innerHTML = data.total
  })

}

function renderiza_ultimo_dia(url){  
  fetch(url, {
      method: 'get',
  }).then(function(result){
      return result.json()
  }).then(function(data){
      document.getElementById('ultimo_dia').innerHTML = data.total
  })

}