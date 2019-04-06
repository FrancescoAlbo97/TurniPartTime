import pulp

persone = ['x', 'bi', 'ugo', 'albo', 'lollo', 'chiara', 'selenia', 'pancotto', 'giacomino', 'eugenietto', 'ermenegildo', 'francescopio', 'gianmichelino', 'francescomario', 'annamariateresa', 'elkammmmmmmmoide']

ore = ['1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h', '22h', '23h', '24h', '25h']

hMax = {'x': 1, 'bi': 3, 'ugo': 4, 'albo': 4, 'lollo': 3, 'chiara': 4, 'selenia': 4, 'pancotto': 4, 'giacomino': 4, 'eugenietto': 4, 'ermenegildo': 2, 'francescopio': 4, 'gianmichelino': 4, 'francescomario': 4, 'annamariateresa': 4, 'elkammmmmmmmoide': 4}
hMin = {'x': 1, 'bi': 3, 'ugo': 3, 'albo': 3, 'lollo': 3, 'chiara': 3, 'selenia': 3, 'pancotto': 3, 'giacomino': 3, 'eugenietto': 3, 'ermenegildo': 2, 'francescopio': 3, 'gianmichelino': 3, 'francescomario': 3, 'annamariateresa': 3, 'elkammmmmmmmoide': 3}


disponibilita ={
'x': {'1h': 1, '2h': 0, '3h': 0, '4h': 0, '5h': 0, '6h': 1, '7h': 0, '8h': 0, '9h': 1, '10h': 0, '11h': 1, '12h': 0, '13h': 0, '14h': 1, '15h': 0, '16h': 1, '17h': 0, '18h': 0, '19h': 1, '20h': 0, '21h': 0, '22h': 1, '23h': 0, '24h': 0, '25h': 1 },
'bi': {'1h': 1, '2h': 1, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 0, '8h': 1, '9h': 0, '10h': 0, '11h': 0, '12h': 1, '13h': 0, '14h': 0, '15h': 1, '16h': 0, '17h': 0, '18h': 1, '19h': 1, '20h': 0, '21h': 1, '22h': 1, '23h': 1, '24h': 0, '25h': 0 },
'ugo': {'1h': 0, '2h': 0, '3h': 0, '4h': 1, '5h': 0, '6h': 0, '7h': 1, '8h': 0, '9h': 0, '10h': 1, '11h': 0, '12h': 0, '13h': 0, '14h': 1, '15h': 0, '16h': 1, '17h': 0, '18h': 0, '19h': 0, '20h': 1, '21h': 0, '22h': 0, '23h': 0, '24h': 1, '25h': 0 },
'albo': {'1h': 0, '2h': 1, '3h': 0, '4h': 1, '5h': 0, '6h': 1, '7h': 0, '8h': 0, '9h': 0, '10h': 1, '11h': 0, '12h': 0, '13h': 1, '14h': 0, '15h': 0, '16h': 0, '17h': 0, '18h': 1, '19h': 1, '20h': 1, '21h': 0, '22h': 1, '23h': 0, '24h': 1, '25h': 0 },
'lollo': {'1h': 1, '2h': 0, '3h': 1, '4h': 0, '5h': 1, '6h': 0, '7h': 1, '8h': 0, '9h': 0, '10h': 1, '11h': 0, '12h': 0, '13h': 0, '14h': 1, '15h': 0, '16h': 1, '17h': 1, '18h': 1, '19h': 0, '20h': 0, '21h': 1, '22h': 0, '23h': 1, '24h': 1, '25h': 1 },
'chiara': {'1h': 0, '2h': 1, '3h': 0, '4h': 0, '5h': 0, '6h': 1, '7h': 0, '8h': 0, '9h': 0, '10h': 0, '11h': 0, '12h': 0, '13h': 1, '14h': 0, '15h': 0, '16h': 1, '17h': 0, '18h': 1, '19h': 0, '20h': 0, '21h': 0, '22h': 1, '23h': 0, '24h': 0, '25h': 0 },
'selenia': {'1h': 1, '2h': 1, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 1, '8h': 0, '9h': 1, '10h': 1, '11h': 0, '12h': 1, '13h': 0, '14h': 1, '15h': 0, '16h': 0, '17h': 1, '18h': 0, '19h': 0, '20h': 0, '21h': 1, '22h': 1, '23h': 0, '24h': 1, '25h': 0 },
'pancotto': {'1h': 1, '2h': 0, '3h': 1, '4h': 0, '5h': 0, '6h': 1, '7h': 0, '8h': 1, '9h': 0, '10h': 1, '11h': 1, '12h': 0, '13h': 0, '14h': 0, '15h': 1, '16h': 0, '17h': 0, '18h': 1, '19h': 0, '20h': 0, '21h': 1, '22h': 0, '23h': 1, '24h': 0, '25h': 1 },
'giacomino': {'1h': 1, '2h': 1, '3h': 0, '4h': 1, '5h': 0, '6h': 0, '7h': 0, '8h': 1, '9h': 0, '10h': 0, '11h': 0, '12h': 1, '13h': 0, '14h': 0, '15h': 0, '16h': 0, '17h': 1, '18h': 0, '19h': 1, '20h': 0, '21h': 0, '22h': 0, '23h': 0, '24h': 0, '25h': 0 },
'eugenietto': {'1h': 0, '2h': 1, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 1, '8h': 0, '9h': 1, '10h': 0, '11h': 1, '12h': 0, '13h': 0, '14h': 1, '15h': 1, '16h': 0, '17h': 0, '18h': 0, '19h': 1, '20h': 0, '21h': 1, '22h': 0, '23h': 0, '24h': 1, '25h': 0 },
'ermenegildo': {'1h': 0, '2h': 0, '3h': 1, '4h': 0, '5h': 0, '6h': 1, '7h': 0, '8h': 1, '9h': 0, '10h': 1, '11h': 0, '12h': 1, '13h': 0, '14h': 1, '15h': 0, '16h': 1, '17h': 1, '18h': 1, '19h': 0, '20h': 0, '21h': 0, '22h': 1, '23h': 0, '24h': 1, '25h': 0 },
'francescopio': {'1h': 0, '2h': 0, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 0, '8h': 0, '9h': 0, '10h': 1, '11h': 0, '12h': 0, '13h': 0, '14h': 1, '15h': 0, '16h': 0, '17h': 0, '18h': 0, '19h': 0, '20h': 1, '21h': 0, '22h': 0, '23h': 1, '24h': 1, '25h': 1 },
'gianmichelino': {'1h': 1, '2h': 1, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 1, '8h': 0, '9h': 1, '10h': 0, '11h': 0, '12h': 0, '13h': 1, '14h': 1, '15h': 0, '16h': 1, '17h': 0, '18h': 1, '19h': 0, '20h': 0, '21h': 0, '22h': 1, '23h': 0, '24h': 0, '25h': 0 },
'francescomario': {'1h': 0, '2h': 0, '3h': 1, '4h': 0, '5h': 0, '6h': 0, '7h': 0, '8h': 1, '9h': 0, '10h': 0, '11h': 1, '12h': 0, '13h': 0, '14h': 1, '15h': 1, '16h': 0, '17h': 1, '18h': 0, '19h': 0, '20h': 0, '21h': 0, '22h': 0, '23h': 0, '24h': 1, '25h': 1 },
'annamariateresa': {'1h': 1, '2h': 1, '3h': 0, '4h': 0, '5h': 0, '6h': 1, '7h': 1, '8h': 0, '9h': 1, '10h': 0, '11h': 0, '12h': 1, '13h': 0, '14h': 1, '15h': 1, '16h': 0, '17h': 0, '18h': 1, '19h': 1, '20h': 0, '21h': 0, '22h': 0, '23h': 1, '24h': 0, '25h': 0 },
'elkammmmmmmmoide': {'1h': 0, '2h': 1, '3h': 0, '4h': 0, '5h': 1, '6h': 0, '7h': 1, '8h': 0, '9h': 1, '10h': 0, '11h': 1, '12h': 0, '13h': 1, '14h': 0, '15h': 0, '16h': 1, '17h': 0, '18h': 0, '19h': 1, '20h': 0, '21h': 1, '22h': 0, '23h': 0, '24h': 1, '25h': 1 }}

