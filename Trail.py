#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 1.0
# Author: Miguel Seridonio Almeida Fernandes


from trail_dic import *


class Trail:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.trails_d = {}
        self.set_trails_d()


    def set_trails_d(self, l:list=None):
        if l == None:
            return
        n_d = {}
        for i in range(len(HEADERS)):
            n_d[HEADERS[i]] = l[i]
        self.trails_d[l[0]] = n_d
        return self.trails_d


    def get_trails_d(self):
        return self.trails_d


#     def add_file_trail(self, l:list):
#         try:
#             f = open(self.file_path, 'a')
#             for i in l:
#                 f.write(str(i)+';')
#             f.write('\n')
#             f.close()
#             return 0
#         except Exception:
#             return 1


    def modify_file_trail(self, l:list):
        try:
            self.remove_file_trail(l[0])
            f = open(self.file_path, 'a')
            for i in l:
                f.write(str(i)+';')
            f.write('\n')
            f.close()
            return 0
        except Exception:
            return 1


    def remove_file_trail(self, name:str):
        try:
            f = open(self.file_path, 'r')
            l_n = []
            for line in f:
                if name not in line:
                    l_n.append(line)

            f = open(self.file_path, 'w')
            for line in l_n:
                f.write(line)
            f.close()
            return 0
        except Exception:
            return 1


    def get_file_trails(self):
        try:
            self.trails_d = {}
            f = open(self.file_path, 'r')
            for line in f:
                n = ""
                l = []
                n_d = {}
                for c in line:
                    if c == ';':
                        l.append(n)
                        n = ""
                    else:
                        n += c
                for i in range(len(HEADERS)):
                    n_d[HEADERS[i]] = l[i]
                self.trails_d[n_d[HEADERS[0]]] = n_d
            f.close()
            return self.trails_d
        except Exception:
            f = open(self.file_path, 'w')
            f.close()
            return 1


    def set_file_trails(self):
        f = open(self.file_path, 'w')
        for i in self.trails_d:
            for y in self.trails_d[i]:
                f.write(self.trails_d[i][y]+';')
            f.write('\n')
        f.close()


# def main():
#     t = Trail("test.txt")
#     t.get_file_trails()
#     print("2!:" + str(t.trails_d))
#     t.set_trails_d(["salto do cabrito", "sta maria", "vila do porto", "44n 32o", "44km", "facil", "linear", "ganda bosta"])
#     print("3!:"+str(t.trails_d))
#     t.set_file_trails()
#     t.modify_file_trail(["lo", "stamaria", "vilado porto", "44n32o", "44k", "fail", "liear", "gandbosta"])
#     f = open("test.txt", "r")
#     text = f.read()
#     print("4!:"+str(text))
#     f.close()
#     t.remove_file_trail("salto do cabrito")
#     print("removing: "+str(t.trails_d))

# main()



#eof
