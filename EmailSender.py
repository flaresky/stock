# -*- coding: utf-8 -*-
import smtplib
from email.message import EmailMessage

DEBUG = False

mail_list = []

mail_list.extend([
            '6641323@qq.com',
                  ])  

from_name = '李天齐 <nhmltq@163.com>'

emails = (
          {"email":'6641323@qq.com', "password":'kupsiubnqhalbijh', "smtp":'smtp.qq.com', 'ssl':True},
          {"email":'nhmltq@163.com', "password":'nihaoma0809', "smtp":'smtp.163.com'},
          )

def send_mail(title, msg):
    es = EmailSender()
    es.send_mail(title, msg)
    es.close()

class EmailSender(object):
    def __init__(self):
        email_config = emails[0]
        self.email = email_config['email']
        self.password = email_config['password']
        self.recv_list = ", ".join(mail_list)
        if 'ssl' in email_config and email_config['ssl']:
            self.s = smtplib.SMTP_SSL(email_config['smtp'])
        else:
            self.s = smtplib.SMTP(email_config['smtp'])
        self.s.login(self.email, self.password)
    
    def send_mail(self, title, content):
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = title
        msg['From'] = from_name
        msg['To'] = self.recv_list
        for to_mail in mail_list:
            self.s.sendmail(self.email, to_mail, msg.as_string())
    
    def close(self):
        self.s.close()

if __name__ == '__main__':
    send_mail("[AUTO_KILL] %s, count is %d"%('test', 100), 'hahahahaha')