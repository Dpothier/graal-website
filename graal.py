#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template
app = Flask(__name__)


member_status_pretty_names = {"undergrad": {"fr": "Étudiant sous-gradué", "en": "Undergraduate student"},
                              "master": {"fr": "Étudiant de maîtrise", "en": "Masters student"},
                              "phd": {"fr": "Étudiant doctorant", "en": "PhD Student"},
                              "postdoc": {"fr": "Chercheur post-doctoral", "en": "Postdoctoral Researcher"},
                              "prof": {"fr": "Professeur", "en": "Professor"}}


class Graalien(object):
    def __init__(self, first_name, last_name, status, joined_year, face_picture=None, linkedin=None, scholar=None,
                 github=None, website=None, twitter=None, departed=False):
        self.first_name = first_name
        self.last_name = last_name
        self.status_ = status
        self.joined_year = joined_year
        self.face_picture = face_picture
        self.linkedin = linkedin
        self.scholar_ = scholar
        self.github = github
        self.website = website
        self.twitter = twitter
        self.departed = departed

        if status not in member_status_pretty_names.keys():
            raise ValueError("Incorrect graalien status. Supporter values are {0!s}".format(self.status_pretty_names))

    @property
    def scholar(self):
        return self.scholar_ + "&view_op=list_works&sortby=pubdate" if self.scholar_ is not None else None

    @property
    def status(self):
        return member_status_pretty_names[self.status_]


