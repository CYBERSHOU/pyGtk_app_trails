#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 1.0
# Author: Miguel Seridonio Almeida Fernandes


USER_CREATED = "User created successfully!"

INVALID_USER = "Username is invalid!\nMust contain at least 3 letters\n"
INVALID_USER += "and no special characters."

INVALID_USER_EXISTS = "Cannot create account!\nUser already exists!"

INVALID_PASS = "Password is invalid!\n"
INVALID_PASS += "Must contain at least 8 characters.\n"
INVALID_PASS += "Special characters accepted\nare !\"#$%&'()*+,.-/;<=>?@ ."

N_MATCH_PASS = "Passwords do not match!"


class Access:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.users = dict()
        self.u_pass = dict()
        self.cty = ""
        self.gdr = ""
        self.age = ""
        self.logged_user = None
        try:
            f = open(self.file_path, 'r')
            for line in f:
                l = line.strip('\n').split(':')
                self.users[l[0]] = l
            for u in self.users:
                self.u_pass[u] = self.users[u][1]
            f.close()
        except Exception:
            f = open(self.file_path, 'w')
            f.close()


    def get_u_pass(self):
        return self.u_pass


    def del_acc(self, u:str):
        self.users.pop(u, None)
        return self.u_pass.pop(u, None)


    def create_acc_gtk(self, l:list):
        u, p, ck_p, c, g, a = l[0], l[1], l[2], l[3], l[4], l[5]
        #checking validity
        if u in self.users:
            return INVALID_USER_EXISTS
        if(c for c in u if
                (c.lower() >= 'a' and c.lower() <= 'z') or
                (c >= '0' and c <= '9')):
            i = 0
            for c in u:
                i += 1
            if i < 3:
                return INVALID_USER
        else:
            return INVALID_USER
        if(c for c in p if (c >= '!' and c <= '9') or
                (c.upper() >= ';' and c.upper() <= 'Z')):
            i = 0
            for c in p:
                i += 1
            if i < 8:
                return INVALID_PASS
        else:
            return INVALID_PASS
        if p != ck_p:
            return N_MATCH_PASS
        #everything is correct
        f = open(self.file_path, 'a')
        f.write(u+':'+p+':'+c+':'+g+':'+a)
        f.write('\n')
        f.close()
        l.pop(2)
        self.u_pass[u] = p
        self.users[u] = l
        return USER_CREATED


    def get_logged_user(self):
        return self.logged_user


    def get_cty(self):
        return self.cty


    def get_gdr(self):
        return self.gdr


    def get_age(self):
        return self.age


    def set_logged_acc(self, u):
        self.logged_user = u
        self.cty = self.users[u][2]
        self.gdr = self.users[u][3]
        self.age = self.users[u][4]


    def login_gtk(self, u:str, p:str):
        if u in self.get_u_pass():
            if self.u_pass[u] == p:
                self.set_logged_acc(u)
                return 0
            else:
                return 1
        else:
            return 1



#eof
