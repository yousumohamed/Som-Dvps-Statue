```text
================================================================================
          SOMALIA DEVOPS STATUE - CORE TELEMETRY DAEMON (v0.1.0)
================================================================================

Initial Release : January 15, 2009
Lead Author     : Yusuf Mohamed <yousumohamed>
Website         : [http://yusuf.somdvps.org](http://yusuf.somdvps.org)
Target Arch     : x86 / POSIX / Linux Kernel 2.6
Licence         : GNU General Public License v2 (GPLv2)

--------------------------------------------------------------------------------
[1.0] SYSTEM OVERVIEW
--------------------------------------------------------------------------------
Som-Dvps-Statue is an enterprise Linux system telemetry daemon. It records 
kernel event traces, packet routes, and CPU cycle footprints on low-spec 
nodes with zero overhead.

"Only intelligent engineers bend system constraints."

--------------------------------------------------------------------------------
[2.0] SYSTEM REQUIREMENTS
--------------------------------------------------------------------------------
  * GCC 4.3+ Compiler
  * GNU Make 3.81
  * Perl 5.10.0 / Python 2.6+
  * Linux Kernel 2.6.18+

--------------------------------------------------------------------------------
[3.0] BUILD & INSTALLATION
--------------------------------------------------------------------------------
To compile and deploy the telemetry binary from source:

    $ tar -zxvf som-dvps-statue-0.1.0.tar.gz
    $ cd som-dvps-statue-0.1.0/
    $./configure --prefix=/usr/local$ make
    # make install

--------------------------------------------------------------------------------
[4.0] CONFIGURATION
--------------------------------------------------------------------------------
Adjust daemon settings in /etc/statue/statue.conf:

    INTERVAL_SECONDS=60
    LOG_FILE=/var/log/statue_activity.log
    ENABLE_REMOTE_TRACE=0

--------------------------------------------------------------------------------
[5.0] MAINTAINER CONTACT
--------------------------------------------------------------------------------
Lead Architect : Yusuf Mohamed
Portfolio      : [http://yusuf.somdvps.org](http://yusuf.somdvps.org)
GitHub Profile : [http://github.com/yousumohamed](http://github.com/yousumohamed)

================================================================================
                 (C) Copyright 2009 Yusuf Mohamed. All rights reserved.
================================================================================
