from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.core.files.storage import FileSystemStorage
from .forms import QuizUploadForm
from .models import Quiz
import sys
import time
from django.http import HttpResponse, HttpResponseRedirect


dirPath = './copyleaks'
if dirPath not in sys.path:
    sys.path.insert(0, dirPath)

from copyleakscloud import CopyleaksCloud
from processoptions import ProcessOptions
from product import Product

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created ! You are now able to login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form': form})

	
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()	
			messages.success(request,f'Your account has been updated! ')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)	

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)



def materialpage(request):
	return render(request,'users/materialpage.html')
	

def quizzing(request):
	return render(request,'users/quizzing.html')

"""def handle_uploaded_file(f):
	with open('some/file/name.txt','wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return render('profile')

		else:
			form = UploadFileForm()
			return render(request,'quizpage.html',{'form': form})			"""

def upload(request):
	context = {}
	if request.method == "POST":
		form = QuizUploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render(request,'users/profile.html',context)

	else:
			form = QuizUploadForm()
	return render(request,'users/upload.html',{'form': form})			

def quizfiles(request):
	quizs = Quiz.objects.all()
	return render(request,'users/quizfiles.html',{'quizs': quizs})	


def doubts(request):
	return render(request,'users/doubts.html')

def index(request):
	return render(request,'users/index.html')

def game(request):
	return render(request,'users/game.html')

def highscores(request):
	return render(request,'users/highscores.html')


def end(request):
	return render(request,'users/end.html')




def plag(request):
	#if request.method == 'POST':
		cloud = CopyleaksCloud(Product.Businesses, 'diksharaj78@gmail.com', 'D086DF39-6538-41F2-B025-C50AEEFF7846')
		print("You've got %s Copyleaks %s API credits" % (cloud.getCredits(), cloud.getProduct())) #get credit balance
		options = ProcessOptions()
		options.setSandboxMode(True)
		print("Submitting a scan request...")
		#process = cloud.createByUrl('https://copyleaks.com', options)

		process = cloud.createByText("Lorem ipsum torquent placerat quisque rutrum tempor lacinia aliquam habitant ligula arcu faucibus gravida, aenean orci lacinia mattis purus consectetur conubia mauris amet nibh consequat turpis dictumst hac ut nullam sodales nunc aenean pharetra, aenean ut sagittis leo massa nisi duis nullam iaculis, nulla ultrices consectetur facilisis curabitur scelerisque quisque primis elit sagittis dictum felis ornare class porta rhoncus lobortis donec praesent curabitur cubilia nec eleifend fringilla fusce vivamus elementum semper nisi conubia dolor, eros habitant nisl suspendisse venenatis interdum nulla interdum, libero urna maecenas potenti nam habitant aliquam donec class sem hendrerit tempus.")
		print ("Submitted. In progress...")
		iscompleted = False
		while not iscompleted:
			[iscompleted, percents] = process.isCompleted()
			print ('%s%s%s%%' % ('#' * int(percents / 2), "-" * (50 - int(percents / 2)), percents))
			if not iscompleted:
				time.sleep(2)
		print ("Process Finished!")
		results = process.getResults()
		print ('\nFound %s results...' % (len(results)))
		for result in results:
			print('')
			print('------------------------------------------------')
			print(result)
			return render(request,'users/plag.html',{'result':result})





    # Available process options
#     options.setHttpCallback("http://yoursite.here/callback")
#     options.setHttpInProgressResultsCallback("http://yoursite.here/callback/results")
#     options.setEmailCallback("Your@email.com")
#     options.setCustomFields({'Custom': 'field'})
#     options.setAllowPartialScan(True)
#     options.setCompareDocumentsForSimilarity(True)  # Available only on compareByFiles
#     options.setImportToDatabaseOnly(True)  # Available only on Education API