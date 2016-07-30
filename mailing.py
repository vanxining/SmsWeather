# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.utils import make_msgid

import config


def _make_mail(body, fmt):
    msg = MIMEMultipart()

    msg["To"] = config.to_mail_addr
    msg["From"] = config.mail_sender_desc
    msg["Subject"] = config.mail_subject
    msg["Message-Id"] = make_msgid()
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(body, "plain" if fmt == "txt" else "html", "utf-8"))

    return msg


def _do_send_mail(msg):
    srv = smtplib.SMTP(config.mail_smtp_server)
    srv.ehlo()
    srv.starttls()
    srv.ehlo()
    srv.login(config.mail_smtp_usr, config.mail_smtp_pwd)
    srv.sendmail(msg["From"], msg["To"], msg.as_string())
    srv.quit()


def send_mail(content):
    msg = _make_mail(body=content, fmt="txt")
    _do_send_mail(msg)