@app.route('/')
def hello():
    professors = [
        Graalien(first_name="François",
                 last_name="Laviolette",
                 status="prof",
                 joined_year=-10000,
                 face_picture="images/faces/flaviolette.png",
                 linkedin="https://www.linkedin.com/in/francois-laviolette-3933879/",
                 scholar="https://scholar.google.ca/citations?user=uwwWC3cAAAAJ",
                 website="https://www.ift.ulaval.ca/departement-et-professeurs/professeurs-et-personnel/professeurs-reguliers/fiche/show/laviolette-francois/"),
        Graalien(first_name="Mario",
                 last_name="Marchand",
                 status="prof",
                 joined_year=-10000,
                 face_picture="images/faces/mmarchand.png",
                 linkedin="https://www.linkedin.com/in/mario-marchand-50460913/",
                 scholar="https://scholar.google.ca/citations?user=M792u2sAAAAJ",
                 website="https://www.ift.ulaval.ca/departement-et-professeurs/professeurs-et-personnel/professeurs-reguliers/fiche/show/marchand-mario/"),
        Graalien(first_name="Luc",
                 last_name="Lamontagne",
                 status="prof",
                 joined_year=2004,
                 face_picture="images/faces/llamontagne.png",
                 linkedin="https://www.linkedin.com/in/luc-lamontagne-a42566b/",
                 scholar="https://scholar.google.com/citations?user=mCsuyb0AAAAJ",
                 website="http://www.ift.ulaval.ca/~lamontagne/lamontagne-en.html"),
        Graalien(first_name="Jacques",
                 last_name="Corbeil",
                 status="prof",
                 joined_year=2010,
                 face_picture="images/faces/jcorbeil.png",
                 linkedin="https://www.linkedin.com/in/jacques-corbeil-0486391/",
                 scholar="https://scholar.google.ca/citations?user=ZOxQV80AAAAJ",
                 website="http://corbeillab.genome.ulaval.ca/team_member/jacques-corbeil/"),
        Graalien(first_name="Richard",
                 last_name="Khoury",
                 status="prof",
                 joined_year=2016,
                 face_picture="images/faces/rkhoury.png",
                 linkedin="https://www.linkedin.com/in/richard-khoury-59b92130",
                 scholar="http://scholar.google.ca/citations?user=PgyHf0oAAAAJ",
                 website="http://www2.ift.ulaval.ca/~rikho/")
    ]
    graaliens = [
        Graalien(first_name="Alexandre",
                 last_name="Drouin",
                 status="phd",
                 joined_year=2012,
                 face_picture="images/faces/adrouin.png",
                 linkedin="https://www.linkedin.com/in/drouinalexandre/",
                 scholar="https://scholar.google.ca/citations?user=LR6aJcEAAAAJ",
                 github="https://github.com/aldro61",
                 website="http://graal.ift.ulaval.ca/adrouin/",
                 twitter="https://twitter.com/alexandredrouin"),
        Graalien(first_name="Ulysse",
                 last_name="Côté Allard",
                 status="phd",
                 joined_year=2014,
                 face_picture="images/faces/uacote.png",
                 scholar="https://scholar.google.ca/citations?user=RF5bU6sAAAAJ&hl",
                 github="https://github.com/giguelingueling",
                 website="http://graal.ift.ulaval.ca/ulysse/"),
        Graalien(first_name="Gaël",
                 last_name="Letarte St-Pierre",
                 status="undergrad",
                 joined_year=2016,
                 face_picture="images/faces/gletarte.png",
                 scholar="https://scholar.google.ca/citations?user=XMCOvKoAAAAJ",
                 github="https://github.com/gletarte"),
        Graalien(first_name="Pier-Luc",
                 last_name="Plante",
                 status="phd",
                 joined_year=2014,
                 face_picture="images/faces/plplante.png",
                 linkedin="https://www.linkedin.com/in/pier-luc-plante-b777716b/",
                 scholar="https://scholar.google.ca/citations?user=8Vp-4GgAAAAJ",
                 github="https://github.com/plpla"),
        Graalien(first_name="Frédéric",
                 last_name="Raymond",
                 status="postdoc",
                 joined_year=2011,
                 face_picture="images/faces/fraymond.png",
                 linkedin="https://www.linkedin.com/in/fredericraymond/",
                 scholar="https://scholar.google.ca/citations?user=Ulexpm0AAAAJ",
                 github="https://github.com/fredericraymond",
                 website="http://corbeillab.genome.ulaval.ca/team_member/frederic-raymond/",
                 twitter="https://twitter.com/fredericraymond"),
        Graalien(first_name="Francis",
                 last_name="Brochu",
                 status="phd",
                 joined_year=2014,
                 face_picture="images/faces/fbrochu.png",
                 linkedin="https://www.linkedin.com/in/francis-brochu-a31948139/",
                 scholar="https://scholar.google.ca/citations?user=eH0dEcwAAAAJ",
                 github="https://github.com/PhrankBrochu"),
        Graalien(first_name="Jonathan",
                 last_name="Gingras",
                 status="master",
                 joined_year=2016,
                 face_picture="images/faces/jgingras.png",
                 linkedin="https://www.linkedin.com/in/jonathan-gingras-084b3a84/",
                 github="https://github.com/jonathangingras"),
        Graalien(first_name="Hana",
                 last_name="Ajakan",
                 status="phd",
                 joined_year=2014,
                 face_picture="images/faces/hajakan.png",
                 linkedin="https://www.linkedin.com/in/hana-ajakan-9a4379b2/",
                 scholar="https://scholar.google.ca/citations?user=jalwnN8AAAAJ",
                 github="https://github.com/haajakan"),
        Graalien(first_name="Maxime",
                 last_name="Déraspe",
                 status="phd",
                 joined_year=2014,
                 face_picture="images/faces/mderaspe.png",
                 linkedin="https://www.linkedin.com/in/MaximeDeraspe",
                 scholar="https://scholar.google.ca/citations?user=CqOMEq0AAAAJ",
                 github="https://github.com/zorino",
                 website="http://maxime.deraspe.net"),
        Graalien(first_name="Nicolas",
                 last_name="Garneau",
                 status="master",
                 joined_year=2014,
                 face_picture="images/faces/ngarneau.png",
                 linkedin="https://www.linkedin.com/in/nicolas-garneau-ab98b526/",
                 github="https://github.com/ngarneau"),
        Graalien(first_name="Mazid Abiodoun",
                 last_name="Osseni",
                 status="phd",
                 joined_year=2015,
                 face_picture="images/faces/mosseni.png",
                 linkedin="https://www.linkedin.com/in/mazidosseni/",
                 scholar="https://scholar.google.ca/citations?user=lu6ZxEYAAAAJ",
                 github="https://github.com/dizam92"),
        Graalien(first_name="Jean-Francis",
                 last_name="Roy",
                 status="phd",
                 joined_year=2008,
                 face_picture="images/faces/jfroy.png",
                 linkedin="https://www.linkedin.com/in/jeanfrancisroy/",
                 scholar="https://scholar.google.ca/citations?user=AjjKEd0AAAAJ",
                 github="https://github.com/jeanfrancisroy",
                 website="https://jeanfrancisroy.info",
                 departed=True),
        Graalien(first_name="Pascal",
                 last_name="Germain",
                 status="phd",
                 joined_year=2007,
                 face_picture="images/faces/pgermain.png",
                 linkedin="https://www.linkedin.com/in/germainml/",
                 scholar="https://scholar.google.com/citations?user=mgOIj_4AAAAJ",
                 github="https://github.com/pgermain",
                 website="http://www.di.ens.fr/~germain/",
                 departed=True)
    ]

    # Sort by name date
    graaliens = sorted(graaliens, key=lambda x: x.joined_year, reverse=False)
    graaliens = professors + graaliens
    return render_template('index.html',
                           graaliens=[g for g in graaliens if not g.departed],
                           alumni=[g for g in graaliens if g.departed])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3333, debug=False)
