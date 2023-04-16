# ScrappingAppSumo

## Dependencies: 
```
attrs==22.2.0
Automat==22.10.0
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==3.1.0
constantly==15.1.0
cryptography==40.0.2
cssselect==1.2.0
filelock==3.11.0
greenlet==2.0.1
hyperlink==21.0.0
idna==3.4
incremental==22.10.0
itemadapter==0.8.0
itemloaders==1.0.6
jmespath==1.0.1
lxml==4.9.2
packaging==23.1
parsel==1.7.0
Protego==0.2.1
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.21
PyDispatcher==2.0.7
pyee==9.0.4
pyOpenSSL==23.1.1
queuelib==1.6.2
requests==2.28.2
requests-file==1.5.1
Scrapy==2.8.0
scrapy-playwright==0.0.26
service-identity==21.1.0
six==1.16.0
tldextract==3.4.0
Twisted==22.10.0
typing_extensions==4.5.0
urllib3==1.26.15
w3lib==2.1.1
zope.interface==6.0
```

All of the above dependencies can be installed by: 
- ``` pip install python3 ```
- ``` pip3 install scrapy ```
- Activating the virtual environment.

### In order to run the spider and generate a csv file as an output: 
- ``` scrapy crawl sumo_spider -O results.csv  ```
