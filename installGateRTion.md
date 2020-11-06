## VM setup

Installed Lubuntu v18.04 LTS

uname:  rtion  
psswd:  simulate



Using instructions from  
https://github.com/OpenGate/wiki/Gate-RTion-project


Configuration
- GEANT-10.3
- ROOTv6.08.06
- Physics:  GBBC_EMZ or QGSP_BIC_EMZ







##  Basic preparation

making root level directory for install  
set permission to 757 for ease of use in future installation steps

```console
cd /
sudo mkdir MCpackages
sudo chmod 757 MCpackages
```

#### Required basic packages for installation

```console
sudo apt-get install gcc g++ cmake make
```







##   GEANT4.10.03.p03

following instructions from:  
https://scicomex.com/how-to-install-geant4-on-linux

additional dependencies for geant4 - produce error messages:  
> missing:  EXPAT_LIBRARY EXPAT_INCLUDE_DIR
```console
sudo apt-get install libexpat-dev
```
> Qt version "" from NOTFOUND, this code requires Qt 4.x  
> X11 Xmu library and/or headers  
```console
sudo apt-get install qt5-default libx11-dev libxmu-dev
```

obtain geant4.10.03 with patch-03 from:  
https://geant4.web.cern.ch/support/download_archive

```console
cd /MCpackages/
mkdir geant4
cd geant4/
wget -c http://cern.ch/geant4-data/releases/geant4.10.03.p03.tar.gz
tar -zxf geant4.10.03.p03.tar.gz
mkdir geant4.10.03.p03-build
mkdir geant4.10.03.p03-install
mkdir geant4.10.03.p03-data
```

```console
cd geant4.10.03.p03-build/
```

generate install files with cmake and following options
```console
cmake \
-DCMAKE_INSTALL_PREFIX=/MCpackages/geant4/geant4.10.03.p03-install/ \
-DGEANT4_BUILD_MULTITHREADED=OFF \
-DGEANT4_INSTALL_DATA=ON \
-DCMAKE_INSTALL_DATADIR=cdata/ \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_QT=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
-/MCpackages/geant4/geant4.10.03.p03-install/ \
/MCpackages/geant4/geant4.10.03.p03/
```

if cmake successful
```console
make (-j<nCPU>)

make test

make install
```

activate by sourcing the appropriate .sh file
```console
source /MCpackages/geant4/geant4.10.03.p03-install/bin/geant4.sh
```
also add into .bash_aliases for future useres







## ROOTv6.08.06

install required dependencies as listed at:  
https://root.cern/install/dependencies

```console
sudo apt-get install git dpkg-dev cmake g++ gcc \
binutils libx11-dev libxpm-dev libxext-dev
```

libxft-dev doesn't install straigh forwardly  
requires specific version of libfreetype6
```console
sudo apt-get install libfreetype6=2.10.1-2
sudo apt-get install libxft-dev
```

install required version of ROOT from:  
https://root.cern/install/all_releases/  
https://root.cern/releases/release-60806/  
use the pre-compiled binary as compiling from source is troublesome

```console
cd /MCpackages/
wget -c https://root.cern/download/root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
tar -xzf root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
mv root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz root/
```

activate by sourcing the appropriate .sh file
```console
source /MCpackages/root/bin/thisroot.sh
```
also add into .bash_aliases for future useres








## GATE 8.1 RT-ion

http://www.opengatecollaboration.org/GateRTion  
https://github.com/OpenGATE/Gate/tree/GateRTion

additional dependencies identified during installation - produce error messages:
> something
```console
fix
```

```console
cd /MCpackages/
mkdir gate
cd gate/
wget -c https://github.com/OpenGATE/Gate/archive/GateRTion.zip
unzip GateRTion.zip
```

then following the instructions from:  
https://opengate.readthedocs.io/en/latest/compilation_instructions.html

```console
mkdir gate-build
mkdir gate-install
cd gate-build/
```

generate install files with cmake and following options
```console
cmake \
-DCMAKE_INSTALL_PREFIX=/MCpackages/gate/gate-install/ \
/MCpackages/gate/Gate-GateRTion/
```

if cmake successful
```console
make (-j<nCPU>)

make test

make install
```

finally add the location of the gate executable to the system path
```console
export PATH=$PATH:/MCpackages/gate/gate-install/bin/
```
also add into .bash_aliases for future useres





###  Issues

When preparing Gate can download testing data however this always seems to cause issues:
generate install files with cmake and following options
```console
cmake \
-DBUILD_TESTING=ON \
-DGATE_DOWNLOAD_BENCHMARKS_DATA=ON \
-DCMAKE_INSTALL_PREFIX=/MCpackages/gate/gate-install/ \
/MCpackages/gate/Gate-GateRTion/
```

Also, below are listed the previous build options used on an older system
```console
sudo cmake \
-DBUILD_TESTING=OFF \
-DCMAKE_BACKWARDS_COMPATIBILITY=2.4 \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=/usr/local/gate/gate_v8.0-install \
-DGATE_DOWNLOAD_BENCHMARKS_DATA=ON \
-DGATE_USE_ECAT7=OFF \
-DGATE_USE_GEANT4_UIVIS=ON \
-DGATE_USE_ITK=ON \
-DGATE_USE_OPTICAL=OFF \
-DGATE_USE_STDC11=ON \
-DGeant4_DIR=/usr/local/geant4/geant4.10.03.p03-install/lib/Geant4-10.3.3 \
/usr/local/gate/gate_v8.0
```


