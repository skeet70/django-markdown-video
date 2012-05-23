Django Markdown Video
=====================

Hoping to establish a github presence for this great little python-markdown extension by Tyler Lesmann(http://code.google.com/p/python-markdown-video/), to keep it modern. It's incorporated into a little django templatetag for ease of use, as well as giving some markItUp examples.

Examples
---------

A simple markdown templatetag for django users has been added. This enables embedding of video using markdown like so, 
**|video|(http://www.youtube.com/watch?v=fFO-Y7NfqMg&feature=g-all-u)** which when rendered with...

```html
{% load markdown_video %}

{{ post.body|video|markdown }}
```

would produce...

```html
Need to update, personal project is currently broken.
```

All you actually need for this to work is mdx-video.py somewhere in your python path. If you have that it will
enable funcionality such as (copied from original):

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

Blip.tv
Dailymotion
Gametrailers
Metacafe
Veoh
Vimeo
Yahoo! video
Youtube

> NOTE: Blip.tv works a little differently than the others because there is no way to construct a working object with the player URL. Instead of the URL to the Blip.tv page, you will use the URL to the flv file, like http://blip.tv/file/get/Pycon-DjangoOnJython531.flv for example. This is located in Files and Links section of Blip.tv.