prob = pulp.LpProblem("problema part time", pulp.LpMaximize)

assegnamento = [(p, h) for p in persone for h in ore]

# definizione variabile
x = pulp.LpVariable.dicts("assegnamento", (persone, ore), lowBound = 0, cat ='Binary')

prob += sum([x[p][h] * disponibilita[p][h] for (p, h) in assegnamento]), "Funzione_Obiettivo"

for p in persone:prob += sum([x[p][h] for h in ore]) <= hMax[p], "Ore_Massime_%s" % p

for p in persone:prob += sum([x[p][h] for h in ore]) >= hMin[p], "Ore_Minime_%s" % p

for h in ['1h', '2h', '3h', '4h', '9h', '10h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h', '22h', '23h', '24h', '25h']:prob += sum([x[p][h] for p in persone]) == 2, "Ore_da_fare_%s" % h

for h in ['5h', '6h', '7h', '8h']:prob += sum([x[p][h] for p in persone]) == 3, "Ore_da_fare_con_agraria%s" % h

for (p, h) in assegnamento:
    if disponibilita[p][h] == 0:
        prob += x[p][h] == 0

# for p in persone:prob += x[p]['21h'] == x[p]['22h']

# for p in persone:prob += x[p]['3h'] + x[p]['21h'] <= 1

# for p in persone:prob += x[p]['4h'] + x[p]['21h'] <= 1
# for p in persone:prob += x[p]['4h'] + x[p]['22h'] <= 1

# for p in persone:prob += x[p]['5h'] + x[p]['22h'] <= 1

var = prob.solve()

print(var)

a = ''
for p in persone:
    print('ore affidate ad ' + p + ':')
    for h in ore:
        if x[p][h].value() != 0:
            a = a + h + ' '
    print(a)
    a = ''
'''
for (p, h) in assegnamento:
    if x[p][h].value() != 0:
        print('%s --> %s' % (x[p][h], x[p][h].value()))'''