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
android.api = 31
android.minapi = 21
android.accept_sdk_license = True

# Forziamo i percorsi SDK/NDK
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/21.4.7075529

# Specifica il bootstrap stabile (SDL2)
p4a.bootstrap = sdl2
p4a.branch = stable

# Architetture supportate
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

