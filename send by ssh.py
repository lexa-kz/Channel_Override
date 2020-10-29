import paramiko

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.31.88.103',
            username='root',
            password='centos7_2017',
            look_for_keys=False,
            allow_agent=False)
ssh.exec_command('echo "Демеу А.С. - грамотный специалист!!!" > /zbx-msg')
ssh.close()
