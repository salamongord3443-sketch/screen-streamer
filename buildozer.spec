[app]

title = Screen Streamer
package.name = screenstreamer
package.domain = org.stream
version = 0.1

source.include_exts = py,png,jpg,kv,atlas
source.dir = .

requirements = python3,kivy,pyjnius

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
