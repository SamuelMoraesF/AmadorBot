###
# Copyright (c) 2014, Samuel Moraes
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import httplib

class SiteStatus(callbacks.Plugin):
    """Add the help for "@plugin help SiteStatus" here
    This should describe *how* to use this plugin."""
    pass

    def mozstatus(self, irc, msg, args):


    	#1
        conn = httplib.HTTPConnection("mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason
        irc.reply("Main Site: %s %s" % (res.status, res.reason))

        #2
        conn = httplib.HTTPConnection("pad.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Etherpad: %s %s" % (res.status, res.reason))

        #3
        conn = httplib.HTTPConnection("diaspora.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Diaspora: %s %s" % (res.status, res.reason))

        #4
        conn = httplib.HTTPConnection("sheet.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Ethersheet: %s %s" % (res.status, res.reason))

        #5
        conn = httplib.HTTPConnection("cloud.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("ownCloud: %s %s" % (res.status, res.reason))

        #6
        conn = httplib.HTTPConnection("social.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("GNU Social: %s %s" % (res.status, res.reason))

        #7
        conn = httplib.HTTPConnection("planet.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Planet: %s %s" % (res.status, res.reason))

        #8
        conn = httplib.HTTPConnection("webmaker.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Webmaker: %s %s" % (res.status, res.reason))

        #9
        conn = httplib.HTTPConnection("comunidade.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("NodeBB: %s %s" % (res.status, res.reason))

        #10
        conn = httplib.HTTPConnection("blog.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Ghost: %s %s" % (res.status, res.reason))

        #11
        conn = httplib.HTTPConnection("pastebin.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Pastebin: %s %s" % (res.status, res.reason))


        conn = httplib.HTTPConnection("bugzilla.mozillabrasil.org.br")
        conn.request("HEAD", "/")
        res = conn.getresponse()
        resposta = res.status, res.reason

        irc.reply("Bugzilla: %s %s" % (res.status, res.reason))

        irc.reply("== END ==")


    mozstatus = wrap(mozstatus)


Class = SiteStatus


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
