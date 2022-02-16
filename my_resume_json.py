import json
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_auto_page_break(auto = True, margin = 10)

file = open('json files\gia_nieto.json','r')

obj = json.load(file)

pdf.set_font('helvetica', 'BU', 20)
pdf.cell(200, 10, obj.get('Name'), ln=1,)

pdf.set_font('helvetica', '', 12)
pdf.cell(1,6, obj.get('Position'), ln=1,)
pdf.cell(1,6, obj.get('Email'), ln=1,)
pdf.cell(1,6, obj.get('Phone'), ln=1,)
pdf.cell(1,6, obj.get('Location'), ln=1,)
pdf.ln(3)
pdf.line(x1=-1, y1=45, x2=220, y2=45)


# basic info
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(100,10, 'PERSONAL INFORMATION', ln=1,)  

pdf.set_font('helvetica', '', 11)
pdf.cell(0,5, obj.get('Age'), ln=1,)
pdf.cell(0,5, obj.get('Birthdate'), ln=1,)
pdf.cell(0,5, obj.get('Civil Status'), ln=1,) 
pdf.cell(0,5, obj.get("Religion"), ln=1,)  
pdf.ln(2)
pdf.line(x1=-1, y1=79, x2=220, y2=79) 

pdf.line(x1=-1, y1=100, x2=220, y2=100)
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(100,10, 'DESCRIPTION', ln=1,)  
pdf.set_font('helvetica', '', 11)
for summary in range(len(obj.get("Description"))):
    pdf.cell(0,5, obj.get("Description")[summary], ln=1,) 
pdf.ln(1)

pdf.line(x1=-1, y1=184, x2=220, y2=184) 
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(100,10, 'SOCIAL WEBSITES', ln=1,)

# print(obj.get('Social Media')[0].get('Network')) 

#Social Media
for socmed in range(len(obj.get("Social Media"))):
    pdf.set_font('helvetica', '', 11)
    pdf.ln(1)
    pdf.cell(0,5, obj.get("Social Media")[socmed].get('Network'), ln=1,) #Gets the list of Social Media Network
    pdf.cell(0,5, obj.get("Social Media")[socmed].get('Username'), ln=1,) #Gets the list of Username
    pdf.cell(0,5, obj.get("Social Media")[socmed].get('URL'), ln=1,) #Gets the list of URK
    pdf.ln(3)

pdf.line(x1=-1, y1=246, x2=220, y2=246)
pdf.set_font('helvetica', 'BU', 14) 
pdf.cell(0,5, 'WORK EXPERIENCE', ln=3,) 

#work
for work in range(len(obj.get("Work Experiences"))):
    pdf.set_font('helvetica', '', 11)
    pdf.ln(3)
    pdf.cell(0,5, obj.get("Work Experiences")[work].get('Company'), ln=1,) 
    pdf.cell(0,5, obj.get("Work Experiences")[work].get('Position'), ln=1,) 
    pdf.cell(0,5, obj.get("Work Experiences")[work].get('Website'), ln=1,) 
    if(work == 1):
        pdf.cell(0,5, obj.get("Work Experiences")[1].get('End Date'), ln=1,)
    pdf.cell(0,5, obj.get("Work Experiences")[work].get('Start Date'), ln=1,) 
    pdf.ln(3)

pdf.set_font('helvetica', 'BU', 14)
pdf.cell(0,5, 'EDUCATION', ln=1,)
pdf.ln(3)

pdf.set_font('helvetica', '', 11)   
pdf.cell(0,5, obj.get("Education"), ln=1,)  
pdf.ln(5)
pdf.line(x1=-1, y1=265, x2=220, y2=265)

##Using for loop since our json file has nested data
#Languages
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(0,5, 'Languages', ln=1,)


for lang in range(len(obj.get("Languages"))):
    pdf.set_font('helvetica', '', 11)
    pdf.cell(0,5, obj.get("Languages")[lang].get('1'), ln=1,) 
    pdf.cell(0,5, obj.get("Languages")[lang].get('2'), ln=1,)
pdf.ln(4) 

#Skills
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(0,5, 'Skills', ln=1,)

for skills in range(len(obj.get("Skills"))):
    pdf.set_font('helvetica', '', 11)
    pdf.cell(0,5, obj.get("Skills")[skills].get('first'), ln=1,) 
    pdf.cell(0,5, obj.get("Skills")[skills].get('second'), ln=1,) 
    pdf.cell(0,5, obj.get("Skills")[skills].get('third'), ln=1,) 
    pdf.cell(0,5, obj.get("Skills")[skills].get('fourth'), ln=1,) 
pdf.ln(4) 
    
#Interests
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(0,5, 'Interests', ln=1,)

for interests in range(len(obj.get("Interests"))):
    pdf.set_font('helvetica', '', 11)
    pdf.cell(0,5, obj.get("Interests")[interests].get('lists'), ln=1,) 
pdf.ln(4) 
 
#Programming Languages
pdf.set_font('helvetica', 'BU', 14)
pdf.cell(0,5, 'Programming Languages', ln=1,)

for prog in range(len(obj.get("Programming Languages"))):
    pdf.set_font('helvetica', '', 11)
    pdf.cell(0,5, obj.get("Programming Languages")[prog].get('one'), ln=1,) 
    pdf.cell(0,5, obj.get("Programming Languages")[prog].get('two'), ln=1,) 
    pdf.cell(0,5, obj.get("Programming Languages")[prog].get('three'), ln=1,) 
    pdf.cell(0,5, obj.get("Programming Languages")[prog].get('four'), ln=1,) 
pdf.ln(4)      

pdf.set_line_width(0.5)


pdf.output('nieto_camille.pdf')