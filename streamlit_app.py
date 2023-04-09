import streamlit as S

import logging
import os
import subprocess as sub

  
logging.critical(sub.run("cd / && ls -al", shell=True, stdout=sub.PIPE, stderr=sub.PIPE).stdout.decode("utf"))
