def tablu(n):
    with open(f'tablegenerator/tablebook/table_{i}.txt','w') as f:
        for n in range(1,11):
            f.write(f'{i} X {n} = {n*i}\n')

for i in range(2,21):
    tablu(i)