#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Version: 0.9.8
# Authors: Miguel Seridonio Almeida Fernandes,
#       Isaac Sousa,
#       Andre Pacheco


import datetime
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import sys


import Access
import Trail
import Visit
import Recommend
import Report
from models_setup import model_country, model_age, model_gender, ISLES
from models_setup import model_rating, model_report, model_isle, model_county
from models_setup import model_dificulty, model_extension, model_form, COUNTIES


ABOUT = """
License: GPL
Version: 0.9.8
Author: Miguel Seridoneo
"""

ACCESS_FILE = "files/accounts.txt"
TRAIL_FILE = "files/trails.txt"

LOGGIN_IN = [
        "Logging in.",
        "Logging in..",
        "Logging in..."
        ]


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

        self.update_model_trail()
        self.model_county = model_county
        self.log = Access.Access(ACCESS_FILE)
        self.visit = Visit.Visit()

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
        u_recomendation_button = Gtk.Button(label="Trail Recommendation")
        u_recomendation_button.connect("clicked", self.trail_recommendation, u_show_button)
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
                            )
        manage_grid = Gtk.Grid(halign=3,
                            column_spacing=16,
                            )
        add_button = Gtk.Button(label="Add Trail")
        add_button.connect("clicked", self.add_trail)
        remove_button = Gtk.Button(label="Remove Trail")
        remove_button.connect("clicked", self.remove_trail)
        modify_button = Gtk.Button(label="Modify Trail")
        modify_button.connect("clicked", self.modify_trail)
        show_button = Gtk.Button(label="Show Trails")
        show_button.connect("clicked", self.show_trails)
        manage_grid.attach(add_button, 0, 0, 1, 1)
        manage_grid.attach(remove_button, 1, 0, 1, 1)
        manage_grid.attach(modify_button, 2, 0, 1, 1)
        manage_grid.attach(show_button, 3, 0, 1, 1)
        a_back_button = Gtk.Button(label="Logout", halign=3)
        a_back_button.connect("clicked", self.main_menu)
        admin_menu.attach(manage_grid, 0, 0, 1, 1)
        admin_menu.attach(a_back_button, 0, 1, 1, 1)
        self.grid.remove(self.l)
        self.grid.attach(admin_menu, 0, 1, 1, 1)
        self.grid.attach(self.trails_table, 0, 2, 1, 1)
        self.grid.show_all()
        return False


    def add_trail(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        holder_grid = Gtk.Grid(halign=3,
                        row_spacing=16,
                        margin_bottom=64,
                        margin_right=64,
                        margin_left=64,
                        )
        add_grid = Gtk.Grid(halign=3,
                        column_spacing=16,
                        row_spacing=16,
                        )
        add_title = Gtk.Label(label="Add Trail")
        # self.model_county = model_county
        trail_label = Gtk.Label(label="Trail:", halign=2)
        trail_entry = Gtk.Entry(max_length=32, placeholder_text="Trail's Name")
        isle_label = Gtk.Label(label="Isle:", halign=2)
        isle_cbox = Gtk.ComboBox.new_with_model(model_isle)
        county_label = Gtk.Label(label="County:", halign=2)
        county_cbox = Gtk.ComboBox.new_with_model(self.model_county)
        gps_label = Gtk.Label(label="GPS:", halign=2)
        gps_entry = Gtk.Entry(placeholder_text="Coordenates",
                            max_length=16,
                            )
        dfct_label = Gtk.Label(label="Dificulty:", halign=2)
        dfct_cbox = Gtk.ComboBox.new_with_model(model_dificulty)
        ext_label = Gtk.Label(label="Extension:", halign=2)
        ext_cbox = Gtk.ComboBox.new_with_model(model_extension)
        form_label = Gtk.Label(label="Form:", halign=2)
        form_cbox = Gtk.ComboBox.new_with_model(model_form)
        desc_label = Gtk.Label(label="Description:", halign=2)
        desc_entry = Gtk.Entry(max_length=64, placeholder_text="Brief Description")
        cell = Gtk.CellRendererText()
        isle_cbox.pack_start(cell, True)
        isle_cbox.add_attribute(cell, "text", 0)
        county_cbox.pack_start(cell, True)
        county_cbox.add_attribute(cell, "text", 0)
        dfct_cbox.pack_start(cell, True)
        dfct_cbox.add_attribute(cell, "text", 0)
        ext_cbox.pack_start(cell, True)
        ext_cbox.add_attribute(cell, "text", 0)
        form_cbox.pack_start(cell, True)
        form_cbox.add_attribute(cell, "text", 0)
        isle_cbox.connect("changed", self.change_county_cbox, [county_cbox, isle_cbox])
        add_grid.attach(trail_label, 0, 0, 1, 1)
        add_grid.attach(trail_entry, 1, 0, 1, 1)
        add_grid.attach(isle_label, 0, 1, 1, 1)
        add_grid.attach(isle_cbox, 1, 1, 1, 1)
        add_grid.attach(county_label, 2, 1, 1, 1)
        add_grid.attach(county_cbox, 3, 1, 1, 1)
        add_grid.attach(gps_label, 2, 0, 1, 1)
        add_grid.attach(gps_entry, 3, 0, 1, 1)
        add_grid.attach(dfct_label, 4, 1, 1, 1)
        add_grid.attach(dfct_cbox, 5, 1, 1, 1)
        add_grid.attach(ext_label, 0, 2, 1, 1)
        add_grid.attach(ext_cbox, 1, 2, 1, 1)
        add_grid.attach(form_label, 2, 2, 1, 1)
        add_grid.attach(form_cbox, 3, 2, 1, 1)
        add_grid.attach(desc_label, 4, 0, 1, 1)
        add_grid.attach(desc_entry, 5, 0, 1, 1)
        submit_button = Gtk.Button(label="Submit", halign=3)
        submit_button.connect("clicked", self.submit_add_trail, [trail_entry,
                                                                isle_cbox,
                                                                county_cbox,
                                                                gps_entry,
                                                                dfct_cbox,
                                                                ext_cbox,
                                                                form_cbox,
                                                                desc_entry
                                                                ])
        holder_grid.attach(add_title, 0, 0, 1, 1)
        holder_grid.attach(add_grid, 0, 1, 1, 1)
        holder_grid.attach(submit_button, 0, 2, 1, 1)
        self.grid.attach(holder_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def submit_add_trail(self, parent, w:list):
        t, i, c, g  = w[0], w[1], w[2], w[3]
        df, e, f, desc = w[4], w[5], w[6], w[7]
        pop = Gtk.Popover.new(parent)
        if(i.get_active() == -1 or c.get_active() == -1 or
                df.get_active() == -1 or e.get_active() == -1 or
                f.get_active() == -1 or t.get_text() == "" or
                g.get_text() == "" or desc.get_text() == ""):
            pop.add(Gtk.Label(label="Fill all parameters!"))
            pop.show_all()
            pop.popup()
            self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)
            return
        self.trail.modify_file_trail([t.get_text(),
                            model_isle[i.get_active()][0],
                            self.model_county[c.get_active()][0],
                            g.get_text(),
                            model_dificulty[df.get_active()][0],
                            model_extension[e.get_active()][0],
                            model_form[f.get_active()][0],
                            desc.get_text()
                            ])
        self.update_model_trail()
        t.set_text("")
        i.set_active(-1)
        c.set_active(-1)
        g.set_text("")
        df.set_active(-1)
        e.set_active(-1)
        f.set_active(-1)
        desc.set_text("")
        pop.add(Gtk.Label(label="Submit Successfully!"))
        pop.show_all()
        pop.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)


    def change_county_cbox(self, parent, widgets):
        c, i = widgets[0], widgets[1]
        i = model_isle[i.get_active()][0]
        l = COUNTIES[ISLES[i]]
        self.model_county = Gtk.ListStore(str)
        for i in l:
            self.model_county.append([i])
        c.set_model(self.model_county)
        c.set_active(-1)


    def remove_trail(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        holder_grid = Gtk.Grid(halign=3,
                        row_spacing=16,
                        margin_bottom=64,
                        margin_right=64,
                        margin_left=64,
                        )
        remove_grid = Gtk.Grid(halign=3,
                        column_spacing=16,
                        row_spacing=16,
                        )
        remove_title = Gtk.Label(label="Remove Trail")
        trail_label = Gtk.Label(label="Trail:", halign=2)
        trail_cbox = Gtk.ComboBox.new_with_model(self.model_trail)
        cell = Gtk.CellRendererText()
        trail_cbox.pack_start(cell, True)
        trail_cbox.add_attribute(cell, "text", 0)
        submit_b = Gtk.Button(label="Submit")
        submit_b.connect("clicked", self.submit_remove_trail, trail_cbox)
        remove_grid.attach(trail_label, 0, 0, 1, 1)
        remove_grid.attach(trail_cbox, 1, 0, 1, 1)
        holder_grid.attach(remove_title, 0, 0, 1, 1)
        holder_grid.attach(remove_grid, 0, 1, 1, 1)
        holder_grid.attach(submit_b, 0, 2, 1, 1)
        self.grid.attach(holder_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def submit_remove_trail(self, parent, t):
        pop = Gtk.Popover.new(parent)
        if self.model_trail[t.get_active()][0] == -1:
            pop.add(Gtk.Label(label="Please choose a Trail!"))
            pop.show_all()
            pop.popup()
            self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)
            return
        self.trail.remove_file_trail(self.model_trail[t.get_active()][0])
        self.update_model_trail()
        t.set_model(self.model_trail)
        pop.add(Gtk.Label(label="Submitted Successfully!"))
        pop.show_all()
        pop.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)

    def modify_trail(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        holder_grid = Gtk.Grid(halign=3,
                        row_spacing=16,
                        margin_bottom=64,
                        margin_right=64,
                        margin_left=64,
                        )
        modify_grid = Gtk.Grid(halign=3,
                        column_spacing=16,
                        row_spacing=16,
                        )
        modify_title = Gtk.Label(label="Modify Trail")
        trail_label = Gtk.Label(label="Trail:", halign=2)
        trail_cbox = Gtk.ComboBox.new_with_model(self.model_trail)
        isle_label = Gtk.Label(label="Isle:", halign=2)
        isle_cbox = Gtk.ComboBox.new_with_model(model_isle)
        isle_cbox.set_sensitive(False)
        county_label = Gtk.Label(label="County:", halign=2)
        county_cbox = Gtk.ComboBox.new_with_model(self.model_county)
        county_cbox.set_sensitive(False)
        gps_label = Gtk.Label(label="GPS:", halign=2)
        gps_entry = Gtk.Entry(placeholder_text="Coordenates",
                            max_length=16,
                            sensitive=False
                            )
        dfct_label = Gtk.Label(label="Dificulty:", halign=2)
        dfct_cbox = Gtk.ComboBox.new_with_model(model_dificulty)
        dfct_cbox.set_sensitive(False)
        ext_label = Gtk.Label(label="Extension:", halign=2)
        ext_cbox = Gtk.ComboBox.new_with_model(model_extension)
        ext_cbox.set_sensitive(False)
        form_label = Gtk.Label(label="Form:", halign=2)
        form_cbox = Gtk.ComboBox.new_with_model(model_form)
        form_cbox.set_sensitive(False)
        desc_label = Gtk.Label(label="Description:", halign=2)
        desc_entry = Gtk.Entry(max_length=64, sensitive=False)
        cell = Gtk.CellRendererText()
        trail_cbox.pack_start(cell, True)
        trail_cbox.add_attribute(cell, "text", 0)
        isle_cbox.pack_start(cell, True)
        isle_cbox.add_attribute(cell, "text", 0)
        county_cbox.pack_start(cell, True)
        county_cbox.add_attribute(cell, "text", 0)
        dfct_cbox.pack_start(cell, True)
        dfct_cbox.add_attribute(cell, "text", 0)
        ext_cbox.pack_start(cell, True)
        ext_cbox.add_attribute(cell, "text", 0)
        form_cbox.pack_start(cell, True)
        form_cbox.add_attribute(cell, "text", 0)
        isle_cbox.connect("changed", self.change_county_cbox, [county_cbox, isle_cbox])
        trail_cbox.connect("changed", self.modify_unset_sensitive, [trail_cbox,
                                                                isle_cbox,
                                                                county_cbox,
                                                                gps_entry,
                                                                dfct_cbox,
                                                                ext_cbox,
                                                                form_cbox,
                                                                desc_entry
                                                                ])
        modify_grid.attach(trail_label, 0, 0, 1, 1)
        modify_grid.attach(trail_cbox, 1, 0, 1, 1)
        modify_grid.attach(isle_label, 0, 1, 1, 1)
        modify_grid.attach(isle_cbox, 1, 1, 1, 1)
        modify_grid.attach(county_label, 2, 1, 1, 1)
        modify_grid.attach(county_cbox, 3, 1, 1, 1)
        modify_grid.attach(gps_label, 2, 0, 1, 1)
        modify_grid.attach(gps_entry, 3, 0, 1, 1)
        modify_grid.attach(dfct_label, 4, 1, 1, 1)
        modify_grid.attach(dfct_cbox, 5, 1, 1, 1)
        modify_grid.attach(ext_label, 0, 2, 1, 1)
        modify_grid.attach(ext_cbox, 1, 2, 1, 1)
        modify_grid.attach(form_label, 2, 2, 1, 1)
        modify_grid.attach(form_cbox, 3, 2, 1, 1)
        modify_grid.attach(desc_label, 4, 0, 1, 1)
        modify_grid.attach(desc_entry, 5, 0, 1, 1)
        submit_button = Gtk.Button(label="Submit", halign=3)
        submit_button.connect("clicked", self.submit_modify_trail, [trail_cbox,
                                                                isle_cbox,
                                                                county_cbox,
                                                                gps_entry,
                                                                dfct_cbox,
                                                                ext_cbox,
                                                                form_cbox,
                                                                desc_entry
                                                                ])
        holder_grid.attach(modify_title, 0, 0, 1, 1)
        holder_grid.attach(modify_grid, 0, 1, 1, 1)
        holder_grid.attach(submit_button, 0, 2, 1, 1)
        self.grid.attach(holder_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def submit_modify_trail(self, parent, w:list):
        t, i, c, g  = w[0], w[1], w[2], w[3]
        df, e, f, desc = w[4], w[5], w[6], w[7]
        pop = Gtk.Popover.new(parent)
        if(i.get_active() == -1 or c.get_active() == -1 or
                df.get_active() == -1 or e.get_active() == -1 or
                f.get_active() == -1 or t.get_active() == -1 or
                g.get_text() == "" or desc.get_text() == ""):
            pop.add(Gtk.Label(label="Fill all parameters."))
            pop.show_all()
            pop.popup()
            self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)
            return
        self.trail.modify_file_trail([self.model_trail[t.get_active()][0],
                            model_isle[i.get_active()][0],
                            self.model_county[c.get_active()][0],
                            g.get_text(),
                            model_dificulty[df.get_active()][0],
                            model_extension[e.get_active()][0],
                            model_form[f.get_active()][0],
                            desc.get_text()
                            ])
        self.update_model_trail()
        pop.add(Gtk.Label(label="Submitted Successfully!"))
        pop.show_all()
        pop.popup()
        self.t_pop = GLib.timeout_add(3000, self.pop_down, pop)


    def modify_unset_sensitive(self, parent, w:list):
        t, i, c, g  = w[0], w[1], w[2], w[3]
        df, e, f, desc = w[4], w[5], w[6], w[7]
        if t.get_active() == -1:
            return
        i.set_sensitive(True)
        c.set_sensitive(True)
        g.set_sensitive(True)
        df.set_sensitive(True)
        e.set_sensitive(True)
        f.set_sensitive(True)
        desc.set_sensitive(True)


    def show_trails(self, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        self.grid.attach(self.trails_table, 0, 2, 1, 1)
        self.grid.show_all()


    def trail_experience_input(self, par, parent):
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

        trail = Gtk.ComboBox.new_with_model(self.model_trail)
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
        pop = Gtk.Popover.new(parent)
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
        date = y+'-'+m+'-'+d
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


    def trail_recommendation(self, par, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        user_att = [self.log.get_cty(), self.log.get_gdr(), self.log.get_age()]
        rec = Recommend.Recommend(self.visit.get_rec_info(), user_att)
        new_recommendation = Gtk.Label(label="We recommend this trail: "+rec.get_rec())
        self.grid.attach(new_recommendation, 0, 2, 1, 1)
        self.grid.show_all()


    def trail_report(self, par, parent):
        while(self.grid.get_child_at(0, 2) != None):
            self.grid.remove_row(2)
        trail_cb = Gtk.ComboBox.new_with_model(self.model_trail)
        mode_cb = Gtk.ComboBox.new_with_model(model_report)
        cell = Gtk.CellRendererText()
        trail_cb.pack_start(cell, True)
        trail_cb.add_attribute(cell, "text", 0)
        mode_cb.pack_start(cell, True)
        mode_cb.add_attribute(cell, "text", 0)
        trail_cb.connect("changed", self.change_report, [trail_cb, mode_cb])
        mode_cb.connect("changed", self.change_report, [trail_cb, mode_cb])
        trail_label = Gtk.Label(label="Trail:")
        period_label = Gtk.Label(label="Periodicity:")
        report_grid = Gtk.Grid(halign=3,
                            column_spacing=16,
                            # column_homogeneous=True,
                            )
        report_grid.attach(trail_label, 0, 0, 1, 1)
        report_grid.attach(period_label, 2, 0, 1, 1)
        report_grid.attach(trail_cb, 1, 0, 1, 1)
        report_grid.attach(mode_cb, 3, 0, 1, 1)
        self.grid.attach(report_grid, 0, 2, 1, 1)
        self.grid.show_all()


    def change_report(self, par, widgets:list):
        t, m = widgets[0], widgets[1]
        if t.get_active() == -1 or m.get_active() == -1:
            return
        mode = model_report[m.get_active()][0]
        d = datetime.date.today()
        d = str(d)
        if mode == "Monthly" or mode == "Season":
            d = d[:-3]
        trail = self.model_trail[t.get_active()][0]
        #get trail info with right date
        max_rating = Gtk.Label(label="Max Rating")
        min_rating = Gtk.Label(label="Min Rating")
        number_visitors = Gtk.Label(label="Number of Visitors")
        mode_rating = Gtk.Label(label="Rating Mode")
        max_rating_value = Gtk.Label(label="")
        min_rating_value = Gtk.Label(label="")
        number_visitors_value = Gtk.Label(label="")
        mode_rating_value = Gtk.Label(label="")
        report_grid = Gtk.Grid(halign=3,
                            column_spacing=16,
                            margin_bottom=64,
                            )
        report_grid.attach(max_rating, 0, 0, 1, 1)
        report_grid.attach(min_rating, 1, 0, 1, 1)
        report_grid.attach(number_visitors, 2, 0, 1, 1)
        report_grid.attach(mode_rating, 3, 0, 1, 1)
        report_grid.attach(max_rating_value, 0, 1, 1, 1)
        report_grid.attach(min_rating_value, 1, 1, 1, 1)
        report_grid.attach(number_visitors_value, 2, 1, 1, 1)
        report_grid.attach(mode_rating_value, 3, 1, 1, 1)
        while(self.grid.get_child_at(1, 3) != None):
            self.grid.remove_row(4)
        self.grid.attach(report_grid, 0, 3, 1, 1)
        self.grid.show_all()


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
        pop = Gtk.Popover.new(parent)
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


    def update_model_trail(self):
        self.trail = Trail.Trail(TRAIL_FILE)
        trail_rows = self.trail.get_file_trails()
        order_i = sorted(trail_rows)
        while(self.trails_table.get_child_at(0, 0) != None):
            self.trails_table.remove_row(0)
        r = 0
        for i in order_i:
            c = 0
            for n in trail_rows[i]:
                self.trails_table.attach(Gtk.Label(label=trail_rows[i][n]), c, r, 1, 1)
                c += 1
            r += 1

        self.model_trail = Gtk.ListStore(str)
        for i in order_i:
            if i != 'Name':
                self.model_trail.append([i])



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
