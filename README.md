Django Markdown Video
=====================

Python-markdown-video allows for embedding video in markdown formatted text.
Original python-markdown extension by Tyler Lesmann(http://code.google.com/p/python-markdown-video/)
This app incorporates the extension into a django filter for ease of use, as well as giving some markItUp examples.

Examples
---------

A simple markdown templatetag for django users has been added. This enables embedding of video using markdown like so,

```
|video|(http://www.youtube.com/watch?v=fFO-Y7NfqMg&feature=g-all-u)
```

which when rendered with...

```html
{% load markdown_video %}

{{ post.body|markdown:"safe"|video|safe }}
```

would produce...

```html
<object data="http://www.youtube.com/v/fFO-Y7NfqMg&amp;amp" height="344" type="application/x-shockwave-flash" width="425">
   <param name="movie" value="http://www.youtube.com/v/fFO-Y7NfqMg&amp;amp"></param>
   <param name="allowFullScreen" value="true"></param>
</object>
```

All you actually need for the base functionality to work (not the templatetags) is mdx-video.py somewhere in your python path (such as you webapp root, where your settings.py file is). If you have that it will enable funcionality such as (copied from original):

The following code...

```python
import markdown
url = "http://www.youtube.com/watch?v=ZlpbprBeN5M&hd=1"
markdown.markdown(url, ['video'])
```

...produces this HTML minus indenting and newlines.

```html
<p>
    <object data="http://www.youtube.com/v/ZlpbprBeN5M&amp;hd=1" height="344" 
        type="application/x-shockwave-flash" width="425">
        <param name="movie"
            value="http://www.youtube.com/v/ZlpbprBeN5M&amp;hd=1" />
        <param name="allowFullScreen" value="true" />
    </object>
</p>
```

You can also define the size of the object like so:

```python
markdown.markdown(url, ['video(youtube_width=853,youtube_height=505)'])
```

This extension supports the following services:

```
Blip.tv
Dailymotion
Gametrailers
Metacafe
Veoh
Vimeo
Yahoo! video
Youtube
```

> NOTE: Blip.tv works a little differently than the others because there is no way to construct a working object with the player URL. Instead of the URL to the Blip.tv page, you will use the URL to the flv file, like http://blip.tv/file/get/Pycon-DjangoOnJython531.flv for example. This is located in Files and Links section of Blip.tv.