from BackWardFacts import *
from rich.text import Text
from rich import print
from rich.panel import Panel

def check_answer(answer, options):
    if answer in options:
        return True
    return False

class BackwardEngine(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield NOFACT(answer="yes")

    @Rule(SYMPTOM(answer="no"))
    def disease_negative_1(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)

    @Rule(SYMPTOM(answer="yes"))
    def ask_breathlessness(self):
        while True:
            print(Text("Are you experiencing any breathlessness ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(BREATHLESSNESS(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="no")))
    def ask_footsore(self):
        while True:
            print(Text("Are you experiencing any footsore ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),
                  end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(FOOTSORE(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="no"), FOOTSORE(answer="yes")))
    def ask_result(self):
        self.declare(ABTEST(answer="yes"))
        while True:
            print(Text("what's the result of Ankle brachial test ? ", style="#bb0873") + Text("[positive/negative]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["positive", "negative"]):
                break
        self.declare(RESULT(answer=ans))

    @Rule(AND(ABTEST(answer="yes"), RESULT(answer="negative")))
    def disease_negative_2(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)

    @Rule(AND(ABTEST(answer="yes"), RESULT(answer="positive")))
    def disease_positive_1(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have PERIPHERAL ARTERIAL DISEASE", style="#ff0000"))
        print(panel)


    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes")))
    def ask_chestpain(self):
        while True:
            print(Text("Are you experiencing any chest pain ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(CHESTPAIN(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="no")))
    def ask_cyanosis(self):
        while True:
            print(Text("Are you experiencing any cyanosis ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(CYANOSIS(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="no"), CYANOSIS(answer="yes")))
    def ask_graph(self):
        self.declare(ECHOCARDIOGRAM(answer="yes"))
        while True:
            print(Text("What's the result of Echo cardiogram test ? ", style="#bb0873") + Text("[abnormal/normal]",style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["abnormal", "normal"]):
                break
        self.declare(GRAPH(answer=ans))

    @Rule(AND(ECHOCARDIOGRAM(answer="yes"), GRAPH(answer="normal")))
    def disease_negative_3(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)


    @Rule(AND(ECHOCARDIOGRAM(answer="yes"), GRAPH(answer="abnormal")))
    def disease_positive_2(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have CONGENITAL HEART DISEASE", style="#ff0000"))
        print(panel)


    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="no"), CYANOSIS(answer="no")))
    def ask_hmurmurs(self):
        while True:
            print(Text("Are you experiencing any heart murmurs ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(HMURMURS(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="no"), CYANOSIS(answer="no"), HMURMURS(answer="yes")))
    def ask_rxray(self):
        self.declare(XRAY(answer="yes"))
        while True:
            print(Text("What's the result of X-RAY ? ", style="#bb0873") + Text("[abnormal/normal]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["abnormal", "normal"]):
                break
        self.declare(RXRAY(answer=ans))

    @Rule(AND(XRAY(answer="yes"), RXRAY(answer="normal")))
    def disease_negative_4(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)


    @Rule(AND(XRAY(answer="yes"), RXRAY(answer="abnormal")))
    def ask_rmri(self):
        self.declare(CARDIACMRI(answer="yes"))
        while True:
            print(Text("What's the result of cardiac MRI test? ", style="#bb0873") + Text("[thin/thick/normal]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["thin", "thick", "normal"]):
                break
        self.declare(RMRI(answer=ans))

    @Rule(AND(CARDIACMRI(answer="yes"), RMRI(answer="thin")))
    def disease_positive_3(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have DILATED CARDIOMYOPATHY", style="#ff0000"))
        print(panel)


    @Rule(AND(CARDIACMRI(answer="yes"), RMRI(answer="thick")))
    def disease_positive_4(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have HYPERTROPHIC CARDIOMYOPATHY", style="#ff0000"))
        print(panel)


    @Rule(AND(CARDIACMRI(answer="yes"), RMRI(answer="normal")))
    def ask_rctscan(self):
        self.declare(CTSCAN(answer="yes"))
        while True:
            print(Text("What's the result of RCT scan ? ", style="#bb0873") + Text("[positive/negative]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["positive", "negative"]):
                break
        self.declare(RCTSCAN(answer=ans))

    @Rule(AND(CTSCAN(answer="yes"), RCTSCAN(answer="negative")))
    def disease_negative_5(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)

    @Rule(AND(CTSCAN(answer="yes"), RCTSCAN(answer="positive")))
    def disease_positive_5(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have ANGINA", style="#ff0000"))
        print(panel)


    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="yes")))
    def ask_discomfort(self):
        while True:
            print(Text("Are you experiencing any discomfort ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["yes", "no"]):
                break
        self.declare(DISCOMFORT(answer=ans))

    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="yes"), DISCOMFORT(answer="no")))
    def ask_report(self):
        self.declare(ULTRASONOGRAPHY(answer="yes"))
        while True:
            print(Text("What's the result of Ultra sonography ? ", style="#bb0873") + Text("[abnormal/normal]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["abnormal", "normal"]):
                break
        self.declare(REPORT(answer=ans))

    @Rule(AND(ULTRASONOGRAPHY(answer="yes"), REPORT(answer="normal")))
    def disease_negative_6(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)


    @Rule(AND(ULTRASONOGRAPHY(answer="yes"), REPORT(answer="abnormal")))
    def disease_positive_6(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have DEEP VEIN THROMBOSIS", style="#ff0000"))
        print(panel)


    @Rule(AND(SYMPTOM(answer="yes"), BREATHLESSNESS(answer="yes"), CHESTPAIN(answer="yes"), DISCOMFORT(answer="yes")))
    def ask_recg(self):
        self.declare(ECG(answer="yes"))
        while True:
            print(Text("What's the result of ECG ? ", style="#bb0873") + Text("[valveabnormalities/abnormal/normal]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["valveabnormalities", "abnormal", "normal"]):
                break
        self.declare(RECG(answer=ans))

    @Rule(AND(ECG(answer="yes"), RECG(answer="normal")))
    def disease_negative_7(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)


    @Rule(AND(ECG(answer="yes"), RECG(answer="valveabnormalities")))
    def ask_stresstest(self):
        while True:
            print(Text("what's the result of Stress test ? ", style="#bb0873") + Text("[high/low]", style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["high", "low"]):
                break
        self.declare(STRESSTEST(answer=ans))

    @Rule(AND(ECG(answer="yes"), RECG(answer="valveabnormalities"), STRESSTEST(answer="high")))
    def disease_positive_7(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have HEART VALVE DISEASE", style="#ff0000"))
        print(panel)


    @Rule(AND(ECG(answer="yes"), RECG(answer="abnormal")))
    def ask_bloodreport(self):
        self.declare(BLOODTEST(answer="yes"))
        while True:
            print(Text("What's the result of blood test ? ", style="#bb0873") + Text("[highprotein/lowiron/abnormal/normal]", style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["highprotein", "lowiron", "abnormal", "normal"]):
                break
        self.declare(BLOODREPORT(answer=ans))

    @Rule(AND(BLOODTEST(answer="yes"), BLOODREPORT(answer="highprotein")))
    def disease_positive_8(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have HEART ATTACK", style="#ff0000"))
        print(panel)


    @Rule(AND(BLOODTEST(answer="yes"), BLOODREPORT(answer="lowiron")))
    def disease_positive_9(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have STROKE", style="#ff0000"))
        print(panel)


    @Rule(AND(BLOODTEST(answer="yes"), BLOODREPORT(answer="abnormal")))
    def disease_positive_10(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have HEART FAILURE", style="#ff0000"))
        print(panel)


    @Rule(AND(BLOODTEST(answer="yes"), BLOODREPORT(answer="normal")))
    def ask_rcath(self):
        self.declare(CATHDERIZATION(answer="yes"))
        while True:
            print(
                Text("What's the result of Cathodic catheterization ? ", style="#bb0873") + Text("[positive/negative]",style="#ffd400"),end=" ")
            ans = input()
            if check_answer(ans, ["positive", "negative"]):
                break
        self.declare(RCATH(answer=ans))

    @Rule(AND(CATHDERIZATION(answer="yes"), RCATH(answer="positive")))
    def disease_positive_11(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have ARRHYTHMIAS", style="#ff0000"))
        print(panel)


    @Rule(AND(CATHDERIZATION(answer="yes"), RCATH(answer="negative")))
    def ask_tresult(self):
        self.declare(TREADMILLTEST(answer="yes"))
        while True:
            print(Text("What's the result of Treadmill test? ", style="#bb0873") + Text("[positive/negative]",style="#ffd400"), end=" ")
            ans = input()
            if check_answer(ans, ["positive", "negative"]):
                break
        self.declare(TRESULT(answer=ans))

    @Rule(AND(TREADMILLTEST(answer="yes"), TRESULT(answer="negative")))
    def disease_negative_8(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("There is no Disease", style="#ff0000"))
        print(panel)


    @Rule(AND(TREADMILLTEST(answer="yes"), TRESULT(answer="positive")))
    def disease_positive_12(self):
        self.reset()
        self.declare(NOFACT(answer="no"))
        panel = Panel(Text("you have CORONARY HEART DISEASE", style="#ff0000"))
        print(panel)

    @Rule(NOFACT(answer="yes"))
    def default(self):
        panel = Panel(Text("We Have No Facts For you DISEASE", style="#ff0000"))
        print(panel)
