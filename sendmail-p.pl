#!/usr/bin/perl -w

use Mail::Sendmail;
use strict;
use warnings;

# #################################################################
# define the e-mail participants, server and content
# #################################################################
# create the main e-mail hash structure [REQUIRED]
my %mail;

# set the smtp mail server [REQUIRED]
$mail{Smtp} = "mxXXXXXX.smtp-engine.com";
$mail{Debug} = 6;
$mail{Port} = 25;
$mail{Auth} = {user => "outmail-username", pass => "outmail-password",
               method => "LOGIN", required => 1};

# set the recipients (to) address [REQUIRED]
$mail{To}      = 'recipient@example.com';

# set the mail sender address [REQUIRED]
$mail{From}    = 'me@example.com';
$mail{Sender}  = 'me@example.com';

# set the  mail subject line
$mail{subject} = "Test message";

# set the mail content
$mail{body}    = "The test messsage is having this body line inside.";

# set the mail encoding type
$mail{'content-type'} = qq(text/plain; charset="utf-8");

# #################################################################
# send the e-mail out and return verbose information
# #################################################################
sendmail(%mail) or die $Mail::Sendmail::error;
print "The sendmail log reports:\n".$Mail::Sendmail::log."\n";
exit 0;