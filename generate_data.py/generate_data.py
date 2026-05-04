import pandas as pd
import random

names = ["Rahul","Sita","Amit","Riya","Arjun","Pooja","Kiran","Neha","Vikas","Anita"]
genders = ["Male","Female"]
occupations = ["Student","Engineer","Teacher","Doctor","Farmer","Driver","Labor","Business","Unemployed"]
education = ["Primary","Secondary","Graduate","Postgraduate"]
states = ["Madhya Pradesh","Uttar Pradesh","Bihar","Delhi","Rajasthan","Maharashtra"]

data = []

for i in range(500):
    row = [
        random.choice(names),
        random.randint(-5, 120),   # invalid + valid ages
        random.choice(genders),
        random.randint(-5000, 2000000),  # invalid + valid income
        random.choice(occupations),
        random.choice(education),
        random.randint(0, 10),  # family size
        random.choice(states),
        random.choice(["Yes","No"]),
        random.choice(["Yes","No"])
    ]
    data.append(row)

columns = ["Name","Age","Gender","Income","Occupation","Education","FamilySize","State","HasElectricity","HasInternet"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data.csv", index=False)

print("✅ 500 rows dataset created successfully!")