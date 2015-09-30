from aula5.pessoa import  import Pessoa
from aula6.pessoas_tipos import  Homem, Mulher

if __name__=='__main__':
    gomes = Homem('Gomes')
    gomes_igual = Homem('Gomes')
    gomes_identico=gomes
    selina=Mulher('Selina')
    igor=Homem('Igor')
    print(gomes is gomes_igual)
    print(gomes is gomes_identico)
    print(gomes == gomes_igual)
    print(gomes == gomes_identico)

    conjunto=set((gomes,gomes_identico,gomes_igual,selina))
    conjunto2=set((igor,selina))
    print(conjunto)
    print(gomes is conjunto)
    print(gomes is conjunto2)
    print(conjunto+conjunto2)
