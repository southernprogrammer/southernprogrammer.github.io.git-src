SageTV Rename
#############
:date: 2010-06-06 15:40
:author: bryan
:category: Blog
:tags: BeyondTV, BeyondTV Rename, SageTV, SageTV Rename
:slug: sagetv-rename
:status: published

Many of you may remember that I wrote a script for BeyondTV (`BeyondTV
Renamer <pages/coding-projects.html>`__) that utilized a
command line tool that someone had written to create an XML file giving
detailed information about the given file.  My script compared the
airdate from this dumped XML file with airdates of matching shows on
TVRage.com to rename the files in such a way that XBMC or Boxee could
read the file and get the metadata (like show description and images). 

Well today I’m releasing a script that I wrote that does something
similar for SageTV.  Technically speaking, it does not actually rename
the file.  It creates symlinks to the files named in such a way that
XBMC or Boxee can read the files and pickup the metadata.  And instead
of needing the command line tool, you need the SageTV Web Interface that
was written by Neilm.  By creating symlinks, it allows for only 1 true
copy of the file to exist and for the show to remain in SageTV and in
Boxee or XBMC.

Original `BeyondTV
Renamer <https://github.com/southernprogrammer/BTVRenamer>`__ \| New `SageTV
Rename <https://github.com/southernprogrammer/SageTVRename>`__
