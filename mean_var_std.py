import numpy as np

def calculate(lista):

  if len(lista) != 9:
      raise ValueError("List must contain nine numbers.")

  else:
    dicta = {
    'mean' : [], 
    'variance' : [],
    'standard deviation' : [],
    'max' : [],
    'min' : [],
    'sum' : []
}
    ListaReshaped = (np.array(lista).reshape(3,3))
    mean = [np.mean(ListaReshaped, axis=0).tolist(), np.mean(ListaReshaped, axis=1).tolist(), np.mean(ListaReshaped)]
    variance = [np.var(ListaReshaped, axis=0).tolist(),   np.var(ListaReshaped, axis=1).tolist(), np.var(ListaReshaped)]
    std = [np.std(ListaReshaped, axis=0).tolist(), np.std(ListaReshaped, axis=1).tolist(), np.std(ListaReshaped)]
    maxi = [np.max(ListaReshaped, axis=0).tolist(), np.max(ListaReshaped, axis=1).tolist(), np.max(ListaReshaped)]
    mini = [np.min(ListaReshaped, axis=0).tolist(), np.min(ListaReshaped, axis=1).tolist(), np.min(ListaReshaped)]
    sumi = [np.sum(ListaReshaped, axis=0).tolist(), np.sum(ListaReshaped, axis=1).tolist(), np.sum(ListaReshaped)]


    dicta['mean'] = mean
    dicta['variance'] = variance
    dicta['standard deviation'] = std
    dicta['max'] = maxi
    dicta['min'] = mini
    dicta['sum'] = sumi

    calculations = dicta
    
  return calculations
