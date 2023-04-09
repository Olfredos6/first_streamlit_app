import streamlit as S

import logging
import os


S.title("My Parents New Heathy Diner")
print(f""" Something to view 
  {dir(S)}
""")
logging.critical(os.path)
for p in os.scandir("."):
    logging.critical(p)
