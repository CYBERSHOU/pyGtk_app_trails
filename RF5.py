# Version: 0.5.0
# Author: Isaac Sousa

class RelatorioActividade:
    def __init__(self, lista):
        self.lista_trilhos = lista
        self.trilhos_info = {}
        for i in range(len(lista)):
            self.trilhos_info[lista[i]] = {"numero de visitas:":0,
                                           "classificação máxima:":0,
                                           "classificação minima:":5,
                                           "moda:":0}


    def get_info(self,dic,trilho,duracao = "diaria"):

        moda_dic = {}
        if duracao == "diaria":
            counter = 0
            for i in dic:
                #contador e classificaçoes maximas e minimas
                counter +=1
                temp = dic[i].classificacao
                if self.trilhos_info[trilho]["classificação máxima:"] < temp:
                    self.trilhos_info[trilho]["classificação máxima:"] = temp
                elif self.trilhos_info[trilho]["classificação minima:"] > temp:
                    self.trilhos_info[trilho]["classificação minima:"] = temp
                #moda
                if temp in moda_dic:
                    moda_dic[temp] +=1
                else:
                    moda_dic[temp] = 1
            temp2 = 0
            valor_moda = 1
            
            for i in moda_dic:
                if moda_dic[i] > temp2:
                    temp2 = moda_dic[i]
                    valor_moda = i
                    
            self.trilhos_info[trilho]["moda"] = valor_moda
            self.trilhos_info[trilho]["numero de visitas:"] = counter
            
                    

class teste:
    def __init__(self, classificacao_entrada, data):
        self.classificacao = classificacao_entrada
        self.data_visita = data

    def classificacao(self):
        return self.classificacao
    def data(self):
        return self.data_visita
    
# APAGAR MAIN NA VERSÃO FINAL ----   
def main():
    trilhos = ["trilho1", "trilho2", "trilho3", "trilho4"]
    joao1 = teste(4,"03-10-20")
    pedro1 = teste(3,"03-10-20")
    ricardo1 = teste(3,"03-10-20")
    rodrigo1 = teste(2,"03-10-20")
    entrada_RF2 = {"joao":joao1, #get("trilho1") por exemplo
                   "pedro":pedro1,
                   "Ricardo":ricardo1,
                   "Rodrigo":rodrigo1}
    
    relatorio = RelatorioActividade(trilhos)
    relatorio.get_info(entrada_RF2,"trilho1")
    print(relatorio.trilhos_info[trilhos[0]]["moda"])
main()
