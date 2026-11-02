[app]

# (str) Title of your application
title = Bursa Ezan Vakti

# (str) Package name
package.name = bursaezan

# (str) Package domain (needed for android packaging)
package.domain = org.bursa

# (list) Source files (letting it default will include all files in the directory)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Supported orientations
orientation = portrait
