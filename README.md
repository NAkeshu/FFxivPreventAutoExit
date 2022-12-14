# FFxiv 防t

## 原理

模拟键盘`esc`键，每20分钟按两次，更新状态。

## 使用方法：

### 直接使用编译好的exe文件

`Releases` 中下载`FFxivPreventAutoExit.exe`文件，**管理员权限**运行，回到游戏中**并保持游戏窗口在前台且保持活动状态**。

### 自行编译：

环境：python3、pyinstaller

```bash
git clone git@github.com:NAkeshu/FFxivPreventAutoExit.git
cd FFxivPreventAutoExit
pyinstaller -F --uac-admin ./ffxiv_prevent_auto_exit.py
```

**管理员权限**运行`dist`文件夹下的`ffxiv_prevent_auto_exit.exe`文件。

### 直接运行

环境：python3、pyinstaller

**需要在管理员权限下运行脚本**

```bash
git clone git@github.com:NAkeshu/FFxivPreventAutoExit.git
cd FFxivPreventAutoExit
python ./ffxiv_prevent_auto_exit.py
```

## 可选配置

```python
# Configurations
WaitTime = 20 * 60  # 自动执行间隔（单位：秒）
NeedAlert = True  # 更新状态后是否发出提示音（True / False）
```

## 参考

1. [How to simulate raw input / Send a WM_INPUT message to an application the right way? (stackoverflow)](https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game)
2. [Scan Key Code](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)?redirectedfrom=MSDN)
