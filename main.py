import json
import os

#读取配置文件
config_file = open("config.json","r")
config = json.loads(config_file.read())

#调用esptool进行read_flash
#记得先pip install esptool
build_shell = "esptool -p " + config["com_port"] + " -b 921600 read_flash 0 " + config["read_flash_hex"] + " flash_contents.bin"
print(build_shell)
os.system(build_shell)

flash_size = int (config["read_flash_hex"], 16) / 1024
# 打开bin文件
try:
    with open("flash_contents.bin", "rb") as f:
        # 读取bin文件的内容
        data = f.read()
        # 初始化非FF的hex的数量
        non_ff_count = 0
        # 遍历每个字节
        for byte in data:
            # 如果字节不是FF，就增加非FF的hex的数量
            if byte != 255:
                non_ff_count += 1
        # 计算非FF的hex占了多少k的空间
        non_ff_size = non_ff_count / 1024
        # 计算剩余空间
        free_size = flash_size - non_ff_size
        # 输出结果
        print(f"非FF的hex占了{non_ff_size:.2f}k的空间")
        print(f"也就是说：你的Flash总共有{flash_size:.2f}k的空间，还剩下{free_size:.2f}k空间可用，你已经用了{non_ff_size:.2f}k的空间")
except FileNotFoundError:
    print("操作失败，原因：flash_contents.bin不存在，可能是因为在read_flash过程中出现了错误，请确保config填写正确！")

config_file.close()