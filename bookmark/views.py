from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404

from .models import t_tag
from .models import t_url
from .models import t_url_tag

#from bs4 import BeautifulSoup
from  BeautifulSoup import BeautifulSoup
import requests
import urllib2

from django.http import JsonResponse
from django.core import serializers
import json


def destroyBookmark(request):
	URLID = int(str((request.POST['URLID'])))
	obj = t_url.objects.filter(URLID=URLID).delete()
	return HttpResponseRedirect('../')


def destroyTag(request):
	TagID = int(str((request.POST['TagID'])))
	obj = t_tag.objects.filter(TagID=TagID).delete()
	return HttpResponseRedirect('../')



def searchBookmark(request):
	
	print "searchBookmark"
	Tag =str(request.POST['tag'])
	print Tag
	
	tag_list = t_tag.objects.filter(Tag=Tag)
	

	TagIDList = []
	for tag_row in tag_list:
		TagID = int(str(tag_row.TagID))

		TagIDList.append(TagID)

	#print "TagIDList", TagIDList
	
	URLTaglist = t_url_tag.objects.filter(TAGID__in=TagIDList)


	URLIDList = []

	for tag_url_row in URLTaglist:
		URLID = int(str(tag_url_row.URLID))
		URLIDList.append(URLID)

	#print "URLIDList", URLIDList
	

	URLList = t_url.objects.filter(URLID__in=URLIDList)

	#print "URLList", URLList

	data = serializers.serialize('json', URLList, fields=('URLID','URL'))
	
	datadict = {}

	for URLrow in URLList:
		datadict[URLrow.URLID] = URLrow.URL

	jsonData = json.dumps(datadict)

	return JsonResponse(jsonData, safe=False)


def addBookmark(request):
	addstring =  str(request.POST['urltag'])
	addstring =  addstring.split(',')
	
	URL = str(addstring[0])

	# insert URL and store URLID in URLID variable 	
	objURL = t_url.objects.create(URL=URL)
	objURL.save()
	URLID = objURL.URLID
	u = t_url.objects.only('URLID').get( URLID=URLID )

	#insert or get Tag obj
	for Tag in addstring[1:]:
		Tag = str(Tag)
		objTag, tagCreated = t_tag.objects.get_or_create(Tag=Tag)
		objTag.save()
		TagID = objTag.TagID
		t = t_tag.objects.only('TagID').get(TagID= TagID)
		obj = t_url_tag.objects.create( URLID=u, TAGID=t )
		obj.save()

	return HttpResponseRedirect('../')


def updateBookmarkAndShow(request, url_id):
	print request.POST

	#newTag =  str(request.POST['newTag'])
	updatedURL = str(request.POST['updatedURL'])
	TagIDList = request.POST.getlist('selectedIds[]')

	obj = t_url_tag.objects.filter(URLID=int(str(url_id))).delete()
	url_id = str(url_id)

	#user = User.objects.only('id').get(id=data['user_id'])

	u = t_url.objects.only('URLID').get( URLID=url_id )
	print type(u), u

	for TagID in TagIDList:
		tag_id = str(TagID)
		t = t_tag.objects.only('TagID').get(TagID= tag_id)
		print type(t), t
		obj = t_url_tag.objects.create( URLID=u, TAGID=t )
		obj.save()

	return HttpResponseRedirect('/bookmark/' + str(url_id) +'/')

def editURL(request, url_id):
	tag_list =  t_tag.objects.all()
	url_list = t_url.objects.filter(URLID=url_id)
	if (len(url_list) < 1):
		raise Http404("Page not found")
	tag_associated_list = t_url_tag.objects.filter(URLID=url_id)

	for url_row in url_list:
		url = str(url_row.URL)
	print url

	TagIDList = []

	for tag_row in tag_associated_list:
		TagID = int(str(tag_row.TAGID))
		TagIDList.append(TagID)

	print TagIDList

	context = {
		'TagIDList':TagIDList,
		'tag_list':tag_list,
		'URL':url,
		'URLID':url_id,
		'tag_associated_list':tag_associated_list,
	}
	return render(request, 'bookmark/editURL.html', context)

def updateTagAndShow(request, tag_id):
	if (request.method == 'POST'):
		updatedTag =  str(request.POST['updatedTag'])

		obj = t_tag.objects.get(TagID=tag_id)
		obj.Tag = updatedTag
		print obj
		obj.save()
	return HttpResponseRedirect('/tags/' + str(tag_id) +'/')

def editTag(request, tag_id):
	tag_list =  t_tag.objects.filter(TagID=tag_id)
	if (len(tag_list) < 1):
		raise Http404("Page not found")

	for tag_row in tag_list:
		Tag = str(tag_row.Tag)
		TagID = int(str(tag_row.TagID))
	
	context = {
		'Tag': Tag,
		'TagID':TagID,
	}
	return render(request, 'bookmark/editTag.html', context)

def insertTagAndShow(request):
	if (request.method == 'POST'):
		newTag =  str(request.POST['newTag'])
		obj = t_tag.objects.create(Tag=newTag)
		obj.save()
		print obj.TagID
	return HttpResponseRedirect('/tags/' + str(obj.TagID))

def addTag(request):
	context = {}
	return render(request,'bookmark/addTag.html', context)


def showTags(request):
	tag_list =  t_tag.objects.all()
	context = {
	'tag_list': tag_list,
	}
	return render(request,'bookmark/tags.html', context)

def showTag(request, tag_id):
	tag_list =  t_tag.objects.filter(TagID=tag_id)
	if (len(tag_list) < 1):
		raise Http404("Page not found")

	isNewTag = False
	context = {
	'isNewTag': isNewTag,
	'tag_list': tag_list,
	}
	return render(request,'bookmark/tag.html', context)


def showHome(request):
	
	url_list = t_url.objects.all()
	tag_list = t_tag.objects.all()
	url_tag_list = t_url_tag.objects.all()
	context = {
		'url_list': url_list,
		'tag_list': tag_list,
		'url_tag_list': url_tag_list,
	}
	return render(request,'bookmark/index.html', context)


def showDetails(request, url_id):
	url_list = t_url.objects.filter(URLID=url_id)
	url_tag_list = t_url_tag.objects.filter(URLID=url_id)
	tag_list = t_tag.objects.all()
	tags = []

	if(len(url_list) <1):
		raise Http404("Page not found")
		return None

	for url_tag_row in url_tag_list:
		for tag_row in tag_list:
			a= int(str(tag_row.TagID))
			b = int(str(url_tag_row.TAGID))
			if( a == b):
				#print a, type(a)
				tags.append(str(tag_row.Tag)) 

	for url_row in url_list:
		url  = str(url_row.URL)

	urlPage = BeautifulSoup(urllib2.urlopen(url))
	if(urlPage.title == None):
		title = 'No title'
	else:
		title = urlPage.title.string

	tag_list = tags

	context = {
		'url_list': url_list,
		'tag_list': tag_list,
		'title': title,
	}
	return render(request,'bookmark/urldetails.html', context)

