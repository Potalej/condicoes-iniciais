import Plotar from "./plot.js"

function exibir_valores (infos) {
  for (let [id, valor] of Object.entries(infos)) {
    try {
      if (typeof(valor) == 'boolean') {
        document.getElementById(`valor_${id}`).checked = valor
      } else {
        document.getElementById(`valor_${id}`).value = valor
      }
    } catch {
      console.warn(`Não inserido: ${id}`)
    }
  }
}

const modos = {
  "1": "./data/vi/",
  "2": "./data/sorteio/"
}


class Main {
  constructor () {
    this.zoom_input = document.getElementById("zoom")

    this.fator_V_input = document.getElementById("fator_V")
    this.fator_T_input = document.getElementById("fator_T")
    this.valor_fator_V_div = document.getElementById('valor_fator_V')
    this.valor_fator_T_div = document.getElementById('valor_fator_T')

    const atualizar = (quem) => {
      let fator_V = this.fator_V_input.value
      let fator_T = this.fator_T_input.value

      if (quem == 1) {
        fator_T = Math.sqrt((this.valores.H - this.valores.V/fator_V)/this.valores.T)
        this.fator_T_input.value = fator_T
      } 
      else if (quem==2) {
        fator_V = this.valores.V / (this.valores.H - fator_T**2 * this.valores.T)
        this.fator_V_input.value = fator_V
      }

      console.log(1/fator_V*this.valores.V + fator_T**2*this.valores.T,this.valores.H)

      this.valor_fator_V_div.textContent = (Math.round(fator_V * 10**4) / 10**4).toFixed(4);
      this.valor_fator_T_div.textContent = (Math.round(fator_T * 10**4) / 10**4).toFixed(4);
      
      var x = this.zoom_input.value;
      if (x >= 1) { x = 9*x - 8;             } 
      else        { x = this.zoom_input.value; }
      document.getElementById("valor_zoom").textContent = (Math.round(x * 100) / 100).toFixed(2);
      
      this.Plot.atualizar_zoom(x)
      this.Plot.atualizar_posicoes(1/fator_V)
      this.Plot.atualizar()
    }

    this.fator_V_input.oninput = () => atualizar(1)
    this.fator_T_input.oninput = () => atualizar(2)
    this.zoom_input.oninput = () => atualizar(0)
  }

  async exibir_informacoes (arquivo, modo) {
    let dir = modos[modo];
    if (modo == 1) {
      this.valores = await eel.ler_valores_iniciais(`${dir}${arquivo}`)()
      this.Plot = new Plotar(this.valores.nome, this.valores.posicoes)
    } else {
      this.valores = await eel.ler_sorteio(`${dir}${arquivo}`)()
    }
    exibir_valores(this.valores)  
  }
}

const M = new Main()
M.exibir_informacoes('teste.txt',1)
