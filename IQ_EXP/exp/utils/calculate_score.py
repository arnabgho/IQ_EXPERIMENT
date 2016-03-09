# from .. import models
from ..models import Correct_Answers , Response ,Scores
import datetime

def calc_score(response_dict,set_id):
	num_admin=0
	date=datetime.datetime.now().date().isoformat()
	try:		
		name=response_dict['name'][0]
		age=int(response_dict['age'][0])
		class_id=int(response_dict['class_id'][0])
		# set_id=int(response_dict['set_id'][0])

	except:
		print("Data not entered correctly")
		return -1
	else:
		print("Data entered correctly")
		ans_ins=[]
		num_correct=0
		for key in response_dict.keys():

			if(key.startswith("admin")):
				num_admin+=1
				try:
					c_ans=Correct_Answers.objects.get(question=key)
					ans=c_ans.answer
				except Correct_Answers.DoesNotExist:
					print "Data Not Present in Correct_Answers"
				else:
					print "Data found in database"
				finally:
					ans_ins.append(Response(name=name,date=date,age=age,class_id=class_id,set_id=set_id,question=key,answer=ans))
					if int(response_dict[key][0])==ans:
						num_correct+=1
		if num_admin!=12:
			print "Data not correctly entered"
			return -1
		else:
			#Insert into the database	
			# print "Hello\n"				
			for res in ans_ins:
				res.save()
			score=Scores(name=name,date=date,age=age,class_id=class_id,set_id=set_id,score=num_correct)	
			score.save()
			return num_correct	