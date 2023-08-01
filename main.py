import utils.utils as utils
import xlwt

if __name__ == "__main__" :
    # Membaca File inputan(mobil.xls)
    df = utils.readFile("data/mobil.xls")
    
    # Rename Kolom Harga Mobil
    df = df.rename(columns={'Harga (Ratus Juta)': 'Harga'})

    print("Data Mobil Sebelum Normalisasi\n==============================")
    print(df)
    print()

    # Membaca Inputan User
    inputUser = utils.readUser()
    print("\ninput User Sebelum Normalisasi :", inputUser)   

    # Normalisasi Data (Praprocessing Data)
 
    # Melakukan normalisasi data untuk data mobil dan data user
    dfNorm = utils.normalizeData(df, inputUser)
    print("Hasil Normalisasi Data dengan Metode Min Max\n=============================================")
    print(dfNorm)
    
    # Ambil input data user hasil Normalisasi
    inputUserNorm = []
    for i in range(len(inputUser)):
        inputUserNorm.append(dfNorm.iloc[len(dfNorm.axes[0]) - 1][i+1])
    print("\ninput User hasil Normalisasi :", inputUserNorm)

    # Euclidean Distance
    euclideanRes = utils.euclidean(inputUserNorm, dfNorm)

    # Manhattan Distance
    manhattanRes = utils.manhattan(inputUserNorm, dfNorm)

    # Mainkowski Distance
    minkowskiRes = utils.minkowski(inputUserNorm, dfNorm)

    # Supremum Distance
    supremumRes = utils.supremum(inputUserNorm, dfNorm)

    # Hasil Rekomendasi 3 data teratas
    print("Rekomendasi Mobil dengan Metode Euclidean Distance\n===================================================")
    for i in range(3):
        print(f"{i+1}. {euclideanRes.iloc[i+1][0]} dengan Ukuran {round(df.iloc[euclideanRes.index[i+1]][1],2)}; ", end="")
        print(f"Kenyamanan {round(df.iloc[euclideanRes.index[i+1]][2],2)}; ", end="")
        print(f"Irit {round(df.iloc[euclideanRes.index[i+1]][3],2)}; ", end="")
        print(f"Kecepatan {round(df.iloc[euclideanRes.index[i+1]][4],2)}; ", end="")
        print(f"Harga {round(df.iloc[euclideanRes.index[i+1]][5]*100,2)} Juta Rp")
    print()

    print("Rekomendasi Mobil dengan Metode Manhattan Distance\n===================================================")
    for i in range(3):
        print(f"{i+1}. {manhattanRes.iloc[i+1][0]} dengan Ukuran {round(df.iloc[manhattanRes.index[i+1]][1],2)}; ", end="")
        print(f"Kenyamanan {round(df.iloc[manhattanRes.index[i+1]][2],2)}; ", end="")
        print(f"Irit {round(df.iloc[manhattanRes.index[i+1]][3],2)}; ", end="")
        print(f"Kecepatan {round(df.iloc[manhattanRes.index[i+1]][4],2)}; ", end="")
        print(f"Harga {round(df.iloc[manhattanRes.index[i+1]][5]*100,2)} Juta Rp")
    print() 

    print("Rekomendasi Mobil dengan Metode Minkowski Distance\n===================================================")
    for i in range(3):
        print(f"{i+1}. {minkowskiRes.iloc[i+1][0]} dengan Ukuran {round(df.iloc[minkowskiRes.index[i+1]][1],2)}; ", end="")
        print(f"Kenyamanan {round(df.iloc[minkowskiRes.index[i+1]][2],2)}; ", end="")
        print(f"Irit {round(df.iloc[minkowskiRes.index[i+1]][3],2)}; ", end="")
        print(f"Kecepatan {round(df.iloc[minkowskiRes.index[i+1]][4],2)}; ", end="")
        print(f"Harga {round(df.iloc[minkowskiRes.index[i+1]][5]*100,2)} Juta Rp")
    print()

    print("Rekomendasi Mobil dengan Metode Supremum Distance\n===================================================")
    for i in range(3):
        print(f"{i+1}. {supremumRes.iloc[i+1][0]} dengan Ukuran {round(df.iloc[supremumRes.index[i+1]][1],2)}; ", end="")
        print(f"Kenyamanan {round(df.iloc[supremumRes.index[i+1]][2],2)}; ", end="")
        print(f"Irit {round(df.iloc[supremumRes.index[i+1]][3],2)}; ", end="")
        print(f"Kecepatan {round(df.iloc[supremumRes.index[i+1]][4],2)}; ", end="")
        print(f"Harga {round(df.iloc[supremumRes.index[i+1]][5]*100,2)} Juta Rp")

    # Output Excel Hasil Rekomendasi
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Output')

    for i in range(3):
        sheet.write(i,0, euclideanRes.iloc[i+1][0])

    wb.save('result/rekomendasi.xls')