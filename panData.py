import pandas as pd
import random

fNames = ['Kevin', 'John', 'David', 'Chris', 
          'Mike', 'Mark', 'Paul', 'Daniel', 
          'James', 'Robert', 'Mary', 'Patricia', 
          'Jennifer', 'Linda', 'Elizabeth',
          'Kanye']

lNames = ["Smith", "Johnson", "Williams", "Jones", 
          "Brown", "Davis", "Miller","Wilson", 
          "Moore", "Taylor ", "Anderson", "Thomas",
          "West"]

years = ["Freshman","Sophomore","Jenior","Senior","Super Senior"]
pathways = ["Early College","Engineering","Business","Marketing","Early Childhood Education","Criminal Justice","Biology","Medical"]
names = []

for i in range(2000):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(14,19) for _ in names],
    "GPA": [round(random.uniform(0.3,4.5),2) for _ in names],
    "Credits Completed": [random.randint(0,60) for  _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}
pennData = pd.DataFrame(data)
pennData.to_csv("pennData.csv", index=False)
print(pennData)
print(names)