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
    contact_info = {
        'name': 'Riddhi Mishra'}

    professional_info = {
        'profile': '<font face = "Century">A creative and quick thinking individual with a bent towards communicating and building strong business models. Well versed with digital marketing tools and strategies. Skilled at integrated marketing methodologies and can drive sales and increase brand awareness. I have worked as an Executive Operations Manager before. Those responsibilities have helped me grow in essential business skills falling under the category of communication, management and technical skills. The experience and knowledge gained during the tenure is reflected well in my work. I am always open to job opportunities where I can use these skills effectively to help business growth.</font>',

        'personal-details' : '<br/>'.join(['<font face = "Century">DOB - 15/06/2000</font>',
                                           '<font face = "Century">Address - Indore</font>',
                                           '<font face = "Century"><b>Contacts</b></font>',
                                           '<font face = "Century">Phone - +91 9874563215</font>',
                                           '<font face = "Century">E-Mail - riddhi@gmail.com</font>',
                                           '<font face = "Century">Linkedin - <a href = "https://www.linkedin.com/riddhimishra">https://www.linkedin.com/riddhimishra/</a></font>',
                                           '<font face = "Century">GitHub - <a href = "https://github.com/riddhi">https://github.com/riddhi</a></font>']),

        'education': '<br/>'.join(['<font face = "Century"><b>[10th] St. George H.S. School Dhar, Madhya Pradesh.</b></font>',
                                   '<font face = "Century">March 2015 - March 2016</font>',
                                   '<font face = "Century">9 CGPA</font>',
                                   '<font face = "Century"><b>[12th] St. George H.S. School Dhar, Madhya Pradesh.</b></font>',
                                   '<font face = "Century">March 2017 - March 2018</font>',
                                   '<font face = "Century">80%</font>',
                                   '<font face = "Century"><b>[B.Tech CSE Specialization] ITM University Gwalior</b></font>',
                                   '<font face = "Century">August 2019 - Till date</font>',
                                   '<font face = "Century">8.88 CGPA(Upto 3rd Sem)</font>',
                                   '<font face = "Century">8.27 SGPA(1st Sem), 8.7 SGPA(2nd Sem), 9.27 SGPA(3rd Sem)</font>']),

        'trainings' : '<br/>'.join(['<font face = "Century"><b>Nelumbus Educare - Python Programming</b></font>',
                                    '<font face = "Century"> July 2020 - December 2020</font>',
                                    '<font face = "Century"> A 40-Hours online training focusing on the programming language Python.</font>',
                                    '<font face = "Century"> The training focused on basics of Python as well as advanced concepts like file handling, tkinter.</font>',
                                    '<font face = "Century"><b>Udemy - Python Programming Masterclass by Tim Buchalka</b></font>',
                                    '<font face = "Century"> January 2021 - March 2021</font>',
                                    '<font face = "Century"> A 60-Hours recorded - lectures based training focusing on the programming language Python.</font>',
                                    '<font face = "Century"> The training focused on Python basics and other concepts like functions and modules, databases etc.</font>'


                                    ]),

        'experience': [''.join(['<font face = "Century"><b>[Doorstepshopee(DSS), Gwalior] - Executive Operations Manager</b> <br/></font>',
                                '<font face = "Century">February 2020 - Till date<br/></font>',
                                '<font face = "Century">Was responsible for a number of administrative duties such as typing, accounts and stock management.</font>',
                                '<font face = "Century">Oversaw all aspects of design and development for the mobile and web-app, and offered necessary design solutions when necessary.<br/></font>',
                                '<font face = "Century">Organized and prioritized work to complete assignments in a timely, efficent manner.<br/></font>',
                                '<font face = "Century">Cooperated with superiors and colleagues to achieve goals and managed a variety of internal communications as well.<br/></font>',
                                '<font face = "Century">Overall, served as friendly, hardworking and punctual employee with client satisfaction in mind.<br/></font>',
                                ])],

        'skills': '<br/>'.join(['<font face = "Century"><b>Soft skills</b>  Problem solving, critical thinking, communication, teamwork, creativity, attention to detail, customer service, leadership, ability to work under pressure.</font>',
                                '<font face = "Century"><b>Hard skills</b> Computer software and Application Knowledge, Negotiation, Project Management, Marketing, Administrative, Writing and record keeping.</font>',
                                '<font face = "Century"><b>Technical skills</b> Languages - [C, C++, Java, Python], Frameworks - [Django, Flask], Tools - [IntelliJ IDEA, Git/GitHub], Databases - [MySQL, PL/SQL].</font>']),

        'hobbies' : '<font face = "Century">Art, Writing, Reading, Painting, Marketing</font>',

        'projects': [
            ''.join(['<font face = "Century"><b>WebCam Motion Detector</b> - <a href = "http://github.com/webcammotiondetector">http://github.com/webcammotiondetector</a><br/></font>',
                     '<font face = "Century">This project detects a moving object using webcam.</font>',
                     '<font face = "Century">It then records the timestamp when the motion started and timestamp when it ended.</font>',
                     '<font face = "Century">The output of timestamps is in form of a csv file .</font> ']),
        ]}
    table_elements = [
        ['PROFILE', Paragraph(professional_info['profile'], styles['custom-style'])],
        ['PERSONAL\nDETAILS', Paragraph(professional_info['personal-details'], styles['custom-style'])],
        ['EDUCATION', Paragraph(professional_info['education'], styles['custom-style'])],
        ['TRAININGS', Paragraph(professional_info['trainings'], styles['custom-style'])],
        ['EXPERIENCE', [Paragraph(x, styles['custom-style']) for x in professional_info['experience']]],
        ['PROJECTS', [Paragraph(x, styles['custom-style']) for x in professional_info['projects']]],
        ['SKILLS', Paragraph(professional_info['skills'], styles['custom-style'])],
        ['HOBBIES', Paragraph(professional_info['hobbies'], styles['custom-style'])],
    ]
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

