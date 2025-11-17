[app]

# Title of your application
title = Maintenance App

# Package name
package.name = maintenanceapp

# Package domain
package.domain = org.test

# Source code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Requirements
requirements = python3,kivy,requests,opencv

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 1

# Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Storage
android.allow_backup = True
android.private_storage = True
android.copy_libs = 1

# --- FIXED SECTION ---
# Let Buildozer manage SDK/NDK paths automatically
# android.ndk_path =
# android.sdk_path =
# android.ant_path =

# Minimum Android API
android.minapi = 24

# Target Android API
android.api = 33

# Android NDK API
android.ndk_api = 24

# Bootstrap
p4a.bootstrap = sdl2

# Debug artifact format
android.debug_artifact = apk

# Accept SDK licenses automatically
android.accept_sdk_license = True

# --- Removed skip_update ---
# android.skip_update = True

# Logging
log_level = 2
warn_on_root = 0
