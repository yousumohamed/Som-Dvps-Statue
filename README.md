===============================================================================
SOMALIA DEVOPS STATUE - CORE INFRASTRUCTURE TELEMETRY DAEMON
===============================================================================
Initial Release Date : January 15, 2009
Author               : Yusuf Mohamed <yousumohamed@github>
Website              : http://yusuf.somdvps.org
Architecture         : x86 / POSIX / Linux 2.6 Kernel
Licence              : GNU General Public License v2 (GPLv2)
===============================================================================

[1.0] OVERVIEW
-------------------------------------------------------------------------------
Som-Dvps-Statue is a lightweight system daemon designed for Linux and Unix-like
servers to trace local network activity, system load, and memory usage.

Designed for maximum efficiency on minimal resources. "Only intelligent 
engineers bend system constraints."

[2.0] REQUIREMENTS
-------------------------------------------------------------------------------
* GCC 4.3 or higher
* GNU Make 3.81
* Perl 5.10.0
* Python 2.6+
* Linux Kernel 2.6.18+

[3.0] INSTALLATION & BUILD INSTRUCTIONS
-------------------------------------------------------------------------------
To compile and install the telemetry daemon on your server:

    $ tar -zxvf som-dvps-statue-0.1.0.tar.gz
    $ cd som-dvps-statue-0.1.0/
    $ ./configure --prefix=/usr/local
    $ make
    # make install

[4.0] CONFIGURATION
-------------------------------------------------------------------------------
Edit /etc/statue/statue.conf to adjust log intervals:

    # /etc/statue/statue.conf - Configuration file
    INTERVAL_SECONDS=60
    LOG_FILE=/var/log/statue_activity.log
    ENABLE_REMOTE_TRACE=0

[5.0] CONTACT & MAINTAINER
-------------------------------------------------------------------------------
Lead Architect : Yusuf Mohamed
Web           : http://yusuf.somdvps.org
GitHub        : http://github.com/yousumohamed

===============================================================================
(C) Copyright 2009 Yusuf Mohamed. All rights reserved.
===============================================================================
