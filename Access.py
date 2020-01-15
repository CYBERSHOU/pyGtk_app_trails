#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 0.9.5
# Author: Miguel Seridonio Almeida Fernandes


import os


ERR_INP = "Error in Input!"
USER = "Username: "
PASS = "Password: "
ADMIN = "admin"
ATTR_FILE = "acess_file.txt"


class Access:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.u_pass = dict()
        try:
            f = open(file_path, "r")
            text = f.read()
            buf = ""
            buf2 = ""
            i = False
            for c in text:
                if c == '\n':
                    self.u_pass[buf] = buf2
                    buf = ""
                    buf2 = ""
                    i = False
                    continue
                if c == ':':
                    i = True
                elif i:
                    buf2 += c
                else:
                    buf += c
        except Exception:
            f = open(file_path, "w")
            f.write("admin:")
            f.close()
            self.u_pass["admin"] = ""
        # self.u_pass = { ADMIN: ""}
        # self.pvlg = { ADMIN: 1}
        self.logged_in = None


    def write_attr(self):
        f = open(ATTR_FILE, "w")
        for u in self.get_u_pass():
            f.write(u+":"+str(self.u_pass[u])+":"+str(self.pvlg[u])+"\n")
        f.close()


    def read_attr(self):
        f = open(ATTR_FILE, "r")
        text = f.read()
        f.close()
        u = ''
        p = ''
        pv = ''
        i = 0
        for c in text:
            if c == '\n':
                self.u_pass[u] = p
                self.pvlg[u] = pv
                u = ''
                p = ''
                pv = ''
                i = 0
            elif c == ':':
                i += 1
            elif i == 0:
                u += c
            elif i == 1:
                p += c
            elif i == 2:
                pv += c


    def get_u_pass(self):
        return self.u_pass


    def get_plvg(self):
        return self.pvlg


    def del_acc(self, u:str):
        self.pvlg.pop(u, None)
        return self.u_pass.pop(u, None)


    def create_acc_gtk(self, l:list):
        self.u_pass[u] = p
        if(c for c in u if c.lower() >= 'a' and c.lower() <= 'z'):
            if u != '':
                return 0
            else:
                return 1

        f = open(self.file_path, 'a')
        f.write(str(u)+':'+str(p))
        for i in l:
            f.write(':'+i)
        f.write('\n')
        f.close()


    def get_logged_in(self):
        return self.logged_in


    def set_logged_in(self, u):
        self.logged_in = u


    def login_gtk(self, u:str, p:str):
        if u in self.get_u_pass():
            if self.u_pass[u] == p:
                self.set_logged_in(u)
                return 0
            else:
                return 1
        else:
            return 1


    def change_pvlg(self, u:str):
        if u in self.get_plvg():
            p = input("Insert new privilege(1-7): ")
            self.pvlg[u] = p
            print("Privilege for user: "+u+" has been changed.")
        else:
            print("User not found!")


    def crt_acc(self):
        print("-- Creating Account --")
        u = ''
        y = 'n'
        p = ''

        while(y != 'y'):
            u = ADMIN
            while(u in self.get_u_pass()):
                try:
                    u = input(USER)
                except:
                    print(ERR_INP)
                    return 1
                if u == '' or ':' in u or ' ' in u:
                    u = ADMIN
                    print("Invalid Username!\n")
            i = False
            while(i == False):
                os.system("stty -echo")
                try:
                    p = input(PASS)
                    os.system("stty echo")
                except:
                    print(ERR_INP)
                    os.system("stty echo")
                    return 1
                os.system("stty -echo")
                try:
                    p2 = input("\nChecking "+ PASS)
                    os.system("stty echo")
                except:
                    print(ERR_INP)
                    os.system("stty echo")
                    return 1
                if p == p2:
                    i = True
                else:
                    print("\nPasswords don't match. Try again.")
            y = input("\nIs this username and password ok?(y/n) ")

        self.u_pass[u] = p
        self.pvlg[u] = 4


    def login_input(self, d:dict):
        u = input(USER)
        os.system("stty -echo")
        try:
            p = input(PASS)
            os.system("stty echo")
        except:
            print(ERR_INP)
            os.system("stty echo")
            return 1
        if u in d:
            if d[u] == p:
                return u
            else:
                return False
        return False


    def login(self):
        while(True):
            u = self.login_input(self.get_u_pass())
            if u:
                print("\nWelcome " + u)
                break
            else:
                print("\nUsername or Password is incorrect!")



#eof
