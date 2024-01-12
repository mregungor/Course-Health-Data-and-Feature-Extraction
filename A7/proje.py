import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# DOSYA YOLU OKUTMA
df = pd.read_csv(r'C:\\Users\\bnymn\Desktop\\data\\data.csv', header=0)

# GEREKSİZ VERİLERİ SİLME
df.drop('id', axis=1, inplace=True)
df.drop('Unnamed: 32', axis=1, inplace=True)

# KÖTÜ HUYLU:1 İYİ HUYLU:0

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})


# Hastalık durumuna göre 2 ayrı dataframe oluşturma
features_mean = list(df.columns[1:11])


dfM = df[df['diagnosis'] == 1]
dfB = df[df['diagnosis'] == 0]


# EĞİTİM VE TEST SETİ OLUŞTUR.
traindf, testdf = train_test_split(df, test_size=0.3)

# MODEL EĞİTİMİ
def classification_model(model, data, predictors, outcome):
    model.fit(data[predictors], data[outcome])

    # SETTEKİ ÖZELLİKLERE BAKARAK TAHMİN
    predictions = model.predict(data[predictors])

    # YAPILAN TAHMİNLERİN DOĞRULUK HESAPLAMASI
    accuracy = metrics.accuracy_score(predictions, data[outcome])
    print("Doğruluk : %s" % "{0:.3%}".format(accuracy))

    # 5 KATLI ÇARPRAZ DOĞRULAMA
    kf = KFold(n_splits=5)
    error = []
    for train, test in kf.split(data):
        # Eğitim verilerinin filtrelenmesi
        train_predictors = data[predictors].iloc[train, :]

        # Algoritmayı eğitmek için hedef seçimi
        train_target = data[outcome].iloc[train]

        model.fit(train_predictors, train_target)

        # Her çapraz doğrulama çalışmasından hata kaydı
        error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))

    print("Çapraz Doğrulama Skoru : %s" % "{0:.3%}".format(np.mean(error)))

    # MODELİ TEKRAR EĞİT.
    model.fit(data[predictors], data[outcome])

# Using top 5 features
predictor_var = ['concave points_mean','area_mean','radius_mean','perimeter_mean','concavity_mean']
outcome_var = 'diagnosis'
model = RandomForestClassifier(n_estimators=100, min_samples_split=25, max_depth=7, max_features=2)
classification_model(model, traindf, predictor_var, outcome_var)

# Kullanıcıdan özellik değerlerini al
concave_points_mean = float(input("concave points mean: "))
area_mean = float(input("area mean: "))
radius_mean = float(input("radius mean: "))
perimeter_mean = float(input("perimeter mean: "))
concavity_mean = float(input("concavity mean: "))

# Yeni veriyi oluştur
new_data = pd.DataFrame({
    'concave points_mean': [concave_points_mean],
    'area_mean': [area_mean],
    'radius_mean': [radius_mean],
    'perimeter_mean': [perimeter_mean],
    'concavity_mean': [concavity_mean],
})

# 3. Tahmin Yapma
predictions = model.predict(new_data)
print("Tahminler:", predictions)


