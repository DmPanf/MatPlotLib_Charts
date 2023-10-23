import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Настройка стиля
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

# Создание данных
data = {
    'Россия': [120, 80, 50, 30, 40],
    'США': [150, 90, 55, 35, 42],
    'Франция': [110, 70, 48, 29, 38],
    'Германия': [100, 85, 52, 28, 39],
    'Япония': [130, 75, 53, 31, 41]
}

df = pd.DataFrame(data, index=['Смартфоны', 'Ноутбуки', 'Наушники', 'Умные часы', 'Планшеты'])

# Построение графика
plt.figure(figsize=(12,8))
df.plot(kind='barh', stacked=True, figsize=(10,7))
plt.title('Продажи продуктов по странам', fontsize=15)
plt.xlabel('Продажи в миллионах долларов', fontsize=12)
plt.ylabel('Продукты', fontsize=12)
plt.legend(title='Страны')
plt.tight_layout()
plt.show()
