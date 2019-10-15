#-*- coding: utf-8 -*-
from . import utils
from socket  import *
from host_port import * #-
import atexit

s = socket(AF_INET, SOCK_STREAM)

def connect():
	#Starts server
	s.connect((HOST, PORT)) # connect to server (block until accepted)
	print("conected")
	atexit.register(exit_handler)
	pass

def exit_handler():
    print("desconected")
    s.close()

def __del__():
	#Ends server
	print("desconected")
	s.close()


class TupleSpace:

	def __init__(self, **kwargs):
		if kwargs and len(kwargs) == 1 and "blog_name" in kwargs:
			#parametros corretos
			self.blog_name = kwargs["blog_name"]
		else:
			self.blog_name = ""

		self.dictionary = {}


	def _rd(self, t):
		"""
			:param publisher: name of the author of the message
			:param topic: name of the topic on which the message will be published
			:param type_return: tyoe of the message to be read
			:return:
		"""
		publisher, topic, type_return = t
		print("\nReading messages from {} at {}".format(publisher, topic))

		# Making tuple
		msg_send = utils.tuple_to_bin((publisher, topic, type_return), "rd")
		s.send(msg_send)	
		tuple_list_bin = b''
		r = b''
		while r.decode() != "." :
			tuple_list_bin+=r
			r = s.recv(1)
		tuple_list = utils.bin_to_tuple(tuple_list_bin, has_op=False)
		if tuple_list:
			messages = ""
			for tpl in tuple_list:
				messages += "Topic " + tpl[1] + " " + tpl[0] + " said: " + tpl[2] + "\n"
				print("Topic " + tpl[1] + " " + tpl[0] + " said: " + tpl[2] + "\n")
			return messages
		else:
			print(publisher + " didn't published in this topic or " + topic + " doesn't exist")
			return publisher + " didn't published in this topic or " + topic + " doesn't exist"
    
	def _in(self, t):
		"""
			:param publisher: name of the author which message will be deleted 
			:param topic: name of the topic on which the message will be deleted
			:param type_return: message to be deleted
			:return:
		"""
		publisher, topic, content = t
		print("\nDeleting message '{}' from {} at {}".format(content, publisher, topic))
		# Making tuple
		msg_send = utils.tuple_to_bin((publisher, topic, content), "in")
		s.send(msg_send)

		r = s.recv(1)

		if r == b"0":
			print("\nMessage doesn't exist in topic")
			return content + " doesn't exist in topic " + topic
		else:
			print("\nMessage deleted!")
			return "Deleting message '{}' from {} at {}".format(content, publisher, topic)

	def _out(self, t):
		"""
			:param publisher: name of the author
			:param topic: name of the topic on which the message will be posted 
			:param content: message 
			:return:
		"""
		publisher, topic, content = t
		print("\nWriting message '{}' from {} at {}".format(content, publisher, topic))

		# Making tuple
		msg_send = utils.tuple_to_bin((publisher, topic, content), "out")
		s.send(msg_send)  # send some data

		return "Writing message '{}' from {} at {}".format(content, publisher, topic)


	def set_name(self, new_name):
		if new_name or new_name is not None:
			self.blog_name = new_name

class Universe():
	def __init__(self):
		pass
	
	def _rd(self, t):

		blog_name, tuplespace_class = t

		if tuplespace_class == TupleSpace:
			tuplespace = tuplespace_class(blog_name=blog_name)

		return "", tuplespace

	def _out(self, t):
		blog_name, tuplespace = t
		tuplespace.set_name(blog_name)
		pass

# Universo
universe = Universe()
