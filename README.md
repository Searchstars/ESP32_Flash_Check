# ESP32_Flash_Check

一个用于检测ESP32的Flash使用情况的小工具

## 使用方法
首先安装esptool：

`pip install esptool`

然后尝试在shell中输入`esptool`，若成功输出esptool的help则请继续，否则请重启shell并检查您的环境变量

然后，在修改`config.json`中的`read_flash_hex`字段，改成你的ESP32的Flash大小，比如我的Flash大小是4M，就默认写`0x400000`了。然后再修改里面的`com_port`字段，这取决于ESP32连接在你电脑的哪个端口上，我的是COM3，就默认写COM3了。

最后，运行main.py，等待输出结果