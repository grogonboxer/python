# -*- coding: UTF-8 -*-
'''
发送html邮件
'''
import json
import smtplib
import sys  
import ConfigParser,os
from email.mime.text import MIMEText   
mail_host=sys.argv[4]  #设置服务器
mail_user=sys.argv[5]    #用户名
mail_pass=sys.argv[6]    #口令 
mail_postfix="dpjia.com"  #发件箱的后缀
mail_author=sys.argv[7]   #author
cp = ConfigParser.SafeConfigParser()
cp.read('files/plugins/python/dpj_mail/mail.conf')
ssl_conf = cp.get('ssl','is_ssl')
# print ssl_conf

def send_mail(to_list,sub,content):  
    me=mail_author+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='html',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try: 
        if ssl_conf == 'TRUE':
            server = smtplib.SMTP_SSL()
            server.connect(mail_host,465)
        if ssl_conf == 'FALSE':
            server = smtplib.SMTP()
            server.connect(mail_host)
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return {'message':'发送成功', 'status': True}
    except Exception, e:  
        message = str(e)
        return {'message':message, 'status': False}
if __name__ == '__main__':
    subject = sys.argv[1];
    mailto_list = sys.argv[2].split(',')
    content = sys.argv[3];  
    result = send_mail(mailto_list,subject,content)
    print json.dumps(result)
