#Este código esta hecho con la intención de actualizar un archivo de texto que
#está junto a este código en el directorio cuando la variable stat se actualiza,
#Idea: https://stackoverflow.com/questions/6190468/how-to-trigger-function-on-value-change

import os
"""Contiene una variable stat, que se guarda en el archivo stat.txt, acompañando al código __main__,
es decir que si importa la clase desde otro código, stat.txt acompaña al que  importa y no este, que
como property se actualiza en tiempo real"""
class File:
    def __init__(self,stat_default = 1,_status_file_name="stat.txt"):
        self._stat = stat_default
        self._status_file_name = "\\"+_status_file_name
        self._dir = os.getcwd()
        self._path_stat_file = r'{}'.format(self._dir+self._status_file_name)
        pass

    def get_stat(self):
        #Obtiene variable del archivo
        with open(self._path_stat_file, 'r') as f:
            r = f.readline()
            if (r!=''):
                line = int(r)
            f.close()
        self._stat = line
        return self._stat

    def set_stat(self,val):
        self._stat = val
        with open(self._path_stat_file, 'w') as f:
            #Reescribe
            f.write(str(val))
            f.close()
        pass

    stat = property(get_stat,set_stat)
