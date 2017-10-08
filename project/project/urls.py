"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    url(r'^app/',include('app.urls')),
    url(r'^admin/', admin.site.urls),
]

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import string
import random
from app import models #
from django.conf import settings

sched=BlockingScheduler()

logging.basicConfig()

@sched.scheduled_job("cron",second="*/20")

#models.Salts.objects.create(content="ABCDEFGH") ##

#log=logging.getLogger('apscheduler.executors.default')
#	log.setLevel(logging.INFO)
#	fmt=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
#	h=logging.StreamHandler()
#	h.setFormatter(fmt)
#	log.addHandler(h)

#logging.basicConfig()

def mytask():
#	print "now is '%s' " %datetime.datetime.now()
#	logging.basicConfig()
#	models.Salts.objects.create(content="ABCDEFGH") ##
	salt=''.join(random.sample(string.ascii_letters+string.digits,8))
	print salt
	settings.SALT=salt
	print settings.SALT	
#	models.Salts.objects.filter(pk=1).update(content=salt)
#	result=models.Salts.objects.filter(pk=1).first()
#	print result

sched.start()
