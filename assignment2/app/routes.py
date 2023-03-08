from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
from forms import NewsLetterForm
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
    
@app.route('/menu')
def menu():
    return render_template('menu.html', title='Menu')

@app.route('/about')
def about():
    return render_template('about.html', title='About')
    
@app.route('/specials')
def specials():
    return render_template('specials.html', title='WeeklySpecials')
    
@app.route('/registered')
def registered():
    return render_template('Registered.php', title='Registered')

    
@app.route('/donuts')
def donuts():
    return render_template('Donuts.html', title='Donuts')
    
@app.route('/vanillaslice')
def vanillaslice():
    return render_template('VanillaSlice.html', title='VanillaSlice')
    
@app.route('/randytart')
def randytart():
    return render_template('RandyTart.html', title='RandyTart')
    
@app.route('/custardtart')
def custardtart():
    return render_template('CustardTart.html', title='CustardTart')
    
@app.route('/raspberrycheesecake')
def raspberrycheesecake():
    return render_template('Raspberrycheesecake.html', title='RaspberryCheeseCake')
    
@app.route('/applecakeslice')
def applecakeslice():
    return render_template('AppleCakeSlice.html', title='AppleCakeSlice')

 
###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################
@app.route('/newsletter', methods=["GET","POST"])
def get_newsletter():
    form = NewsLetterForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        res = pd.DataFrame({'name':name, 'email':email}, index=[0])
        res.to_csv('./newsletter.csv')
        return render_template('newsletter.html', form=form)
    else:
        return render_template('newsletter.html', form=form)