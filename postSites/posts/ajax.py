from django.shortcuts import get_object_or_404
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils import timezone

from posts.models import Post, Form

@dajaxice_register(method='GET')
def dajaxice_example(request,text):
    return simplejson.dumps({'message':'Your message is %s!' % text})

@dajaxice_register(method='GET')
def addPost(request, text):
	content = text
	post = Post(content=content, pub_date=timezone.now())
	post.save();
	return simplejson.dumps({'message':'Post Added'})

@dajaxice_register(method='GET')
def addComment(request,postID, text):
	post_id = postID;
	content = text
	post = get_object_or_404(Post,pk=post_id)
	comment = post.comment_set.create(content=content, pub_date=timezone.now())
	post.save()
	return simplejson.dumps({'message':'Comment Added','id':post_id})
