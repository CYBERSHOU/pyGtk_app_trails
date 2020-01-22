#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Author: Isaac Silva


class Report:
    def __init__(self, classificacao):
        self.classificacao_entrada = classificacao
        self.num_visitas = len(classificacao)
        self.classificacao_max = 0
        if self.num_visitas == 0:
            self.classificacao_min = 0
        else:
            self.classificacao_min = 5
        self.moda = 0

        #percorre a lista de classificações e obtem a classificação maxima e minima
        dic_temp = {}
        for i in classificacao:
            i = int(i)
            if self.classificacao_max < i:
                self.classificacao_max = i
            if self.classificacao_min > i:
                self.classificacao_min = i

            #cria um dicionario, as keys sao as classificações, e la dentro a frequencia de cada
            if i in dic_temp:
                dic_temp[i] +=1
            else:
                dic_temp[i] = 1

        #procura por qual key tem o valor maior, ou seja, qual classificação é mais frequencte, e poe o valor dessa key na self.moda
        temp = 0
        classificacao_mais_frequente = 0
        for i in dic_temp:
            if dic_temp[i] > temp:
                classificacao_mais_frequente = i
                temp = dic_temp[i]

        self.moda = classificacao_mais_frequente

    def get_classificacao_max(self):
        return self.classificacao_max

    def get_classificacao_min(self):
        return self.classificacao_min

    def get_num_visitas(self):
        return self.num_visitas

    def get_moda(self):
        return self.moda


