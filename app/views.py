from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost

# Create your views here.

job_title = [
    "first job","second job"
]
job_descroption = [
    "first job desc","second job desc "
]


def hello(requset):
    return HttpResponse("Hello text")

def jobs_list(request ):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail',args=(job_id,))
    #     # print(reverse('jobs_detail',args=(job_id,)))        
    #     list_of_jobs += f"<li> <a href ='job/{job_id}'>{j}</a></li>"
    # list_of_jobs += '</ul>'
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    # context= {"job_title_lsits":job_title}
    context = {"jobs":jobs}
    return render(request,"app/index.html",context)

def jobs_detail(request , id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # context = {"job_title":job_title[id],"job_description":job_descroption[id]}
        job = JobPost.objects.get(id = id)
        context = {"job":job}
        return render(request,"app/job_detail.html",context)
        
        # return_html = f"<h1> {job_title[int(id)]} data={job_descroption[int(id)]}</h1>"
    except:
        return HttpResponseNotFound("not found")


    # return HttpResponse(f"Job detail name {id} ")
    # return HttpResponse(return_html)

class tempClass:
    x =233;

def hello (request):
    # template = loader.get_template('hello.html')
    is_authentication = False
    ages = 23
    temp = tempClass()
    list = ["rajesh", "kamleshh"]
    context  = {"age":ages , "temp_object":temp , "first_list":list , "name":"cjoram" ,"is_authentication":is_authentication  }
    return render (request,"app/hello.html",context )
    # return HttpResponse(template.render(context,request))
