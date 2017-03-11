#!/usr/bin/env python3
import re
import sys
import argparse


definitions = {
	'email': re.compile('^([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-_]+\.[a-zA-Z0-9-.]+)$'),
	'twitter': re.compile('^https?://(?:(?:www|mobile)\.)?twitter\.com/(?:#!/)?@?([a-zA-Z0-9_]+)/?$'),
	'facebook': re.compile('^https?://(?:www\.|[a-z]{2}-[a-z]{2}\.)?facebook\.com/(?:(?:profile\.php\?id=)?([0-9]+)|([a-zA-Z0-9.]+))(?:/#)?(?:\?.*)?$'),
	'github': re.compile('https?://(?:www\.)?github.com/([a-zA-Z0-9-]+)/?$'),
	'stackoverflow': re.compile('https?://(?:www\.)?stackoverflow\.com/users/([0-9]+)/'),
	'stackexchange': re.compile('https?://(?:www\.)?stackexchange\.com/users/([0-9]+)/'),
	'serverfault': re.compile('https?://(?:www\.)?serverfault\.com/users/([0-9]+)/'),
	'superuser': re.compile('https?://(?:www\.)?superuser\.com/users/([0-9]+)/'),
	'askubuntu': re.compile('https?://(?:www\.)?askubuntu\.com/users/([0-9]+)/'),
	'mathoverflow': re.compile('https?://(?:www\.)?mathoverflow\.net/users/([0-9]+)/'),
	'pt.stackoverflow': re.compile('https?://pt\.stackoverflow\.com/users/([0-9]+)/'),
	'ja.stackoverflow': re.compile('https?://ja\.stackexchange\.com/users/([0-9]+)/'),
	'ru.stackoverflow': re.compile('https?://ru\.stackexchange\.com/users/([0-9]+)/'),
	'es.stackoverflow': re.compile('https?://es\.stackexchange\.com/users/([0-9]+)/'),
	'linkedin':  re.compile('^https?://(?:(?:www|mobile|[a-z]{2})\.)?linkedin\.com/(?:(?:in/([a-zA-Z0-9_-]+))|(?:pub/([a-zA-Z0-9-]+(?:/[a-zA-Z0-9]+){3}))|profile/view\?id=([0-9]+))[/&]?$'),
	'instagram': re.compile('^https?://(?:www\.)?instagram\.com/([a-zA-Z0-9_]+)$'),
	'googleplus': re.compile('^https?://(?:plus\.google\.com/(?:([0-9]+)|(?:u/0/)?((?:\+[a-zA-Z0-9.]+)|[0-9]+))|(?:www\.)?google.com/profiles/([a-zA-Z0-9.]+)|profiles\.google\.com/([a-zA-Z0-9.]+)|(?:www\.)?google\.com/[+]([a-zA-Z0-9.]+))(?:/(?:about)?)?$'),
	'pinterest': re.compile('^https?://(?:(?:www|[a-z]{2})\.)?pinterest\.com\/([a-zA-Z0-9_]+)/?$'),
	'skype': re.compile('^skype:([a-zA-Z0-9_]+)(\?call)?$'),
	'youtube': re.compile('^https?://(?:www\.)?youtube\.com\/user/(?:\w+/)?([a-zA-Z0-9_-]+)$'),
	'vine': re.compile('^https?://(?:www\.)?vine\.co/(?:u/([0-9]+)|([a-zA-Z0-9._-]+))$'),

	'bitbucket': re.compile('^https?://bitbucket\.org/([^/]+)/?$'),
	'stackoverflow_cv': re.compile('^https?://(?:careers.stackoverflow.com/(?:cv/)?|stackoverflow.com/cv/)([^/]+)$'),
	'amazon': re.compile('^https?://(?:amzn\.com/w/([^/]+)$|www\.amazon\.com/gp/registry/wishlist/([^/]+)/)'),
	'paypal': re.compile('^https?://www.paypal.me/([a-zA-Z0-9]+)'),

	'lastfm': re.compile('^https?://www.last.fm/user/([a-zA-Z0-9.]+)/?$'),
	'flickr': re.compile('^https?://www.flickr.com/photos/([a-zA-Z0-9.]+)/?$'),
	'aboutme': re.compile('^https?://about\.me/([a-zA-Z0-9._]+)#?(?:/(?:bio)?)?$'),

	'wordpress': re.compile('^https?://([^.]+)\.wordpress\.com/$'),
	'xing': re.compile('^https?://www\.xing\.com/profile/([^/]+)$'),
	'reddit': re.compile('^https?://www.reddit.com/user/([^/]+)$'),
	'hackernewsers': re.compile('^https?://hackernewsers.com/users/(.*?)\.html'),

	'microsot_mvp': re.compile('^https?://mvp\.support\.microsoft\.com/profile/([a-zA-Z.]+)'),

	'scoop': re.compile('^https?://www\.scoop\.it/u/([^/]+)$'),
	'upwork': re.compile('^https?://www\.upwork\.com/(?:freelancers/|o/profiles/users/_)~([^/?]+)$'),
	'odesk': re.compile('^https?://www\.odesk\.com/users/~~([^/?]+)$'),
	'ohloh': re.compile('^https?://www\.ohloh\.net/accounts/([0-9]+)(?:\?ref=Detailed)?$'),
	'codementor': re.compile('^https?://www.codementor.io/([a-zA-Z0-9]+)(?:\?[^/]+)?$'),
	'sourceforge': re.compile('^https?://sourceforge\.net/users/([^/]+)$'),
	'soundcloud': re.compile('^https?://soundcloud\.com/([a-zA-Z0-9-]+)$'),
	'rubygems': re.compile('^https?://rubygems\.org/profiles/([^/]+)$'),
	'magentocommerce': re.compile('^https?://magentocommerce\.com/certification/directory/dev/([0-9]+)/'),
	'msdn': re.compile('^https?://social\.msdn\.microsoft\.com/profile/([^/]+)/?$'),

	'googleplay': re.compile('^https?://play\.google\.com/store/apps/developer\?id=([^/]+)$'),
	'coderwall': re.compile('^https?://coderwall\.com/([^/]+)$'),
	'medium': re.compile('^https?://medium.com/@([^/]+)/?$'),
	'github_gist': re.compile('^https?://gist\.github\.com/([^/]+)$'),
	'launchpad': re.compile('^https?://launchpad\.net/~([^/]+)$'),
	'android': re.compile('^https?://market\.android\.com/developer\?pub=([^/]+)$'),
	'ycombinator': re.compile('^https?://news\.ycombinator\.com/user\?id=([^/]+)$'),
	#paypal': re.compile('^https?:// ([]+)'),
}

