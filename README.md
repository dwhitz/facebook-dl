# facebook-dl
> Download facebook videos from your terminal

<p align="center">
<a href="https://asciinema.org/a/CBMOA9wlR4D4jULgCmD0o4VNY">
<img src="https://camo.githubusercontent.com/b7ff10e98daf50d02cf1a2bf95fb964369531475/68747470733a2f2f61736369696e656d612e6f72672f612f3237323738312e737667">
</a>
</p>

## :floppy_disk: Installation

```bash
# clone the repo
$ git clone https://github.com/dwhitz/facebook-dl

# install the requirements
$ pip3 install -r requirements.txt
```

## :hammer: Usage
```
usage: 

single video: facebook-dl.py url [resolution]

No space between commas
bulk videos: facebook-dl.py url1,url2,url3 [resolution]
```

---
Download video in High Definition.
```bash
$ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/ hd
$ python3 facebook-dl.py https://www.facebook.com/adidasoriginals/videos/1298703840302845/,https://www.facebook.com/adidasoriginals/videos/327766521427078/ hd
```
OR
```bash
# Without mentioning the resolution will also download in HD
single: $ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/
bulk: $ python3 facebook-dl.py https://www.facebook.com/adidasoriginals/videos/1298703840302845/,https://www.facebook.com/adidasoriginals/videos/327766521427078/
```
Download video in Standard Definition.
```bash
single: $ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/ sd
bulk: $ python3 facebook-dl.py https://www.facebook.com/adidasoriginals/videos/1298703840302845/,https://www.facebook.com/adidasoriginals/videos/327766521427078/ sd
```
Your videos will be downloaded in *fb_videos* folder

## :scroll: License
MIT License

Copyright (c) 2019 Dwhitz
