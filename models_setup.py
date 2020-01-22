#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


model_country = Gtk.ListStore(str)
model_age = Gtk.ListStore(str)
model_gender = Gtk.ListStore(str)
model_rating = Gtk.ListStore(str)
model_report = Gtk.ListStore(str)
model_isle = Gtk.ListStore(str)
model_county = Gtk.ListStore(str)
model_dificulty = Gtk.ListStore(str)
model_extension = Gtk.ListStore(str)
model_form = Gtk.ListStore(str)


for i in ["Daily", "Monthly", "Season"]:
    model_report.append([i])


RATINGS = [1, 2, 3, 4, 5]


for i in RATINGS:
    model_rating.append([str(i)])


AGES = [
        "12-18",
        "19-29",
        "30-39",
        "40-49",
        "50-64",
        "+65"
        ]


GENDERS = [
        "Male",
        "Female",
        "Other",
        ]


COUNTRIES = [
        "Afghanistan",
        "Albania",
        "Algeria",
        "Andorra",
        "Angola",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bhutan",
        "Bolivia",
        "Bosnia and Herzegovina",
        "Botswana",
        "Brazil",
        "Brunei",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cabo Verde",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Colombia",
        "Comoros",
        "Democratic Republic of the Congo",
        "Costa Rica",
        "Cote d'Ivoire",
        "Croatia",
        "Cuba",
        "Cyprus",
        "Czechia",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Eswatini",
        "Ethiopia",
        "Fiji",
        "Finland",
        "France",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Greece",
        "Grenada",
        "Guatemala",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Honduras",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Kosovo",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Mauritania",
        "Mauritius",
        "Mexico",
        "Micronesia",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "North Korea",
        "North Macedonia",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Qatar",
        "Romania",
        "Russia",
        "Rwanda",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Korea",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Sweden",
        "Switzerland",
        "Syria",
        "Taiwan",
        "Tajikistan",
        "Tanzania",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States of America",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Vatican City",
        "Venezuela",
        "Vietnam",
        "Yemen",
        "Zambia",
        "Zimbabwe",
        ]


ISLES = {
        "St. Maria": 0,
        "São Miguel": 1,
        "Terceira": 2,
        "Graciosa": 3,
        "São Jorge": 4,
        "Pico": 5,
        "Faial": 6,
        "Flores": 7,
        "Corvo": 8
        }


COUNTIES = {
        0: ["Vila do Porto"],
        1: [
            "Lagoa",
            "Nordeste",
            "Ponta Delgada",
            "Vila da Povoação",
            "Ribeira Grande",
            "Vila Franca do Campo"
            ],
        2: [
            "Angra do Heroísmo",
            "Praia da Vitória"
            ],
        3: ["Santa Cruz da Graciosa"],
        4: [
            "Calheta de São Jorge",
            "Velas"
            ],
        5: [
            "Lajes do Pico",
            "Madalena",
            "São Roque do Pico"
            ],
        6: ["Horta"],
        7: [
            "Lajes das Flores",
            "Santa Cruz das Flores"
            ],
        8: ["Vila do Corvo"]
        }


DIFICULTIES = [
        "Fácil",
        "Médio",
        "Difícil"
        ]


EXTENSIONS = [
        "<5Km",
        "5-10Km",
        "10-15Km",
        "15-30Km",
        ">30Km"
        ]


FORMS = ["Circular", "Linear"]


for i in COUNTRIES:
    model_country.append([i])


for i in AGES:
    model_age.append([i])


for i in GENDERS:
    model_gender.append([i])


for i in ISLES:
    model_isle.append([i])


for i in COUNTIES:
    for y in COUNTIES[i]:
        model_county.append([y])


for i in DIFICULTIES:
    model_dificulty.append([i])


for i in EXTENSIONS:
    model_extension.append([i])


for i in FORMS:
    model_form.append([i])



#eof
