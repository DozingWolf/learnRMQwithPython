# centos7 rabbit mq 部署手册
## https://packagecloud.io/rabbitmq
1. 安装依赖支持

    sudo yum install -y gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf java-1.8.0-openjdk-devel git

2. 下载erlang源码并解压

    #省略cd路径，自行注意
    wget http://erlang.org/download/otp_src_20.2.tar.gz
    tar -zvxf otp_src_20.2.tar.gz

3. 编译安装erlang

    cd otp_src_20.2/
    ./otp_build autoconf
    ./configure && make && sudo make install

4. 完成后检查下erlang安装

    erl

***完成erlang安装，进行mq部署***

5. 安装socat

    yum install -y socat

6. 从官方下载rpm包并安装

    rpm -Uvh https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.7.3/rabbitmq-server-3.7.3-1.el7.noarch.rpm

7. 安装RPM包，可能需要--nodeps强制不检查依赖参数

    rpm -Uvh rabbitmq-server-3.7.3-1.el7.noarch.rpm  --nodeps

8. 检查网络策略，添加防火墙策略

    firewall-cmd --permanent --add-port=15672/tcp
