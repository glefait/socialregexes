#!/usr/bin/env python3
import re
import sys
import argparse


definitions = {
	'email': re.compile(r'^(?:mailto:)?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-_]+\.[a-zA-Z0-9-.]+)$'),
	'phone': re.compile(r'^(?:tel|phone|mobile):(\+?[0-9. -]+)$'),
	'twitter': re.compile(r'^https?://(?:(?:www|mobile)\.)?twitter\.com/(?:#!/)?@?([a-zA-Z0-9_]+)/?$'),
	'facebook': re.compile(r'^https?://(?:www\.|[a-z]{2}-[a-z]{2}\.)?facebook\.com/(?:(?:profile\.php\?id=)?([0-9]+)|([a-zA-Z0-9.]+))(?:/#)?(?:\?.*)?$'),
	'github': re.compile(r'^https?://(?:www\.)?github.com/([a-zA-Z0-9-]+)/?$'),
	'stackoverflow': re.compile(r'^https?://(?:www\.)?stackoverflow\.com/users/([0-9]+)/'),
	'stackexchange': re.compile(r'^https?://(?:www\.)?stackexchange\.com/users/([0-9]+)/'),
	'serverfault': re.compile(r'^https?://(?:www\.)?serverfault\.com/users/([0-9]+)/'),
	'superuser': re.compile(r'^https?://(?:www\.)?superuser\.com/users/([0-9]+)/'),
	'askubuntu': re.compile(r'^https?://(?:www\.)?askubuntu\.com/users/([0-9]+)/'),
	'mathoverflow': re.compile(r'^https?://(?:www\.)?mathoverflow\.net/users/([0-9]+)/'),
	'pt.stackoverflow': re.compile(r'^https?://pt\.stackoverflow\.com/users/([0-9]+)/'),
	'ja.stackoverflow': re.compile(r'^https?://ja\.stackexchange\.com/users/([0-9]+)/'),
	'ru.stackoverflow': re.compile(r'^https?://ru\.stackexchange\.com/users/([0-9]+)/'),
	'es.stackoverflow': re.compile(r'^https?://es\.stackexchange\.com/users/([0-9]+)/'),
	'linkedin':  re.compile(r'^https?://(?:(?:www|mobile|[a-z]{2})\.)?linkedin\.com/(?:(?:in/([a-zA-Z0-9_-]+))|(?:pub/([a-zA-Z0-9-]+(?:/[a-zA-Z0-9]+){3}))|profile/view\?id=([0-9]+))[/&]?$'),
	'instagram': re.compile(r'^https?://(?:www\.)?instagram\.com/([a-zA-Z0-9_]+)$'),
	'googleplus': re.compile(r'^https?://(?:plus\.google\.com/(?:([0-9]+)|(?:u/0/)?((?:\+[a-zA-Z0-9.]+)|[0-9]+))|(?:www\.)?google.com/profiles/([a-zA-Z0-9.]+)|profiles\.google\.com/([a-zA-Z0-9.]+)|(?:www\.)?google\.com/[+]([a-zA-Z0-9.]+))(?:/(?:about)?)?$'),
	'pinterest': re.compile(r'^https?://(?:(?:www|[a-z]{2})\.)?pinterest\.com/([a-zA-Z0-9_]+)/?$'),
	'skype': re.compile(r'^skype:([a-zA-Z0-9_]+)(\?call)?$'),
	'youtube': re.compile(r'^https?://(?:www\.)?youtube\.com\/user/(?:\w+/)?([a-zA-Z0-9_-]+)$'),
	'vine': re.compile(r'^https?://(?:www\.)?vine\.co/(?:u/([0-9]+)|([a-zA-Z0-9._-]+))$'),

	'bitbucket': re.compile(r'^https?://bitbucket\.org/([^/]+)/?$'),
	'stackoverflow_cv': re.compile(r'^https?://(?:careers.stackoverflow.com/(?:cv/)?|stackoverflow.com/cv/)([^/]+)$'),
	'amazon': re.compile(r'^https?://(?:amzn\.com/w/([^/]+)$|www\.amazon\.com/gp/registry/wishlist/([^/]+)/)'),
	'paypal': re.compile(r'^https?://www.paypal.me/([a-zA-Z0-9]+)'),

	'lastfm': re.compile(r'^https?://www.last.fm/user/([a-zA-Z0-9.]+)/?$'),
	'flickr': re.compile(r'^https?://www.flickr.com/photos/([a-zA-Z0-9.]+)/?$'),
	'aboutme': re.compile(r'^https?://about\.me/([a-zA-Z0-9._]+)#?(?:/(?:bio)?)?$'),

	'wordpress': re.compile(r'^https?://([^.]+)\.wordpress\.com/$'),
	'xing': re.compile(r'^https?://www\.xing\.com/profile/([^/]+)$'),
	'reddit': re.compile(r'^https?://www.reddit.com/user/([^/]+)$'),
	'hackernewsers': re.compile(r'^https?://hackernewsers.com/users/(.*?)\.html'),

	'microsot_mvp': re.compile(r'^https?://mvp\.support\.microsoft\.com/profile/([a-zA-Z.]+)'),

	'scoop': re.compile(r'^https?://www\.scoop\.it/u/([^/]+)$'),
	'upwork': re.compile(r'^https?://www\.upwork\.com/(?:freelancers/|o/profiles/users/_)~([^/?]+)$'),
	'odesk': re.compile(r'^https?://www\.odesk\.com/users/~~([^/?]+)$'),
	'ohloh': re.compile(r'^https?://www\.ohloh\.net/accounts/([0-9]+)(?:\?ref=Detailed)?$'),
	'codementor': re.compile(r'^https?://www.codementor.io/([a-zA-Z0-9]+)(?:\?[^/]+)?$'),
	'sourceforge': re.compile(r'^https?://sourceforge\.net/users/([^/]+)$'),
	'soundcloud': re.compile(r'^https?://soundcloud\.com/([a-zA-Z0-9-]+)$'),
	'rubygems': re.compile(r'^https?://rubygems\.org/profiles/([^/]+)$'),
	'magentocommerce': re.compile(r'^https?://magentocommerce\.com/certification/directory/dev/([0-9]+)/'),
	'msdn': re.compile(r'^https?://social\.msdn\.microsoft\.com/profile/([^/]+)/?$'),

	'googleplay': re.compile(r'^https?://play\.google\.com/store/apps/developer\?id=([^/]+)$'),
	'coderwall': re.compile(r'^https?://coderwall\.com/([^/]+)$'),
	'medium': re.compile(r'^https?://medium.com/@([^/]+)/?$'),
	'github_gist': re.compile(r'^https?://gist\.github\.com/([^/]+)$'),
	'launchpad': re.compile(r'^https?://launchpad\.net/~([^/]+)$'),
	'android': re.compile(r'^https?://market\.android\.com/developer\?pub=([^/]+)$'),
	'ycombinator': re.compile(r'^https?://news\.ycombinator\.com/user\?id=([^/]+)$'),

	'pinboard': re.compile(r'^https?://pinboard\.in/u:([^/]+)$'),

	'feedburner': re.compile(r'^https?://feeds\.feedburner\.com/([a-zA-Z0-9]+)$'),
	'blogger': re.compile(r'^https?://www\.blogger\.com/profile/([0-9]+)$'),
	'slideshare': re.compile(r'^https?://www\.slideshare\.net/([^/]+)$'),
	#paypal': re.compile('^https?:// ([]+)'),
	#paypal': re.compile('^https?:// ([]+)'),
}

