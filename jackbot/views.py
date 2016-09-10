from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
# Create your views here.
VERIFY_TOKEN='7thsep2016'
PAGE_ACCESS_TOKEN ='EAAZAmgNlvlm8BADe3cBcDQZAvaWb4uivxgbKavBzm6DefYmhFSQfGDvvC0ZAWJMjSaoVhVZANZAKZAbBbSamyeSFuPzXZAelNRnP6jNtZCgy7jID0tYJdZBN5fubQcUaHtzxFCemltFM0liqPb5pJZBsWZBekU68t3qvw3mGpCzBxBz6wZDZD'
def post_facebook_message(fbid,message_text):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	# print status.json()
class MychatbotView(generic.View):
	def get(self,request,*args,**kwargs):
		if self.request.GET['hub.verify_token']==VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])

		else :
			return HttpResponse('oops invalid session')


	global messagelist
	messagelist=['this is nipun']
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self,request,*args,**kwargs)
	def post (self,request,*args,**kwargs):
		incoming_message=json.loads(self.request.body.decode('utf-8'))
		print 'the incoming message is:',incoming_message
		requestcount=1
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				print 'the request count is',requestcount
				requestcount=requestcount+1
				print 'the sender id is',message['sender']['id']
				try:
					sender_id = message['sender']['id']
					#print 'the sender id is working'
					message_text =messagelist[0]
					#message['message']['text']
					messagelist.pop()
					# print '*' * 8
					# print 'this is the message text',message_text
					post_facebook_message(sender_id,message_text) 
				except Exception as e:
				 	#print e
				 	print 'this is an error'
					pass

		return HttpResponse()  
	
def index(request):
	print 'this is me'
	return HttpResponse()
