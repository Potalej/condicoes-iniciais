def momento_linear_total (momentos_lineares):
  P=[0.0,0.0,0.0]
  for p in momentos_lineares:
    for i in range(3):
      P[i] += p[i]
  return P

def centro_de_massas (massas, posicoes):
  M = sum(massas)
  Rcm = [0.0,0.0,0.0]
  for i,R in enumerate(posicoes):
    for j in range(3):
      Rcm[j] += R[j]*massas[i]/M
  return Rcm

def momento_angular_total (posicoes, momentos_lineares):
  J = [0.0,0.0,0.0]
  for a in range(len(posicoes)):
    r, p = posicoes[a], momentos_lineares[a]
    J[0] += r[1]*p[2]-r[2]*p[1]
    J[1] += -(r[0]*p[2]-r[0]*p[2])
    J[0] += r[0]*p[1]-r[1]*p[0]
  return J

def prod_int (u,v):
  return sum(u[i]*v[i] for i in range(3))

def norma2 (u): return prod_int(u,u)

def energia_cinetica (massas, momentos_lineares):
  return sum(norma2(momentos_lineares[a])/(2*massas[a]) for a in range(len(massas)))

def energia_potencial (G, massas, posicoes):
  V = 0.0
  for a in range(len(massas)):
    ma,ra = massas[a], posicoes[a]
    for b in range(a):
      mb,rb = massas[b], posicoes[b]
      rb_ra = [rb[i]-ra[i] for i in range(3)]
      V -= G*ma*mb/(norma2(rb_ra)**(1/2))
  return V

def energia_total (G, massas, posicoes, momentos_lineares):
  H=0.0
  for a in range(len(massas)):
    ma,ra,pa = massas[a], posicoes[a], momentos_lineares[a]
    # Energia cinetica
    H += norma2(pa)/(2*ma)
    # Energia potencial
    V = 0.0
    for b in range(a):
      mb,rb,pb = massas[b], posicoes[b], momentos_lineares[b]
      rb_ra = [rb[i]-ra[i] for i in range(3)]
      V -= G*ma*mb/(norma2(rb_ra)**(1/2))
    H += V
  return H