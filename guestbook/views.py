from django.shortcuts import render_to_response, get_object_or_404
from guestbook.models import Comments
from django.template.context import RequestContext
from guestbook.forms import AddCommentForm, SearchForm
from django.http import HttpResponseRedirect

def index(request):
    form = AddCommentForm()
    nickname = None
    
    if "nickname" in request.session:
        nickname = request.session["nickname"]
        all_comments = Comments.objects.all().filter(nickname__icontains=nickname).order_by('-pub_date')
    else:
        all_comments = Comments.objects.all().filter().order_by('-pub_date')        
    
    search_form = SearchForm(initial={'nickname': nickname})
    message = None
    if "message" in request.session:
        message = request.session["message"]
        del request.session["message"]
    
    return render_to_response('guestbook/index.html', {'all_comments': all_comments, 'message':message, 'form':form, 'search_form':search_form}, context_instance=RequestContext(request))

def add(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid(): 
            form.save()
        else:
            request.session["message"] = "Valid form error"

    return HttpResponseRedirect('/guestbook/')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            request.session["nickname"] = form.cleaned_data['nickname']
        else:
            if "nickname" in request.session:
                del request.session["nickname"]
    return HttpResponseRedirect('/guestbook/')

def detail(request, com_id):
    p = get_object_or_404(Comments, pk=com_id)
    return render_to_response('guestbook/detail.html', {'com': p})
