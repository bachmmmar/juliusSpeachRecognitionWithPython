#!/bin/bash


function checkSuccess() {
    if [ $1 -ne 0 ]; then
	echo "ERROR: ${2}"
	exit 1
    fi
}

function isCurrentDirBaseOfRepository() {
    INSTALL_DIR=$(pwd)/julius_install
    SOURCE_DIR=$(pwd)/julius_source    
    WORD_DIR=$(pwd)/word_configuration
    if [ ! -e ${BUILD_DIR} ]; then
	echo "build directory does not exists! You have to execute the script from the repository base directory!"
	exit 1
    fi

    
}


# Start Compile and installation
isCurrentDirBaseOfRepository

pushd $SOURCE_DIR > /dev/null
$SOURCE_DIR/configure --prefix=${INSTALL_DIR}
checkSuccess $? "Configure Julius"

make
checkSuccess $? "Build Julius"

make install
checkSuccess $? "Installing Julius to ${INSTALL_DIR}"

pushd $WORD_DIR > /dev/null

# Compile Word data
$INSTALL_DIR/bin/mkdfa.pl babycamera
checkSuccess $? "Could not generate babycamera data."




