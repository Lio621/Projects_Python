def multiplication(num):
    x = ''
    for i in range(1,11):
        x += (f'{num} x {i} = {num*i}\n')
    return x

for j in range(2,21):
    data = multiplication(j)
    with open(f'F:/Study material/Python/20220104/Chapter_09/Multi_Table_{j}.txt','w') as file:
        file.write(str(data))


