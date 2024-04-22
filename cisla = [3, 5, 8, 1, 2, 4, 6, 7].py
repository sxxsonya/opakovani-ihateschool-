cisla = [3, 5, 8, 1, 2, 4, 6, 7]

cisla_sorted = sorted(cisla)
print (cisla_sorted)

cisla_sorted_reverse = sorted(cisla, reverse=True)
print(cisla_sorted_reverse)

sumarize = sum(cisla)
prumerna_hodnota = sumarize/len(cisla)
print(prumerna_hodnota)

for i in range(0, len(cisla)):
    for k in range(i+1, len(cisla)):
        if cisla[i] >= cisla[k]:
            cisla[i], cisla[k] = cisla[k], cisla[i]
print(cisla)

for i in range(0, len(cisla)):
    for k in range(i+1, len(cisla)):
        if cisla[i] <= cisla[k]:
            cisla[i], cisla[k] = cisla[k], cisla[i]
print(cisla)

total_sum = int(0)
misto_cisla= int(0)

while misto_cisla < len(cisla):
    total_sum = total_sum + cisla[misto_cisla]
misto_cisla +=1

prumerna_hodnota_plus_sum = total_sum/len(cisla) 

print(prumerna_hodnota_plus_sum)

