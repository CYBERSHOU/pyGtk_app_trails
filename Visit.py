#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author : André Pacheco
# Version - 1.0


import random
from models_setup import COUNTRIES, AGES, RATINGS , GENDERS


class Visit:
    def __init__(self, file_path, trails:list):
        self.file_path = file_path
        self.visit = {}
        trails.pop("Name", None)
        self.trail = trails
        self.setup()


    def create_visitor(self, trail:str, visitor:list):
        self.visit[trail].append(visitor)
        f = open(self.file_path, 'a')
        f.write(str(trail)+';')
        for i in visitor:
            f.write(str(i)+';')
        f.write('\n')
        f.close()


    def get_rec_info(self):
        v = {}
        for i in self.visit:
            lst = []
            for e in self.visit[i]:
                new_lst = [e[1], e[2], e[3]]
                lst.append(new_lst)
            v[i] = lst
        return v


    def get_report_info(self, trail, date):
        lst = []
        if trail in self.visit:
            for e in self.visit[trail]:
                d = e[4][:len(date)]
                if date == d:
                    lst.append(e[5])
        return lst


    def setup(self):
        try:
            f = open(self.file_path, 'r')
            for line in f:
                v = line.split(';')
                if v[0] in self.visit:
                    self.visit[v[0]].append(v[1:])
                else:
                    self.visit[v[0]] = [v[1:]]
            f.close()
        except:
            self.generate_visitor()
            f = open(self.file_path, 'w')
            for i in self.visit:
                for e in self.visit[i]:
                    f.write(str(i) +';')
                    for c in e:
                        f.write(str(c) +';')
                    f.write('\n')
            f.close()


    def generate_visitor(self):
        for i in self.trail:
            l = []
            for n in range(20):
                c_i = COUNTRIES[random.randint(0, len(COUNTRIES) - 1)]
                g_i = GENDERS[random.randint(0, len(GENDERS) - 1)]
                a_i = AGES[random.randint(0, len(AGES) - 1)]
                r_i = RATINGS[random.randint(0, len(RATINGS) - 1)]
                visit_year = random.randint(2000, 2020)
                visit_month = random.randint(1,12)
                if visit_month < 10:
                    visit_month = '0' + str(visit_month)
                visit_day = random.randint(1,28)
                if visit_day < 10:
                    visit_day = '0' + str(visit_day)
                visit_date = str(visit_year) + '-' + str(visit_month) + '-' + str(visit_day)
                user = 'user{}'.format(n)
                l.append([user, c_i, g_i, a_i, visit_date, r_i])
            self.visit[i] = l


    def get_visit(self):
        return self.visit



#eof