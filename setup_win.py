# -*- coding: utf-8 -*-
# Copyright (C) 2017 Ashlar Ruby
# Licensed under the MIT license. See COPYING.md for details.
"""
Build a standalone Windows executable.
See BUILDING.md for instructions.
"""
import os
import subprocess
import shutil
import platform

pwd = os.getcwd()

# Remove old build directories
if os.path.exists('__pycache__'):
    shutil.rmtree('__pycache__', ignore_errors=True)
if os.path.exists('build'):
    shutil.rmtree('build', ignore_errors=True)
if os.path.exists('dist'):
    shutil.rmtree('dist', ignore_errors=True)

main = ['pyinstaller']
excludes = ['--exclude-module=tkinter']
opts = ['--noconsole', '--clean', '--icon=RespiRate.ico']
target = ['RespiRate.py']

cmd = main + excludes + opts + target
print(cmd)

subprocess.call(cmd)

# Copy the icon
shutil.copyfile('RespiRate.ico', pwd + '\dist\RespiRate\RespiRate.ico')

# We require ffmpeg. Pyinstaller fails to build a .dll for it in Windows, so we
# must copy a prebuild .dll to the proper location.
shutil.copyfile('opencv_ffmpeg320_64.dll',
                pwd + '\dist\RespiRate\opencv_ffmpeg320_64.dll')
shutil.copyfile('opencv_ffmpeg320.dll',
                pwd + '\dist\RespiRate\opencv_ffmpeg320.dll')
