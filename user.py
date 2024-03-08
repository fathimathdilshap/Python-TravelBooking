from public import *
from database import *
import uuid

  
user=Blueprint('user',__name__)


@user.route('/userhome')
def userhome():
	return render_template("userhome.html")

@user.route('/user_manage_trips',methods=['get','post'])
def user_manage_trips():
	uid=session['user_id']
	data={}
	q="SELECT * FROM trips where User_id='%s'"%(uid)
	res=select(q)
	print(res)
	data['user']=res
	user_id=session['user_id']
	if 'Submit' in request.form:
		Place=request.form['Place']
		Vehicle=request.form['Vehicle']
		Description=request.form['Description']
		Tripstartdate=request.form['Tripstartdate']
		Tripenddate=request.form['Tripenddate']
		Starttime=request.form['Starttime']
		StartPlace=request.form['StartPlace']

		q="insert into trips values(null,'%s','%s','%s','%s','%s','%s','%s','%s')" %(user_id,Place,Vehicle,Description,Tripstartdate,Tripenddate,Starttime,StartPlace)
		insert(q)
		return redirect(url_for('user.user_manage_trips'))
	return render_template("user_manage_trips.html",data=data)

@user.route('/user_view_trips',methods=['get','post'])
def user_view_trips():
	uid=session['user_id']
	data={}
	q="SELECT * FROM trips inner join userregistration using(user_id) where user_id!='%s'"%(uid)
	res=select(q)
	print(res)
	data['user']=res
	if 'action' in request.args:
		action=request.args['action']
		tid=request.args['tid']
		print(action,tid)
	else:
		action=None
	if action=='request':
		q="insert into request values(null,'%s','%s','pending',NOW())"%(tid,uid)
		insert(q)

	return render_template('user_view_trips.html',data=data)

@user.route('/user_view_trips_request',methods=['get','post'])
def user_view_trips_request():
	tid=request.args['tid']
	data={}
	data['tid']=tid
	q="select *,`request`.`Status` AS rstatus from request inner join userregistration on(request.User_id=userregistration.user_id) where Trip_id='%s'"%(tid)
	res=select(q)
	data['user']=res

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=="accept":
		q="update request set Status='Accept' where Request_id='%s'"%(rid)
		update(q)
		return redirect(url_for('user.user_view_trips_request',tid=tid))
	if action=="reject":
		q="update request set Status='reject' where Request_id='%s'"%(rid)
		update(q)
		return redirect(url_for('user.user_view_trips_request',tid=tid))
	return render_template('user_view_trips_request.html',data=data)


@user.route('/user_add_image',methods=['get','post'])
def user_add_image():
	tid=request.args['tid']
	data={}
	if 'Submit' in request.form:
		f=request.files['File']
		path="static/"+str(uuid.uuid4())+f.filename
		f.save(path)
		q="insert into files values(null,'%s','%s',curdate())"%(tid,path)
		insert(q)
	return render_template('user_add_image.html',data=data)



@user.route('/user_view_feedback',methods=['get','post'])
def user_view_feedback():
	data={}
	tid=request.args['tid']
	q="select * from feedback inner join userregistration on(feedback.User_id=userregistration.user_id) where Trip_id='%s'"%(tid)
	print(q)
	print(q)
	res=select(q)
	print(res)
	data['feedback']=res
	return render_template('user_view_feedback.html',data=data)

@user.route('/user_view_req_status',methods=['get','post'])
def user_view_req_status():
	data={}
	uid=session['user_id']
	q="SELECT * FROM `userregistration` INNER JOIN request ON `request`.`User_id`=`userregistration`.`user_id` INNER JOIN trips ON(trips.Trips_id=request.Trip_id) WHERE `request`.`User_id`='%s' "%(uid)
	print(q)
	res=select(q)
	data['rqt']=res
	print(res)
	return render_template('user_view_req_status.html',data=data)


	
@user.route('/user_add_images',methods=['get','post'])
def user_add_images():
	data={}
	if 'Submit' in request.form:
		f=request.files['File']
		tid=request.args['tid']
		path="static/"+str(uuid.uuid4())+f.filename
		f.save(path)
		q="insert into files values(null,'%s','%s',curdate())"%(tid,path)
		insert(q)
	return render_template('user_add_images.html',data=data)


@user.route('/user_add_feedback',methods=['get','post'])
def user_add_feedback():
	tid=request.args['tid']
	uid=session['user_id']
	data={}
	if 'Send' in request.form:
		f=request.form['Feedback']
		
		q="insert into feedback values(null,'%s','%s','%s',curdate())"%(tid,uid,f)
		insert(q)
		flash("Add Feedback")
	return render_template('user_add_feedback.html',data=data)


@user.route('/user_send_complaint',methods=['get','post'])
def user_send_complaint():
	data={}
	uid=session['user_id']

	if 'Send' in request.form:
		complaint=request.form['Complaint']
		q="insert into complaint values(null,'%s','%s','pending',curdate())" %(uid,complaint)
		insert(q)
		flash("sended")
		return redirect(url_for('user.user_send_complaint'))


	q="select * from complaint where user_id='%s'"%(uid)
	res=select(q)
	data['complaint']=res
	return render_template('user_send_complaint.html',data=data)


@user.route('/user_viewplannerinfo',methods=['get','post'])
def user_viewplannerinfo():
	pid=request.args['pid']
	data={}
	data['pid']=pid
	q="select * from userregistration where User_id='%s'"%(pid)
	print(q)
	res=select(q)
	data['user']=res

	
	return render_template('user_viewplannerinfo.html',data=data)



@user.route('user_chat',methods=['get','post'])
def user_chat():
	data={}
	uid=session['user_id']
	data['uid']=uid
	opuid=request.args['uid']
	q="select * from chat where sender_id='%s' and Receiver='%s' or sender_id='%s' and Receiver='%s'"%(uid,opuid,opuid,uid)
	data['chat']=select(q)
	print(q)
	print(data['chat'])
	q="select * from userregistration where user_id='%s'"%(opuid)
	res=select(q)
	data['opuname']=res[0]['Firstname']
	if 'send' in request.form:
		msg=request.form['msg']
		q="insert into chat values(NULL,'%s','%s','%s',NOW())"%(uid,opuid,msg)
		insert(q)
		return redirect(url_for('user.user_chat',uid=opuid))
	return render_template('user_chat.html',data=data)



@user.route('user_view_chatted_users',methods=['get','post'])
def user_view_chatted_users():
	data={}
	uid=session['user_id']
	data['uid']=uid
	
	q="SELECT DISTINCT(Sender_id),`Firstname`  FROM chat INNER JOIN userregistration ON(chat.Sender_id=`userregistration`.`user_id`) WHERE `Receiver`='%s'"%(uid)
	res=select(q)
	print(res)
	data['user']=res
	# print(data['chat'])
	# q="select * from userregistration where user_id='%s'"%(opuid)
	# res=select(q)
	# data['opuname']=res[0]['Firstname']
	# if 'send' in request.form:
	# 	msg=request.form['msg']
	# 	q="insert into chat values(NULL,'%s','%s','%s',NOW())"%(uid,opuid,msg)
	# 	insert(q)
	# 	return redirect(url_for('user.user_view_chatted_users',uid=opuid))
	return render_template('user_view_chatted_users.html',data=data)