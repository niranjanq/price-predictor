import pandas as pd

df = pd.read_csv("laptop_data.csv")

# ======================================== SSD ========================

print(df['Memory'].head(24))

# print(df['Memory'].str.split('SSD').head(24))

df['test_ssd'] = df['Memory'].str.split('SSD')

df['test_ssd'] = df['test_ssd'].apply(lambda x:  x[0] if len(x) == 2 else 0)


df['test_ssd'] = df['test_ssd'].apply(lambda x:  x.split('GB')[0] if 'GB' in str(x) else x.split('TB')[0] if 'TB' in str(x) else 0)

df['SSD'] = df['test_ssd'].astype('float32')
df['SSD'] = df['SSD'].astype('int32')



# =============================================== hdd ========================
# print(df['Memory'].head(24))


df['test_hdd'] = df['Memory'].str.split('+' or 'HDD')

# print(df['test_hdd'].head(24))

df['test_hdd'] = df['test_hdd'].apply(lambda x:  x[-1] if len(x) == 2 else  x[0]  if "HDD" in x[0] else 0)
# print(df['test_hdd'].head(24))
# print(df['test_hdd'].apply(lambda x:  x.split('GB')[0] if 'GB' in str(x) else x.split('TB')[0] if 'TB' in str(x) else 0 ).head(24))

df['test_hdd'] = df['test_hdd'].apply(lambda x:  x.split('GB')[0] if 'GB' in str(x) else x.split('TB')[0] if 'TB' in str(x) else 0 )
#
# print(df['test_hdd'].sample(24))
df['HDD'] = df['test_hdd'].astype('float32')
df['HDD'] = df['HDD'].astype('int32')
df['HDD'] = df['HDD'].apply(lambda x: x*1024 if x<10 else x)
# print(df['HDD'].head(24))


df.drop(columns=['test_ssd','test_hdd'],inplace=True)
# print(df['Memory'].head(24))
print(df.head(24))

# print(sorted(df['Inches'].unique(),reverse=True))

print(df.corr()['Price'])

# Apply these all changes in my main file of EDA and Feature Engineering

