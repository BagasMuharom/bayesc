import numpy as np
import dataset

def getJumlahData():
    jumlah_data = len(dataset.dataset)

    return jumlah_data

def hitung_probabilitas_hasil(target):
    final_result = []
    unique, counts = np.unique(target, return_counts = True)
    prob = dict(zip(unique, counts))
    
    for key, value in prob.items():
        final_result.append(value / getJumlahData())
        
    return final_result

def test(data):
    result = []
    for i in range(len(data)):
        temp = []
        for k in range(4):
            # print(data[i], ' ', (k+1), ' ', len(np.intersect1d(np.where(dataset.dataset[:,i] == data[i]), np.where(dataset.target == (k+1)))))
            temp.append(len(np.intersect1d(np.where(dataset.dataset[:,i] == data[i]), np.where(dataset.target == (k+1))))/ getJumlahData())
            
        result.append(temp)

    mult = []

    for i in range(4):
        multiply = np.prod(np.array(result)[:,i])
        mult.append(multiply)

    hasil = np.array(mult) * np.array(hitung_probabilitas_hasil(dataset.target))
    maks = np.max(hasil)
    index_hasil = np.where(hasil == maks)
        
    return hasil
