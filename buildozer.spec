[app]

# (str) Title of your application
title = Screen Streamer

# (str) Package name
package.name = screenstreamer

# (str) Package domain (needed for android packaging)
package.domain = org.stream

# (str) Application versioning (version or version.regex)
version = 0.1

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (optional)
source.dir = .

# (list) Application requirements
# Specify Python dependencies here
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (list) The android api to target
android.api = 33

# (list) The android minimum API to use
android.minapi = 21
