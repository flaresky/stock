# -*- coding: utf-8 -*-
import smtplib,mimetypes
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

DEBUG = False

mail_list = []

mail_list.extend([
            '6641323@qq.com',
#             '176847544@qq.com',
                  ])  

from_name = '李天齐 <nhmltq@163.com>'

emails = (
          {"email":'nhmltq@163.com', "password":'nihaoma0809', "smtp":'smtp.163.com'},
          {"email":'6641323@qq.com', "password":'nihaoma0809', "smtp":'smtp.qq.com'},
          )

class EmailSender(object):
    def __init__(self):
        email_config = emails[0]
        self.email = email_config['email']
        self.password = email_config['password']
        self.recv_list = ", ".join(mail_list)
        self.s = smtplib.SMTP(email_config['smtp'])
        self.s.login(self.email, self.password)
    
    def send_mail(self, title, content):
        msg = MIMEMultipart()
        msg['Subject'] = title
        msg['From'] = from_name
        msg['To'] = self.recv_list
        txt = MIMEText(content, 'html', _charset='utf-8')
        msg.attach(txt)
        for to_mail in mail_list:
            self.s.sendmail(self.email, to_mail, msg.as_string())
    
    def close(self):
        self.s.close()

if __name__ == '__main__':
    msg = '''<div class="article-detail">
        <p class="tt" style="text-align:center;">关于上报11月群体师德创优扣分情况的通知</p>
        <p class="t-indent fn-right">截止日期：&nbsp;&nbsp;一年</p>
        <div class="des">
            <p class="t-indent"></p><p>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 现请相关部门将11月群体师德创优扣分情况于12月9日前报办公室。
</p>
<p align="center">
    办公室
</p>
<p align="center">
    2014年12月5日
</p><p></p>
        </div>
    </div>'''
    es = EmailSender()
    es.send_mail('EmailSender Test3', msg)
    es.close()