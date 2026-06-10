import pandas as pd



df = pd.DataFrame(
        [
            {'name': "a", 'type': "b", 'int': "1"},
            {'name': "a", 'type': "c", 'int': "2"},
            {'name': "b", 'type': "b", 'int': "3"},
            {'name': "c", 'type': "c", 'int': "4"},
            {'name': "b", 'type': "c", 'int': "5"},
        ]
    )
print(df)

print(df.where(df["name"]==df["type"]))
print(df[df["name"]==df["type"]])
