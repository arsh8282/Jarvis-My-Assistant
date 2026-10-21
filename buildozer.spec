[app]  
title = JARVIS AI  
package.name = jarvisai  
package.domain = org.jarvis  
  
# All app code is inside the jarvis folder  
source.dir = jarvis  
source.include_exts = py,png,jpg,kv,atlas,ttf,json,sql  
  
version = 1.1.0  
  
requirements = python3==3.12.10,kivy==2.3.0,requests,urllib3,charset-normalizer,idna,certifi,pillow,pyjnius,android  
  
orientation = portrait  
fullscreen = 0  
android.presplash_color = #070B19  
  
# Permissions required for Android 14 (API 34) and Android 15 (API 35)  
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE,FOREGROUND_SERVICE_SPECIAL_USE,FOREGROUND_SERVICE_MEDIA_PROJECTION,FOREGROUND_SERVICE_MICROPHONE,POST_NOTIFICATIONS,QUERY_ALL_PACKAGES  
  
# Target Android 15 (API 35) with backward compatibility down to Android 8.0 (API 26)  
android.api = 35  
android.minapi = 26  
android.ndk = 25b  
android.accept_sdk_license = True  
android.archs = arm64-v8a, armeabi-v7a  
android.allow_backup = False  
  
# Include custom Java helper classes inside jarvis/android_src  
android.add_src = jarvis/android_src  
  
# Enable AndroidX required for modern notifications and core libraries  
android.enable_androidx = True  
p4a.bootstrap = sdl2
p4a.branch = master  
  
[buildozer]  
log_level = 2  
warn_on_root = 1  
  