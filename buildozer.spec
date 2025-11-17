[app]

# Title of your application
title = Maintenance App

# Package name
package.name = maintenanceapp

# Package domain (needed for android/ios packaging)
package.domain = org.test

# Source code where main.py lives
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Requirements
requirements = python3,kivy,requests,opencv

# Supported orientations
orientation = portrait

# Fullscreen mode
fullscreen = 1

# Android permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Android architectures
android.archs = arm64-v8a, armeabi-v7a

# Enable auto backup feature (optional)
android.allow_backup = True

# Use private storage
android.private_storage = True

# Copy libraries instead of building libpymodules.so
android.copy_libs = 1

# Android SDK, NDK, and Ant paths (local for GitHub Actions)
android.ndk_path = ./android/android-ndk
android.sdk_path = ./android/android-sdk
android.ant_path = ./android/apache-ant

# Minimum Android API
android.minapi = 24

# Target Android API
android.api = 33

# Android NDK API
android.ndk_api = 24

# Kivy bootstrap
p4a.bootstrap = sdl2

# Debug artifact format
android.debug_artifact = apk

# Release artifact format (optional)
# android.release_artifact = aab

# Skip SDK update during CI
android.skip_update = True

# Accept SDK licenses automatically
android.accept_sdk_license = True

# Log level
log_level = 2

# Warn when running as root
warn_on_root = 0


