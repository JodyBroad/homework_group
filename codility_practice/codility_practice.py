E = '10:00'
L = '13:21'

# this worked and got 100% on the tests
def parking_solution(E, L):
    hours_e_int = int(E[:2])
    hours_l_int = int(L[:2])
    mins_e_int = int(E[-2:])
    mins_l_int = int(L[-2:])
    total_hours = hours_l_int - hours_e_int
    total_minutes = mins_l_int - mins_e_int
    print(total_hours)
    print(total_minutes)
    if total_minutes > 0:
        total_hours += 1

    total_cost = 2 + 3 + (4 * (total_hours - 1))
    print(total_cost)

parking_solution('10:00', '13:21')


# this seemed work but failed all the more extensive tests
def solution(N):
    k = 0
    a = 2

    while a < N:
        a_doubled = a * 2
        k += 1
        a = a_doubled
    return k

print(solution(24))



