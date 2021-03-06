import io
import re
import subprocess
import sys
import os
import getpass
import git
import shutil
import tempfile
from os.path import isfile, join

############################Set paths for file interactions###################################

path = "/home/%s/Desktop/robomax"% getpass.getuser()
path2 = "/home/%s/Desktop/robomax/osf_Files"% getpass.getuser()
path3 = "/home/%s/Desktop/robomax/gittemp"% getpass.getuser()
path_to_wrapper = "/home/%s/Desktop/robomax/gittemp/bin/"% getpass.getuser()
access_rights = 0o755

############################Creates the robomax folder########################################

def robomax_dir():
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path),
        osf_Files_dir()

if __name__ == "__robomax_dir__":
    robomax_dir()

####Creates osf file directory and initiates OSF file download cmd create_osf_Files()#########

def osf_Files_dir():
    try:
        os.mkdir(path2, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % path2)
    else:
        print("Successfully created the directory %s" % path2),
        os.chdir(path2)
        create_osf_Files()

if __name__ == "__osf_Files_dir__":
    osf_Files_dir()

##Downloads OSF files to osf_File directory

def create_osf_Files():
    
    osf_cmd = "wget https://osf.io/72p6g/download -v -O FOAM_readme.txt"
    subprocess.call(['bash', '-c', osf_cmd])
    osf_cmd = "wget https://osf.io/muan4/download -v -O FOAM-onto_rel1.tsv"
    subprocess.call(['bash', '-c', osf_cmd])
    osf_cmd = "wget https://osf.io/2hp7t/download -v -O KO_classification.txt"
    subprocess.call(['bash', '-c', osf_cmd])
    osf_cmd = "wget https://osf.io/bdpv5/download -v -O FOAM-hmm_rel1a.hmm.gz"
    subprocess.call(['bash', '-c', osf_cmd])
        
if __name__ == "__create_osf_Files__":
    create_osf_Files()

robomax_dir()

################################Install prokka and hmmer dependencies#########################

def install_dependencies():

    prokka_cmd = "conda install -c conda-forge -c bioconda -c defaults prokka"
    subprocess.call(prokka_cmd, shell=True)
    
    hmmer_cmd = "conda install -c bioconda hmmer"
    subprocess.call(hmmer_cmd, shell=True)

if __name__ == "__install_dependencies__":
    install_dependencies()

install_dependencies()
#############################get current wrapper from github###################################

def wrapper_download():

    git_URL = 'https://github.com/raw937/robomax.git'
    os.mkdir(path3, access_rights)
    os.chdir(path3)
    git.Repo.clone_from(git_URL, path3, branch='master')
    shutil.move(os.path.join(path_to_wrapper, 'Robomax_Wrapper_v8.py'), path)
    shutil.rmtree(path3)

if __name__ == "__wrapper_download__":
    wrapper_download()

wrapper_download()

