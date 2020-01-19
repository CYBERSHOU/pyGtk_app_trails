#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 0.9.7
# Authors: Miguel Seridonio Almeida Fernandes,
#       Isaac Slva,
#       Andre Pacheco


# import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import sys


import Access
import Trail
from models_setup import model_country, model_age, model_gender, model_rating


ABOUT = """
License: GPL
Version: 0.9.2
Author: Miguel Seridoneo
"""
ACCESS_FILE = "accounts.txt"
TRAIL_FILE = "trails.txt"

LOGGIN_IN = [
        "Logging in.",
        "Logging in..",
        "Logging in..."
        ]

SHOW_LABEL = ["Show Trails", "Hide Trails"]



class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(Window, self).__init__(title="Trails",
                                    default_width=450,
                                    default_height=300,
                                    application=app,
                                    )

        menubar = Gtk.MenuBar()
        menubar.props.hexpand = True

        fmi = Gtk.MenuItem.new_with_label("File")

        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("Exit")
        emi.connect("activate", self.quit_app)
        ami = Gtk.MenuItem.new_with_label("About")
        ami.connect("activate", self.about)
        menu.append(emi)

        fmi.set_submenu(menu)

        menubar.add(fmi)
        menubar.add(ami)

        self.user_entry = Gtk.Entry(margin_right=64,
                            halign=1,
                            max_length=18,
                            width_chars=17
                            )

        self.pass_entry = Gtk.Entry(margin_right=64,
                            halign=1,
                            max_length=18,
                            width_chars=17,
                            visibility=False,
                            )

        user_label = Gtk.Label(label="Username:",
                            margin_left=64,
                            halign=2,
                            )

        pass_label = Gtk.Label(label="Password:",
                            margin_left=64,
                            halign=2,
                            )

        self.grid2 = Gtk.Grid(column_spacing=32,
                            row_spacing=32,
                            halign=3,
                            valign=3,
                            )

        self.trails_table = Gtk.Grid(row_spacing=12,
                            column_spacing=16,
                            halign=3,
                            # column_homogeneous=True,
                            margin_left=64,
                            margin_right=64,
                            margin_bottom=64,
                            )

        self.trail = Trail.Trail(TRAIL_FILE)
        trail_rows = self.trail.get_trails()

        r = 0
        for i in trail_rows:
            c = 0
            for n in trail_rows[i]:
                self.trails_table.attach(Gtk.Label(label=trail_rows[i][n]), c, r, 1, 1)
                c += 1
            r += 1

        self.login_b = Gtk.Button(label="Login", hexpand=True, halign=3, margin_bottom=64)
        self.login_b.connect("clicked", self.login)

        self.create_acc_b = Gtk.Button(label="Create Account", hexpand=True, halign=3, margin_bottom=64)
        self.create_acc_b.connect("clicked", self.create_acc)

        self.login_grid = Gtk.Grid(halign=3,
                                column_spacing=16,
                                )

        self.login_grid.attach(self.login_b, 0, 0, 1, 1)
        self.login_grid.attach(self.create_acc_b, 1, 0, 1, 1)

        self.grid2.attach(user_label, 0, 0, 1, 1)
        self.grid2.attach(pass_label, 0, 1, 1, 1)
        self.grid2.attach(self.user_entry, 1, 0, 1, 1)
        self.grid2.attach(self.pass_entry, 1, 1, 1, 1)

        self.grid = Gtk.Grid(row_spacing=64, column_homogeneous=True)
        self.grid.attach(menubar, 0, 0, 1, 1)
        self.grid.attach(self.grid2, 0, 1, 1, 1)
        self.grid.attach(self.login_grid, 0, 2, 1, 1)

        self.log = Access.Access(ACCESS_FILE)
        self.add(self.grid)

    def main_menu(self, parent):
        self.user_entry.set_text("")
        self.pass_entry.set_text("")
        while(self.grid.get_child_at(0, 1) != None):
            self.grid.remove_row(1)
        self.grid.attach(self.grid2, 0, 1, 1, 1)
        self.grid.attach(self.login_grid, 0, 2, 1, 1)
        self.resize(450, 300)
        self.grid.show_all()


    def user_win(self, parent):
        user_menu = Gtk.Grid(row_spacing=16,
                            column_spacing=16,
                            halign=3,
                            column_homogeneous=True,
                            margin_right=32,
                            margin_left=32,
                            )
        u_show_button = Gtk.Button(label="Show Trails")
        u_show_button.connect("clicked", self.show_trails)
        u_experience_button = Gtk.Button(label="Trail Experience")
        u_experience_button.connect("clicked", self.trail_experience_input, u_show_button)
        u_recomendation_button = Gtk.Button(label="Trail Recomendation")
        u_recomendation_button.connect("clicked", self.trail_recomendation, u_show_button)
        u_report_button = Gtk.Button(label="Trails Report")
        u_report_button.connect("clicked", self.trail_report, u_show_button)
        u_back_button = Gtk.Button(label="Logout", halign=3)
        u_back_button.connect("clicked", self.main_menu)
        top_grid = Gtk.Grid(column_spacing=16,
                        halign=3,
                        column_homogeneous=True,
                        )
        top_grid.attach(u_show_button, 0, 0, 1, 1)
        top_grid.attach(u_experience_button, 1, 0, 1, 1)
        top_grid.attach(u_recomendation_button, 2, 0, 1, 1)
        top_grid.attach(u_report_button, 3, 0, 1, 1)
        user_menu.attach(top_grid, 0, 0, 1, 1)
        user_menu.attach(u_back_button, 0, 1, 1, 1)
        self.grid.remove(self.l)
        self.grid.attach(user_menu, 0, 1, 1, 1)
        self.grid.show_all()
        return False


    def admin_win(self, parent):
        admin_menu = Gtk.Grid(row_spacing=16,
                            halign=3,
                            row_homogeneous=True,
                            column_homogeneous=True,
                            )
        a_manage_button = Gtk.Button(label="Manage Trails")
        a_manage_button.connect("clicked", self.manage_trails_menu)
        a_back_button = Gtk.Button(label="Logout")
        a_back_button.connect("clicked", self.main_menu)
        admin_menu.attach(a_manage_button, 0, 0, 1, 1)
        admin_menu.attach(a_back_button, 0, 1, 1, 1)
        self.grid.remove(self.l)
        self.grid.attach(admin_menu, 0, 1, 1, 1)
        self.grid.attach(self.trails_table, 0, 2, 1, 1)
        self.grid.show_all()
        return False


    def manage_trails_menu(self, parent):
        pass


    def show_trails(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        if parent.props.label == SHOW_LABEL[0]:
            self.grid.attach(self.trails_table, 0, 2, 1, 1)
            parent.set_label(SHOW_LABEL[1])
            self.grid.show_all()
        else:
            parent.set_label(SHOW_LABEL[0])


    def trail_experience_input(self, par, parent):
        parent.set_label(SHOW_LABEL[0])
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)

        trail_grid = Gtk.Grid(halign=3)
        cell = Gtk.CellRendererText()
        rating = Gtk.ComboBox.new_with_model(model_rating)
        rating.pack_start(cell, True)
        rating.add_attribute(cell, "text", 0)
        rating_label = Gtk.Label(label="Rating:",
                                margin_right=6,
                                margin_left=10,
                                )
        #model_trail
        model_trail = Gtk.ListStore(str)
        d = self.trail.get_trails()
        for i in d:
            model_trail.append([i])

        trail = Gtk.ComboBox.new_with_model(model_trail)
        trail.pack_start(cell, True)
        trail.add_attribute(cell, "text", 0)
        trail_label = Gtk.Label(label="Trail:",
                            margin_right=6,
                            )
        trail_grid.attach(trail_label, 0, 0, 1, 1)
        trail_grid.attach(trail, 1, 0, 1, 1)
        trail_grid.attach(rating_label, 2, 0, 1, 1)
        trail_grid.attach(rating, 3, 0, 1, 1)
        calendar = Gtk.Calendar()
        submit_b = Gtk.Button(label="Submit", halign=3)
        submit_b.connect("clicked", self.submit_trail_experience, [trail, rating, calendar])
        holder_grid = Gtk.Grid(halign=3,
                            row_spacing =16,
                            margin_bottom=32,
                            )
        holder_grid.attach(trail_grid, 0, 0, 1, 1)
        holder_grid.attach(calendar, 0, 1, 1, 1)
        holder_grid.attach(submit_b, 0, 2, 1, 1)
        self.grid.attach(holder_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def submit_trail_experience(self, parent, widgets:list):
        t, r, c = widgets[0], widgets[1], widgets[2]
        pop = Gtk.Popover()
        pop.set_relative_to(parent)
        if t.get_active() == -1 or r.get_active() == -1:
            pop.add(Gtk.Label(label="Fill all parameters."))
            pop.show_all()
            pop.popup()
            self.t_pop = Gtk.GLib.timeout_add(3000, self.pop_down, pop)
            return
        y, m, d = c.get_date()
        m += 1
        if d < 10:
            d = '0'+str(d)
        else:
            d = str(d)
        if m < 10:
            m = '0'+str(m)
        else:
            m = str(m)
        y = str(y)
        date = d+'/'+m+'/'+y
        print(date)
        #status = self.visit.create_visit(model_trail[t.get_active()][0],
        #        [
        #        self.log.get_logged_user(),
        #        self.log.get_cty(),
        #        self.log.get_gdr(),
        #        self.log.get_age(),
        #        date,
        #        model_rating[r.get_active()][0],
        #        ])
        # pop.add(Gtk.Label(label=status))
        # pop.show_all()
        # pop.popup()
        # self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)


    def trail_recomendation(self, par, parent):
        parent.set_label(SHOW_LABEL[0])
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        rec = Recomend.Recomend()
        t = rec.get_rec()
        new_recomendation = Gtk.Label(label=t)
        self.grid.attach(new_recomendation, 0, 2, 1, 1)


    def trail_report(self, par, parent):
        parent.set_label(SHOW_LABEL[0])
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        trail_cb = Gtk.ComboBox.new_with_model(model_trail)


    def create_acc(self, parent):
        #cleanup
        while(self.grid.get_child_at(0, 1) != None):
            self.grid.remove_row(1)
        #labels
        user_label = Gtk.Label(label="Username:")
        pass_label = Gtk.Label(label="Password:")
        ck_pass_label = Gtk.Label(label="Confirm Password:")
        country_label = Gtk.Label(label="Country:")
        gender_label = Gtk.Label(label="Gender:")
        age_range_label = Gtk.Label(label="Age Range:")
        #entries
        user_entry = Gtk.Entry()
        pass_entry = Gtk.Entry(visibility=False)
        ck_pass_entry = Gtk.Entry(visibility=False)
        #comboboxes
        country_cbox = Gtk.ComboBox.new_with_model(model_country)
        gender_cbox = Gtk.ComboBox.new_with_model(model_gender)
        age_range_cbox = Gtk.ComboBox.new_with_model(model_age)
        #setting up comboboxes CellRendererText
        cell = Gtk.CellRendererText()
        country_cbox.pack_start(cell, True)
        country_cbox.add_attribute(cell, 'text', 0)
        gender_cbox.pack_start(cell, True)
        gender_cbox.add_attribute(cell, 'text', 0)
        age_range_cbox.pack_start(cell, True)
        age_range_cbox.add_attribute(cell, 'text', 0)
        #labels, entries, comboboxes grid
        create_acc_grid = Gtk.Grid(halign=3,
                                row_spacing=16,
                                column_spacing=12,
                                                                )
        create_acc_grid.attach(user_label, 0, 0, 1, 1)
        create_acc_grid.attach(pass_label, 0, 1, 1, 1)
        create_acc_grid.attach(ck_pass_label, 0, 2, 1, 1)
        create_acc_grid.attach(country_label, 0, 3, 1, 1)
        create_acc_grid.attach(gender_label, 0, 4, 1, 1)
        create_acc_grid.attach(age_range_label, 0, 5, 1, 1)
        create_acc_grid.attach(user_entry, 1, 0, 1, 1)
        create_acc_grid.attach(pass_entry, 1, 1, 1, 1)
        create_acc_grid.attach(ck_pass_entry, 1, 2, 1, 1)
        create_acc_grid.attach(country_cbox, 1, 3, 1, 1)
        create_acc_grid.attach(gender_cbox, 1, 4, 1, 1)
        create_acc_grid.attach(age_range_cbox, 1, 5, 1, 1)
        #title
        create_acc_label = Gtk.Label(label="Create Account")

        confirm_submission = Gtk.Button(label="Submit",
                                        halign=3,
                                        )
        confirm_submission.connect("clicked", self.submit_acc, [user_entry,
                                                                pass_entry,
                                                                ck_pass_entry,
                                                                country_cbox,
                                                                gender_cbox,
                                                                age_range_cbox,
                                                                ])
        back_b = Gtk.Button(label="Back",
                            halign=3,
                            )
        back_b.connect("clicked", self.main_menu)
        b_grid = Gtk.Grid(halign=3,
                        column_spacing=12,
                        )
        b_grid.attach(confirm_submission, 0, 0, 1, 1)
        b_grid.attach(back_b, 1, 0, 1, 1)
        c_a_grid = Gtk.Grid(halign=3,
                        row_spacing=32,
                        column_homogeneous=True,
                        margin_right=32,
                        margin_left=32,
                        margin_bottom=48,
                        )
        c_a_grid.attach(create_acc_label, 0, 0, 1, 1)
        c_a_grid.attach(create_acc_grid, 0, 1, 1, 1)
        c_a_grid.attach(b_grid, 0, 2, 1, 1)
        self.grid.attach(c_a_grid, 0, 1, 1, 1)
        self.grid.show_all()


    def submit_acc(self, parent, widgets:list):
        u, p, ck_p, c, g, a = widgets[0], widgets[1], widgets[2], widgets[3], widgets[4], widgets[5]
        pop = Gtk.Popover()
        pop.set_relative_to(parent)
        if c.get_active() == -1 or g.get_active() == -1 or a.get_active() == -1:
            pop.add(Gtk.Label(label="Fill all parameters."))
            pop.show_all()
            popup()
            self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)
            return
        status = self.log.create_acc_gtk([
            u.get_text(),
            p.get_text(),
            ck_p.get_text(),
            model_country[c.get_active()][0],
            model_gender[g.get_active()][0],
            model_age[a.get_active()][0]
            ])
        pop.add(Gtk.Label(label=status))
        pop.show_all()
        pop.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)


    def login(self, parent):
        if self.log.login_gtk(self.user_entry.get_text(), self.pass_entry.get_text()):
            pop = Gtk.Popover()
            pop.set_relative_to(self.login_b)
            pop.add(Gtk.Label(label="Incorrect Login!"))
            pop.show_all()
            pop.popup()
            self.pass_entry.set_text("")
            self.t_pop = GLib.timeout_add(1000, self.pop_down, pop)
        else:
            parent = self.grid2.get_parent()
            while(self.grid.get_child_at(0, 1) != None):
                self.grid.remove_row(1)
            self.l = Gtk.Label(label="Logging in")
            self.l_value = 0
            parent.attach(self.l, 0, 1, 1, 1)
            parent.show_all()
            self.pass_entry.set_text("")
            self.user_entry.set_text("")
            print(self.log.get_u_pass())
            self.tid = GLib.timeout_add(300, self.loggin_in, parent)
            if self.log.get_logged_user() == "admin":
                self.t_admin = GLib.timeout_add(1600, self.admin_win, parent)
            else:
                self.t_user = GLib.timeout_add(1600, self.user_win, parent)


    def loggin_in(self, parent):
        if self.l.get_parent() != parent:
            self.l = None
            return False
        if self.l_value < 2:
            self.l_value += 1
        else:
            self.l_value = 0
        self.l.set_text(LOGGIN_IN[self.l_value])
        parent.show_all()
        return True


    def about(self, parent):
        about_win = Gtk.Popover()
        vbox = Gtk.Grid()
        vbox.add(Gtk.Label(label=ABOUT))
        about_win.add(vbox)
        about_win.set_relative_to(parent)
        about_win.show_all()
        about_win.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, about_win)


    def pop_down(self, parent):
        parent.popdown()


    def quit_app(self, parent):
        app.quit()



class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__()


    def do_activate(self):
        self.win = Window(self)
        self.win.show_all()


    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Application()
app.run(sys.argv)



#eof
