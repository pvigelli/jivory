[app]
# Informazioni sull'app
title = Jivory
package.name = jivory
package.domain = org.jivory
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1

# Requisiti: ordinati e completi
requirements = python3,cython,kivy,kivymd,pillow,requests,urllib3,certifi,chardet,idna,setuptools,wheel

# Orientamento
orientation = portrait

# Android settings
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

# Forziamo i percorsi SDK/NDK (quelli installati da GitHub Actions)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /home/runner/android-ndk-r25b
android.ndk_api = 21

# Specifica il bootstrap stabile (SDL2)
p4a.bootstrap = sdl2
p4a.branch = stable

# Architetture supportate
android.archs = arm64-v8a, armeabi-v7a

# Forza output APK (non AAB)
package_format = apk

[buildozer]
log_level = 2
warn_on_root = 1
