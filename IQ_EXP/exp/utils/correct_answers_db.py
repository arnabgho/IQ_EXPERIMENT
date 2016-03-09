#
import os
import re
from exp.models import Correct_Answers

pwd=os.getcwd()

with open(pwd+'/exp/static/exp/correct_option_numbers.txt') as ins:
	for line in ins:
		match=re.search(r'(\w+):(\w+)',line)
		question=match.group(1)
		answer=int(match.group(2))
		ca=Correct_Answers(question=question,answer=answer)
		ca.save()