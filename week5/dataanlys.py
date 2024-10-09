import pandas as pd

# Example
my_marks = pd.Series([45, 56, 76, 86, 53, 34, 61], index=[
    "Math", "Sci", "Geog", "Phy", "CRE", "Comm", "Econ"])
print("Marks obtained by the student are: ", my_marks)
df_marks = pd.DataFrame(my_marks, columns=["student1"])
print("The data frame created from the data series is: \n", df_marks)


# Example
heights = pd.Series([5.3, 5.8, 5.0, 4.7], index=[
                    "Ozzy", "Rogers", "Joan", "John"])
weights = pd.Series([50, 62, 76, 56], index=["Ozzy", "Rogers", "Joan", "John"])

df_person = pd.DataFrame({"Height": heights, "Weight": weights})
print("The personal details are: \n", df_person)
