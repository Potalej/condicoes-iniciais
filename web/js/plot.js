export default class Plotar {
  
  constructor (nome, valores) {
    this.nome = nome
    this.valores = valores
    this.X0 = [], this.Y0 = [], this.Z0 = []
    this.X = [], this.Y = [], this.Z = []
    this.valores.map(valor => {
      this.X.push(valor[0]); this.Y.push(valor[1]); this.Z.push(valor[2])
      this.X0.push(valor[0]); this.Y0.push(valor[1]); this.Z0.push(valor[2])
    })
    this.zoom = 1
    this.minimo = Math.min(Math.min(...this.X), Math.min(...this.Y), Math.min(...this.Z));
    this.maximo = Math.max(Math.max(...this.X), Math.max(...this.Y), Math.min(...this.Z));
    
    this.data = [{
      x: this.X, y: this.Y, z: this.Z,
      mode: 'markers', type: 'scatter3d',
    }];
    
    this.set_layout()

    Plotly.newPlot('plot', this.data, this.layout, {responsive:true, scrollZoom:true});
  }

  set_layout () {
    this.layout = {
      title: this.nome, 
      autosize: true,
      scene: {
        aspectratio: { x: 1, y: 1, z: 1 },
        xaxis: {
          range: [this.minimo,this.maximo], type: 'linear',
          autorange: false, automargin: false,
        },
        yaxis: {
          range: [this.minimo,this.maximo], type: 'linear',
          autorange: false, automargin: false,
        },
        zaxis: {
          range: [this.minimo,this.maximo], type: 'linear',
          autorange: false, automargin: false,
        }
      }
    };
  }

  atualizar_zoom (valor) {
    this.zoom = valor
    this.minimo = (1/this.zoom)*Math.min(Math.min(...this.X0), Math.min(...this.Y0), Math.min(...this.Z0));
    this.maximo = (1/this.zoom)*Math.max(Math.max(...this.X0), Math.max(...this.Y0), Math.min(...this.Z0));
    this.set_layout()
  }

  atualizar_posicoes (fatorX) {
    for (let i = 0; i < this.X.length; i++) {
      this.X[i] = fatorX*this.X0[i]
      this.Y[i] = fatorX*this.Y0[i]
      this.Z[i] = fatorX*this.Z0[i]
    }
    this.data = [{
      x: this.X, y: this.Y, z: this.Z,
      mode: 'markers', type: 'scatter3d',
    }];
  }

  atualizar () {
    Plotly.update('plot', this.data, this.layout, {responsive:true,scrollZoom:true});
  }

}