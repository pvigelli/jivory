[app]
title = Jivory
package.name = jivory
package.domain = org.jivory
source.dir = .
source.include_exts = py,png,jpg,json,kv
version = 0.1
requirements = python3,cython,kivy,kivymd
orientation = portrait
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2

[android]
android.sdk_path = $ANDROIDSDK
android.ndk_path = $ANDROIDNDK