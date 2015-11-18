import re
from .course import course

class user:
	def __init__(self, core, homeContents):
		self.core = core
		self.homeContents = homeContents
		
		self.courses = self._createCourses()
	
	def _createCourses(self):
		courses = []
		
		for item in re.finditer('<tr class="center" bgcolor="(.*?)">(.*?)<\/tr>', self.homeContents, re.S):
			if re.search(r'<td align="left">(.*?)(&nbsp;|&bbsp;)<br>(.*?)<a href="mailto:(.*?)">(.*?)<\/a><\/td>', item.groups()[1], re.S):
				courses.append(course(self.core, item.groups()[1]))
		
		return courses
	
	def getName(self):
		#get the name in format "Last, First Middle" from the page's html
		name = re.search(r'<h1>Grades and Attendance: (.*?)</h1>', self.homeContents, re.S).groups()[0].strip()
		
		#get the last name
		lastName = re.search(r'(.*), ', name).groups()[0].strip()
		
		#get the first name by removing the last name from the 'name' string
		firstName = re.sub(r'(.*), ', '', name)
		
		#concatenate the first and last names
		name = firstName + " " + lastName
		
		#return the name in the format "First Middle Last"
		return name
	
	def getSchoolDistrictName(self):
		name = re.search(r'<div id="print-school">(.*?)<br>', self.homeContents, re.S)
		
		return name.groups()[0].strip()
		
	def getSchoolName(self):
		name = re.search(r'<div id="print-school">.*?<br><span>(.*?)</span></div>', self.homeContents, re.S)
		
		return name.groups()[0].strip()
	
	def getUserName(self):
		name = re.search(r'<li id="userName" .*?<span>(.*?)<\/span>', self.homeContents, re.S)
		
		return name.groups()[0].strip()
	
	def getCourses(self):
		return self.courses
