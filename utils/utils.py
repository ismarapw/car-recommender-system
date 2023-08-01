import pandas as pd

# fungsi Membaca File Inputan mobil.xls 
def readFile(filename):
    file = pd.read_excel(filename)
    return file

# fungsi membaca input user
def readUser():
    arrOfInput = []

    # input ukuran
    ukuran = input("Masukkan Ukuran: ")
    arrOfInput.append(float(ukuran)) 

    # input kenyamanan
    kenyamanan = input("Masukkan Kenyamanan: ")
    arrOfInput.append(float(kenyamanan))  

    # input irit
    irit = input("Masukkan Irit: ")
    arrOfInput.append(float(irit))  

    # input kecepatan
    kecepatan = input("Masukkan Kecepatan: ")
    arrOfInput.append(float(kecepatan)) 

    # input harga
    harga = input("Masukkan Harga: ")
    arrOfInput.append(float(harga))

    return arrOfInput

def getResult(dataFrame, jarak):
    # copy data biar data asli tidak berubah
    resData = dataFrame.copy()
    
    # tambah atribut/kolom distance pada data frame
    resData["Distance"] = jarak

    # Sort dataframe by Distance    
    resData = resData.sort_values(by=["Distance"])
    
    return resData


# Fungsi Euclidean Distance
def euclidean(dataUser, dataMobil):
    euclidList = []

    for i in range (len(dataMobil.axes[0])):
        d = 0
        temp = 0
        
        for j in range (len(dataUser)):
            xiMinxjPow = (dataUser[j] - dataMobil.iloc[i][j + 1])**2
            temp = temp + xiMinxjPow
        
        d = temp**0.5
        euclidList.append(d)
    
    result = getResult(dataMobil, euclidList)
    return result

# Fungsi Manhattan Distance
def manhattan(dataUser, dataMobil):
    manhattList = []

    for i in range (len(dataMobil.axes[0])):
        d = 0
        temp = 0
        
        for j in range (len(dataUser)):
            xiMinxjAbs = abs(dataUser[j] - dataMobil.iloc[i][j + 1])
            temp = temp + xiMinxjAbs
        
        d = temp
        manhattList.append(d)
        
    result = getResult(dataMobil, manhattList)
    return result

# Fungsi Minkowski Distance
def minkowski(dataUser, dataMobil):
    minkowList = []
    h = 3

    for i in range (len(dataMobil.axes[0])):
        d = 0
        temp = 0
        
        for j in range (len(dataUser)):
            xiMinxjAbsPow = (abs(dataUser[j] - dataMobil.iloc[i][j + 1]))**h
            temp = temp + xiMinxjAbsPow
        
        d = temp**(1/h)
        minkowList.append(d)
    
    result = getResult(dataMobil, minkowList)
    return result


# Fungsi Supremum Distance
def supremum(dataUser, dataMobil):
    supremumList = []

    for i in range (len(dataMobil.axes[0])):
        d = 0
        temp = []
        
        for j in range (len(dataUser)):
            xiMinxjAbs = abs(dataUser[j] - dataMobil.iloc[i][j + 1])
            temp.append(xiMinxjAbs)
            
        d = max(temp)
        supremumList.append(d)
    
    result = getResult(dataMobil, supremumList)
    return result
        
# Fungsi Normalisasi
def normalizeData(dataMobil, dataUser):
    # Membuat dataframe user 
    dfUser = pd.DataFrame({
        "Nama Mobil" : ["User Input"],
        "Ukuran" : [dataUser[0]],
        "Kenyamanan" : [dataUser[1]],
        "Irit" : [dataUser[2]],
        "Kecepatan" : [dataUser[3]],
        "Harga" : [dataUser[4]],
    })

    # Membuat dataframe baru untuk normalisasi
    normRes = dataMobil.copy()

    # Menyatukan dataframe user input ke data frame mobil
    normRes = pd.concat([normRes, dfUser], ignore_index = True)

    # Normalisasi Data Frame
    normRes["Ukuran"] = (normRes["Ukuran"] - normRes["Ukuran"].min())/(normRes["Ukuran"].max() - normRes["Ukuran"].min())
    normRes["Kenyamanan"] = (normRes["Kenyamanan"] - normRes["Kenyamanan"].min())/(normRes["Kenyamanan"].max() - normRes["Kenyamanan"].min())
    normRes["Irit"] = (normRes["Irit"] - normRes["Irit"].min())/(normRes["Irit"].max() - normRes["Irit"].min())
    normRes["Kecepatan"] = (normRes["Kecepatan"] - normRes["Kecepatan"].min())/(normRes["Kecepatan"].max() - normRes["Kecepatan"].min())
    normRes["Harga"] = (normRes["Harga"] - normRes["Harga"].min())/(normRes["Harga"].max() - normRes["Harga"].min())
    
    return normRes