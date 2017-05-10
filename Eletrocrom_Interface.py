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
import os
import csv

from PyQt5 import QtCore, QtGui, QtWidgets

import Eletrocrom_Eficiencia
import Eletrocrom_Gera_grafico

class Ui_Form(object):
    def __init__(self):
        self.arq_corr = []
        self.arq_abs = ''
        self.tempo_red = []
        self.tempo_oxi = []
        self.tempo_abs_red = []
        self.tempo_abs_oxi = []

        self.codec_lista = ['UTF-8','UTF-7','UTF-16',
                           'ISO-8859-1','ISO-8859-2','ISO-8859-3',
                           'ASCII']

        self.delimitador_lista = ['","', '";"', '":"',
                                  '"|"', '"-"', '" "']
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 488)

        font = QtGui.QFont()
        font.setPointSize(10)        
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        
        self.groupBoxDadosArq = QtWidgets.QGroupBox(self.tab)
        self.groupBoxDadosArq.setObjectName("groupBoxDadosArq")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxDadosArq)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.labelCodec = QtWidgets.QLabel(self.groupBoxDadosArq)
        self.labelCodec.setFont(font)
        self.labelCodec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCodec.setObjectName("labelCodec")
        self.gridLayout_4.addWidget(self.labelCodec, 0, 2, 1, 1)
        
        self.comboBoxDelimitador = QtWidgets.QComboBox(self.groupBoxDadosArq)
        self.comboBoxDelimitador.setFont(font)
        self.comboBoxDelimitador.setObjectName("comboBoxSeparador")
        self.comboBoxDelimitador.setToolTip("<html><head/><body><p>Escolha o delimitador dos arquivos '.csv'.</p></body></html>")
        for item in self.delimitador_lista:
            self.comboBoxDelimitador.addItem(item)
        self.gridLayout_4.addWidget(self.comboBoxDelimitador, 0, 1, 1, 1)
        
        self.comboBoxCodecs = QtWidgets.QComboBox(self.groupBoxDadosArq)
        self.comboBoxCodecs.setFont(font)
        self.comboBoxCodecs.setObjectName("comboBoxCodecs")
        self.comboBoxCodecs.setToolTip("<html><head/><body><p>Escolha o codec do arquivo '.csv'.</p></body></html>")
        for item in self.codec_lista:
            self.comboBoxCodecs.addItem(item)
        self.gridLayout_4.addWidget(self.comboBoxCodecs, 0, 3, 1, 1)
        
        self.labelDelimitador = QtWidgets.QLabel(self.groupBoxDadosArq)
        self.labelDelimitador.setFont(font)
        self.labelDelimitador.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDelimitador.setObjectName("labelDelimitador")
        self.gridLayout_4.addWidget(self.labelDelimitador, 0, 0, 1, 1)
        
        self.gridLayout.addWidget(self.groupBoxDadosArq, 0, 0, 1, 1)
        
        self.pushButtonCalcula = QtWidgets.QPushButton(self.tab)
        self.pushButtonCalcula.setStyleSheet("background-color: MidnightBlue; color: White")
        self.pushButtonCalcula.setObjectName("pushButtonCalcula")
        self.gridLayout.addWidget(self.pushButtonCalcula, 4, 0, 1, 2)
        
        self.groupBoxDadosGerais = QtWidgets.QGroupBox(self.tab)
        self.groupBoxDadosGerais.setObjectName("groupBoxDadosGerais")
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxDadosGerais)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.verticalLayoutArea = QtWidgets.QVBoxLayout()
        self.verticalLayoutArea.setObjectName("verticalLayoutArea")
        
        self.labelArea = QtWidgets.QLabel(self.groupBoxDadosGerais)
        self.labelArea.setFont(font)
        self.labelArea.setObjectName("labelArea")
        self.verticalLayoutArea.addWidget(self.labelArea)
        
        self.doubleSpinBoxArea = QtWidgets.QDoubleSpinBox(self.groupBoxDadosGerais)
        self.doubleSpinBoxArea.setFont(font)
        self.doubleSpinBoxArea.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxArea.setMaximum(99999.99)
        self.doubleSpinBoxArea.setToolTip("<html><head/><body><p>Área do eletrodo em cm².</p></body></html>")
        self.doubleSpinBoxArea.setObjectName("doubleSpinBoxArea")
        self.verticalLayoutArea.addWidget(self.doubleSpinBoxArea)
        
        self.gridLayout_5.addLayout(self.verticalLayoutArea, 0, 0, 1, 1)
        
        self.verticalLayoutCiclos = QtWidgets.QVBoxLayout()
        self.verticalLayoutCiclos.setObjectName("verticalLayoutCiclos")
        
        self.labelCiclos = QtWidgets.QLabel(self.groupBoxDadosGerais)
        self.labelCiclos.setFont(font)
        self.labelCiclos.setObjectName("labelCiclos")
        self.verticalLayoutCiclos.addWidget(self.labelCiclos)
        
        self.lineEditCiclos = QtWidgets.QLineEdit(self.groupBoxDadosGerais)
        self.lineEditCiclos.setFont(font)
        self.lineEditCiclos.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEditCiclos.setToolTip("<html><head/><body><p>Insira os ciclos a serem analisados. <br> Exemplo: 30,60,90 (trigésimo, sexagésimo e nonagésimo)</p></body></html>")
        self.lineEditCiclos.setObjectName("lineEditCiclos")
        self.verticalLayoutCiclos.addWidget(self.lineEditCiclos)
        
        self.gridLayout_5.addLayout(self.verticalLayoutCiclos, 0, 1, 1, 1)
        
        self.verticalLayoutDtCiclos = QtWidgets.QVBoxLayout()
        self.verticalLayoutDtCiclos.setObjectName("verticalLayoutDtCiclos")
        
        self.labelDtCiclos = QtWidgets.QLabel(self.groupBoxDadosGerais)
        self.labelDtCiclos.setFont(font)
        self.labelDtCiclos.setObjectName("labelDtCiclos")
        self.verticalLayoutDtCiclos.addWidget(self.labelDtCiclos)
        
        self.doubleSpinBoxDtCiclos = QtWidgets.QDoubleSpinBox(self.groupBoxDadosGerais)
        self.doubleSpinBoxDtCiclos.setFont(font)
        self.doubleSpinBoxDtCiclos.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxDtCiclos.setMaximum(99999.99)
        self.doubleSpinBoxDtCiclos.setToolTip("<html><head/><body><p>Tempo de duração de cada ciclo.</p></body></html>")
        self.doubleSpinBoxDtCiclos.setObjectName("doubleSpinBoxDtCiclos")
        self.verticalLayoutDtCiclos.addWidget(self.doubleSpinBoxDtCiclos)
        
        self.gridLayout_5.addLayout(self.verticalLayoutDtCiclos, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBoxDadosGerais, 0, 1, 1, 1)
        
        self.groupBoxAbs = QtWidgets.QGroupBox(self.tab)
        self.groupBoxAbs.setObjectName("groupBoxAbs")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxAbs)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.gridLayoutIntRedAbs = QtWidgets.QGridLayout()
        self.gridLayoutIntRedAbs.setObjectName("gridLayoutIntRedAbs")
        
        self.doubleSpinBoxInicioIntRedAbs = QtWidgets.QDoubleSpinBox(self.groupBoxAbs)
        self.doubleSpinBoxInicioIntRedAbs.setFont(font)
        self.doubleSpinBoxInicioIntRedAbs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxInicioIntRedAbs.setMaximum(99999.99)
        self.doubleSpinBoxInicioIntRedAbs.setToolTip("""<html><head/><body><p>Insira tempo de INÍCIO do salto de Redução dos dados de
                                                Densidade de Corrente dos ciclos a serem analisados. <br> Exemplo:<br> 10</p></body></html>""")
        self.doubleSpinBoxInicioIntRedAbs.setObjectName("doubleSpinBoxInicioIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.doubleSpinBoxInicioIntRedAbs, 2, 0, 1, 1)
        
        self.labelIntRedAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelIntRedAbs.setFont(font)
        self.labelIntRedAbs.setObjectName("labelIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.labelIntRedAbs, 0, 0, 1, 4)
        
        self.doubleSpinBoxFimIntRedAbs = QtWidgets.QDoubleSpinBox(self.groupBoxAbs)
        self.doubleSpinBoxFimIntRedAbs.setFont(font)
        self.doubleSpinBoxFimIntRedAbs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxFimIntRedAbs.setMaximum(99999.99)
        self.doubleSpinBoxFimIntRedAbs.setToolTip("""<html><head/><body><p>Insira tempo de FIM do salto de Redução dos dados de
                                                Densidade de Corrente dos ciclos a serem analisados. <br> Exemplo:<br> 10</p></body></html>""")
        self.doubleSpinBoxFimIntRedAbs.setObjectName("doubleSpinBoxFimIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.doubleSpinBoxFimIntRedAbs, 2, 1, 1, 1)
        
        self.toolButtonExcIntRedAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonExcIntRedAbs.setFont(font)
        self.toolButtonExcIntRedAbs.setToolTip("""<html><head/><body><p>EXCLUIR últimos dados de intervalo de salto de Redução dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcIntRedAbs.setObjectName("toolButtonExcIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.toolButtonExcIntRedAbs, 2, 3, 1, 1)
        
        self.labelInicioIntRedAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelInicioIntRedAbs.setFont(font)
        self.labelInicioIntRedAbs.setObjectName("labelInicioIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.labelInicioIntRedAbs, 1, 0, 1, 1)
        
        self.labelFimIntRedAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelFimIntRedAbs.setFont(font)
        self.labelFimIntRedAbs.setObjectName("labelFimIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.labelFimIntRedAbs, 1, 1, 1, 1)
        
        self.toolButtonAddIntRedAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonAddIntRedAbs.setFont(font)
        self.toolButtonAddIntRedAbs.setToolTip("""<html><head/><body><p>ADICIONAR dados de intervalo de salto de Redução dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddIntRedAbs.setObjectName("toolButtonAddIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.toolButtonAddIntRedAbs, 2, 2, 1, 1)
        
        self.lineEditIntRedAbs = QtWidgets.QLineEdit(self.groupBoxAbs)
        self.lineEditIntRedAbs.setFont(font)
        self.lineEditIntRedAbs.setToolTip("<html><head/><body><p>Insira os intervalos de tempos de Redução dos dados de Absorbância dos ciclos a serem analisados. <br> Exemplo:<br> [110, 120],[550, 570],[990, 1010] <br><br> Obs: Os intervalos devem estar na mesma ordem dos arquivos de Densidade de Corrente.</p></body></html>")
        self.lineEditIntRedAbs.setObjectName("lineEditIntRedAbs")
        self.gridLayoutIntRedAbs.addWidget(self.lineEditIntRedAbs, 3, 0, 1, 4)
        
        self.gridLayout_3.addLayout(self.gridLayoutIntRedAbs, 1, 0, 1, 1)
        
        self.gridLayoutIntOxiAbs = QtWidgets.QGridLayout()
        self.gridLayoutIntOxiAbs.setObjectName("gridLayoutIntOxiAbs")
        
        self.labelInicioIntOxiAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelInicioIntOxiAbs.setFont(font)
        self.labelInicioIntOxiAbs.setObjectName("labelInicioIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.labelInicioIntOxiAbs, 1, 0, 1, 1)
        
        self.doubleSpinBoxInicioIntOxiAbs = QtWidgets.QDoubleSpinBox(self.groupBoxAbs)
        self.doubleSpinBoxInicioIntOxiAbs.setFont(font)
        self.doubleSpinBoxInicioIntOxiAbs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxInicioIntOxiAbs.setToolTip("""<html><head/><body><p>Insira tempo de INÍCIO do salto de Oxidação dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxInicioIntOxiAbs.setMaximum(99999.99)
        self.doubleSpinBoxInicioIntOxiAbs.setObjectName("doubleSpinBoxInicioIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.doubleSpinBoxInicioIntOxiAbs, 2, 0, 1, 1)
        
        self.labelFimIntOxiAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelFimIntOxiAbs.setFont(font)
        self.labelFimIntOxiAbs.setObjectName("labelFimIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.labelFimIntOxiAbs, 1, 1, 1, 1)
        
        self.toolButtonExcIntOxiAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonExcIntOxiAbs.setFont(font)
        self.toolButtonExcIntOxiAbs.setToolTip("""<html><head/><body><p>EXCLUIR últimos dados de intervalo de salto de Oxidação dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcIntOxiAbs.setObjectName("toolButtonExcIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.toolButtonExcIntOxiAbs, 2, 3, 1, 1)
        
        self.toolButtonAddIntOxiAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonAddIntOxiAbs.setFont(font)
        self.toolButtonAddIntOxiAbs.setToolTip("""<html><head/><body><p>ADICIONAR dados de intervalo de salto de Oxidação dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddIntOxiAbs.setObjectName("toolButtonAddIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.toolButtonAddIntOxiAbs, 2, 2, 1, 1)
        
        self.doubleSpinBoxFimIntOxiAbs = QtWidgets.QDoubleSpinBox(self.groupBoxAbs)
        self.doubleSpinBoxFimIntOxiAbs.setFont(font)
        self.doubleSpinBoxFimIntOxiAbs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxFimIntOxiAbs.setMaximum(99999.99)
        self.doubleSpinBoxFimIntOxiAbs.setToolTip("""<html><head/><body><p>Insira tempo de FIM do salto de Oxidação dos dados de
                                                ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxFimIntOxiAbs.setObjectName("doubleSpinBoxFimIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.doubleSpinBoxFimIntOxiAbs, 2, 1, 1, 1)
        
        self.lineEditIntOxiAbs = QtWidgets.QLineEdit(self.groupBoxAbs)
        self.lineEditIntOxiAbs.setFont(font)
        self.lineEditIntOxiAbs.setToolTip("<html><head/><body><p>Insira os intervalos de tempos de Oxidação dos dados de Absorbância dos ciclos a serem analisados. <br> Exemplo:<br> [110, 120],[550, 570],[990, 1010] <br><br> Obs: Os intervalos devem estar na mesma ordem dos arquivos de Densidade de Corrente.</p></body></html>")
        self.lineEditIntOxiAbs.setObjectName("lineEditIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.lineEditIntOxiAbs, 3, 0, 1, 4)
        
        self.labelIntOxiAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelIntOxiAbs.setFont(font)
        self.labelIntOxiAbs.setObjectName("labelIntOxiAbs")
        self.gridLayoutIntOxiAbs.addWidget(self.labelIntOxiAbs, 0, 0, 1, 4)
        
        self.gridLayout_3.addLayout(self.gridLayoutIntOxiAbs, 2, 0, 1, 1)
        
        self.gridLayoutArqAbs = QtWidgets.QGridLayout()
        self.gridLayoutArqAbs.setObjectName("gridLayoutArqAbs")
        
        self.labelArqAbs = QtWidgets.QLabel(self.groupBoxAbs)
        self.labelArqAbs.setFont(font)
        self.labelArqAbs.setObjectName("labelArqAbs")
        self.gridLayoutArqAbs.addWidget(self.labelArqAbs, 0, 1, 1, 1)
        
        self.toolButtonLimpaArqAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonLimpaArqAbs.setFont(font)
        self.toolButtonLimpaArqAbs.setToolTip("""<html><head/><body><p>LIMPAR arquivos de ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonLimpaArqAbs.setObjectName("toolButtonLimpaArqAbs")
        self.gridLayoutArqAbs.addWidget(self.toolButtonLimpaArqAbs, 0, 4, 1, 1)
        
        self.toolButtonExcArqAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonExcArqAbs.setFont(font)
        self.toolButtonExcArqAbs.setToolTip("""<html><head/><body><p>EXCLUIR arquivos de ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcArqAbs.setObjectName("toolButtonExcArqAbs")
        self.gridLayoutArqAbs.addWidget(self.toolButtonExcArqAbs, 0, 3, 1, 1)
        
        self.toolButtonAddArqAbs = QtWidgets.QToolButton(self.groupBoxAbs)
        self.toolButtonAddArqAbs.setFont(font)
        self.toolButtonAddArqAbs.setToolTip("""<html><head/><body><p>ADICIONAR arquivos de ABSORBÂNCIA dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddArqAbs.setObjectName("toolButtonAddArqAbs")
        self.gridLayoutArqAbs.addWidget(self.toolButtonAddArqAbs, 0, 2, 1, 1)
        
        self.lineEditArqAbs = QtWidgets.QLineEdit(self.groupBoxAbs)
        self.lineEditArqAbs.setFont(font)
        self.lineEditArqAbs.setToolTip("<html><head/><body><p>Insira o nome do arquivo com dados de Absorbância. <br> Exemplo: Abs1.csv</p></body></html>")
        self.lineEditArqAbs.setObjectName("lineEditArqAbs")
        self.gridLayoutArqAbs.addWidget(self.lineEditArqAbs, 1, 1, 1, 4)

        self.gridLayout_3.addLayout(self.gridLayoutArqAbs, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBoxAbs, 2, 1, 1, 1)

        self.groupBoxCorr = QtWidgets.QGroupBox(self.tab)
        self.groupBoxCorr.setObjectName("groupBoxCorr")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxCorr)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayoutIntRedCorr = QtWidgets.QGridLayout()
        self.gridLayoutIntRedCorr.setObjectName("gridLayoutIntRedCorr")

        self.doubleSpinBoxInicioIntRedCorr = QtWidgets.QDoubleSpinBox(self.groupBoxCorr)
        self.doubleSpinBoxInicioIntRedCorr.setFont(font)
        self.doubleSpinBoxInicioIntRedCorr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxInicioIntRedCorr.setMaximum(99999.99)
        self.doubleSpinBoxInicioIntRedCorr.setToolTip("""<html><head/><body><p>Insira tempo de INÍCIO do salto de Redução dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxInicioIntRedCorr.setObjectName("doubleSpinBoxInicioIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.doubleSpinBoxInicioIntRedCorr, 2, 0, 1, 1)
        
        self.labelFimIntRedCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelFimIntRedCorr.setFont(font)
        self.labelFimIntRedCorr.setObjectName("labelFimIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.labelFimIntRedCorr, 1, 1, 1, 1)
        
        self.doubleSpinBoxFimIntRedCorr = QtWidgets.QDoubleSpinBox(self.groupBoxCorr)
        self.doubleSpinBoxFimIntRedCorr.setFont(font)
        self.doubleSpinBoxFimIntRedCorr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxFimIntRedCorr.setMaximum(99999.99)
        self.doubleSpinBoxFimIntRedCorr.setToolTip("""<html><head/><body><p>Insira tempo de FIM do salto de Redução dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxFimIntRedCorr.setObjectName("doubleSpinBoxFimIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.doubleSpinBoxFimIntRedCorr, 2, 1, 1, 1)
        
        self.toolButtonAddIntRedCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonAddIntRedCorr.setFont(font)
        self.toolButtonAddIntRedCorr.setToolTip("""<html><head/><body><p>ADICIONAR dados de intervalo de salto de Redução dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddIntRedCorr.setObjectName("toolButtonAddIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.toolButtonAddIntRedCorr, 2, 2, 1, 1)
        
        self.labelIntRedCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelIntRedCorr.setFont(font)
        self.labelIntRedCorr.setObjectName("labelIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.labelIntRedCorr, 0, 0, 1, 4)
        
        self.labelInicioIntRedCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelInicioIntRedCorr.setFont(font)
        self.labelInicioIntRedCorr.setObjectName("labelInicioIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.labelInicioIntRedCorr, 1, 0, 1, 1)

        self.toolButtonExcIntRedCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonExcIntRedCorr.setFont(font)
        self.toolButtonExcIntRedCorr.setToolTip("""<html><head/><body><p>EXCLUIR últimos dados de intervalo de salto de Redução dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcIntRedCorr.setObjectName("toolButtonExcIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.toolButtonExcIntRedCorr, 2, 3, 1, 1)

        self.lineEditIntRedCorr = QtWidgets.QLineEdit(self.groupBoxCorr)
        self.lineEditIntRedCorr.setFont(font)
        self.lineEditIntRedCorr.setObjectName("lineEditIntRedCorr")
        self.gridLayoutIntRedCorr.addWidget(self.lineEditIntRedCorr, 3, 0, 1, 4)

        self.gridLayout_2.addLayout(self.gridLayoutIntRedCorr, 3, 2, 1, 1)

        self.gridLayoutIntOxiCorr = QtWidgets.QGridLayout()
        self.gridLayoutIntOxiCorr.setObjectName("gridLayoutIntOxiCorr")

        self.doubleSpinBoxInicioIntOxiCorr = QtWidgets.QDoubleSpinBox(self.groupBoxCorr)
        self.doubleSpinBoxInicioIntOxiCorr.setFont(font)
        self.doubleSpinBoxInicioIntOxiCorr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxInicioIntOxiCorr.setMaximum(99999.99)
        self.doubleSpinBoxInicioIntOxiCorr.setToolTip("""<html><head/><body><p>Insira tempo de INÍCIO do salto de Oxidação dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxInicioIntOxiCorr.setObjectName("doubleSpinBoxInicioIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.doubleSpinBoxInicioIntOxiCorr, 2, 0, 1, 1)

        self.doubleSpinBoxFimIntOxiCorr = QtWidgets.QDoubleSpinBox(self.groupBoxCorr)
        self.doubleSpinBoxFimIntOxiCorr.setFont(font)
        self.doubleSpinBoxFimIntOxiCorr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxFimIntOxiCorr.setMaximum(99999.99)
        self.doubleSpinBoxFimIntOxiCorr.setToolTip("""<html><head/><body><p>Insira tempo de FIM do salto de Oxidação dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.doubleSpinBoxFimIntOxiCorr.setObjectName("doubleSpinBoxFimIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.doubleSpinBoxFimIntOxiCorr, 2, 1, 1, 1)

        self.labelIntOxiCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelIntOxiCorr.setFont(font)
        self.labelIntOxiCorr.setObjectName("labelIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.labelIntOxiCorr, 0, 0, 1, 4)

        self.toolButtonExcIntOxiCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonExcIntOxiCorr.setFont(font)
        self.toolButtonExcIntOxiCorr.setToolTip("""<html><head/><body><p>EXCLUIR últimos dados de intervalo de salto de Oxidação dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcIntOxiCorr.setObjectName("toolButtonExcIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.toolButtonExcIntOxiCorr, 2, 3, 1, 1)

        self.toolButtonAddIntOxiCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonAddIntOxiCorr.setFont(font)
        self.toolButtonAddIntOxiCorr.setToolTip("""<html><head/><body><p>ADICIONAR dados de intervalo de salto de Oxidação dos dados de
                                                DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddIntOxiCorr.setObjectName("toolButtonAddIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.toolButtonAddIntOxiCorr, 2, 2, 1, 1)

        self.labelFimIntOxiCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelFimIntOxiCorr.setFont(font)
        self.labelFimIntOxiCorr.setObjectName("labelFimIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.labelFimIntOxiCorr, 1, 1, 1, 1)

        self.labelInicioIntOxiCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelInicioIntOxiCorr.setFont(font)
        self.labelInicioIntOxiCorr.setObjectName("labelInicioIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.labelInicioIntOxiCorr, 1, 0, 1, 1)

        self.lineEditIntOxiCorr = QtWidgets.QLineEdit(self.groupBoxCorr)
        self.lineEditIntOxiCorr.setFont(font)
        self.lineEditIntOxiCorr.setToolTip("<html><head/><body><p>Insira os intervalos de tempos de Oxidação dos dados de Densidade de Corrente dos ciclos a serem analisados. <br> Exemplo:<br> [0, 10]</p></body></html>")
        self.lineEditIntOxiCorr.setObjectName("lineEditIntOxiCorr")
        self.gridLayoutIntOxiCorr.addWidget(self.lineEditIntOxiCorr, 3, 0, 1, 4)

        self.gridLayout_2.addLayout(self.gridLayoutIntOxiCorr, 4, 2, 1, 1)

        self.gridLayoutArqCorr = QtWidgets.QGridLayout()
        self.gridLayoutArqCorr.setObjectName("gridLayoutArqCorr")

        self.labelArqCorr = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelArqCorr.setFont(font)
        self.labelArqCorr.setObjectName("labelArqCorr")
        self.gridLayoutArqCorr.addWidget(self.labelArqCorr, 0, 0, 1, 1)

        self.toolButtonExcArqCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonExcArqCorr.setFont(font)
        self.toolButtonExcArqCorr.setToolTip("""<html><head/><body><p>EXCLUIR arquivos de DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonExcArqCorr.setObjectName("toolButtonExcArqCorr")
        self.gridLayoutArqCorr.addWidget(self.toolButtonExcArqCorr, 0, 2, 1, 1)

        self.toolButtonLimpaArqCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonLimpaArqCorr.setFont(font)
        self.toolButtonLimpaArqCorr.setToolTip("""<html><head/><body><p>LIMPAR arquivos de DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonLimpaArqCorr.setObjectName("toolButtonLimpaArqCorr")
        self.gridLayoutArqCorr.addWidget(self.toolButtonLimpaArqCorr, 0, 3, 1, 1)

        self.toolButtonAddArqCorr = QtWidgets.QToolButton(self.groupBoxCorr)
        self.toolButtonAddArqCorr.setFont(font)
        self.toolButtonAddArqCorr.setToolTip("""<html><head/><body><p>ADICIONAR arquivos de DENSIDADE DE CORRENTE dos ciclos a serem analisados.</p></body></html>""")
        self.toolButtonAddArqCorr.setObjectName("toolButtonAddArqCorr")
        self.gridLayoutArqCorr.addWidget(self.toolButtonAddArqCorr, 0, 1, 1, 1)

        self.lineEditArqCorr = QtWidgets.QLineEdit(self.groupBoxCorr)
        self.lineEditArqCorr.setFont(font)
        self.lineEditArqCorr.setToolTip("<html><head/><body><p>Insira o nome dos arquivos com dados de Densidade de Corrente. <br> Exemplo: [corrente1.csv, corrente2.csv, corrente3.csv]</p></body></html>")
        self.lineEditArqCorr.setObjectName("lineEditArqCorr")
        self.gridLayoutArqCorr.addWidget(self.lineEditArqCorr, 1, 0, 1, 4)

        self.labelDx = QtWidgets.QLabel(self.groupBoxCorr)
        self.labelDx.setFont(font)
        self.labelDx.setObjectName("labelDx")
        self.gridLayoutArqCorr.addWidget(self.labelDx, 0, 4, 1, 1)

        self.doubleSpinBoxDx = QtWidgets.QDoubleSpinBox(self.groupBoxCorr)
        self.doubleSpinBoxDx.setFont(font)
        self.doubleSpinBoxDx.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxDx.setMaximum(99999.99)
        self.doubleSpinBoxDx.setToolTip("<html><head/><body><p>Tempo de varredura da leitura de corrente. É o &Delta;t do gráfico de Densidade de Corrente.</p></body></html>")
        self.doubleSpinBoxDx.setObjectName("doubleSpinBoxDx")
        self.gridLayoutArqCorr.addWidget(self.doubleSpinBoxDx, 1, 4, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayoutArqCorr, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.groupBoxCorr, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_2, "")
        
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
##################
##Funçoes Chamadas
##################
        self.toolButtonAddArqCorr.clicked.connect(self.add_arq_corr)
        self.toolButtonExcArqCorr.clicked.connect(self.exc_arq_corr)
        self.toolButtonLimpaArqCorr.clicked.connect(self.limpa_arq_corr)

        self.toolButtonAddIntRedCorr.clicked.connect(self.add_int_clar_corr)
        self.toolButtonExcIntRedCorr.clicked.connect(self.exc_int_clar_corr)
        self.toolButtonAddIntOxiCorr.clicked.connect(self.add_int_oxi_corr)
        self.toolButtonExcIntOxiCorr.clicked.connect(self.exc_int_oxi_corr)

        self.toolButtonAddArqAbs.clicked.connect(self.add_arq_abs)
        self.toolButtonExcArqAbs.clicked.connect(self.exc_arq_abs)
        
        self.toolButtonAddIntRedAbs.clicked.connect(self.add_int_clar_abs)
        self.toolButtonExcIntRedAbs.clicked.connect(self.exc_int_clar_abs)
        self.toolButtonAddIntOxiAbs.clicked.connect(self.add_int_oxi_abs)
        self.toolButtonExcIntOxiAbs.clicked.connect(self.exc_int_oxi_abs)

        self.pushButtonCalcula.clicked.connect(self.clicked_pushButtonCalcula)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EletroCrom"))
        self.groupBoxDadosArq.setTitle(_translate("Form", "Dados Arquivos"))
        self.labelCodec.setText(_translate("Form", "Codec:"))
        self.labelDelimitador.setText(_translate("Form", 'Delimitador ".csv":'))
        self.pushButtonCalcula.setText(_translate("Form", "Calcular Eficiência"))
        self.groupBoxDadosGerais.setTitle(_translate("Form", "Dados Gerais"))
        self.labelArea.setText(_translate("Form", "Área(cm²):"))
        self.labelCiclos.setText(_translate("Form", "Ciclos Analisados:"))
        self.labelDtCiclos.setText(_translate("Form", "Duração ciclo:"))
        self.groupBoxAbs.setTitle(_translate("Form", "Dados de Absorbância"))
        self.labelIntRedAbs.setText(_translate("Form", "Intervalos de Redução:"))
        self.toolButtonExcIntRedAbs.setText(_translate("Form", "-"))
        self.labelInicioIntRedAbs.setText(_translate("Form", "Inicio:"))
        self.labelFimIntRedAbs.setText(_translate("Form", "Fim:"))
        self.toolButtonAddIntRedAbs.setText(_translate("Form", "+"))
        self.labelInicioIntOxiAbs.setText(_translate("Form", "Início:"))
        self.labelFimIntOxiAbs.setText(_translate("Form", "Fim:"))
        self.toolButtonExcIntOxiAbs.setText(_translate("Form", "-"))
        self.toolButtonAddIntOxiAbs.setText(_translate("Form", "+"))
        self.labelIntOxiAbs.setText(_translate("Form", "Intervalos de Oxidação:"))
        self.labelArqAbs.setText(_translate("Form", "Arquivo de Absorbância:"))
        self.toolButtonLimpaArqAbs.setText(_translate("Form", "Limpar"))
        self.toolButtonExcArqAbs.setText(_translate("Form", "-"))
        self.toolButtonAddArqAbs.setText(_translate("Form", "+"))
        self.groupBoxCorr.setTitle(_translate("Form", "Dados de densidade de Corrente"))
        self.labelFimIntRedCorr.setText(_translate("Form", "Fim:"))
        self.toolButtonAddIntRedCorr.setText(_translate("Form", "+"))
        self.labelIntRedCorr.setText(_translate("Form", "Intervalo de Redução:"))
        self.labelInicioIntRedCorr.setText(_translate("Form", "Inicio:"))
        self.toolButtonExcIntRedCorr.setText(_translate("Form", "-"))
        self.labelIntOxiCorr.setText(_translate("Form", "Intervalo de Oxidação:"))
        self.toolButtonExcIntOxiCorr.setText(_translate("Form", "-"))
        self.toolButtonAddIntOxiCorr.setText(_translate("Form", "+"))
        self.labelFimIntOxiCorr.setText(_translate("Form", "Fim:"))
        self.labelInicioIntOxiCorr.setText(_translate("Form", "Inicio:"))
        self.labelArqCorr.setText(_translate("Form", "Arquivos de Corrente:"))
        self.toolButtonExcArqCorr.setText(_translate("Form", "-"))
        self.toolButtonLimpaArqCorr.setText(_translate("Form", "Limpar"))
        self.toolButtonAddArqCorr.setText(_translate("Form", "+"))
        self.labelDx.setText(_translate("Form", "dx(s):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Eficiência Coulômbica e Eletrocrômica"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline; color:#000000;\">Orietação Geral</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">:</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline; color:#000000;\"><br /></span><span style=\" font-size:9pt; color:#000000;\"><br />Este software, projetado em Python 3.5, foi elaborado para otimizar o tratamento de dados de Densidade de Corrente e Absorbância em resultados provenientes de equipamentos que geram um arquivo único de Absorbância para todos os saltos e tantos arquivos de Densidade de Corrente quantos são os saltos analisados.</span></li>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Por Exemplo, caso se analise 15 saltos, será necessário informar:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Um arquivo com os dados de Absorbância de todo o experimento e os 15 intervalos a serem analisados do arquivos de absorbância</li>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 arquivos de Densidade de Corrente inseridos na ordem de cada salto.</li></ul>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Os arquivos devem ter extensão &quot;.csv&quot;, conter duas colunas sem títulos/cabeçalhos. <br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Os dados podem estar separaos por: &quot;,&quot; &quot;;&quot; &quot;:&quot; &quot;|&quot; &quot;-&quot; &quot; &quot;<br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Ao selecionar os arquivos, certifique-se de que estão no mesmo codec selecionado. Ex: \'UTF-8\', \'ISO-8859-1\',\'ASCII\' ...</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Versão </span><span style=\" font-weight:600; font-style:italic;\">: </span>EletroCrom - BETA1.0</li></ul>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Link para Exemplos</span><span style=\" font-weight:600; font-style:italic;\">: </span>sclab.pythonanywhere.com/eletrocrom/</li>\n"
"<li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Pacotes utilizados</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">:<br /></span></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Matplotlib 2.0.0</li>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numpy 1.12.0</li>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pyqt5 5.8.1</li>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyInstaller 3.2.1</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Licença</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">: </span><span style=\" font-size:9pt; text-decoration:none; color:#000000;\">LGPL v3</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Este programa é um software livre: você pode redistribuí-lo e/ou  modificá-lo sob os termos da GNU Lesser General Public License (LGPL) publicada pela Free Software Foundation (FSF),  na versão 3 da licença.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA; sem garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a GNU LGPL (Lesser General Public License) para mais detalhes.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Veja a cópia dessa licença em sua língua original em:  www.gnu.org/licenses/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Todo o código pode ser encontrado em: github.com/guilhermetabordaribas/sclab-github/</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Doações</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">: </span><span style=\" font-size:9pt; text-decoration:none; color:#000000;\">sclab.pythonanywhere.com/doacoes/</span></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Sobre"))

##Densidade de Corrente
    def add_arq_corr(self):        
        filename = QtWidgets.QFileDialog()
        file_path = filename.getOpenFileName(directory=os.getenv('HOME'), filter='*.csv')
        self.arq_corr.append(file_path[0])
        arq_tmp = []
        for x in self.arq_corr:
            arq_tmp.append(x.split('/')[-1])
        self.lineEditArqCorr.setText(', '.join(arq_tmp))

    def exc_arq_corr(self):
        if self.arq_corr:
            arq_tmp = []
            self.arq_corr.pop()
            for x in self.arq_corr:
                arq_tmp.append(x.split('/')[-1])
            self.lineEditArqCorr.setText(', '.join(arq_tmp))

    def limpa_arq_corr(self):
        if self.arq_corr:
            self.arq_corr = []
            self.lineEditArqCorr.setText('')

    def add_int_clar_corr(self):
        self.tempo_red = []
        self.tempo_red.append(self.doubleSpinBoxInicioIntRedCorr.value())
        self.tempo_red.append(self.doubleSpinBoxFimIntRedCorr.value())        
        self.lineEditIntRedCorr.setText(str(self.tempo_red))

    def exc_int_clar_corr(self):
        self.tempo_red = []
        self.lineEditIntRedCorr.setText('')

    def add_int_oxi_corr(self):
        self.tempo_oxi = []
        self.tempo_oxi.append(self.doubleSpinBoxInicioIntOxiCorr.value())
        self.tempo_oxi.append(self.doubleSpinBoxFimIntOxiCorr.value())        
        self.lineEditIntOxiCorr.setText(str(self.tempo_oxi))

    def exc_int_oxi_corr(self):
        self.tempo_oxi = []
        self.lineEditIntOxiCorr.setText('')

####Absorbância
    def add_arq_abs(self):        
        filename = QtWidgets.QFileDialog()
        file_path = filename.getOpenFileName(directory=os.getenv('HOME'), filter='*.csv')
        self.arq_abs = file_path[0]
        arq_tmp = ''
        self.lineEditArqAbs.setText(self.arq_abs.split('/')[-1])

    def exc_arq_abs(self):
        self.arq_abs = ''
        self.lineEditArqAbs.setText('')

    def add_int_clar_abs(self):
        self.tempo_abs_red.append([self.doubleSpinBoxInicioIntRedAbs.value(), self.doubleSpinBoxFimIntRedAbs.value()])
        self.lineEditIntRedAbs.setText(str(self.tempo_abs_red)[1:-1])

    def exc_int_clar_abs(self):
        if self.tempo_abs_red:
            self.tempo_abs_red.pop()
            self.lineEditIntRedAbs.setText(str(self.tempo_abs_red)[1:-1])

    def add_int_oxi_abs(self):
        self.tempo_abs_oxi.append([self.doubleSpinBoxInicioIntOxiAbs.value(), self.doubleSpinBoxFimIntOxiAbs.value()])
        self.lineEditIntOxiAbs.setText(str(self.tempo_abs_oxi)[1:-1])

    def exc_int_oxi_abs(self):
        if self.tempo_abs_oxi:
            self.tempo_abs_oxi.pop()
            self.lineEditIntOxiAbs.setText(str(self.tempo_abs_oxi)[1:-1])
            

    def clicked_pushButtonCalcula(self):
        erro = False

        if self.doubleSpinBoxArea.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira a área do eletrodo de trabalho em cm².')
            msg.setWindowTitle("Atenção - Inserir Área do eletrodo")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.lineEditCiclos.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira os nomes dos ciclos analisados.')
            msg.setWindowTitle("Atenção - Inserir ciclos")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.arq_corr:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('''Insira pelo menos um arquivo de Densidade de Corrente clicando em "+" ao lado de "Arquivos de Corrente: "''')
            msg.setWindowTitle("Atenção - Escolher Arquivo de Densidade de Corrente")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxDx.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira o intervalo de varredura da leitura dos dados de Densidade de Corrente em "dx(s): ".')
            msg.setWindowTitle("Atenção - Inserir Intervalo de varredura")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.tempo_red:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('''Insira o intervalo de Redução para os dados de Densidade de Corrente selecionando instante de "início" e "fim" e clicando no sinal "+".''')
            msg.setWindowTitle("Atenção - Inserir intervalo de Redução.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.tempo_oxi:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira o intervalo de Oxidação para os dados de Densidade de Corrente selecionando instante de "início" e "fim" e clicando no sinal "+".')
            msg.setWindowTitle("Atenção - Inserir intervalo de Oxidação.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.arq_abs:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira um Arquivo de Absorbância clicando em "+" ao lado de "Arquivo de Absorbância: ".')
            msg.setWindowTitle("Atenção - Inserir Data de Início")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.tempo_abs_red:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('''Insira o intervalo de Redução para os dados de Absorbância selecionando instante de "início" e "fim" e clicando no sinal "+".''')
            msg.setWindowTitle("Atenção - Inserir intervalo de Redução.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif not self.tempo_abs_oxi:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira o intervalo de Oxidação para os dados de Absorbância selecionando instante de "início" e "fim" e clicando no sinal "+".')
            msg.setWindowTitle("Atenção - Inserir intervalo de Oxidação.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()        
        elif len(self.arq_corr) != len(self.lineEditCiclos.text().split(',')):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('A quantidade e Arquivos de Densidade de Corrente deve ter a mesma quantidade de Ciclos. Por favor, verificar!')
            msg.setWindowTitle("Atenção - Quantidade de Ciclos diferente da quantidade de Arquivos")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif len(self.tempo_abs_red) != len(self.lineEditCiclos.text().split(',')):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('A quantidade e intervalos de Absorbância (Redução) deve ter a mesma quantidade de Ciclos. Por favor, verificar!')
            msg.setWindowTitle("Atenção - Quantidade de Ciclos diferente da quantidade de intervalos")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif len(self.tempo_abs_oxi) != len(self.lineEditCiclos.text().split(',')):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('A quantidade e intervalos de Absorbância (Oxidação) deve ter a mesma quantidade de Ciclos. Por favor, verificar!')
            msg.setWindowTitle("Atenção - Quantidade de Ciclos diferente da quantidade de intervalos")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:            
            arquivos_densidadeCorrente = self.arq_corr
            delimitador = self.comboBoxDelimitador.currentText().replace('"','')
            codec = self.comboBoxCodecs.currentText()
            tempo_red = self.tempo_red
            tempo_oxi = self.tempo_oxi            
            arquivos_absorbancia = self.arq_abs
            tempo_abs_red = self.tempo_abs_red
            tempo_abs_oxi = self.tempo_abs_oxi
            ciclos = self.lineEditCiclos.text().split(',')
            dt_ciclos = self.doubleSpinBoxDtCiclos.value()
            tempo_dx = self.doubleSpinBoxDx.value()
            area = self.doubleSpinBoxArea.value()
            
            row1 = []            
            for arq in self.arq_corr:
                try:
                    with open(arq, encoding = codec) as f:
                        reader = csv.reader(f, delimiter=delimitador)
                        row1 = next(reader)
                except UnicodeError:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('O "codec" do arquivo "'+arq+'" talvez seja outro. Por favor verificar!')
                    msg.setWindowTitle('Atenção - Erro de Codec')
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    erro = True
                                        
                if not erro and len(row1) != 2:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('A quantidade de colunas do arquivo "'+arq.split('/')[-1]+'" pode estar em quantidade diferente de 2 ("tempo","densidade de corrente") ou o delimitador pode ser outro.')
                    msg.setWindowTitle('Atenção - Arquivo ".csv"')
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    erro = True

            row1 = []
            try:
                with open(self.arq_abs, encoding = codec) as f:
                    reader = csv.reader(f, delimiter=delimitador)
                    row1 = next(reader)
            except UnicodeError:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('O "codec" do arquivo "'+self.arq_abs+'" talvez seja outro. Por favor verificar!')
                    msg.setWindowTitle('Atenção - Erro de Codec')
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    erro = True

            if not erro and len(row1) != 2:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('A quantidade de colunas do arquivo "'+self.arq_abs.split('/')[-1]+'" pode estar em quantidade diferente de 2 ("tempo","densidade de corrente") ou o delimitador pode ser outro.')
                msg.setWindowTitle('Atenção - Arquivo ".csv"')
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                erro = True
                
            if not erro:
                try:
                    ef = Eletrocrom_Eficiencia.Eficiencia().calcula_eficiencia(delimitador, codec,
                                                                                       arquivos_densidadeCorrente, tempo_red, tempo_oxi,
                                                                                       arquivos_absorbancia, tempo_abs_red, tempo_abs_oxi,
                                                                                       ciclos, dt_ciclos, tempo_dx, area)
                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('Nosso programa não conseguiu especificar o erro. Verifique os dados de entrada, principalmente os intervalos de analise. Caso o erro persista, envie-nos um email explicando o que ocorreu.')
                    msg.setWindowTitle("Atenção - Erro Desconhecido")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()                    
                
                if ef in ['Intervalo(s) de Absorbância-Redução não encotrado. Por favor verificar Intervalo(s).',
                          'Intervalo(s) de Absorbância-Oxidação não encotrado. Por favor verificar Intervalo(s).']:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText(ef)
                    msg.setWindowTitle('Atenção - Intervalo Absorbância')
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                else:
                    try:
                        graf = Eletrocrom_Gera_grafico.Gera_grafico(ef).show_grafico(ciclos)
                    except:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText('Nosso programa não conseguiu especificar o erro. Verifique os dados de entrada, principalmente os intervalos de analise. Caso o erro persista, envie-nos um email explicando o que ocorreu.')
                        msg.setWindowTitle("Atenção - Erro Desconhecido")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.exec_()
                        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
