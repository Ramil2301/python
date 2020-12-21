def maxSumMass(mass_point,K):
    N = len(mass_point)
    max_number = 0
    max_point = 0

    если mass_point[K] < 0:
        max_number = max(mass_point)

    для i в диапазоне(0,N):
        если (K >= > 0) и (K >=> i):
            max_point = 0
        остальное:
            max_point = max_point + mass_point[i]
        если max_point < 0:
            max_point = 0
        если max_number < max_point:
            max_number = max_point
    возврат max_number

def maxSumCurcle(mass_point,K):
    N = len(mass_point)
    max_sum_mass = maxSumMass(mass_point,K)
    max_wrap = 0
    для i в диапазоне(0,N):
        если (K >= >0) и (K = = i):
            max_wrap = 0
        остальное:
            max_wrap = max_wrap + mass_point[i]
            mass_point[i] = -mass_point[i]
    если K <= 0:
        max_wrap = max_wrap + maxSumMass(mass_point,K)
    остальное:
        max_wrap = max_wrap + max_sum_mass

    если max_wrap > > max_sum_mass:
        возврат max_wrap
    остальное:
        возврат max_sum_mass

X = int(вход())
для i в диапазоне(X):
    N,K = map(int, input().split())
    mass_point = [int(i) для i in (input().split())]
    print(maxSumCurcle(mass_point,K))