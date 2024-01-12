import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from PyQt5.QtWidgets import QMessageBox

df = pd.read_csv(r'C:\Users\arda\PycharmProjects\PROJELAAAA\\data.csv', header=0)

df.drop('id', axis=1, inplace=True)
df.drop('Unnamed: 32', axis=1, inplace=True)

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

features_mean = list(df.columns[1:11])

dfM = df[df['diagnosis'] == 1]
dfB = df[df['diagnosis'] == 0]

traindf, testdf = train_test_split(df, test_size=0.3)

def classification_model(model, data, predictors, outcome):
    model.fit(data[predictors], data[outcome])

    predictions = model.predict(data[predictors])

    accuracy = metrics.accuracy_score(predictions, data[outcome])
    print(accuracy) #konsolda görmek içi

    kf = KFold(n_splits=5)
    error = []
    for train, test in kf.split(data):
        train_predictors = data[predictors].iloc[train, :]

        train_target = data[outcome].iloc[train]

        model.fit(train_predictors, train_target)

        error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))

    model.fit(data[predictors], data[outcome])

predictor_var = ['concave points_mean','area_mean','radius_mean','perimeter_mean','concavity_mean']
outcome_var = 'diagnosis'
model = RandomForestClassifier(n_estimators=100, min_samples_split=25, max_depth=7, max_features=2)
classification_model(model, traindf, predictor_var, outcome_var)

def tahmin_yap(Ortalama_İçbükey_Noktalar,Ortalama_Alan,Ortalama_Yarıçap,Ortalama_Çevresi,Ortalama_İçbükeylik):
    #predictor_var = ['İçbükey Noktalar Hatası','Ortalama Alan','Ortalama Yarıçap','Ortalama Çevresi','Ortalama İçbükeylik']
    concave_points_mean = float(Ortalama_İçbükey_Noktalar)
    area_mean = float(Ortalama_Alan)
    radius_mean = float(Ortalama_Yarıçap)
    perimeter_mean = float(Ortalama_Çevresi)
    concavity_mean = float(Ortalama_İçbükeylik)

    new_data = pd.DataFrame({
        'concave points_mean': [concave_points_mean],
        'area_mean': [area_mean],
        'radius_mean': [radius_mean],
        'perimeter_mean': [perimeter_mean],
        'concavity_mean': [concavity_mean],
    })
    tahmin = model.predict(new_data)

    if tahmin[0] == 0:
        QMessageBox.information(None, 'Tümür Huy', 'Tümör iyi huylu (beign) olarak tahmin ediliyor.')
        tumors = 'B'
    else:
        QMessageBox.information(None, 'Tümür Huy', 'Tümör kötü huylu (malign) olarak tahmin ediliyor.')
        tumors = 'M'

    return tumors
