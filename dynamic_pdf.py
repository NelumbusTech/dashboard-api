from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfdoc
from reportlab.lib.units import inch, cm
from reportlab.platypus.flowables import Spacer
from reportlab.lib.enums import TA_RIGHT

registerFont(TTFont('Century', 'CenturyGothicRegular.ttf'))
registerFont(TTFont('CenturyBold', 'CenturyGothicBold.ttf'))
registerFontFamily('Century', normal='Century', bold='CenturyBold')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='custom-style',
                          fontFamily= 'Century',
                          fontSize=8,
                          spaceAfter=.1*inch))

WIDTH = 8.5 * inch
HEIGHT = 11 * inch

def main():
    print("Enter your details for resume\n")
    name = input("Enter your name: ").title()

    resume_sections = []
    contact_info = {
        'name': name}

    professional_info = {}


    while True:
        choice = input("Do you wish to add a 'profile summary' section to your resume? (Y/N): ")
        if choice== 'y' or choice == 'Y':
            resume_sections.append('PROFILE')
            professional_info['PROFILE'] = []
            profile = input("Enter your profile summary: ")
            if profile.strip() == "":
                pass
            else:
                professional_info['PROFILE'].append('<font face = "Century">{}</font>'.format(profile))
            break
        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add 'personal details' (contacts, dob, address) section to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('PERSONAL DETAILS')
            professional_info['PERSONAL DETAILS'] = []
            print("\nEnter your personal details")
            dob = input("Enter your date of birth(dd-mm-yyyy): ")
            if dob.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">DOB - {}</font>'.format(dob))
            address = input("Enter your address: ")
            if address.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">Address - {}</font>'.format(address))
            # professional_info['PERSONAL DETAILS'].append('<font face = "Century"><b>Contacts</b></font>')
            contact_number = input("Enter your contact number: ")
            if contact_number.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">Phone - {}</font>'.format(contact_number))
            email_id = input("Enter your E-Mail address: ")
            if email_id.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">Linkedin - <a href = {0}>{0}</a></font>'.format(email_id))
            linkedin = input("Enter the link to your linkedin profile: ")
            if linkedin.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">Linkedin - <a href = {0}>{0}</a></font>'.format(linkedin))
            github = input("Enter the link to your GitHub profile: ")
            if github.strip() == "":
                pass
            else:
                professional_info['PERSONAL DETAILS'].append('<font face = "Century">GitHub - <a href = {0}>{0}</a></font>'.format(github))

            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add 'educational details' section to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('EDUCATION')
            professional_info['EDUCATION'] = []
            print("\nEnter your educational details")

            while True:
                degree = input("\nEnter the standard/degree : ")
                institution = input("Enter institution name : ")
                if institution.strip() != "" and degree.strip() == "":
                    professional_info['EDUCATION'].append('<font face = "Century"><b>{}</b></font>'.format(institution))
                elif degree.strip() != "" and institution.strip() == "":
                    professional_info['EDUCATION'].append('<font face = "Century"><b>[{}]</b></font>'.format(degree))
                else:
                    professional_info['EDUCATION'].append('<font face = "Century"><b>[{}] - {}</b></font>'.format(degree, institution))
                duration = input("Enter duration : ")
                professional_info['EDUCATION'].append('<font face = "Century">{}</font>'.format(duration))
                grade = input("Enter grade obtained : ")
                professional_info['EDUCATION'].append('<font face = "Century">{}</font>'.format(grade))
                choice = input("Do you wish to add more standard/degrees(Y/N): ")

                if degree.strip() == institution.strip() == duration.strip() ==grade.strip() == "":
                    professional_info['EDUCATION'] = []

                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    break
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add your 'trainings' to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('TRAININGS')
            professional_info['TRAININGS'] = []
            print("\nEnter your trainings details")

            while True:
                organization = input("\nEnter name of the organization : ")
                training = input("Enter name of the course/training : ")
                professional_info['TRAININGS'].append('<font face = "Century"><b>{} - {}</b></font>'.format(organization, training))
                duration = input("Enter duration : ")
                professional_info['TRAININGS'].append('<font face = "Century">{}</font>'.format(duration))
                description = input("Enter your training description: ")
                professional_info['TRAININGS'].append('<font face = "Century"> {}</font>'.format(description))
                choice = input("Do you wish to add more trainings(Y/N): ")

                if organization.strip() == training.strip() == duration.strip() == description.strip() == "":
                    professional_info['TRAININGS'] = []
                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    break
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add your 'work experience' to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('EXPERIENCE')
            professional_info['EXPERIENCE'] = []
            print("\nEnter your experience details")

            while True:
                organization = input("\nEnter name of the organization : ")
                role = input("Enter job role : ")
                professional_info['EXPERIENCE'].append('<font face = "Century"><b>{} - {}</b></font>'.format(organization, role))
                duration = input("Enter duration : ")
                professional_info['EXPERIENCE'].append('<font face = "Century">{}</font>'.format(duration))
                description = input("Enter your job description: ")
                professional_info['EXPERIENCE'].append('<font face = "Century"> {}</font>'.format(description))
                choice = input("Do you wish to add more experiences(Y/N): ")

                if organization.strip() == role.strip() == duration.strip() == description.strip() == "":
                    professional_info['EXPERIENCE'] = []
                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    break
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add your 'projects' to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('PROJECTS')
            professional_info['PROJECTS'] = []
            print("\nEnter your project details")

            while True:
                heading = input("\nEnter name of the project : ")
                link = input("Enter link to your project : ")
                professional_info['PROJECTS'].append('<font face = "Century"><b>{0}</b> - <a href = {1}>{1}</a></font>'.format(heading, link))
                description = input("Enter your project description: ")
                professional_info['PROJECTS'].append('<font face = "Century"> {}</font>'.format(description))
                choice = input("Do you wish to add more projects (Y/N): ")

                if heading.strip() == link.strip() == description.strip() == "":
                    professional_info['PROJECTS'] = []
                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    break
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add your 'skills' to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('SKILLS')
            professional_info['SKILLS'] = []
            print("\nEnter your skills")

            soft_skills = hard_skills = technical_skills = ""
            anotherChoice = input("\nDo you wish to add 'soft skills' to 'SKILLS' section of your resume(Y/N): ")
            if anotherChoice == 'y' or anotherChoice == 'Y':
                soft_skills = input("Enter 'soft skills' separated by commas. Example - English proficiency, social intelligence: ")
                professional_info['SKILLS'].append('<font face = "Century"><b>Soft skills </b> - {}</font>'.format(soft_skills))
            else:
                pass

            anotherChoice = input("\nDo you wish to add 'hard skills' to 'SKILLS' section of your resume(Y/N): ")
            if anotherChoice == 'y' or anotherChoice == 'Y':
                hard_skills = input("Enter 'hard skills' separated by commas. Example - SEO Marketing, Project management: ")
                professional_info['SKILLS'].append('<font face = "Century"><b>Hard skills </b> - {}</font>'.format(hard_skills))
            else:
                pass

            anotherChoice = input("\nDo you wish to add 'technical skills' to 'SKILLS' section of your resume(Y/N): ")
            if anotherChoice == 'y' or anotherChoice == 'Y':
                technical_skills = input("Enter 'technical skills' separated by commas. Example - Coding Ability, Microsoft Office proficiency: ")
                professional_info['SKILLS'].append('<font face = "Century"><b>Technical skills </b> - {}</font>'.format(technical_skills))
            else:
                pass

            if soft_skills.strip() == hard_skills.strip() == technical_skills.strip() == "":
                professional_info['SKILLS'] = []
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        choice = input("\nDo you wish to add your 'hobbies' to your resume? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            resume_sections.append('HOBBIES')
            professional_info['HOBBIES'] = []
            while True:
                hobby = input("Enter a hobby : ")
                if hobby == "":
                    pass
                else:
                    professional_info['HOBBIES'].append('<font face = "Century">{}</font>'.format(hobby))
                anotherChoice = input("Do you wish to add more hobbies. (Y/N): ")
                if anotherChoice == 'y' or anotherChoice == 'Y':
                    continue
                else:
                    break
            break

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue

    while True:
        print("\nYour resume contains following sections: ",end="")
        for resume_section in resume_sections:
            print(resume_section, end= ", ")
        choice = input("\nDo you wish to have more sections(Example - Certifications, References). Enter(Y/N): ")
        if choice == 'y' or choice == 'Y':
            title = input("\nEnter title for the section(This will be displayed in bold): ")
            resume_sections.append(title.upper())
            professional_info[title.upper()] = []
            professional_info[title.upper()].append('<font face = "Century"><b>{}</b></font>'.format(title))
            description = input("\nEnter description: ")
            professional_info[title.upper()].append('<font face = "Century">{}</font>'.format(description))
            if title.strip() == description.strip() == "":
                professional_info[title.upper()] = []

            continue

        elif choice == 'n' or choice == 'N':
            break
        else:
            print("Kindly enter (Y/N) only.\n")
            continue
    table_elements = []
    for resume_section in resume_sections:
        print()
        if professional_info[resume_section] == []:
            pass
        else:
            table_elements.append([(resume_section.replace(" ","\n").upper()), Paragraph('<br/>'.join(professional_info[resume_section]), styles['custom-style'])]),

    pdf_serializer(table_elements, contact_info)

def pdf_serializer(professional_info, contact_info):
    pdf_name = 'student-resume.pdf'
    doc = SimpleDocTemplate(
        pdf_name,
        pagesize=letter,
        bottomMargin=.5 * inch,
        topMargin=.7 * inch,
        rightMargin=.4 * inch,
        leftMargin=.4 * inch)

    style = styles['custom-style']
    table = Table(
        professional_info,
        colWidths=[
            0.8 * inch,
            6.9 * inch],
    )

    table_properties = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Century'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT')])
    table.setStyle(table_properties)

    elements = []
    elements.append(table)

    doc.build(
        elements,
        onFirstPage=pdf_first_page_header(contact_info)
    )
    return pdf_name

def pdf_first_page_header(contact_info):

    def myPage(canvas, doc):
        canvas.saveState()
        canvas.setFont('CenturyBold', 16)
        canvas.drawString(
            .4 * inch,
            HEIGHT - (.4 * inch),
            contact_info['name'])

        canvas.line(.4 * inch, HEIGHT - (.47 * inch),
                    WIDTH - (.4 * inch), HEIGHT - (.47 * inch))
        canvas.restoreState()
    return myPage

main()

