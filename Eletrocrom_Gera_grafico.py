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

import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Button, CheckButtons
from matplotlib.cbook import get_sample_data

class Gera_grafico():
    def __init__(self, resultado):
        self.dados_ef = resultado
        self.str_relatorio = []
        self.show_imagem = False
        self.tabela = []
    
    def show_grafico(self, ciclos):
        carga_red = self.dados_ef[0]
        carga_oxi = self.dados_ef[1]
        vabs_red = self.dados_ef[2]
        vabs_oxi = self.dados_ef[3]
        ec = self.dados_ef[4]
        eer = self.dados_ef[5]
        eeo = self.dados_ef[6]
        
        saldo_aux = 0
        
        fig = plt.figure(figsize=(10, 5))
        fig.canvas.set_window_title('Resultado de Eficiência')
##        fig.patch.set_facecolor('#222211')
        font_color1 = 'Black'
        width = 0.35
        
#######################
##Eficiência Coulômbica
#######################
            
        ax1_range = np.arange(len(ec))
        ax1 = plt.subplot(2,3,1)
        ax1.bar(ax1_range, ec, width,alpha=0.9, color='DarkGreen')           
        ax1.set_xticks(ax1_range)
        ax1.set_xticklabels(ciclos, rotation='horizontal', fontsize = 8)
        ax1.set_xlabel('Nº de Ciclos', color = font_color1)
        ax1.set_title('Eficiência Coulômbica (%)', fontsize = 10, color = font_color1)
        ax1.tick_params(colors=font_color1)        
        ax1.yaxis.grid(True)
        
############################
####Eficiência Eletrocrômica
############################
        ax2_range = np.arange(len(eer))
        ax2 = plt.subplot(2,3,2)
        ax2.bar(ax2_range, eer, width,alpha=0.9, color='DarkBlue', label='Redução')
        ax2.bar(ax2_range+width, eeo, width,alpha=0.9, color='DarkRed', label='Oxidação')
        ax2.set_xticks(ax2_range + width/2)
        ax2.set_xticklabels(ciclos, rotation='horizontal', fontsize = 8)
        ax2.set_xlabel('Nº de Ciclos', color = font_color1)
        ax2.set_title('Eficiência Eletrocrômica (%)', fontsize = 10, color = font_color1)
        ax2.tick_params(colors=font_color1)
        ax2.yaxis.grid(True)
        ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, shadow=True)

################################
####Tabela com dados
################################
        
        nomes = ['Ciclos', 'Carga Red', 'Carga Oxi', 'EC%', 'Abs Red', 'Abs Oxi', 'EER', 'EEO']
        
        collabel=ciclos

        i = 0
        while i < len(collabel):
            self.tabela.append([collabel[i],round(1000*carga_red[i],2),round(1000*carga_oxi[i],2),round(ec[i],1),round(vabs_red[i],4),round(vabs_oxi[i],4),round(eer[i],2),round(eeo[i],2)])
            i+=1
                
        ax3 = plt.subplot(2,3,(4,6))
        ax3.axis('off')
        ax3.table(cellText=self.tabela, colLabels=nomes,loc='center')

        fig.tight_layout()

        ax_dados_csv = plt.axes([0.725, 0.565, 0.25, 0.05])
        button_dados_csv = Button(ax_dados_csv, "Salvar Dados da Tabela'.csv'")
        button_dados_csv.on_clicked(self.clicked_button_dados_csv)
        
        plt.show()
        

    def clicked_button_dados_csv(self, label):
        now = str(datetime.datetime.now())
        now = now.replace(' ', '_').replace(':', '-').replace('.', '-')
        now = 'relatorios/relatorio_'+now + '.csv'
        print(now)
        ##Primeira Linha
        saveLine = 'Ciclos,Carga Red,Carga Oxi,EC%,Abs Red,Abs Oxi,EER,EEO\n'
        saveFile = open(now, 'a')
        saveFile.write(saveLine)
        saveFile.close()
            
        for linha in self.tabela:
            saveLine = str(linha[0])+','+str(linha[1])+','+str(linha[2])+','+str(linha[3])+','+str(linha[4])+','+str(linha[5])+',' +str(linha[6])+','+str(linha[7])+'\n'
            saveFile = open(now, 'a')
            saveFile.write(saveLine)
            saveFile.close()


            

   
