import pandas as pd

df = pd.read_csv('Data.csv')

df = df[df['Salary Estimate'] != '-1']
df = df.reset_index()
df = df.drop(['index'], axis=1)
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x.replace('K','').replace('$',''))
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x if 'Per Hour' not in x else 0)
df = df[df['Salary Estimate'] != 0]
df['Min Salary'] = df['Salary Estimate'].apply(lambda x:int(x.split(' - ')[0]))
df['Max Salary'] = df['Salary Estimate'].apply(lambda x:int(x.split(' - ')[1]))
df['Average Salary'] = (df['Min Salary'] + df['Max Salary']) / 2
df = df[df['Location'] != 'Remote']
df['Job State'] = df['Location'].apply(lambda x:x.split(', ')[1])
df.drop(['Headquarters', 'Competitors'], axis=1, inplace=True)
df['Age'] = df['Founded'].apply(lambda x:2020-x if x!=-1 else x)
df['Python'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
df['Spark'] = df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)


df.to_csv('filtered.csv', index=False)