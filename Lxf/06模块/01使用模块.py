##############
#模块

# mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py
#
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
#
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
# 也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

import hello
#hello.test()

hello.greeting('ffff')















