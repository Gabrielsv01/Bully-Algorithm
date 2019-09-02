
class Processo():
    def __init__(self, id_Processo , is_Coordenador = False, is_Ativo = True):
        self.identificador = id_Processo
        self.coordenador = is_Coordenador
        self.ativo = is_Ativo
        self.qualCoord = "null"
    
    def Eleicao(self):
        for c in enderecos_processos:
            
            if (c.Identificador() > self.identificador) :
                if (c.Is_Ativo() == True):
                    if (c.identificador != self.identificador):
                        text = "O processo com ID: {} saiu da eleição.".format(self.identificador)
                    self.coordenador = False
                    print(text) 
                    c.Eleicao()
                    break

                if ((c.Is_Ativo() == False) and c.Is_Coordenador()):
                    self.coordenador = True
                    enderecos_processos[self.identificador-1].Verifica_coordenador()
                    print("\nO processo: {} é o novo Coordenador(Valentão)\n".format(self.identificador))
            
            if(c.Is_Ativo() and c.Is_Coordenador()):
                print("\nO processo: {} é o novo Coordenador(Valentão)\n".format(self.identificador))

    ### Funções de retorno de valores de processos
    def Is_Ativo(self):
        return self.ativo
    def Is_Coordenador(self):
        return self.coordenador
    def Set_Coordenador(self):
        if (self.coordenador):
            self.coordenador = False
        else:
            self.coordenador = True
    def Identificador(self):
        return self.identificador
    def SetIDcoord(self,id_coord):
        self.qualCoord = id_coord
    
    def Coord(self,_id):
        for d in enderecos_processos:
            d.SetIDcoord(_id)
    
    ### Simular parada de processo
    def Simular_erro(self):
        if (self.ativo):
            self.ativo = False
            print("O processo {} parou".format(self.identificador))
            
                       
        
    ### Verifica se o coordenador esta ativo
    def Verifica_coordenador(self):
        quant_coordenador = []
        for c in enderecos_processos:
            if (c.Is_Coordenador() and c.Is_Ativo()):
                quant_coordenador.append(enderecos_processos.index(c))
                
            elif (c.Is_Coordenador()):
                quant_coordenador.append(enderecos_processos.index(c))
       
            if (len(quant_coordenador) >= 2):
                enderecos_processos[quant_coordenador[1]].Set_Coordenador()
                enderecos_processos[quant_coordenador[0]].Coord(quant_coordenador[0]+1)
                quant_coordenador.pop(1)
                
    def Print(self):
        if (self.ativo):
            print("Identificador: {} , Coordenador: {} , Ativo: {} ".format(self.identificador,self.qualCoord, self.ativo))
        else:
            print("Processo: {} não respondendo".format(self.identificador))



criar_processos = int(input("Digite o numero de processos a serem criados: "))
chama_eleicao = list(map(int,input("Digite qual processo ira requisitar a eleição: ").split(' ')))
count = 1
enderecos_processos = []

while count <= criar_processos:
    if (count == criar_processos):
        p = Processo(count,True)
        enderecos_processos.append(p)
        p.Coord(count)
    else:
        p = Processo(count,False)  
        enderecos_processos.append(p)
        
    count+=1



print("Criando Processos \n")
for d in enderecos_processos:
    d.Print()



print("\nSimulando Parada de Processos Aleatoriamente \n")
enderecos_processos[len(enderecos_processos)-1].Simular_erro() ## parando Coordenador
#enderecos_processos[18].Simular_erro() ## parando Coordenador

from random import randint
count2 = 0
while count2 < randint(0,len(enderecos_processos) // 2):
    enderecos_processos[randint(0,len(enderecos_processos)-1)].Simular_erro()
    count2 +=1



print("\nCoordenador e outros processos não estão respondendo\n")
for d in enderecos_processos:
    d.Print()



for e in chama_eleicao:
    print("\nProcesso {} Requisitando Eleição \n".format(e))
    enderecos_processos[e].Eleicao()



print("Processos após a escolha do novo coordenador(Valentão)\n")
for d in enderecos_processos:
    d.Print()