for sub in ("meta.", "webapps.", "gaming.", "webmasters.", "cooking.", "gamedev.", "photo.", "stats.", "math.", "diy.", "gis.", "tex.", "money.", "english.", "ux.", "unix.", "wordpress.", "cstheory.", "apple.", "rpg.", "bicycles.", "softwareengineering.", "electronics.", "android.", "boardgames.", "physics.", "homebrew.", "security.", "writers.", "video.", "graphicdesign.", "dba.", "scifi.", "codereview.", "codegolf.", "quant.", "pm.", "skeptics.", "fitness.", "drupal.", "mechanics.", "parenting.", "sharepoint.", "music.", "sqa.", "judaism.", "german.", "japanese.", "philosophy.", "gardening.", "travel.", "productivity.", "crypto.", "dsp.", "french.", "christianity.", "bitcoin.", "linguistics.", "hermeneutics.", "history.", "bricks.", "spanish.", "scicomp.", "movies.", "chinese.", "biology.", "poker.", "mathematica.", "cogsci.", "outdoors.", "martialarts.", "sports.", "academia.", "cs.", "workplace.", "windowsphone.", "chemistry.", "chess.", "raspberrypi.", "russian.", "islam.", "salesforce.", "patents.", "genealogy.", "robotics.", "expressionengine.", "politics.", "anime.", "magento.", "ell.", "sustainability.", "tridion.", "reverseengineering.", "networkengineering.", "opendata.", "freelancing.", "blender.", "space.", "sound.", "astronomy.", "tor.", "pets.", "ham.", "italian.", "aviation.", "ebooks.", "alcohol.", "softwarerecs.", "arduino.", "expatriates.", "matheducators.", "earthscience.", "joomla.", "datascience.", "puzzling.", "craftcms.", "buddhism.", "hinduism.", "communitybuilding.", "startups.", "worldbuilding.", "emacs.", "hsm.", "economics.", "lifehacks.", "engineering.", "coffee.", "vi.", "musicfans.", "woodworking.", "civicrm.", "health.", "rus.", "mythology.", "law.", "opensource.", "elementaryos.", "portuguese.", "computergraphics.", "hardwarerecs.", "3dprinting.", "ethereum.", "latin.", "languagelearning.", "retrocomputing.", "crafts.", "korean.", "monero.", "ai.", "esperanto.", "sitecore.", "iot.", "literature.", "vegetarianism."):
	definitions[sub + "stackexchange"] = re.compile('https?://'+sub+'stackexchange.com/users/([0-9]+)/')

filters = {
	'twitter': re.compile('twitter.com/(?:tos|about)$'),
	'facebook': re.compile('facebook.com/(?:intl|help|policies|profile/|find-friend|privacy|campaign|page|bookmark|groups|settings|messages|permalink)'),
	'github': re.compile('github.com/(?:pulls|issues|blog|new|watching|site|security|contact|about|explore|integrations|settings|notifications|search(?:\?.*)?)$'),

}

def identify(text):
	results = []
	for account in definitions:
		account_match = definitions[account].search(text)
		if account_match and (not account in filters or not filters[account].search(text)):
			the_value = next((item for item in account_match.groups() if item is not None), None)
			return account, the_value
	return None

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='print the social network and the user account identified on this/theses urls', nargs='+')
	args = parser.parse_args()

	for url in args.url:
		print(identify(url))