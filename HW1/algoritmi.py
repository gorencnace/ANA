# N KRALJIC
def reduce_nq_sat(n):
    table = [[i + j for j in range(n)] for i in range(1, n * (n - 1) + n, n)]
    klavzule = [[i + j for j in range(n)] for i in range(1, n * (n - 1) + n, n)]
    klavazulele = []
    for j in range(n):
        tmp = []
        for i in range(1, n * (n - 1) + n, n):
            tmp.append(i + j)
        klavzule.append(tmp)
    count = 0
    for k in klavzule:
        klavzula = ''
        for i in k:
            klavzula += str(i) + ' '
        klavazulele.append(klavzula + '0')
        count += 1

    for col in range(1, n):
        startcol = col
        startrow = 0
        klavzula = []
        while startcol >= 0 and startrow < n:
            klavzula.append(table[startrow][startcol])
            startcol -= 1
            startrow += 1
        klavzule.append(klavzula)

    for row in range(1, n - 1):
        startrow = row
        startcol = n - 1
        klavzula = []
        while startrow < n and startcol >= 0:
            klavzula.append(table[startrow][startcol])
            startcol -= 1
            startrow += 1
        klavzule.append(klavzula)

    for col in range(n - 1):
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
    print('p cnf ' + str(n ** 2) + ' ' + str(count))
    for i in klavazulele:
        print(i)



# DOMINANTNA MNOŽICA
def dominating_set(g, k, name):
    spr = {v: {q: None for q in range(1, k + 1)} for v in range(1, len(g) + 1)}

    i = 1
    for v, d in spr.items():
        for q in d.keys():
            spr[v][q] = i
            i += 1

    txt = ''

    for v in g.keys():
        for w in g.keys():
            if v < w:
                for i in range(1, k + 1):
                    txt += str(-spr[v][i]) + ' ' + str(-spr[w][i]) + ' 0\n'

    for v, e in g.items():
        str_v = ''
        for i in range(1, k + 1):
            str_v += str(spr[v][i]) + ' '
        for w in e:
            str_w = ''
            for i in range(1, k+1):
                str_w += str(spr[w][i]) + ' '
            str_v += str_w
        txt += str_v + '0\n'

    f = open(name, 'w')
    f.write(txt)
    f.close()


def get_graph(file):
    g = None
    with open(file) as f:
        for line in f:
            if line.startswith('p'):
                n = int(line.split()[-2])
                g = {i: [] for i in range(1, n + 1)}
            else:
                a = int(line.split()[-2])
                b = int(line.split()[-1])
                g[a].append(b)
                g[b].append(a)
    return g


def reduce_ds_sat():
    g = get_graph('data/g2.col')
    dominating_set(g, 3, 'g2.txt')



def tvori_pi(p):
    pi = [0] * len(p)
    k = 0
    for q in range(1, len(p)):
        while k > 0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k += 1
        pi[q] = k
    print(pi)


def is_am(codon):
    s = 0
    i = 0
    sez = []
    for c in codon:
        if c == 'A':
            if s == 0:
                s = 1
            elif s == 1:
                s = 2
            elif s == 2:
                i += 1
                s = 2
            elif s == 3:
                s = 4
            elif s == 4:
                i += 3
                s = 2
            else:
                i += 5
                s = 1
        elif c == 'U':
            if s == 2:
                s = 3
            elif s == 4:
                s = 5
            else:
                i += s + 1
                s = 0
        elif c == 'C':
            if s == 2:
                s = 3
            else:
                i += s + 1
                s = 0
        elif c == 'G':
            if s == 5:
                sez.append(i)
            i += s + 1
            s = 0
        else:
            i += s + 1
            s = 0
    print(len(sez))



if __name__ == '__main__':
    # klic funkcije problema n kraljic
    #reduce_nq_sat(4)
    # klic funkcije prevedbe dominantne množice
    #reduce_ds_sat()
    f = open('data/generated_genome.txt', 'r')
    s = f.readline()
    is_am(s)
