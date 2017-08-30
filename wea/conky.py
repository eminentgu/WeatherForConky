#coding=utf-8
import urllib
import re
import os
import time
def getWeather(html,findkey):
    reg = findkey
    weatherList = re.compile(reg).findall(html)
    return weatherList
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html
def changeIcon(icon) :
    if icon == '晴' :
        dt=list(time.localtime())
        if (dt[3] >= 19) or (dt[3] <= 6) :
            os.system('rm -rf /wea/显示/1.png')  
            os.system('cp /wea/图片/Moon.png /wea/显示/1.png')
        else :
            os.system('rm -rf /wea/显示/1.png')  
            os.system('cp /wea/图片/Sun.png /wea/显示/1.png')
    if icon == '多云' :
        dt=list(time.localtime())
        if (dt[3] >= 19) or (dt[3] <= 6) :
            os.system('rm -rf /wea/显示/1.png')  
            os.system('cp /wea/图片/Cloudy-Nighttime.png /wea/显示/1.png')
        else :
            os.system('rm -rf /wea/显示/1.png')  
            os.system('cp /wea/图片/Cloudy-Daytime.png /wea/显示/1.png')
    if icon == '阴' :
        dt=list(time.localtime())
        os.system('rm -rf /wea/显示/1.png')  
        os.system('cp /wea/图片/Overcast-Sky.png /wea/显示/1.png')
    if icon == '雷阵雨' :
        dt=list(time.localtime())
        os.system('rm -rf /wea/显示/1.png')  
        os.system('cp /wea/图片/Thunder-Shower.png /wea/显示/1.png')
    if (icon == '小雨') or (icon == '中雨') or (icon == '大雨') or (icon == '暴雨') or (icon == '阵雨') :
        dt=list(time.localtime())
        os.system('rm -rf /wea/显示/1.png')  
        os.system('cp /wea/图片/Drizzle.png /wea/显示/1.png')
    if (icon == '小雪') or (icon == '中雪') or (icon == '大雪') or (icon == '暴雪') or (icon == '阵雪') :
        dt=list(time.localtime())
        os.system('rm -rf /wea/显示/1.png')  
        os.system('cp /wea/图片/Snow.png /wea/显示/1.png')
try :
    m =getHtml('http://www.weather.com.cn/weather/101190402.shtml')
    high = getWeather(m,'<span>(.*?)</span>/<i>')
    low = getWeather(m,'</span>/<i>(.*?)</i>')
    condition = getWeather(m,'class="wea">(.*?)</p>')
    conditionA = condition[1]
    print conditionA
    print '          ' + high[0] +'～' + low[0]

    t = condition[1] +'n'
    img = getWeather(t,'转(.*?)n')
    imga = getWeather(t,'间(.*?)n')
    if imga == []:
        if img == []:
            changeIcon(condition[1])
            #print condition[0]
        else :
            if t.find('转') == t.rfind('转'):
                changeIcon(img[0])
                #print img[0]
            else :
                d = img[0]+'n'
                c = getWeather(d,'转(.*?)n')
                changeIcon(c[0])
                #print c[0]
    else:
        changeIcon(imga[0])
        #print imga[0]
except :
    print 'ERROR!'
