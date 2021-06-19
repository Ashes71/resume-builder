from django.shortcuts import render,redirect
from PIL import Image,ImageDraw, ImageFont
from django.http import HttpResponse
from django.template.loader import get_template
import textwrap3
# Create your views here.
def Template1(request):
    if request.method=='POST':
        data=request.POST
        img = Image.open("images/11th hr template-01.png").convert("RGB")
        pics = ['images/maps1.png', 'images/phone1.png', 'images/email1.png']
        x = 190
        y = 550
        for pic in pics:
            image = Image.open(pic)
            img.paste(image, (x, y))
            y += 100
        font = ImageFont.truetype("fonts/Montserrat-Bold.ttf", 70)
        font1 = ImageFont.truetype("fonts/Montserrat-Regular.ttf", 50)
        font3 = ImageFont.truetype("fonts/Montserrat-Regular.ttf", 40)
        font2 = ImageFont.truetype("fonts/Montserrat-Bold.ttf", 65)
        draw = ImageDraw.Draw(img)
        draw.text((190, 365), data['name'], font=font, fill="black")
        draw.text((x + 100, 540),data['location'], font=font1, fill="black")
        draw.text((x + 100, 640), data['mobile'], font=font1, fill="black")
        draw.text((x + 100, 740), data['email'], font=font1, fill="black")
        Career_Objective = data['carrer_objective']
        lines = textwrap3.wrap(Career_Objective, 101)
        draw.text((149, 1100), "Career Objective", font=font2, fill="black")
        x1, y1 = 190, 1200
        draw.rectangle((x1, y1 + 25, x1 + 15, y1 + 40), fill="black")
        for line in lines:
            draw.text((x1 + 50, y1), text=line, fill='black', font=font3)
            y1 = y1 + 70
        draw.line((0, y1 + 50, img.size[0], y1 + 50), fill="grey", width=3)
        draw.text((x1 - 50, y1 + 100), "Education", font=font2, fill="black")
        y1 = y1 + 250
        for j in range(1,4):
            c = 'class'+ str(j)
            s = 'school'+ str(j)
            y = 'year' + str(j)
            m = 'marks'+ str(j)
            draw.rectangle((x1, y1, x1 + 15, y1 + 15), fill="black")
            draw.text((x1 + 50, y1 - 20),data[c]+'- '+data[s]+'- '+data[y]+'- '+data[m], font=font3, fill="black")
            y1 += 60
        skills = data['skills'].split(',')
        draw.line((0, y1 + 50, img.size[0], y1 + 50), fill="grey", width=3)
        draw.text((149, y1 + 60), "Skills", font=font2, fill="black")
        y1 += 200
        for i in range(len(skills)):
            draw.rectangle((x1, y1, x1 + 15, y1 + 15), fill="black")
            draw.text((x1 + 50, y1 - 20), skills[i], font=font3, fill="black")
            y1 += 50
        draw.line((0, y1 + 50, img.size[0], y1 + 50), fill="grey", width=3)
        projects = data['projects'].split(',')
        draw.text((x1 - 50, y1 + 100), "Key Projects & Presentation", font=font2, fill="black")
        y1 = y1 + 250
        for k in range(len(projects)):
            draw.rectangle((x1, y1, x1 + 15, y1 + 15), fill="black")
            draw.text((x1 + 50, y1 - 20), projects[k], font=font3, fill="black")
            y1 += 60
        draw.line((0, y1 + 50, img.size[0], y1 + 50), fill="grey", width=3)
        draw.text((x1 - 50, y1 + 100), "Achievements", font=font2, fill="black")
        Achievements = data['achievements'].split(',')
        y1 = y1 + 250
        for l in range(len(Achievements)):
            draw.rectangle((x1, y1, x1 + 15, y1 + 15), fill="black")
            draw.text((x1 + 50, y1-20 ), Achievements[l], font=font3, fill="black")
            y1 += 50
        draw.line((0, y1 + 50, img.size[0], y1 + 50), fill="grey", width=3)
        draw.text((x1 - 50, y1 + 100), "Languages Known", font=font2, fill="black")
        languages = data['languages'].split(',')
        y1 = y1 + 250
        for m in range(len(languages)):
            draw.rectangle((x1, y1, x1 + 15, y1 + 15), fill="black")
            draw.text((x1 + 50, y1 -20), languages[m], font=font3, fill="black")
            x1 += 250
        img.save('static/resume.pdf')
        request= PDF(request)
        return request


    else:
        return render(request,'template.html')
def Template1_About(request):
    return render(request,"About.html")
def Template1_Contact_Us(request):
    return render(request,"Contact_Us.html")
def PDF(request):
    return render(request,"pdf.html")

