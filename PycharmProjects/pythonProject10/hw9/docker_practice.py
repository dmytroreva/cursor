1. Save the ubuntu images to a tar/zip archive and then extract the layers and metadata files from them.(Tip: use `docker save -o` command)


dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
cowsay       latest    8276cce3dff5   40 hours ago   149MB
flask_v2     latest    92a23939a32f   42 hours ago   422MB
flask        latest    5bd14cfe75ed   43 hours ago   422MB
ubuntu       20.04     7e0aa2d69a15   4 weeks ago    72.7MB
ubuntu       latest    7e0aa2d69a15   4 weeks ago    72.7MB

dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker save -o ubuntu.tar ubuntu

dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ ls -sh ubuntu.tar
72M ubuntu.tar

dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ mkdir ubuntu && tar -xvf ubuntu.tar -C ./ubuntu
2ae7aa944634fefcfd5b886827d742268228e070238fb405b4d846b266060dbb/
2ae7aa944634fefcfd5b886827d742268228e070238fb405b4d846b266060dbb/VERSION
2ae7aa944634fefcfd5b886827d742268228e070238fb405b4d846b266060dbb/json
2ae7aa944634fefcfd5b886827d742268228e070238fb405b4d846b266060dbb/layer.tar
6e04f1f804d0d621b5a098dc2ecb5bcc7515cdf7f13d530a12fab11a194cfc72/
6e04f1f804d0d621b5a098dc2ecb5bcc7515cdf7f13d530a12fab11a194cfc72/VERSION
6e04f1f804d0d621b5a098dc2ecb5bcc7515cdf7f13d530a12fab11a194cfc72/json
6e04f1f804d0d621b5a098dc2ecb5bcc7515cdf7f13d530a12fab11a194cfc72/layer.tar
7e0aa2d69a153215c790488ed1fcec162015e973e49962d438e18249d16fa9bd.json
f3f2ad580f7e6eb71163e45a6cbef2d6b82377e274e5193ff5708f506e9322bc/
f3f2ad580f7e6eb71163e45a6cbef2d6b82377e274e5193ff5708f506e9322bc/VERSION
f3f2ad580f7e6eb71163e45a6cbef2d6b82377e274e5193ff5708f506e9322bc/json
f3f2ad580f7e6eb71163e45a6cbef2d6b82377e274e5193ff5708f506e9322bc/layer.tar
manifest.json
repositories
dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker load -i ubuntu.tar
ccdbb80308cc: Loading layer  75.07MB/75.07MB
63c99163f472: Loading layer  15.36kB/15.36kB
2f140462f3bc: Loading layer  3.584kB/3.584kB
Loaded image: ubuntu:20.04
Loaded image: ubuntu:latest

dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       20.04     7e0aa2d69a15   4 weeks ago   72.7MB
ubuntu       latest    7e0aa2d69a15   4 weeks ago   72.7MB
serhii@serhii-X540NV:~/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$


2*. Run a container that outputs the current date and time in Rome. Should be only Dockerfile.

dmytro@dmytro-Aspire-ES1-571:~$/PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker build . -t time_in_rome
Sending build context to Docker daemon  150.2MB
Step 1/2 : FROM ubuntu
 ---> 7e0aa2d69a15
Step 2/2 : CMD TZ="Italy/Rome" date
 ---> Running in 7fb0a6a0933f
Removing intermediate container 7fb0a6a0933f
 ---> 4bb43fd86b64
Successfully built 4bb43fd86b64
Successfully tagged time_in_rome:latest

dmytro@dmytro-Aspire-ES1-571:~$ /PycharmProjects/Cursor-HW-Advansed/HW9_Docker-practice$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED         SIZE
time_in_rome   latest    4bb43fd86b64   8 seconds ago   72.7MB
ubuntu         20.04     7e0aa2d69a15   4 weeks ago     72.7MB
ubuntu         latest    7e0aa2d69a15   4 weeks ago     72.7MB





