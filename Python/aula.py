numeros = [1,3,4,5,6,7,9,13];
count = 0;

for i in numeros:
    if i % 2 != 0:
        count += 1;

print('Estão contidos, ', count,' números ímpares na lista');
