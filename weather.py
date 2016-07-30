#!/usr/bin/env python2
# coding=utf-8

import json

import common
import mailing
import config


def _parse(raw):
    obj = json.loads(raw, encoding="utf-8")
    desc = u""
    for i in range(2):
        d = obj["results"][0]["weather_data"][i]
        desc += d["date"] + u"：" + d["weather"] + u"，"
        desc += u"风力" + d["wind"] + u"，"
        desc += u"气温" + d["temperature"] + u"。"

    return desc


def main():
    url = "http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=%s"
    raw = common.guarded_read(url % (config.location, config.api_key))
    result = _parse(raw)
    mailing.send_mail(result)

    print("DONE!")


if __name__ == "__main__":
    main()
