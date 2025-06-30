from carro import Carro
from moto import Moto
corolla=Carro(marca='Toyota',modelo='Corolla',portas=4)
argo=Carro(marca='Fiat',modelo='Argo',portas=4)
gol=Carro(marca='Volkswagen',modelo='Gol',portas=2)
mt_03=Moto(marca='Yamaha',modelo='MT-03',tipo='Esportiva')
biz=Moto(marca='Honda',modelo='Biz',tipo='Casual')
gsx_r1000=Moto(marca='Suzuki',modelo='GSX-R1000',tipo='Esportiva')


def main():
    print(corolla)
    print(gol)
    print(argo)
    print(mt_03)
    print(biz)
    print(gsx_r1000)
    corolla.ligar()

if __name__=='__main__':
    main()