for sub in ("meta.", "webapps.", "gaming.", "webmasters.", "cooking.", "gamedev.", "photo.", "stats.", "math.", "diy.", "gis.", "tex.", "money.", "english.", "ux.", "unix.", "wordpress.", "cstheory.", "apple.", "rpg.", "bicycles.", "softwareengineering.", "electronics.", "android.", "boardgames.", "physics.", "homebrew.", "security.", "writers.", "video.", "graphicdesign.", "dba.", "scifi.", "codereview.", "codegolf.", "quant.", "pm.", "skeptics.", "fitness.", "drupal.", "mechanics.", "parenting.", "sharepoint.", "music.", "sqa.", "judaism.", "german.", "japanese.", "philosophy.", "gardening.", "travel.", "productivity.", "crypto.", "dsp.", "french.", "christianity.", "bitcoin.", "linguistics.", "hermeneutics.", "history.", "bricks.", "spanish.", "scicomp.", "movies.", "chinese.", "biology.", "poker.", "mathematica.", "cogsci.", "outdoors.", "martialarts.", "sports.", "academia.", "cs.", "workplace.", "windowsphone.", "chemistry.", "chess.", "raspberrypi.", "russian.", "islam.", "salesforce.", "patents.", "genealogy.", "robotics.", "expressionengine.", "politics.", "anime.", "magento.", "ell.", "sustainability.", "tridion.", "reverseengineering.", "networkengineering.", "opendata.", "freelancing.", "blender.", "space.", "sound.", "astronomy.", "tor.", "pets.", "ham.", "italian.", "aviation.", "ebooks.", "alcohol.", "softwarerecs.", "arduino.", "expatriates.", "matheducators.", "earthscience.", "joomla.", "datascience.", "puzzling.", "craftcms.", "buddhism.", "hinduism.", "communitybuilding.", "startups.", "worldbuilding.", "emacs.", "hsm.", "economics.", "lifehacks.", "engineering.", "coffee.", "vi.", "musicfans.", "woodworking.", "civicrm.", "health.", "rus.", "mythology.", "law.", "opensource.", "elementaryos.", "portuguese.", "computergraphics.", "hardwarerecs.", "3dprinting.", "ethereum.", "latin.", "languagelearning.", "retrocomputing.", "crafts.", "korean.", "monero.", "ai.", "esperanto.", "sitecore.", "iot.", "literature.", "vegetarianism."):
	definitions[sub + "stackexchange"] = re.compile(r'^https?://'+sub+'stackexchange.com/users/([0-9]+)/')

filters = {
	'twitter': re.compile('twitter.com/(?:tos|about|share)$'),
	'facebook': re.compile('facebook.com/(?:intl|help|policies|profile/|find-friend|privacy|campaign|page|bookmark|groups|settings|messages|permalink|share)'),
	'github': re.compile(r'github.com/(?:pulls|issues|blog|new|watching|site|security|contact|about|explore|integrations|settings|notifications|search(?:\?.*)?)$'),

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
