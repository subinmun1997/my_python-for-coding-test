n = 1260
count = 0

coin_type=[500,100,50,10]

for coin in coin_type:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin

print(count)