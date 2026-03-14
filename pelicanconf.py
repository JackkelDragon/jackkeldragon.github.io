AUTHOR = 'Jackkel Dragon'
SITENAME = "Jackkel Dragon's Workshop"
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
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'archives']
INDEX_SAVE_AS = 'updates.html'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['images', "theme/css"]
CSS_FILE = "custom.css"

MENUITEMS = [("Home", "index"), ("Nightshade", "nightshade"), ("Kigenishi", "kigenishi"), ("Tarishu", "tarishu"), ("Standalone", ""), ("Fanworks", "fanworks")]
MENUITEMS.append(("Streaming Guidelines", "streaming_guidelines"))
MENUITEMS.append(("Art References", "character_references"))
MENUITEMS.append(("Updates", "updates"))

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

## https://github.com/pelican-plugins/markdown-include
MD_INCLUDE_BASE_PATH = "content/includes/"
## syntax: {!filename!}