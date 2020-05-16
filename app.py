from selenium import webdriver 
import time
from time import sleep 
from selenium.webdriver.common.keys import Keys


class omegle():
	def __init__(self, interests, chromedriver, headless = False):

		self.driver = webdriver.Chrome(chromedriver) 
		self.driver.get('https://www.omegle.com/')  
		  
		interest = self.driver.find_element_by_class_name('newtopicinput')

		for i in interests:
			interest.send_keys(i)
			interest.send_keys(Keys.RETURN)

		sleep(1)

		self.driver.find_element_by_xpath('//*[@id="textbtn"]').click()

		sleep(1)

		try:
			if self.driver.find_element_by_class_name("statuslog").text != None:
				print('connected ....!')
		except:
			sleep(0.5)
			pass
		self.screen = 0

	def getChat(self):
		r = []

		while True:
			try:
				texts = self.driver.find_elements_by_xpath("//p[@class='strangermsg']")
				
				for x in texts:
					# print(x.text)
					r.append(x.text)
				break
			except:
				sleep(1)

		return r

	def sendChat(self, key = 'hello !'):
		try:
			send = self.driver.find_element_by_class_name('chatmsg')
			send.send_keys(key)
			send.send_keys(Keys.RETURN)
		except:
			print('fail')
			pass
		return

	def newChat(self):
		try:
			dis = self.driver.find_element_by_xpath("//button[@class='disconnectbtn']")
			dis.click()
			dis.click()
			dis.click()
		except:
			print('failed exiting !')

	def checkChat(self):
		try:
			new = self.driver.find_element_by_class_name("newchatbtnwrapper")
			dis = self.driver.find_element_by_xpath("//button[@class='disconnectbtn']")
			self.driver.save_screenshot(f'./omg/screenie{self.screen}.png')
			self.screen += 1
			dis.click()
			print('new chat !')
			return True
		except:
			# print('failed new chat')
			pass
		return False

	def reChat(self):
		try:
			self.driver.find_element_by_class_name("recaptcha-checkbox-border").click()
		except:
			print('failed recapta')

interests = ['NY', 'italy', 'movies', 'justin beiber', 'netflix', 'money hiest', 'iron man', 'marvel','cap','india','mumbai']
omg = omegle(interests = interests, chromedriver = './chromedriver')



from chatt import Tron

tron = Tron()
	
r,s = [0,0]
o = 0
while True:
	
	if r == 0 and s == 0:
		s += 1
		omg.sendChat()

	sleep(1)

	rl = omg.getChat()

	if len(rl) > o:
	
		try:
			text = rl[-1]
			r+=1
		except:
			r = 0
			s = 0
			sleep(1)
			continue
		o = len(rl)

		text = list(text.split(':'))
		text = text[-1]
		print("stranger : ",text)
		st = tron.reply(text)
		st = str(st)
		print(st)
		omg.sendChat(key = st)
		s += 1

	print(f"sent : {s}, recieved : {r}, lenr : {len(rl)}, o : {o}")
	status = omg.checkChat()

	if status:
		s,r,o = 0,0,0
