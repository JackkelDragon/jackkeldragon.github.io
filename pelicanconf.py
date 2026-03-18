AUTHOR = 'Jackkel Dragon'
SITENAME = "<img src=\"/images/jackkel website logo v2.png\" alt=\"Jackkel Dragon's Workshop\">" ## "Jackkel Dragon's Workshop"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Books2Read", "https://books2read.com/ap/n4pgpK/"),
    ("Steam Games", "https://store.steampowered.com/developer/NightshadeDev"),
    ("itch.io  Games", "https://jackkel-dragon.itch.io/"),
)

# Social widget
SOCIAL = (
    ("Bluesky", "https://bsky.app/profile/jackkel-dragon.bsky.social"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'archives', 'tags']
INDEX_SAVE_AS = 'updates.html'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['images', "theme/css"]
CSS_FILE = "custom.css"

MENUITEMS = [("Home", "../index"), ("Nightshade", "../nightshade"), ("Kigenishi", "../kigenishi"), ("Tarishu", "../tarishu"), ("Standalone", "../standalone"), ("Fanworks", "../fanworks")]
MENUITEMS.append(("Streaming/Presskits", "../streaming_guidelines"))
MENUITEMS.append(("Art References", "../character-references"))
MENUITEMS.append(("Archives", "../archives"))
MENUITEMS.append(("Tags", "../tags"))
MENUITEMS.append(("Updates", "../updates"))

RELATIVE_URLS = False ## this broke some stuff when true
DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = PAGE_SAVE_AS = '{category}/{slug}.html' #'pages/{slug}.html'

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
}

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': '' ## no title for TOC ### invoke with a line that only says [TOC]
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

## https://github.com/pelican-plugins/markdown-include
MD_INCLUDE_BASE_PATH = "content/includes/"
## syntax: {!filename!}