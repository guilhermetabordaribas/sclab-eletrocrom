# -*- coding: utf-8 -*-
"""
Copyright (c) 2017 Guilherme Taborda Ribas.

Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved.

Copyright (c) 2017 NumPy developers.

Copyright (c) 2016 Riverbank Computing Limited.

Copyright (c) 2017 The Qt Company.


This file is part of EletroCrom.

    EletroCrom is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any later version.

    EletroCrom is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with EletroCrom.  If not, see <http://www.gnu.org/licenses/>.

"""

import csv
import numpy as np

class Eficiencia():
    def calcula_eficiencia(self, separador, codec, arquivos_densidadeCorrente, tempo_red, tempo_oxi,
                 arquivos_absorbancia, tempo_abs_red, tempo_abs_oxi,
                 ciclos, dt_ciclos, tempo_dx, area):
        
        tempo_abs = []
        absorbancia = []
        tempo_densidade = []
        densidade_corrente = []
        abs_red = []
        abs_oxi = []
        corrente_red = []
        corrente_oxi = []
        carga_red = []
        carga_oxi = []
        efic_coulmb = []

        with open(arquivos_absorbancia, encoding = codec) as f:
            reader = csv.reader(f, delimiter=separador) 
            for row in reader:
                t, c = row
                tempo_abs.append(float(t))
                absorbancia.append(float(c))
         
        for tmp in tempo_abs_red:
            try:
                abs_red.append(absorbancia[tempo_abs.index(float(tmp[1]))] - absorbancia[tempo_abs.index(float(tmp[0]))])
            except ValueError:
                return 'Intervalo(s) de Absorbância-Redução não encotrado. Por favor verificar Intervalo(s).'
        for tmp in tempo_abs_oxi:
            try:
                abs_oxi.append(absorbancia[tempo_abs.index(float(tmp[1]))] - absorbancia[tempo_abs.index(float(tmp[0]))])
            except ValueError:
                return 'Intervalo(s) de Absorbância-Oxidação não encotrado. Por favor verificar Intervalo(s)'

        j = 0     
        while j < len(arquivos_densidadeCorrente):
            i = 0
            tempo_densidade = []
            densidade_corrente = []
            corrente_red = []
            corrente_oxi = []
            with open(arquivos_densidadeCorrente[j], encoding = codec) as f:
                reader = csv.reader(f, delimiter=separador)
                for row in reader:
                    densidade_corrente.append(row)

            ##Corrente

            while i < len(densidade_corrente):
                if float(densidade_corrente[i][0]) >= tempo_red[0] and float(densidade_corrente[i][0]) <= tempo_red[1]:
                    corrente_red.append(float(densidade_corrente[i][1])/area)
                    
                elif float(densidade_corrente[i][0]) >= tempo_oxi[0] and float(densidade_corrente[i][0]) <= tempo_oxi[1]:
                    corrente_oxi.append(float(densidade_corrente[i][1])/area)
                i+=1

            carga_red.append(np.trapz(np.array(corrente_red), dx=tempo_dx))
            carga_oxi.append(np.trapz(np.array(corrente_oxi), dx=tempo_dx))                

            j+=1
            
        ec = []
        eer = []
        eeo = []
        i = 0
        while i < len(carga_red):
            if float(carga_oxi[i]) == 0.0:
                ec.append(0)
                eeo.append(0)
            else:
                ec.append(abs(100*float(carga_red[i])/float(carga_oxi[i])))
                eeo.append(abs(float(abs_oxi[i])/float(carga_oxi[i])))
            if float(carga_red[i]) == 0.0:
                eer.append(0)
            else:
                eer.append(abs(float(abs_red[i])/float(carga_red[i])))
            
            i += 1            

        return [carga_red, carga_oxi, abs_red, abs_oxi, ec, eer, eeo]


