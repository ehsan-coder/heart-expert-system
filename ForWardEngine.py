from ForWardFacts import *
from rich.text import Text
from rich import print
from rich.panel import Panel

class ForwardEngine(KnowledgeEngine):

    @Rule(DISEASE(answer="Angina"))
    def angina(self):
        panel = Panel(Text("Angioplastry and Stent treatment. Should take oral medications that include Nitrates, Aspirin.", style="#ff0000"))
        print(panel)

    @Rule(DISEASE(answer="Arrhythmias"))
    def arrhythmias(self):
        panel = Panel(Text("Maze procedure and cardioversion treatment that uses electricity to shock the heart back into a normal rhythm while the patient is sedated are to be done.", style="#ff0000"))
        print(panel)

    @Rule(DISEASE(answer="Congenital Heart Disease"))
    def congenital_heart_disease(self):
        panel = Panel(Text("Treatment include medicines, catheter procedures, surgery, and heart transplants.", style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Coronary Heart Disease"))
    def coronary_heart_disease(self):
        panel = Panel(Text("Coronary bypass surgery should be done. Beta blockers and calcium channel blockers should be given to the patient for speed recovery.", style="#ff0000"))
        print(panel)

    @Rule(DISEASE(answer="Deep Vein Thrombosis"))
    def deep_vein_thrombosis(self):
        panel = Panel(Text("Oral antocoagulants, Heparin and Vitamin K antagonist should be taken.",style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Dilated Cardiomyopathy"))
    def dilated_Cardiomyopathy(self):
        panel = Panel(Text("Treated with Beta blockers and ACE inhibitors can help to recover soon.",style="#ff0000"))
        print(panel)

    @Rule(DISEASE(answer="Heart Attack"))
    def heart_attack(self):
        panel = Panel(Text("Thrombolysis and baloon Angioplastry surgery are to be undergone.",style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Heart Failure"))
    def heart_failure(self):
        panel = Panel(Text("Heart transplantation or coronary bypass surgery is to be undergone. Blood Thinning medications can prevent further damage to the heart.",style="#ff0000"))
        print(panel)

    @Rule(DISEASE(answer="Heart Valve Disease"))
    def heart_valve_disease(self):
        panel = Panel(Text("Valve repair replacement or Balloon valvuloplastry are to be done.",style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Hypertrophic Cardiomyopathy"))
    def hypertrophic_cardiomyopathy(self):
        panel = Panel(Text("Septal Myectomy and Alcohol septal ablation can cure this disease.",style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Peripheral Arterial Disease"))
    def peripheral_arterial_disease(self):
        panel = Panel(Text("Angioplastry,Bypass surgery are to be done. Supervised exercise program can help with the cure.",style="#ff0000"))
        print(panel)


    @Rule(DISEASE(answer="Stroke"))
    def stroke(self):
        panel = Panel(Text("Tissue plasminogen activator should be given.Thrombectomy should be done.",style="#ff0000"))
        print(panel)
