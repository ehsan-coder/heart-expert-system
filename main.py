from BackWardEngine import *
from ForWardEngine import *
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

diseases_list = [(1,"Angina"),(2,"Arrhythmias"),(3,"Congenital Heart Disease"),(4,"Coronary Heart Disease"),(5,"Deep Vein Thrombosis"),(6,"Dilated Cardiomyopathy"),(7,"Heart Attack"),(8,"Heart Failure"),(9,"Heart Valve Disease"),(10,"Hypertrophic Cardiomyopathy"),(11,"Peripheral Arterial Disease"),(12,"Stroke")]

def backward():
    ke = BackwardEngine()
    ke.reset()
    while True:
        print(Text("Are you experiencing any symptom(s) ? ", style="#bb0873") + Text("[yes/no]", style="#ffd400"), end =" ")
        ans = input()
        if ans == "yes" or ans == "no":
            break
    start_question = ans
    start_fact = SYMPTOM(answer=start_question)
    ke.declare(start_fact)
    ke.run()

def forward():
    ke = ForwardEngine()
    ke.reset()
    table = Table(box=box.DOUBLE_EDGE, style="#123aff")
    table.add_column("No", justify="left", style="#2bab01")
    table.add_column("DISEASES LIST", justify="left", style="#2bab01")
    for diseases in diseases_list:
        table.add_row(str(diseases[0]), diseases[1])

    console = Console(color_system="windows")
    console.print(table)
    def check_answer():
        while True:
            print(Text("Enter Your DISEASE Number ? ", style="#bb0873") + Text("[1, 2 , . . .]", style="#ffd400"),end=" ")
            start_question = input()
            for i, v in enumerate(diseases_list):
                if str(v[0]) == start_question:
                    answer = diseases_list[i][1]
                    return answer

    start_fact = DISEASE(answer=check_answer())
    ke.declare(start_fact)
    ke.run()




if __name__ == '__main__':
    while True:
        table = Table(title=Text("Expert system for diagnosing heart diseases", style="#123aff"), box=box.DOUBLE_EDGE, style="#123aff")

        table.add_column("Choices", justify="left", style="green")
        table.add_row("1 for disease diagnosis")
        table.add_row("2 for treatment")
        table.add_row("3 for exit")

        print("___________________________________________________________________________________________________________________\n")
        console = Console(color_system="windows")
        console.print(table)
        ch = input("Choice ? ")
        print("___________________________________________________________________________________________________________________\n")
        if ch == '1':
            backward()
        if ch == '2':
            forward()
        if ch == '3':
            break
