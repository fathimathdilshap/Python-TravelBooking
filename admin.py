from public import *
from database import *


admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")

@admin.route('/adminviewuser',methods=['get','post'])
def adminviewuser():
	data={}
	q="select * from userregistration"
	res=select(q)
	data['user']=res
	if 'action' in request.args:
		action=request.args['action']
		login_id=request.args['login_id']
	else:
		action=None
	if action=="accept":
		q="update userregistration set Status='accept' where login_id='%s'"%(login_id)
		update(q)
		z="update login set usertype='user' where login_id='%s'"%(login_id)
		update(z)
		
		return redirect(url_for('admin.adminviewuser'))
	if action=="reject":
		x="update userregistration set Status='reject' where login_id='%s'"%(login_id)
		update(x)
		y="update login set usertype='reject' where login_id='%s'"%(login_id)
		update(y)
		return redirect(url_for('admin.adminviewuser'))			

	return render_template('adminviewuser.html',data=data)

@admin.route('/adminviewtrip',methods=['get','post'])
def adminviewtrip():
	data={}
	q="select *,trips.place as tplace from trips inner join userregistration using(user_id)"
	res=select(q)
	data['user']=res
	return render_template('adminviewtrip.html',data=data)
@admin.route('/admin_view_user',methods=['get','post'])
def admin_view_user():
	data={}
	id=request.args['id']
	q="Select * from userregistration where User_id='%s'" %(id)
	res=select(q)
	data['user']=res
	return render_template('admin_view_user.html',data=data)


@admin.route('/adminviewcomplaints',methods=['get','post'])
def adminviewcomplaints():
	data={}
	q="SELECT * FROM `complaint` INNER JOIN userregistration USING(User_id)"
	res=select(q)
	data['user']=res
	return render_template('adminviewcomplaints.html',data=data)

@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
	id=request.args['id']
	if 'send' in request.form:
		Reply=request.form['reply']
		q="update complaint set Reply='%s' where Complaint_id='%s'" %(Reply,id)
		update(q)
		flash("updated")
		return redirect(url_for('admin.adminviewcomplaints'))
	return render_template('admin_send_reply.html')

@admin.route('/admin_view_request',methods=['get','post'])
def admin_view_request():
	data={}
	id=request.args['id']
	q="SELECT * FROM request INNER JOIN trips ON `request`.`Trip_id`=`trips`.`Trips_id` INNER JOIN userregistration ON `request`.`User_id`=`userregistration`.`user_id` where Trip_id='%s'"%(id)
	print(q)
	res=select(q)
	print(res)
	data['rqt']=res
	return render_template('admin_view_request.html',data=data)

@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	id=request.args['id']
	q="SELECT * FROM feedback INNER JOIN trips ON `feedback`.`Trip_id`=`trips`.`Trips_id` INNER JOIN userregistration ON `feedback`.`User_id`=`userregistration`.`user_id` where Trip_id='%s'"%(id)
	print(q)
	res=select(q)
	data['fdb']=res
	print(res)
	return render_template('admin_view_feedback.html',data=data)

@admin.route('/admin_view_image',methods=['get','post'])
def admin_view_image():
	data={}
	id=request.args['id']
	q="SELECT place FROM `trips` where Trips_id='%s'"%(id)
	res=select(q)
	data['name']=res[0]['place']
	q="SELECT * FROM  files where Trip_id='%s'"%(id)
	print(q)
	res=select(q)
	data['img']=res
	print(res)
	return render_template('admin_view_image.html',data=data)
