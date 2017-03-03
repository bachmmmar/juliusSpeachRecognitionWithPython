#!/bin/bash

# select usb micriophone on notebook
export ALSADEV="plughw:2,0"

pushd word_configuration > /dev/null
../julius_install/bin/mkdfa.pl babycamera
popd > /dev/null

./julius_install/bin/julius -C babycamera.jconf -input alsa -quiet
