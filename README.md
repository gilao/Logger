# Logger
python的一个logger 类，提供logger组件

实例化 Logger：

```python
from pkg.logger import logger

# 实例化python，定义日志文件和日志等级；
# 日志等级对应：    
	# 0: logging.DEBUG,
    # 1: logging.INFO,
    # 2: logging.WARNING,
    # 3: logging.ERROR,
    # 4: logging.CRITICAL
object_logger = logger.Logger('test.log',0)
```

调用log

```
object_logger.debug('debug')
object_logger.info('info')
object_logger.error('error')
object_logger.warning('warning')
object_logger.critical('critical')
```

