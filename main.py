import pandas as pd

data = {
    'Имя': ['Андрей', 'Борис', 'Виктория', 'Галина', 'Дмитрий', 'Елена', 'Жанна', 'Иван', 'Ксения', 'Леонид'],
    'Математика': [5, 4, 3, 5, 2, 4, 3, 5, 4, 5],
    'Физика': [4, 3, 5, 4, 3, 4, 5, 3, 4, 5],
    'Химия': [3, 4, 2, 5, 4, 3, 4, 5, 4, 3],
    'Литература': [5, 5, 4, 4, 3, 5, 4, 3, 4, 5],
    'История': [4, 3, 5, 4, 5, 2, 3, 4, 5, 4]
}
df = pd.DataFrame(data)
print(df)

mean_scores = df.mean(numeric_only=True)
print("Средние оценки по предметам:")
print(mean_scores)


median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
print(median_scores)

standart = df.std(numeric_only=True)
print("\nСтандартное отклонение по предметам:")
print(standart)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("IQR для оценок по математике:", IQR_math)

