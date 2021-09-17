from django.shortcuts import render


# Create your views here.
def CandidateRegister(request):
    return render(request, 'accounts/candidate-register.html')


def RecruiterRegister(request):
    return render(request, 'accounts/recruiter-register.html')    



def RecruiterLogin(request):
    return render(request, 'accounts/recruiter-login.html')



def CandidateLogin(request):
    return render(request, 'accounts/candidate-login.html')        

