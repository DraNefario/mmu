import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso da tecnica de mapeamento direto

VETOR_MAPEAMENTO = [-1 for _ in range(8)]

def mapeamentoDireto(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    global VETOR_MAPEAMENTO
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    # Já sabemos:
    # Temos 8 páginas na memória física (cache/Memória primária)
    # Temos 16 páginas na memória virtual (RAM/Memória secundária)

    # Para endereçar 8 páginas, precisamos de 3 bits
    # Para endereçar 16 páginas, precisamos de 4 bits

    pagina_requisitada = endereco >> 2
    byte_requisitado = endereco & 0b11

    pagina_direto = pagina_requisitada % qtPaginasMemoriaPrincipal
    if VETOR_MAPEAMENTO[pagina_direto] != pagina_requisitada:
        # Pegar pagina da memória secundária
        pagina_secundaria = memoriaSecundaria.getPagina(pagina_requisitada)

        # Armazenar a página no endereço 0 da memória principal
        memoriaPrincipal.setPagina(pagina_secundaria, pagina_direto)
        VETOR_MAPEAMENTO[pagina_direto] = pagina_requisitada

    #retorna endereco
    return pagina_direto

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoDireto,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)


    VETOR_MAPEAMENTO = [-1 for _ in range(1028)]
    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoDireto, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

