from pyscript import document

def check_eligibility(event):

    result_element = document.querySelector("#Result")
    

    reg_node = document.querySelector('input[name="answer1"]:checked')
    med_node = document.querySelector('input[name="answer3"]:checked')
    
    registration = reg_node.value if reg_node else None
    medical = med_node.value if med_node else None
    

    grade = document.querySelector("#grd").value
    section = document.querySelector("#sct").value

    if registration != "yes":
        result_element.innerHTML = "<div>You are not eligible. Please register online first.</div>"
        return

    if medical != "yes":
        result_element.innerHTML = "<div>You are not eligible. Please secure medical clearance.</div>"
        return

    if not section or not grade:
        result_element.innerHTML = "<div>Please select both grade and section.</div>"
        return



    team = "Unknown"
    logo_file = ""

    if section == "EMERALD":
        team = "Red Bulldogs"
        logo_file = "bulldogs.jpg"
    elif section == "RUBY":
        team = "Blue Bears"
        logo_file = "bears.jpg"
    elif section == "SAPPHIRE":
        team = "Green Hornets"
        logo_file = "hornets.jpg"
    elif section == "TOPAZ":
        team = "Yellow Tigers"
        logo_file = "tigers.jpg" 

    
    if team != "Unknown":
        result_html = f"""
            <div>
                <img src="{logo_file}" class="team-logo" alt="{team}"><br>
                <strong>{grade} {section} - {team}</strong><br>
                Congratulations! You are in the {team} team.
            </div>
        """
        result_element.innerHTML = result_html
    else:
        result_element.innerText = "Section not recognized."