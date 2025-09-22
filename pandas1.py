import pandas as pd

bNames = ["Noah","Liam","Jacob",
          "William","Mason","Ethan",
          "Michael","Alexander","James","Elijah"]

gNames = ["Emma","Olivia","Sophia,",
          "Isabella", "Ava", "Mia", 
          "Abigail","Emily", "Charlotte","Madison"]

bFreq =[103330, 173981,162266,
        159945,157875,149082,
        145171,142142,139652,137093]

gFreq = [195028,184520,181131,
        170559,155844,129088,
        118713,117626,102470,98419]

df = pd.DataFrame({
    'Boy Names: ':bNames, 
    'bFreq: ':bFreq, 
    'Girl Names: ':gNames,
    'gFreq: ':gFreq
    })
print(df)
print(df.describe())