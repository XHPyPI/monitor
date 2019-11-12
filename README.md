- 一个性能监控的库

# 安装命令：
`pip install xhmonitor`

# 使用方法：
```python
from xhmonitor import start_monitor, end_monitor

def TestProfile():
    iCnt = 0
    for x in range(10000):
        iCnt += x
    print(iCnt)

start_monitor()
TestProfile()
end_monitor()
```
> 会生成一个time.txt和time.view文本
> 
> time.txt: 性能测试的文本文件，可以查看每个函数的运行时间
> 
> time.view：可使用kcachegrind, qcachegrind工具打开该文件可视化查看更详细内容