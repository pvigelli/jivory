[app]
# Informazioni sull'app
title = Jivory
package.name = jivory
package.domain = org.jivory
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1

# Requisiti
requirements = python3,cython,kivy,kivymd,pillow,requests,urllib3,certifi,chardet,idna,setuptools,wheel

# Orientamento
orientation = portrait

# Android settings
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

# Bootstrap stabile
p4a.bootstrap = sdl2
p4a.branch = stable

# Architetture supportate
android.archs = arm64-v8a, armeabi-v7a

# Percorsi SDK/NDK (coerenti col workflow)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /home/runner/android-ndk-r25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
