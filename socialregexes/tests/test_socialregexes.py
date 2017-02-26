from unittest import TestCase

import socialregexes

class TestSocialRegexes(TestCase):

	def test_twitter_true_positive(self):
		for link in ('https://twitter.com/guillem_lefait',
			'https://twitter.com/@guillem_lefait',
			'https://twitter.com/#!/guillem_lefait'):
			res = socialregexes.identify(link)
			self.assertTrue(not res is None and len(res) == 2)
			self.assertTrue(res[0] == 'twitter')
			self.assertTrue(res[1] == 'guillem_lefait')

	def test_twitter_true_negative(self):
		res = socialregexes.identify('https://twitter.com/tos')
		self.assertTrue(res is None)

	def test_email(self):
		res = socialregexes.identify('guillem.lefait@gmail.removemeobviously.com')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'email')
		self.assertTrue(res[1] == 'guillem.lefait@gmail.removemeobviously.com')

	def test_junk(self):
		res = socialregexes.identify('http://blabla.com/xyz')
		self.assertTrue(res is None )

	def test_facebook(self):
		for link in ('https://www.facebook.com/guillem.lefait',
			'https://fr-fr.facebook.com/guillem.lefait',
			'https://www.facebook.com/guillem.lefait?ref=br_rs'):
			res = socialregexes.identify(link)
			self.assertTrue(not res is None and len(res) == 2)
			self.assertTrue(res[0] == 'facebook')
			self.assertTrue(res[1] == 'guillem.lefait')
		res = socialregexes.identify('https://www.facebook.com/profile.php?id=654000317')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'facebook')
		self.assertTrue(res[1] == '654000317')

	def test_github_true_positive(self):
		res = socialregexes.identify('https://github.com/glefait')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'github')
		self.assertTrue(res[1] == 'glefait')

	def test_github_true_negative(self):
		res = socialregexes.identify('https://github.com/search')
		self.assertTrue(res is None)

	def test_stackoverflow(self):
		for link in ('http://stackoverflow.com/users/3090365/glefait',
			'http://stackoverflow.com/users/3090365/glefait?tab'):
			res = socialregexes.identify(link)
			self.assertTrue(not res is None and len(res) == 2)
			self.assertTrue(res[0] == 'stackoverflow')
			self.assertTrue(res[1] == '3090365')

	def test_linkedin(self):
		res = socialregexes.identify('https://www.linkedin.com/in/glefait/')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'linkedin')
		self.assertTrue(res[1] == 'glefait')

	def test_googleplus(self):
		res = socialregexes.identify('https://plus.google.com/u/0/+guillemlefait')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'googleplus')
		self.assertTrue(res[1] == '+guillemlefait')
		res = socialregexes.identify('https://plus.google.com/u/0/116882192944905398376')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'googleplus')
		self.assertTrue(res[1] == '116882192944905398376')

	def test_pinterest(self):
		res = socialregexes.identify('https://fr.pinterest.com/diceverywhere/')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'pinterest')
		self.assertTrue(res[1] == 'diceverywhere')

	def test_vine(self):
		res = socialregexes.identify('https://vine.co/LoganPaul')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'vine')
		self.assertTrue(res[1] == 'LoganPaul')
		res = socialregexes.identify('https://vine.co/u/940474327508377600')
		self.assertTrue(not res is None and len(res) == 2)
		self.assertTrue(res[0] == 'vine')
		self.assertTrue(res[1] == '940474327508377600')