# RaspberryPi3B
## 概要(OverView)
RaspberryPi model3BでHTU21DF(GY-21)温湿度センサーの値とカメラモジュールの画像を取得しSlackに送信できます。
SlackでBOTを作成し、Tokenを使用します。Python3で動作しています。また、動作にはpigpioデーモンが作動している必要があります。

## Install
HTU21DF.py(Check the Link below.)とpicture.pyをフォルダーに入れてください。TokenとChannelIDを指定すると動作させることができます。

Thx for dalexgray(HTU21FD.py developer)
https://github.com/dalexgray/RaspberryPI_HTU21DF
