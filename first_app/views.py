from datetime import timezone
from django.shortcuts import render,HttpResponse,redirect
import razorpay
from first_project import settings
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import commentform
from django.core.mail import send_mail





# Create your views here.
def index(request):
  image = Items_details.objects.all()
  content = homeInfo.objects.all()
  slider = homeslider.objects.all()
  latestnews = homelatestnews.objects.all()
  clientsImg = homeclients.objects.all()
  home = {
    'image' : image,
    'content' : content,
    'slider': slider,
    'latestnews': latestnews,
    'clientsImg': clientsImg
  }
 
  return render(request,'index.html',home)

def indexDemo(request):
   image = ServiceData.objects.all()
   content = homeInfo.objects.all()
   slider = homeslider.objects.all()
   latestnews = homelatestnews.objects.all()
   clientsImg = homeclients.objects.all()
   indexDemo = {
      'image' : image,
      'content' : content,
      'slider': slider,
      'latestnews': latestnews,
      'clientsImg': clientsImg,
   }
   return render(request,'indexDemo.html',indexDemo)
def about(request):
  content = aboutInfo.objects.all()
  creativeteam = aboutcreativeteam.objects.all()
  clientsImg = homeclients.objects.all()
  about = {
    'content' : content,
    'creativeteam':creativeteam,
    'clientsImg': clientsImg
  }
  return render(request,'about.html',about)
def blog(request):
  latestnews = homelatestnews.objects.all()
  indexDemo = {
      
      'latestnews': latestnews,
   
   }
  return render(request,'blog.html',indexDemo)
def contact(request):
  if request.method == 'POST':
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Phone = request.POST.get('phone')
    Subject = request.POST.get('subject')
    Message = request.POST.get('message')
    formData = contactform(name = Name, email = Email, number = Phone, service = Subject, msg = Message)
    formData.save()
    return render(request, 'thank.html')
  return render(request,'contact.html')
def birthday(request):
  return render(request,'birthday.html')

def corporate(request):
  return render(request,'corporate.html')

def D1(request):
  error_message = None
  if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        amount = (int(request.POST.get('amount')))
        totalamount = (int(request.POST.get('totalamount')))
     
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET))

        razorpay_payment = client.order.create(dict(amount=(int(amount*100)), currency='INR'))
        order_id = razorpay_payment['id']
    
        book = Booking.objects.create(
            name=name,
            number=number,
            email = email,
            amount = amount,
            totalamount = totalamount,
            order_id = order_id
        )
        book.save()
        razorpay_payment['name'] = name
        razorpay_payment['amount']= amount
        razorpay_payment['order_id'] = order_id
        form = Booking(request.POST or None)
        return render(request, 'D1.html', {'razorpay_payment': razorpay_payment})
  form = Booking()
  return render(request,'D1.html', {'form': form, 'error_message':error_message})

def payment(request):
    return render(request,"payment.html")

def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        razorpay_save = Booking.objects.get(order_id=response.get('razorpay_order_id'))
        razorpay_save.razorpay_payment_id = response.get('razorpay_payment_id')
        razorpay_save.paid = True
        razorpay_save.save()

        if razorpay_save.paid:
          email = razorpay_save.email
          amount = razorpay_save.amount
          totalamount = razorpay_save.totalamount
          client_name = razorpay_save.name
            # You can customize the email message as needed
          subject = 'Payment Successful'
          message = (
          f"Subject: Payment Confirmation for Your Booking\n\n"
          f"Dear {client_name},\n\n"
          f"We are pleased to inform you that your payment for the booking has been successfully processed. "
          f"Thank you for choosing us and placing your trust in our services!\n\n"
          f"Payment Summary:\n"
          f"- Total Booking Amount: {totalamount}\n"
          f"- Advance Payment: {amount}\n"
          f"- Pending Payment: {totalamount - amount}\n\n"
          f"If you have any questions or need further assistance, please don't hesitate to reach out. "
          f"We look forward to making your experience exceptional.\n\n"
          f"Best regards,\n"
          f"Your Model Team"
)
          sender_email = settings.EMAIL_HOST_USER # Replace with your sender email address
          recipient_email = [email]  # Convert to list if needed

          send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

          return render(request, 'success.html', {'status': True})
    except Exception as e:
        # Handle exceptions, for example, logging the error
        print(f"Error occurred: {str(e)}")
    return render(request, 'success.html', {'status': True})



def festival(request):
  return render(request,'festival.html')


def thank(request):
  return render(request,'thank.html')


def portfolio(request):
  photogallery = portphotogallery.objects.all()
  videogallery = portvideogallery.objects.all()
  videodemo =portdemo.objects.all()
  videodemo1 =portdemo1.objects.all()
  videodemo2 =portdemo2.objects.all()
  portfolio = {
    'photogallery':photogallery,
    'videogallery':videogallery,
    'videodemo':videodemo,
    'videodemo1':videodemo1,
    'videodemo2':videodemo2,
  }
  return render(request,'portfolio.html',portfolio)

def post(request):
    Data = commentform.objects.order_by('-date')[:3]
    context = {
        'data': Data,
    }

    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Date = request.POST.get('date')
        Message = request.POST.get('message')
        
        # Set the date to the current time if not provided
        if not Date:
            Date = datetime.now()

        formData = commentform(name=Name, email=Email, date=Date, msg=Message)
        formData.save()

        return redirect('post.html')  # Redirect after POST to prevent resubmission

    return render(request, 'post.html', context)



def delete_comment(request, id):
    comment = get_object_or_404(commentform, id=id)
    comment.delete()
    return redirect('post.html')


def ringceremony(request):
  return render(request,'ringceremony.html')

def special_page(request):
  return render(request,'special_page.html')
def wedding(request,header):
  items_all = Items_details.objects.filter(header = header)
  wedding = {
     "items_all":items_all,
  }
  return render(request,'wedding.html',wedding)
def services(request):
  image = Items_details.objects.all()
  textplan = servicetextplan.objects.all()
  pricingplan = servicepricingplan.objects.all()
  data = {
    'image' : image,
    'textplan':textplan,
    'pricingplan':pricingplan
  }
  return render(request,'services.html',data)
def profile(request):
  return render(request,'profile.html')
def editprofile(request):
  return render(request,'editprofile.html')








def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index.html')
        
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid Login, Try Again."))
            return redirect('login')
    
    else:
        return render(request,'login.html', {})
    





@login_required

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfull !!"))
    return redirect('index.html')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull !!"))
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request,'signup.html', {'form':form,})


@login_required
def profile_user(request):
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
            # return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'editprofile.html', {'form': form})




@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Log out the user after password change
            logout(request)
            messages.success(request, "Password changed successfully. Please log in with your new password.")
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'changepassword.html', {'form': form})


def booking(request):
    error_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        client = razorpay.Client(auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        razorpay_payment = client.order.create(dict(amount=(int(100)), currency='INR'))
        order_id = razorpay_payment['id']
    
        book = Booking.objects.create(
            name=name,
            number=number,
            email = email,
            amount = 100,
            order_id = order_id
        )
        book.save()
        razorpay_payment['name'] = name
        razorpay_payment['amount']= 100
        razorpay_payment['order_id'] = order_id
        form = Booking(request.POST or None)
        return render(request, 'D1.html', {'razorpay_payment': razorpay_payment})
    form = Booking()
    return render(request,'D1.html', {'form': form, 'error_message':error_message})