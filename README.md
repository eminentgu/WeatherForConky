# WeatherForConky
A weather report which can be run on the desktop,get data from CHINA WEATHER.
####################################### WHAT IS  IT？######################################################
  It is a small tool to get weather report from CHINA WEATHER and show it on the upper right of the desktop.
  这是一个小的工具从中国天气得到天气报告，并在桌面的右上方显示它。
####################################### HOW TO USE IT?####################################################
  1.Copy ‘wea’ to the root directory.
    把wea文件夹复制到根目录。
  2.change the url in /wea/conky.py
    更改/wea/conky.py中的网址。
      2.1 visit www.baidu.com and search your city's weather report.You will be able to see your city's weather report from CHINA WEATHER.Click it and copy the url.(the url should be like this http://www.weather.com.cn/weather/101190402.shtml),open /wea/conky.py,change the url on the line 49 into your url.
          百度搜索你所在城市的天气预报。你能看到中国天气的天气预报。点击，复制网址（URL应该像这个www.weathe.com.cn/weather/101190402.shtml），打开/wea/conky.py，更改第49行的网址。
  3.copy the .conkyrc to your home directory,run conky.
    将.conkyrc复制到家目录，运行conky。
###########################################  注意 ###########################################################
  1.由于桌面不同，可能需要更改.conkyrc的参数。
  2.目前除了北京，其他地区均可使用。（北京地区的主页与其他地区不同）。
  3.建议使用于深色背景。
  4.天气大于5个字，可能不能显示。如：多云转晴转晴间多云。
  
