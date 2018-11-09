import numpy as np
import pandas as pd 
from scipy import stats

from summon import Summon


def main(): 
    input_name = input('Nombre del invocador (solo LAN):  ')
    search = Summon(input_name)

if __name__ == '__main__': main()