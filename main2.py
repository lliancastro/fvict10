from pyscript import display, document # type: ignore

def sign_up(e):
    document.getElementById('output').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade_level = int(document.getElementById('grade').value)
    section = int(document.getElementById('section').value)

    if registration == "yes":
        if clearance == "yes":
            if section == 1:
                if grade_level >=1 and grade_level <=6:
                    display("Congrats, your team is Red Bulldogs", target="output", append=False)
                else:
                    display("Only Grades 7-12 are allowed to participate in the Intramurals.", target="output", append=False)
            elif section == 2:
                if grade_level >=1 and grade_level <=6:
                    display("Congrats, your team is Blue Bears", target="output", append=False)
                else:
                    display("Only Grades 7-12 are allowed to participate in the Intramurals.", target="output", append=False)
            elif section == 3:
                if grade_level >=1 and grade_level <=6:
                    display("Congrats, your team is Green Hornets", target="output", append=False)
                else:
                    display("Only Grades 7-12 are allowed to participate in the Intramurals.", target="output", append=False)
            elif section == 4:
                if grade_level >=1 and grade_level <=6:
                    display("Congrats, your team is Yellow Tigers", target="output", append=False)
                else:
                    display("Only Grades 7-12 are allowed to participate in the Intramurals.", target="output", append=False)
            elif section == 5:
                if grade_level >=1 and grade_level <=6:
                    display("Congrats, your team is Blue Bears", target="output", append=False)
                else:
                    display("Only Grades 7-12 are allowed to participate in the Intramurals.", target="output", append=False)
        else:
            display("Kindly get your clearance letter please.", target="output", append=False)
    else:
        display("Kindly register to be eligible for the Intramurals please.", target="output", append=False)