import src.mecanica as mecanica
from os import listdir
import eel

@eel.expose
def ler_valores_iniciais (dir:str)->dict:
  infos = dict()
  with open(dir, 'r') as arq:
    # Quebra em linhas
    linhas = arq.read().split('\n')

    infos['nome'] = linhas[1].split()[1]
    infos['integrador'] = linhas[2].split()[1]
    infos['timestep'] = float(linhas[3].split()[1])
    infos['passos'] = int(linhas[4].split()[1])
    infos['t0'] = float(linhas[5].split()[1])
    infos['tf'] = float(linhas[6].split()[1])

    infos['corretor'] = linhas[7].split()[1]
    infos['corretor'] = (infos['corretor'] == 'T')
    infos['colisoes'] = linhas[8].split()[1]
    infos['colisoes'] = (infos['colisoes'] == 'T')

    infos['N'] = int(linhas[11].split()[1])
    infos['G'] = float(linhas[12].split()[1])

    infos['massas']=[]
    inicio_massas = 15
    for i in range(inicio_massas,inicio_massas+infos['N']):
      infos['massas'].append(float(linhas[i]))

    infos['posicoes']=[]
    inicio_pos = inicio_massas+infos['N']+2
    for i in range(inicio_pos,inicio_pos+infos['N']):
      posicao = linhas[i].split(',')
      infos['posicoes'].append([float(x) for x in posicao[:3]])

    infos['momentos']=[]
    inicio_mom = inicio_pos+infos['N']+2
    for i in range(inicio_mom,inicio_mom+infos['N']):
      momento = linhas[i].split(',')
      infos['momentos'].append([float(x) for x in momento[:3]])

    infos['V']=mecanica.energia_potencial(infos['G'],infos['massas'],infos['posicoes'])
    infos['T']=mecanica.energia_cinetica(infos['massas'],infos['momentos'])

    # Integrais primeiras
    infos['H']=mecanica.energia_total(infos['G'],infos['massas'],infos['posicoes'],infos['momentos'])
    infos['P']=[round(x,2) for x in mecanica.momento_linear_total(infos['momentos'])]
    infos['Rcm']=[round(x,2) for x in mecanica.centro_de_massas(infos['massas'],infos['posicoes'])]
    infos['J']=[round(x,2) for x in mecanica.momento_angular_total(infos['posicoes'],infos['momentos'])]

  return infos

@eel.expose
def ler_sorteio (dir:str)->dict:
  infos = dict()
  with open(dir, 'r') as arq:
    # Quebra em linhas
    linhas = arq.read().split('\n')

    # Integrais primeiras
    infos['H'] = float(linhas[1].split()[1])
    infos['J'] = [float(x) for x in (linhas[2].split('Jtot')[1]).split(',')[:3]]
    infos['P'] = [float(x) for x in (linhas[3].split('Ptot')[1]).split(',')[:3]]
    infos['Rcm'] = [float(x) for x in (linhas[4].split('Rcm')[1]).split(',')[:3]]

    # Constantes
    infos['G'] = float(linhas[7].split()[1])
    infos['N'] = int(linhas[10].split()[1])

    # Intervalos para geracao
    infos['intervalo_massas'] =   [float(x) for x in (linhas[13].split('Intervalo-Massas')[1]).split(',')[:2]]
    infos['intervalo_posicoes'] = [float(x) for x in (linhas[14].split('Intervalo-Posicoes')[1]).split(',')[:2]]
    infos['intervalo_momentos'] = [float(x) for x in (linhas[15].split('Intervalo-Momentos')[1]).split(',')[:2]]

    # Integracao
    infos['integrador'] = linhas[18].split()[1]
    infos['timestep'] = float(linhas[19].split()[1])
    infos['passos'] = int(linhas[20].split()[1])
    
    infos['t0'] = float(linhas[23].split()[1])
    infos['tf'] = float(linhas[24].split()[1])

    infos['corretor'] = linhas[27].split()[1]
    infos['corretor'] = (infos['corretor'] == 'T')
    infos['colisoes'] = linhas[28].split()[1]
    infos['colisoes'] = (infos['colisoes'] == 'T')

  return infos

@eel.expose
def listar_dir (dir:str)->list:
  return listdir(dir)