from django import template
from django.template.defaultfilters import stringfilter
import markdown, re

register = template.Library()


def replace_tag(matchobj):
	if matchobj.group(1) not in [None, '']:
		return markdown.markdown(matchobj.group(1),['video'])

@register.filter
@stringfilter
def video(value):
   """Tag used to add video support to a markdown formatted string.
      Best use is ``|safe|markdown:"safe"|video``, and the markdown
      format is |video|(http://path/to/video). It will use mdx_video.py
      to handle embedding the video from a variety of sources."""
   new_body = re.sub(r'\|video\|\((.*?)\)', replace_tag, value)
   return new_body
