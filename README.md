SmsWeather
==========

每天发送一封包含天气预报信息的简短邮件到某个运营商邮箱，进而实现天气预报短信的效果。

程序使用的是百度地图提供的天气 API，据称每天提供 5000 次调用。我想用着代码中附带的
这个应该就够用了。

## 配置

程序必须经过（有点繁琐的）配置才能使用。所有可配置项都放在了 config.py 文件中：
* `location`：需要预报的地理位置，例如“海淀”。可以通过 [这种格式]
(http://api.map.baidu.com/telematics/v3/weather?location=海淀&output=json&ak=2b7e46d89c9064014ff84587b8c6010a)
的 URL 在浏览器中验证给定的地方是否合法
* `api_key`：（可选）使用自己的百度账号到 [这里]
(http://lbsyun.baidu.com/index.php?title=car/api/weather)
申请天气 API 的使用权限，得到相应的 API Key
* `to_mail_addr`：接收人邮箱地址。一般为运营商邮箱，如移动的 139 邮箱
* `from_mail_addr`：发送人邮箱地址，任意邮箱提供商均可
* `mail_smtp_server`：发送人邮箱 SMTP 服务器地址
* `mail_smtp_usr`：发送人用来登录 SMTP 服务器的用户名
* `mail_smtp_psw`：发送人用来登录 SMTP 服务器的密码
* `mail_sender_desc`：邮件中“发送人”的描述
* `mail_subject`：邮件主题

## 定时执行

在 Linux 下可以使用 cron 来实现定点执行这个脚本：

```
* 18 * * * /home/tmpusr/scripts/smsweather/weather.py > /tmp/smsweather.log 2>&1
```

上述指令实现了每天 18 点时自动执行这个脚本。

（用法：在终端中输入`crontab -e`打开编辑器，添加上述指令即可）
