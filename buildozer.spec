[app]
title = Jivory
package.name = jivory
package.domain = org.jivory
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1

# Requirements: ordinati e completi
requirements = python3,cython,kivy,kivymd,pillow,requests,urllib3,certifi,chardet,idna,setuptools,wheel

orientation = portrait

# Android API settings
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

# Usa la branch stabile di python-for-android
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Percorsi collegati alle variabili d'ambiente del workflow
android.sdk_path = $ANDROIDSDK
android.ndk_path = $ANDROIDNDK
