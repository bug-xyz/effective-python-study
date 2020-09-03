## Docker命令

- ### 概述

  [官网](https://www.docker.com/)、[文档](https://docs.docker.com/ )、[仓库](https://hub.docker.com/)

  - #### docker的基本组成

    ##### 镜像（image）：

    docker镜像就好比是一个目标，可以通过这个目标来创建容器服务，mysql镜像==>run==>容器（提供服务器），通过这个镜像可以创建多个容器（最终服务运行或者项目运行就是在容器中的）。

    ##### 容器（container）：

    docker利用容器技术，独立运行一个或一组应用，通过镜像来创建的。

    启动，停止，删除，基本命令

    目前就可以把这个容器理解为就是一个简易的Linux系统

    ##### 仓库（repository）：

    仓库就是存放镜像的地方！仓库分为公有仓库和私有仓库。（很类似git）

    docker hub 是国外的，阿里云...都有容器服务器（配置镜像加速！）

- ### 安装

  - #### 安装docker

    帮助文档：https://docs.docker.com/engine/install/

    ```shell
    # eg：Linux下安装docker，Linux要求内核3.0以上
    # 查看系统内核版本和相关信息
    [root@ae56f030562a /]# uname -r
    4.9.125-linuxkit
    [root@ae56f030562a /]# cat /etc/os-release
    NAME="CentOS Linux"
    VERSION="8 (Core)"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="8"
    PLATFORM_ID="platform:el8"
    PRETTY_NAME="CentOS Linux 8 (Core)"
    ANSI_COLOR="0;31"
    CPE_NAME="cpe:/o:centos:centos:8"
    HOME_URL="https://www.centos.org/"
    BUG_REPORT_URL="https://bugs.centos.org/"
    CENTOS_MANTISBT_PROJECT="CentOS-8"
    CENTOS_MANTISBT_PROJECT_VERSION="8"
    REDHAT_SUPPORT_PRODUCT="centos"
    REDHAT_SUPPORT_PRODUCT_VERSION="8"
    # 安装
    # 1、卸载旧版本
    $ yum remove docker \
                      docker-client \
                      docker-client-latest \
                      docker-common \
                      docker-latest \
                      docker-latest-logrotate \
                      docker-logrotate \
                      docker-engine
    # 2、需要的安装包
    $ yum install -y yum-utils
    # 3、设置镜像的仓库
    $ yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo
    # 默认是从国外的，不推荐
    # 推荐使用国内的
    $ yum-config-manager \
        --add-repo \
        https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    # 更新yum软件包索引
    $ yum makecache fast
    # 4、安装docker相关的 docker-ce 社区版 而ee是企业版
    $ yum install docker-ce docker-ce-cli containerd.io
    # 5、启动docker
    $ docker systemctl start docker
    # 6、使用docker version查看是否按照成功
    $ docker version
    # 7、测试
    $ docker run hello-world
    Hello from Docker!
    This message shows that your installation appears to be working correctly.
    
    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
     3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.
    
    To try something more ambitious, you can run an Ubuntu container with:
     $ docker run -it ubuntu bash
    
    Share images, automate workflows, and more with a free Docker ID:
     https://hub.docker.com/
    
    For more examples and ideas, visit:
     https://docs.docker.com/get-started/
    # 8、查看一下下载的镜像
    $ docker images         
    REPOSITORY     TAG         IMAGE ID          CREATED             SIZE
    hello-world    latest      bf756fb1ae65      4 months ago        13.3kB 
    ```

  - #### 配置镜像加速器

    [参考](https://www.daocloud.io/mirror)

    ##### Linux

    将 --registry-mirror 加入到你的 Docker 配置文件 /etc/docker/daemon.json 中

    ```shell
    $ curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s    		http://f1361db2.m.daocloud.io
    $ systemctl restart docker
    ```

    ##### Windows

    在桌面右下角状态栏中右键 docker 图标，修改在 Docker Daemon 标签页中的 json ，把下面的地址:

    ```
    http://f1361db2.m.daocloud.io
    ```

    加到" `registry-mirrors`"的数组里。点击 Apply 。

  - #### 卸载docker

    ```shell
    # 卸载依赖
    $ yum remove docker-ce docker-ce-cli containerd.io
    # 删除资源
    $ rm -rf /var/lib/docker	# /var/lib/docker 是docker的默认工作路径！
    ```
    

- ### 帮助命令

  [参考](https://docs.docker.com/reference/)

  ```shell
  $ docker version			# 显示docker的版本信息
  $ docker info				# 显示docker的系统信息，包括镜像和容器的数量
  $ docker --help				# 帮助命令	
  $ docker 命令 --help		   # 帮助命令
  ```
- ### 镜像命令

  - #### 搜索

    ```shell
    # 格式
    docker search 镜像
    
    # 可选参数
    -f	筛选条件
    
    # eg
    $ docker search mysql		# 搜索mysql相关镜像
    $ docker search mysql -f STARS=3000	# 搜索镜像STARS大于3000的
    ```

    - #### 查看

      ```shell
      # 格式
      docker images
      
      # 可选参数
      -a	列出所有的镜像
      -q	只显示镜像的id
      
      # eg
      $ docker images			# 查看本机所有的镜像
      $ docker images -aq		# 显示所有镜像的id
      ```

    - #### 下载

      ```shell
      # 格式
      docker pull 镜像名:标签
      
      # eg
      $ docker pull mysql:5.7		# 如果不写tag(标签)，默认就是latest
      ```

    - #### 删除

      ```shell
      # 格式
      docker rmi 镜像id
      
      # 可选参数
      -f	强制删除
      
      # eg
      $ docker rmi 镜像id 	# 删除指定的镜像
      $ docker rmi -f 镜像id 镜像id 镜像id		# 强制删除指定的镜像
      $ docker rmi -f $(docekr images -aq)	# 强制删除全部的镜像
      ```

    - #### 重命名

      ```shell
      # 格式
      docker tag 镜像id 新镜像名:标签
      
      # eg
      $ docker tag 镜像id centos01:0.1
      # 就是打新的标签，发现复制了一个镜像，新旧镜像的image id一样，删除旧的就达到重命名的效果了
      ```

    - #### 导出、导入

      ```shell
      # 格式
      docker save -o 导出后本地的镜像名称 源镜像名称		# 导出
      docker load -i 镜像包路径						# 导入
      
      # eg
      $ docker save -o  centos.tar centos		# 讲centos镜像压缩成centos.tar
      $ docker load -i centos.tar		# 解压镜像包centos.tar
      ```

    - #### 构建

      ```shell
      # 格式
      docker build -f Dockerfile路径 -t	镜像名称:tag
      
      # eg
      $ docker build .	# 在Dockerfile文件所在目录下执行，首选
      $ docker build -f mydockerfile -t mysql01:0.2
      $ docker build -t mytomcat:0.1 . # 不写-f默认在本目录下寻找Dockerfile，需要加 .(点)
      ```

    - #### 其他

      ```shell
      $ docker inspect 镜像id	# 查看镜像元数据
      $ docekr history 镜像名	# 查看镜像构建历史
      ```

- ### 容器命令

  - #### 创建

    ```shell
    # 格式
    docker run [可选参数] 镜像id	新建并启动容器
    
    # 可选参数
    --name="Name"	容器名字，centos01、centos02，用来区分容器
    -d				后台方式运行，并返回容器id
    -i				已交互模式运行容器，通常与 -t 同时使用
    -t				为容器重新分配一个伪输入终端，通常与 -i 同时使用
    -it				使用交互方式运行，进入容器查看内容
    -p				端口映射，格式：宿主机端口:容器端口
    -P(大写)		   随机指定端口
    -v				挂载数据卷，格式：宿主机路径:容器路径
    
    # eg
    $ docker run -d centos		# 后台启动
    # 问题docker ps 发现 centos 停止了
    # 常见的坑，docker容器使用后台运行，就必须要有一个前台进程，docker发现没有应用，就会自动停止
    # nginx，容器启动后，发现自己没有提供服务，就会立刻停止，就是没有程序了
    
    # 挂载数据卷   -v
    # docker run -it -v 主机目录:容器内目录 -p 主机端口:容器内端口
    $ docker run -it -v /home/ceshi:/home centos /bin/bash
    ```

  - #### 启动、停止

    ```shell
    docekr start 容器id		# 启动停止的容器
    docker restart 容器id		# 重启容器
    docker stop 容器id 		# 停止当前正在运行的容器
    docker kill 容器id 		# 强制停止当前容器
    ```

  - #### 查看

    ```shell
    # 格式
    docker ps			# 列出当前正在运行的容器
    
    # 可选参数
    -a		显示所有的容器，包括未运行的
    -n		列出最近创建的容器
    -q		只显示容器id
    
    # eg
    $ docker ps -a		# 列出所有的容器（运行中的+停止的）
    $ docekr ps -aq		# 列出所有的容器的id
    $ docker ps -n=2	# 列出最近创建2个创建的容器
    ```

  - #### 进入、退出

    ```shell
    $ docker exec -it 容器id /bin/bash 		# 进入容器，新建伪终端
    $ exit				  # 容器直接退出
    快捷键：ctrl + D		# 容器直接退出
    快捷键：ctrl + P + Q	# 容器不停止退出
    ```

  - #### 删除

    ```shell
    $ docker rm 容器id		# 删除指定的容器，不能删除正在运行的容器
    $ docker rm -f $(docker ps -aq)	# 强制删除所有的容器
    $ docker ps -a -q|xargs docker rm	# 删除所有的容器
    ```

  - #### 容器提交成镜像

    ```shell
    # 格式，命令和git原理类似
    docker commit -m="描述信息" -a="作者" 容器id 目标镜像名:tag
    
    # eg
    $ docker commit -m="初始化" -a="moyangxyz" 容器id centos01:1.0
    ```

  - #### 其他

    ```shell
    $ docker inspect 容器id	# 查看容器元数据
    
    $ docker logs 容器id		# 显示日志
    $ docker logs -t --tail n 容器id		# 查看n行日志
    $ docker logs -ft 容器id		# 跟着日志，实时刷新
    
    $ docker top 容器id	# 查看容器进程信息
    
    $ docker cp 容器id:容器内路径 宿主机目路径	# 从容器内拷贝文件到宿主机，拷贝文件夹要加 -r
    ```

- ### 数据卷

  - #### 直接使用命令挂载数据卷   -v

    ```shell
    # 格式
    docker run -it -v 主机目录:容器内目录 -p 主机端口:容器内端口
    
    # eg
    $ docker run -it -v /home/ceshi:/home centos /bin/bash
    
    # 安装mysql容器，并实现数据同步
    $ docker run -d -p 3310:3306 -v 	E:\personal\docker\mysql\conf:/etc/mysql/conf.d -v E:\personal\docker\mysql\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql01 mysql:5.7
    
    安装启动mysql，需要配置密码的
    -d	后台运行
    -p  端口映射
    -v	卷挂载
    -e	环境配置
    --name	容器名字
    ```

- #### 小结

  ![1598002020202](docker学习.assets/1598002020202.png)

  ```shell
  attach      Attach local standard input, output, and error streams to a running 			container	# 当前 shell 下 attach 连接指定运行的镜像
  build       Build an image from a Dockerfile	# 通过 Dockerfile 定制镜像
  commit      Create a new image from a container's changes # 提交当前容器为新的镜像
  cp          Copy files/folders between a container and the local filesystem
  			# 从容器中拷贝指定文件或者目录到宿主机中
  create      Create a new container	# 创建一个新的容器，同 run，但不启动容器
  diff        Inspect changes to files or directories on a container's filesystem
  			# 查看 docker 容器变化
  events      Get real time events from the server	# 从docker服务获取容器实时事件
  exec        Run a command in a running container	# 在已存在的容器上运行命令
  export      Export a container's filesystem as a tar archive	
  			# 导出容器的内容流作为一个 tar 归档文件[对应 import ]
  history     Show the history of an image	# 展示一个镜像形成历史
  images      List images		# 列出系统当前镜像
  import      Import the contents from a tarball to create a filesystem image
  			# 从 tar 包中的内容创建一个新的文件系统映像[对应 export ]
  info        Display system-wide information	# 显示系统相关信息
  inspect     Return low-level information on Docker objects	# 查看容器详情信息
  kill        Kill one or more running containers	# kill 指定 docker 容器
  load        Load an image from a tar archive or STDIN	
  			# 从一个 tar 包中加载一个镜像[对应 save]
  login       Log in to a Docker registry	# 注册或者登陆一个 docker 源服务器
  logout      Log out from a Docker registry	# 从当前 docker registry 退出
  logs        Fetch the logs of a container	# 输出当前容器日志信息
  pause       Pause all processes within one or more containers	# 暂停容器
  port        List port mappings or a specific mapping for the container
  			# 查看映射端口对应的容器内部源端口
  ps          List containers	# 列出容器列表
  pull        Pull an image or a repository from a registry
  			# 从docker镜像源服务器拉取指定镜像或者库镜像
  push        Push an image or a repository to a registry
  			# 推送指定镜像或者库镜像至docker源服务器
  rename      Rename a container	# 容器重命名
  restart     Restart one or more containers	# 重启运行的容器
  rm          Remove one or more containers	# 移除一个或多个容器
  rmi         Remove one or more images	# 移除一个或多个镜像[无容器使用该镜像才可以删				除，否则需删除相关容器才可以继续 或 -f 强制删除]
  run         Run a command in a new container	# 创建一个新的容器并运行一个命令
  save        Save one or more images to a tar archive (streamed to STDOUT by 				default)	# 保存一个镜像为 tar 包[对应 load]
  search      Search the Docker Hub for images	# 在 docker hub 中搜索镜像
  start       Start one or more stopped containers	# 启动容器
  stats       Display a live stream of container(s) resource usage statistics
  			# 显示实时的容器资源使用情况统计流
  stop        Stop one or more running containers	# 停止容器
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE	
  			# 给源中镜像打标签
  top         Display the running processes of a container # 查看容器中运行的进程信息
  unpause     Unpause all processes within one or more containers	# 取消暂停容器
  update      Update configuration of one or more containers	
  			# 更新一个或多个容器的配置
  version     Show the Docker version information	# 查看 docker 版本号
  wait        Block until one or more containers stop, then print their exit 				    codes	# 截取容器停止时的退出状态值
  ```

- ### DockerFile

  - #### 用过Dockerfile构建镜像

    ```shell
    $ docker build .	# 在Dockerfile文件所在目录下执行
    ```

  - #### DockerFile的指令

    ##### FROM

    ```shell
    # 格式
    FROM [--platform=<platform>] <image> [AS <name>]
    FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
  FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
    
    # 解释
    基础镜像，一切从这里开始构建

    # eg
    FROM mysql
    FROM mysql:5.7
    ```
    
    ##### MAINTAINER（已弃用）改用 LABEL
    
    ```shell
    # 格式
    MAINTAINER <name>
      
    # 解释
    文件维护者信息，类似 docker commit 时候使用-a 参数指定的作者信息，一般是姓名+邮箱
    LABEL更加灵活，它允许设置任何元数据并通过 docker inspect 查看，当然也可以设置作者信息
      
    # eg
    MAINTAINER moyang_xyz@163.com
    LABEL maintainer="moyang_xyz@163.com"
    ```
    
      ##### RUN
    
    ```shell
    # 格式
    RUN <command> (shell 形式) 
    RUN["executable", "param1", "param2"]。 (exec 形式)
      
    # 解释
    镜像构建的时候需要运行的命令,建议使用 exec 形式 ，
    当执行的命令有 确认 输入的时候，需要在命令中增加 -y
    
    # eg
    RUN echo hello
    RUN ["echo", "hello"]
    RUN apt-get upgrade -y		# -y表示在交互中默认y
    ```
    
      ##### CMD
    
      ```shell
  # 格式
    CMD ["executable","param1","param2"] (exec 形式，首选)
    CMD ["param1","param2"] (作为ENTRYPOINT默认参数)
    CMD command param1 param2 (shell 形式)
    
    # 解释
    指定这个容器启动的时候要运行的命令，每个Dockerfile只运行一个CMD命令，
    如果指定了多条，只有最后一条会被执行，
    如果在 docker run 之后添加命令会覆盖Dockerfile中的CMD指令。
    
    # eg
    CMD echo "This is a test."
    CMD ["echo","This is a test."]
    
    CMD ["ls","-a"] Dockerfile build 镜像之后，执行 docker run 镜像id -l  会报错，
    因为执行的是 -l  而不是 ls -al
      ```
    
      ##### ENTRYPOINT

    ```shell
  # 格式
    ENTRYPOINT ["executable", "param1", "param2"]	(exec 形式)
    ENTRYPOINT command param1 param2		(shell 形式)
    
    # 解释
    指定这个容器启动的时候要运行的命令，如果在 docker run 之后添加指令会追加Dockerfile中的 ENTRYPOINT指令
    
    # eg
    ENTRYPOINT echo "This is a test."
    ENTRYPOINT ["echo","This is a test."]
    
    ENTRYPOINT ["ls","-a"] Dockerfile build 镜像之后，执行 docker run 镜像id -l 
    不会会报错，因为执行的是 ls -al  而不是 -l
    ```
    
      ##### LABEL

    ```shell
  # 格式
    LABEL <key>=<value> <key>=<value> <key>=<value>
    
    # 解释
    向镜像元数据增加信息，键值对形式
    
    # eg：
    LABEL maintainer="moyang_xyz@163.com"
    LABEL version="1.0"
    LABEL description="This is a test"
    ```
    
      ##### EXPOSE

    ```shell
  # 格式
    EXPOSE <port> [<port>/<protocol>...]
    
    # 解释
    保留端口配置，默认侦听是TCP，也可以指定UDP，EXPOSE指令实际上不会开放端口，只是预保留，如果需要开放端口，需要在 docker run 的时候增加 -p 参数
    
    # eg
    EXPOSE 80
    EXPOSE 80/udp
    ```
    
      ##### ENV

    ```shell
  # 格式
    ENV <key> <value>
    ENV <key>=<value> ...
    
    # 解释
    构建的时候设置环境变量
    
    # eg
    ENV myName John Doe
    ENV myName="John Doe"
    ```
    
      ##### ADD

    ```shell
  # 格式
    ADD [--chown=<user>:<group>] <src>... <dest>
    ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
    
    # 解释
    将宿主机(src)中的文件复制到容器(dest)中，压缩文件会自动解压， 
    
    # eg
    ADD cms.tar.gz /usr/local/ #复制解压
    ADD ["cms.tar.gz", "/usr/local/"]
    ```
    
      ##### COPY

    ```shell
  # 格式
    COPY [--chown=<user>:<group>] <src>... <dest>
    COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
    
    # 解释
    类似ADD，将我们的文件拷贝到镜像中，但不会自动解压
    
    # eg
    COPY hom* /mydir/	# 复制home路径下所有
    ```
    
    ##### VOLUME

    ```shell
  # 格式
    VOLUME ["/data"]
    
    # 解释
    指定镜像汇总挂载的目录，无法指定主机对应的目录，是自动生成的，参考docker命令volume
    
    # eg
    VOLUME /myvol
    VOLUME ["/myvol"]
    ```
    
      ##### USER

    ```shell
  # 格式:
    USER <user>[:<group>]
    USER <UID>[:<GID>]
    
    # 解释:
    指定运行容器时的用户名和 UID，后续的 RUN 指令也会使用这里指定的用户。 
    如果不输入任何信息，表示默认使用 root 用户
    
    # eg
    USER patrick
    ```
    
    ##### WORKDIR

    ```shell
  # 格式
    WORKDIR /path/to/workdir
    
    # 解释
    WORKDIR指令为Dockerfile中跟在其后的所有RUN，CMD，ENTRYPOINT，
    COPY和ADD指令设置工作目录。 
    如果WORKDIR不存在，即使以后的Dockerfile指令中未使用它，也将创建它。
    WORKDIR指令可在Dockerfile中多次使用。 
    如果提供了相对路径，则它将相对于上一个WORKDIR指令的路径
    
    # eg
    WORKDIR /a 
    WORKDIR b
    WORKDIR c
    RUN pwd 
    则最终路径为 /a/b/c。
    ```
    
      ##### ARG

    ```shell
  # 格式
    ARG <name>[=<default value>]
    
    # 解释
    ARG指令定义了一个变量，用户可以在构建时通过docker构建命令将其传递给构建器，
    使用——build- ARG <varname>=<value>标志。如果用户指定了未在Dockerfile中定义的生成参数，
    则构建将输出警告。
    
    # eg
    ARG user1
    ARG user1=someuser
    ```
    
      ##### ONBUILD

    ```shell
  # 格式
    ONBUILD <INSTRUCTION>
    
    # 解释
    触发指令，在Dockerfile文件中增加ONBUILD指令，ONBUILD指令并不会被执行，而是添加到元数据中，
    当新建DockerFile继承之前构建的镜像时，新的Dockerfile执行FROM命令的时候会执行
    被继承镜像的ONBUILD指令
    
    # eg
    ONBUILD ADD . /app/src
    ONBUILD RUN /usr/local/bin/python-build --dir /app/src
    ```
    
    
