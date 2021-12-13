# github基本使用

#### 1. github注册账号
#### 2. 本地安装git
```bash
	sudo apt-get update  
	sudo apt-get install git
	# 下载地址：https://git-scm.com/downloads
```

#### 3. 初始化目录 在需要git的目录下，建立本地git库
	git init

#### 4. 创建SSH Key（~/.ssh.id_rsa) 并将id_rsa.pub(公钥)添加到GitHub上
```bash
	ssh-keygen -t rsa -C "youremail@example.com"
	#添加页面：（登录GitHub-个人信息-设置-SSH&GPG keys-New SSH key）
	#	名称任意
```

#### 5. 验证是否连接成功
	ssh -T git@github.com

### 建立本地库与github关联
#### 6. 本地配置github
```bash
	git config --global user.name 'WaxRain'
	git config --global user.email 'haoyucomeon@163.com'
	git config --global credential.helper cache  
	git config --global credential.helper 'cache --timeout=3600' 缓存中存在的时间
	# 查看配置信息：
	git config --list 
```

### 本地目录下关联远程repository及其取消方法
```bash
	git remote add origin git@github.com:git_username/repository_name.git
	git remote remove origin
       ------ 其中 origin为其后整个路径的简称， 及在本地即可用origin替代所关联的远程repo，亦可使用其他易于记忆及理解的名称
```

##### 删除.git 文件夹即可回归普通路径