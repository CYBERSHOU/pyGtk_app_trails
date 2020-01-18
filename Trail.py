#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 1.0
# Author: Miguel Seridonio Almeida Fernandes


from trail_dic import *


class Trail:
    def __init__(self, file_path:str,
                    name=NAME,
                    isle=ISLE,
                    county=CNTY,
                    gps=GPS,
                    dificulty=DFCT,
                    extension=EXTN,
                    format_=FORM,
                    description=DESC,
                    ):
        self.file_path = file_path
        self.name = name
        self.isle = isle
        self.county = county
        self.gps = gps
        self.dificulty = dificulty
        self.extension = extension
        self.format = format_
        self.description = description
        self.d = {}
        self.set_d()


    def get_name(self):
        return self.name

    def get_isle(self):
        return self.isle


    def get_county(self):
        return self.county


    def get_gps(self):
        return self.gps


    def get_dificulty(self):
        return self.dificulty


    def get_extension(self):
        return self.extension


    def get_format(self):
        return self.format


    def get_description(self):
        return self.description


    def set_name(self, n):
        self.name = n


    def set_isle(self, i):
        self.isle = i


    def set_county(self, c):
        self.county = c


    def set_gps(self, g):
        self.gps = g


    def set_dificulty(self, d):
        self.dificulty = d


    def set_extension(self, e):
        self.extension = e


    def set_format(self, f):
        self.format = f


    def set_description(self, d):
        self.description = d


    def set_d(self, l=0):
        n = self.name.lower()
        buf = ""
        for c in n:
            if c == ' ':
                buf += '_'
            else:
                buf += c
        if l == 0:
            l = [self.name,
                self.isle,
                self.county,
                self.gps,
                self.dificulty,
                self.extension,
                self.format,
                self.description
                ]
        n_d = {}
        for i in range(len(HEADERS)):
            n_d[HEADERS[i]] = l[i]
        self.d[buf] = n_d


    def get_trails(self):
        return self.d


    def add_file_trail(self, l:list):
        try:
            f = open(self.file_path, 'a')
            for i in l:
                f.write(str(i)+';')
            f.close()
            return 0
        except Exception:
            return 1


    def modify_file_trail(self, name:str, l:list):
        try:
            self.remove_trail(name)
            f = open(self.file_path, 'a')
            for i in l:
                f.write(str(i)+';')
            f.close()
            return 0
        except Exception:
            return 1


    def remove_file_trail(self, name:str):
        try:
            f = open(self.file_path, 'r')
            l_n = []
            for line in f:
                if name in line:
                    continue
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
            self.d = {}
            f = open(self.file_path, 'r')
            l = []
            for line in f:
                n = ""
                for c in line:
                    if c == ';':
                        l += n
                        n = ""
                    else:
                        n += c

            n_d = {}
            for i in range(len(HEADER)):
                n_d[HEADER[i]] = l[i]
            n = l[0].lower()
            buf = ""
            for c in n:
                if c == ' ':
                    buf = '_'
                else:
                    buf = c

            self.d[buf] = n_d
            f.close()
            return self.d
        except Exception:
            f = open(self.file_path, 'w')
            for i in HEADERS:
                f.write(i+';')
            f.close()
            n_d = {}
            for i in range(len(HEADERS)):
                n_d[HEADERS[i]] = COL_HEADER[i]
            d_header = {"header": HEADERS}
            return d_header

    def set_file_trails(self):
        f = open(self.file_path, 'w')
        for i in self.d:
            for y in i:
                f.write(i[y]+';')
        f.close()



#eof
