from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import UbuntuCorpusTrainer

# bot = ChatBot('Norman')
class Tron():
	def __init__(self):

		self.bot = ChatBot(
			'Norman',
			storage_adapter='chatterbot.storage.SQLStorageAdapter',
			logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'],
			database_uri='sqlite:///database.sqlite3'
		)

		trainer = ChatterBotCorpusTrainer(self.bot)
		trainer.train("chatterbot.corpus.english")
		trainer.train("chatterbot.corpus.english.greetings")
		trainer.train("chatterbot.corpus.english.conversations")

	# trainer = UbuntuCorpusTrainer(bot)
	# trainer.train()

	def reply(self, msg):
		if msg:
			bot_out = self.bot.get_response(msg)
			return bot_out


	
# agent = Tron()
# while True:
# 	inp = input("mark here.")
# 	t = agent.reply(inp)
# 	print(t,type(t))
# 	s = str(t)
# 	p = string(t)
# 	print(s, type(s),type(p))

	