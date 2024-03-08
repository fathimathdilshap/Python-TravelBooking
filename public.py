from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('homepage.html')		

@public.route('/login',methods=['get','post'])
def login():
	if 'log' in request.form:
		username=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			print(res)
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				flash("login successfully")
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=="user":
				a="select * from userregistration where login_id='%s'"%(session['lid'])
				res=select(a)
				if res:
					session['user_id']=res[0]['user_id']
					flash("login successfully")
					return redirect(url_for('user.userhome'))
		else:
			flash("invalid username or password")
	return render_template("login.html")


@public.route('/userregistration',methods=['get','post'])
def userregistration():
	
	if 'reg' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		age=request.form['age']
		Gender=request.form['gender']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		idp=request.form['Proof']
		username=request.form['uname']
		password=request.form['pass']
		print(username)
		q="insert into login values(null,'%s','%s','pending')" %(username,password)
		id=insert(q)
		q="insert into userregistration values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','pending','%s')" %(id,fname,lname,address,age,place,phone,email,idp,Gender)
		insert(q)
	return render_template("userregistration.html")   


@public.route('/About')
def About():
	return render_template('About.html')	


@public.route('/Contact')
def Contact():
	return render_template('Contact.html')	

