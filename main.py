import pandas as pd

df = pd.read_csv('data.csv')

print('Dataset = \n',df)

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"]/3

print("\n Dataset with Total and Average : \n",df)

toppers = df.loc[df['Average'].idxmax()]
print("\n Topper :", toppers['Name'])

failed = df[(df['Maths'] < 35) | (df['Science'] < 35) | (df['English'] < 35)]
print("\n Failed Students : ", failed['Name'].tolist())

print("\n Subject Averages : \n")
print(df[["Maths", "Science", "English"]].mean())


def grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    elif avg >= 50: return "C"
    elif avg >= 35: return "D"
    else: return "F"

df["Grade"] = df["Average"].apply(grade)
print("\n Dataset with Grades : \n", df)

df.to_csv('result_analysis.csv', index=False)
print("\n Result analysis saved to 'result_analysis.csv'")

import matplotlib.pyplot as plt
subjects = ["Maths", "Science", "English"]
averages = df[subjects].mean()
plt.bar(subjects, averages, color=['red', 'green', 'blue'])
plt.title('Subject Average Marks')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.show()


# Top Students (Based on Average Marks)
top_students = df.sort_values(by='Average', ascending=False).head(5)

plt.bar(top_students['Name'], top_students["Average"])
plt.title('Top 5 Students by Average Marks')
plt.xlabel('Students')
plt.ylabel('Average Marks')
plt.show()


df["Grade"].value_counts().plot(kind="bar")
plt.title('Grade Distribution')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.show()