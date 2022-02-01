ruudukko_1 = [
    [0,0,0,8,0,5,0,1,3],
    [0,0,0,2,0,3,6,0,0],
    [6,0,0,0,9,0,2,0,4],
    [0,0,0,0,0,0,0,0,5],
    [0,4,0,1,0,0,7,0,6],
    [2,5,6,3,0,4,8,9,0],
    [5,9,8,0,0,7,1,0,2],
    [1,3,2,0,8,0,4,7,0],
    [7,6,4,9,1,0,0,3,8],
]
ruudukko_2 = [
    [4,1,5,9,6,2,3,7,8],
    [7,6,3,1,8,5,4,2,9],
    [9,2,8,3,7,4,5,6,1],
    [8,3,1,6,4,9,2,5,7],
    [5,7,2,5,3,1,9,8,4],
    [5,4,9,0,2,0,6,1,3],
    [3,9,6,2,1,8,7,4,5],
    [1,5,7,4,9,6,8,3,2],
    [2,8,4,7,5,3,1,9,6]
]
ruudukko_3 = [[0 for j in range(9)] for i in range(9)]


def tulosta(lauta: list):
    with open('sudoku.csv', 'w') as sudo:
        
        taulu = ''
        for rivi in range(len(lauta)):
            if rivi % 3 == 0 and rivi != 0:
                taulu += '------+-------+------\n'
            for alkio in range(len(lauta[0])):
                if alkio % 3 == 0 and alkio != 0:
                    taulu += '| '
                if alkio == len(lauta[0])-1:
                    taulu += str(lauta[rivi][alkio]) + '\n'
                else:
                    taulu += str(lauta[rivi][alkio]) + ' '
        print(taulu)
        sudo.write(taulu)
        return taulu

def tulosta_tallennettu(tiedosto) -> list:
    with open(tiedosto) as lauta:
        lista = []
        taulu = ''
        for rivi in lauta:
            rivi = rivi.split()
            lista.append(rivi)
        for i in range(9):
            for j in range(9):
                if j == 8:
                    lista[i][j] = int(lista[i][j])
                    #taulu += str(lista[i][j]) + '\n'
                else:
                    lista[i][j] = int(lista[i][j])
                    #taulu += str(lista[i][j]) + ' '
        return lista

def varmista(lauta: list, numero: int, ruutu: tuple) -> bool:
    
    for sarake in range(9):
        if lauta[ruutu[0]][sarake] == numero:
            return False
    
    for rivi in range(9):
        if lauta[rivi][ruutu[1]] == numero:
            return False
    
    iso_ruutu_rivi = ruutu[0] // 3
    iso_ruutu_sarake = ruutu[1] // 3
    
    for rivi in range(iso_ruutu_rivi * 3, iso_ruutu_rivi * 3 + 3):
        for sarake in range(iso_ruutu_sarake * 3,iso_ruutu_sarake * 3 + 3):
            if lauta[rivi][sarake] == numero and (rivi,sarake) != ruutu:
                return False
    return True 

def tallenna_lauta(lauta):
    tiedosto = input('Mihin tiedostoon tallenetaan?: ')
    with open(tiedosto, 'w') as tallennus_tila:
        taulu = ''
        for rivi in range(len(lauta)):
            for sarake in range(len(lauta[0])):
                if sarake == len(lauta)-1:
                    taulu += str(lauta[rivi][sarake]) + '\n'
                else:
                    taulu += str(lauta[rivi][sarake]) + ' '
        tallennus_tila.write(taulu)
        print(f'\nPeli tallennettu tiedostoon {tiedosto}\n')

merkatut = []
def lisaa_numero(lauta: list) -> bool: 
    rivi = int(input('Anna rivi (0-8): '))
    sarake = int(input('Anna sarake (0-8): '))
    numero = int(input('Anna numero (1-9): '))
    ruutu = (rivi,sarake)
    
    if int(lauta[rivi][sarake]) == 0 or (rivi,sarake) in merkatut:
        if varmista(lauta, numero, ruutu):
            lauta[rivi][sarake] = numero
            merkatut.append(ruutu)
        else:
            print('Väärin')
            return False  
    return True

def tyhja_ruutu(lauta: list) -> tuple:
    for rivi in range(9):
        for sarake in range(9):
            if lauta[rivi][sarake] == 0:
                return (rivi,sarake)
    return None
def tarkista(lauta: list): 
    nolla = tyhja_ruutu(lauta)
    if not nolla:
        return True
    
def pelaa():
    print('\nTervetuloa pelaamaan Sudokua.\nSeuraa ohjeita niin selviät matkasta.\nAluksi sinun tulee valita kolmesta valmiista pelilaudasta tai vaihtoehtoisesti voit valita aikaisemmin tallentamasi pelin.\nTallentaaksesi pelin, kirjoita jokin kirjain missä kohtaa peliä tahansa.\n\nHauskoja pelihetkiä\n')
   
    muoto = input('Tiedosto vai Lauta? (T/L)? ')
    if muoto == 'l' or muoto == 'L':
        nro = int(input('Anna laudan numero(1,2,3): '))
        if nro == 1:
            lauta = ruudukko_1
        elif nro == 2:
            lauta = ruudukko_2
        else: 
            lauta = ruudukko_3
        i = 0
        while i < 3:
            try:
                tulosta(lauta)
                if lisaa_numero(lauta) == False:
                    i += 1
                    if i == 2:
                        print('\nSeuraavasta virheestä loppuu peli.')
                elif tarkista(lauta):
                    print('\nValmis!!!\n')
                    break
                
            except ValueError:
                print('Haluatko tallentaa?')
                tallennus = input('K/E? ')
                if tallennus == 'k' or tallennus == 'K':
                    tallenna_lauta(lauta)
                    break
            except IndexError:
                print('\nTarkista ohjeet!!\n')
            if i == 3:
                print('\nGame Over\n')
    if muoto == 't' or muoto == 'T':
        try:
            tiedosto = input('Anna tiedoston nimi: ')
            lauta = tulosta_tallennettu(tiedosto)
            i = 0
            while i < 3:
                try:
                    tulosta(lauta)
                    if lisaa_numero(lauta) == False:
                        i += 1
                        if i == 2:
                            print('\nSeuraavasta virheestä loppuu peli.')
                    elif tarkista(lauta):
                        print('\nValmis!!!\n')
                        break
                    
                except ValueError:
                    print('Haluatko tallentaa?')
                    tallennus = input('K/E? ')
                    if tallennus == 'k' or tallennus == 'K':
                        tallenna_lauta(lauta)
                        
                        break
                except IndexError:
                    print('\nTarkista ohjeet!!\n')
                if i == 3:
                    print('\nGame Over\n')
        except ValueError:
            print('Ei sopiva tiedosto, kokeile jotain muuta')
        except FileNotFoundError:
            print('Tiedostoa ei löydy.')
        
        

pelaa()