import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier  # Decision Tree'yi İçe Aktar
from sklearn import metrics

# DOSYA YOLU OKUTMA
df = pd.read_csv(r'C:\\Users\\bnymn\Desktop\\data\\data.csv', header=0)
print(df.head())

# GEREKSİZ VERİLERİ SİLME
df.drop('id', axis=1, inplace=True)
df.drop('Unnamed: 32', axis=1, inplace=True)

# KÖTÜ HUYLU:1 İYİ HUYLU:0
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
print(df.head())

# VERİYİ KEŞFET
pd.set_option('display.max_columns', None)
print(df.describe())
# Hasta sınıflandırması histogramı
df.describe()
plt.hist(df['diagnosis'])
plt.title('Teşhis (M=1, B=0)')
plt.show()

# Hastalık durumuna göre 2 ayrı dataframe oluşturma
features_mean = list(df.columns[1:11])
dfM = df[df['diagnosis'] == 1]
dfB = df[df['diagnosis'] == 0]

# ÖZELLİK HİSTOGRAMLARI
plt.rcParams.update({'font.size': 8})
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(8, 10))
axes = axes.ravel()

for idx, ax in enumerate(axes):
    ax.figure
    binwidth = (max(df[features_mean[idx]]) - min(df[features_mean[idx]])) / 50
    ax.hist([dfM[features_mean[idx]], dfB[features_mean[idx]]], bins=np.arange(min(df[features_mean[idx]]), max(df[features_mean[idx]]) + binwidth, binwidth), alpha=0.5, stacked=True, density=True, label=['Kötü', 'İyi'], color=['r', 'g'])
    ax.legend(loc='upper right')
    ax.set_title(features_mean[idx])

plt.tight_layout()
plt.show()

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
tahminci_degisken = ['concave points_mean', 'area_mean', 'radius_mean', 'perimeter_mean', 'concavity_mean']
sonuc_degiskeni = 'diagnosis'

# RandomForestClassifier
rf_modeli = RandomForestClassifier(n_estimators=100, min_samples_split=25, max_depth=7, max_features=2)

# Support Vector MachİNE
svm_modeli = SVC(kernel='linear', C=1)

# Logistic Regression
log_reg_model = LogisticRegression(max_iter=1000)

# Decision Tree
dt_modeli = DecisionTreeClassifier()

# Modelleri Karşılaştır
def modelleri_karsilastir(model1, model2, model3, model4, veri, tahminciler, sonuc):
    print("\nModelleri Karşılaştırma:")
    print("=" * 30)

    # RandomForestClassifier
    print("\nRandomForestClassifier:")
    classification_model(model1, veri, tahminciler, sonuc)

    # Support Vector Machine (SVM)
    print("\nDestek Vektör Makinesi (SVM):")
    classification_model(model2, veri, tahminciler, sonuc)

    # Logistic Regression
    print("\nLogistic Regression:")
    classification_model(model3, veri, tahminciler, sonuc)

    # Decision Tree
    print("\nDecision Tree:")
    classification_model(model4, veri, tahminciler, sonuc)

modelleri_karsilastir(rf_modeli, svm_modeli, log_reg_model, dt_modeli, traindf, tahminci_degisken, sonuc_degiskeni)

# 2. Yeni Verileri Hazırlama
# Örnek: Yeni verileri bir DataFrame'e ekleyerek
new_data = pd.DataFrame({
    'concave points_mean': [0.1471],
    'area_mean': [1001],
    'radius_mean': [17.99],
    'perimeter_mean': [122.8],
    'concavity_mean': [0.3001],
})
###### MAKİNANIN TAHMİNİ 1 OLMALI.

# 3. Tahmin Yapma
predictions_rf = rf_modeli.predict(new_data)
predictions_svm = svm_modeli.predict(new_data)
predictions_log_reg = log_reg_model.predict(new_data)
predictions_dt = dt_modeli.predict(new_data)
print("===========================================")
print("RandomForestClassifier Tahminleri:", predictions_rf)
print("SVM Tahminleri:", predictions_svm)
print("Logistic Regression Tahminleri:", predictions_log_reg)
print("Decision Tree Tahminleri:", predictions_dt)

## RANDOMFOREST DAHA YUKSEK DOGRULUK ORANINA SAHIP.
