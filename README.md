# elf

the magic tool to browse application filesystem on Predix.io

## Deploy
```
$ git clone https://github.com/pxie/elf.git
$ cd elf
$ cf push

* ignore part output during cf push*

requested state: started
instances: 1/1
usage: 256M x 1 instances
urls: elf-subaural-crowdy.run.aws-jp01-pr.ice.predix.io   <-- URL is here
last uploaded: Wed Apr 12 07:43:03 UTC 2017
stack: cflinuxfs2
buildpack: https://github.com/cloudfoundry/python-buildpack.git

     state     since                    cpu    memory          disk             details
#0   running   2017-04-12 03:44:22 PM   0.0%   70.3M of 256M   163.7M of 256M
```

## Usage

* go to browser, type the URL returned from `cf push` command.
  * For example, `https://elf-subaural-crowdy.run.aws-jp01-pr.ice.predix.io`. **https://** protocol is required
* elf will return the results of shell command, `ls -l /`
* and you browse any folder via path.
  * For example, to browse `/bin` folder, type `https://elf-subaural-crowdy.run.aws-jp01-pr.ice.predix.io/bin`
* enjoy!
