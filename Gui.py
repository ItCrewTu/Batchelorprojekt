# -*- coding: utf-8 -*-
"""
provides the functions to create a gui

"""
import os
import sys
from psychopy import gui


class StateCheckIn:
    """
    provides the functions to create a gui
    
    """

    # if this class is started, it opens the gui
    def check_in_name_and_type(self):
        """
        creates a gui for testperson data and experiment type
        
        """
        # ensure that the path starts from the same directery this script is in
        self.this_dir = os.path.dirname(
            os.path.abspath(__file__)).decode(
                sys.getfilesystemencoding())
        os.chdir(self.this_dir)

        # input window for the data of this testperson
        self.gui_input = gui.Dlg(title="Signalentdeckung.py")
        self.gui_input.addField("Versuchsperson:")  # 0
        self.gui_input.addField("Durchgang:")  # 1
        self.gui_input.addField(
            "Experimenttyp:",
            choices=[
                "Yes/No Task",
                "2IFC",
                "4IFC",
                "Constant Stimuli"])  # 2
        self.gui_input.show()

    def set_variables(self, experiment_type):
        """
        creates a gui to configure the experiment
        
        """

        self.gui_input_var = gui.Dlg(title="Signalentdeckung.py")
        
        self.gui_input_var.addText("Einstellungen:")

        self.gui_input_var.addField("Trialanzahl", 10)  # 3
        self.gui_input_var.addField("Anzahl der Trialblocks", 5)  # 4
        self.gui_input_var.addField("Anzahl der Testtrials", 5)  # 5
        self.gui_input_var.addField("Dauer Fixationskreuz", 0.2)  # 6
        self.gui_input_var.addField("Dauer Maske:", 0.1)  # 7
        self.gui_input_var.addField("Dauer Stimulus", 0.2)  # 8
        self.gui_input_var.addField("Dauer Antwortperiode", 2)  # 9
        self.gui_input_var.addField("Dauer Feedback", 0.2)  # 10
        self.gui_input_var.addField("Dauer Pause", 0.1)  # 11
        self.gui_input_var.addField("Stimulusgröße in Pixeln",
                                    choices=["64x64", "128x128", "256x256"])  # 12
        
        self.gui_input_var.addText("Signaleinstellungen:")
        
        self.gui_input_var.addField("Stärke des Signals:", 11)  # 13
        self.gui_input_var.addField("Mittelwert", 128)  # 14
        self.gui_input_var.addField("Standartabweichung", 30)  # 15
        
        # dont show the last 3 options for the constant stimuli task 
        if experiment_type == "Constant Stimuli":
            self.gui_input_var.show()
        self.gui_input_var.addField("Kontrast - X je Trialblock", False)  # 16
        self.gui_input_var.addField("Schrittweite", 2)  # 17
        self.gui_input_var.addField("Zufällig", False)
        if experiment_type != "Constant Stimuli":
            self.gui_input_var.show()
