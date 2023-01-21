def measure_to_points(measure):
    return 50 - measure ** 1.5 * 40

def calc(measure):
#     am54のスコア　＝
# 　（am54の値　－　0.75）　÷　（1　－　0.75）　×　100
    return (0.75 - 0.75) / (1 - 0.75) * 100

for i in range(0, 11):
    mes = i/10
    
    print("area ratio:", mes, ", score:", calc(mes))
    # print("area ratio:", mes, ", score:", measure_to_points(mes))

a = [[180, 0, 20], [2,6,8]]
b = a
# b[0] = 90
# b = [a[0] - 90, a[1], a[2]]
b[0][0] += 90
print(a)
print(b)