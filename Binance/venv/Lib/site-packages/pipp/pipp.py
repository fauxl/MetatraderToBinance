from __future__ import print_function
import json
import subprocess
import pip
import sys
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _get_recommendations(library):
    reco_path = os.path.join(_ROOT, '../', 'data/recommendations.json')
    with open(reco_path) as f:
        recos = json.load(f).get(library, [])
        for reco, _ in sorted(recos, key=lambda z: z[1]):
            yield reco 

def pip_install(args):
    try:
        subprocess.check_call(['pip'] + args)
    except subprocess.CalledProcessError:
        sys.exit()


def main(n_recommendations=2):
    pass_to_pip = sys.argv[1:]
    pip_install(pass_to_pip)

    library_being_install = sys.argv[-1]
    libaries_installed = {lib.project_name for lib in pip.get_installed_distributions()}

    n_recommendations_shown = 0
    for reco in _get_recommendations(library_being_install):
        if reco not in libaries_installed:
            _recommend_library(reco, library_being_install)
            n_recommendations_shown += 1
        if n_recommendations_shown >= n_recommendations:
            break
        


def _recommend_library(reco_lib, reason_lib):
    print("""pipp: Other users who installed {bold}{reason_lib}{end} also installed {bold}{reco_lib}{end}""".format(end=bcolors.ENDC, bold=bcolors.BOLD, reason_lib=reason_lib, reco_lib=reco_lib))





