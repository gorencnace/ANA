def reduce_nq_sat(n):
    table = [[i+j for j in range(n)] for i in range(1, n*(n-1)+n, n)]
    klavzule = [[i+j for j in range(n)] for i in range(1, n*(n-1)+n, n)]
    klavazulele = []
    for j in range(n):
        tmp = []
        for i in range(1, n*(n-1)+n, n):
            tmp.append(i+j)
        klavzule.append(tmp)
    count = 0
    for k in klavzule:
        klavzula = ''
        for i in k:
            klavzula += str(i) + ' '
        klavazulele.append(klavzula + '0')
        count +=1

    for col in range(1, n):
        startcol = col
        startrow = 0
        klavzula = []
        while startcol >= 0 and startrow < n:
            klavzula.append(table[startrow][startcol])
            startcol -= 1
            startrow += 1
        klavzule.append(klavzula)

    for row in range(1, n-1):
        startrow = row
        startcol = n-1
        klavzula = []
        while startrow < n and startcol >= 0:
            klavzula.append(table[startrow][startcol])
            startcol -= 1
            startrow += 1
        klavzule.append(klavzula)

    for col in range(n-1):
        startcol = col
        startrow = 0
        klavzula = []
        while startcol < n and startrow < n:
            klavzula.append(table[startrow][startcol])
            startcol += 1
            startrow += 1
        klavzule.append(klavzula)

    for row in range(1, n - 1):
        startrow = row
        startcol = 0
        klavzula = []
        while startrow < n and startcol < n:
            klavzula.append(table[startrow][startcol])
            startcol += 1
            startrow += 1
        klavzule.append(klavzula)

    for k in klavzule:
        for i in k:
            for j in k:
                if i < j:
                    klavazulele.append(str(-i) + ' ' + str(-j) + ' 0')
                    count += 1
    print('p cnf ' + str(n**2) + ' ' + str(count))
    for i in klavazulele:
        print(i)

if __name__ == '__main__':
    reduce_nq_sat(4)
