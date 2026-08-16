# from django.shortcuts import render,redirect
# from django.db.models import Q
# from .models import Student
# from django.contrib import messages


# # Create your views here.
# def indexPage(request):
#     return render(request, "pages/index.html")


# # ==================for students_page===============
# def student(request):
#     if request.method == "POST":
#         data = request.POST
#         print(data)
        
#         #  to accept data from form
#         fn = request.POST["first_name"]
#         ln = request.POST["last_name"]
#         em = request.POST["email"]
#         age = request.POST["age"]
#         bio = request.POST["bio"]
#         phone = request.POST["phone_number"]
#         gen = request.POST["gender"]
#         sub = request.POST["subjects"]
        
#         obj = Student.objects.create(
#             first_name = fn,
#             last_name = ln,
#             email = em,
#             age = age,
#             bio = bio,
#             phone_number = phone,
#             gender = gen,
#             subjects = sub,            
#         )
#         print(obj)
#         obj.save()
        
#     return render(request, "pages/addStudent.html")

# # =================== studentList ========================
# def studentList(request):
#     searched = request.GET.get("searched", "")
    
#     if searched:
#         student = (
#             Student.objects.filter(first_name__icontains=searched) |
#             Student.objects.filter(last_name__icontains=searched) |
#             Student.objects.filter(email__icontains=searched) |
#             Student.objects.filter(phone_number__icontains=searched)
#         ).distinct()
#     else:
#         student = Student.objects.all()
        
# # ================
#     # if searched:
#     #     student = Student.objects.filter(
#     #         Q(first_name__icontains=searched) |
#     #         Q(last_name__icontains=searched) |
#     #         Q(email__icontains=searched) |
#     #         Q(phone_number__icontains=searched)
#     #     )
    
#     return render(request, "pages/studentList.html", {"stud": student})

# # =======================Delete student==============================
# def deleteStudent(request, sid):  # eg: sid =1
#     student = Student.objects.get(id=sid) # fetch(get) student using this sid from database
#     student.delete() #delete Student
#     messages.success(request, "Student Deleted Successfully")
#     return redirect("student_list")

# def editStudent(request,sid):
#     # Get student by id
#     student = Student.objects.get(id=sid)
#     if request.method == "POST":
        
#         #Receive form data
#         fn = request.POST["firstName"]
#         ln = request.POST["lastName"]
#         em = request.POST["email"]
#         age = request.POST["age"]
#         bio = request.POST["bio"]
#         phone = request.POST["phoneNumber"]
#         gen = request.POST["gender"]
#         sub = request.POST["subjects"]
        
        
#         #email validation
#         if Student.objects.filter(email=em).exclude(id=sid).exists():
#             messages.error(request,"Email already Exists")
#             return redirect("edit_student", sid)
            
            
#         #phone number validation
#         if Student.objects.filter(phone_number=phone).exclude(id=sid).exists():
#             messages.error(request, "phone number already Exist")
#             return redirect("edit_student", sid)
        
#         #for update form data 
#         student.first_name = fn
#         student.last_name = ln
#         student.email = em
#         student.phone_number = phone
#         student.age = age
#         student.gender = gen
#         student.subjects = sub
#         student.bio = bio
        
#         #Save updated data in database
#         student.save()
        
#         #success message
#         messages.success(request, "Student updated successfully")
#         return redirect("student_list")
        
#     return render(request, "pages/editStudent.html", {"stud": student})

# =======================================================================================
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Student
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"pages/index.html")


#-----------------------for students_page-----------

def student_name(request):
    if request.method == "POST":
        print(request.POST)
     # to accept data from form   
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        em = request.POST["email"]
        pn = request.POST["phone_number"]
        a = request.POST["age"]
        gen=request.POST["gender"]
        sub = request.POST["subjects"]
        b = request.POST["bio"]
    
    
        obj = Student.objects.create(
            first_name= fn,
            last_name =ln,
            email =em,
            phone_number = pn,
            age = a,
            gender = gen,
            subjects = sub,
            bio = b,
        )
        print(obj)
        obj.save()
    
    
    
    
    return render(request,"pages/add_student.html")
    
#------------------student list-----------
def studentList(request):
    searched = request.GET.get("searched", "")

    if searched:
        student = (
            Student.objects.filter(first_name__icontains=searched)|  
            Student.objects.filter(last_name__icontains=searched)|          
            Student.objects.filter(email__icontains=searched)|
            Student.objects.filter(age__icontains=searched)|
            Student.objects.filter(phone_number__icontains=searched)
        ).distint()     
    else: 
        student =Student.objects.all()
#----------------best_method---------------   
    '''if searched:
            student = Student.objects.filter(
            Q(first_name__icontains=searched) |
            Q(last_name__icontains=searched) | 
            Q(email__icontains=searched) | 
            Q(age__icontains=searched) |
            Q(phone_number__icontains=searched)
            )'''
    print(student)
    return render(request,"pages/studentList.html",{"stud":student})
#-----------------Delete_Student----------------------
def deleteStudent(request, sid): #eg:sid =1
    student = Student.objects.get(id=sid) #fetch(get) student using sid from database
    student.delete() #delete student
    messages.success(request, "Student Deleted Successfully")
    return redirect("student_list")

def editStudent(request,sid):
    student = Student.objects.get(id=sid) #get student by id
    if request.method == 'POST':
        
        #receive form data
        fn = request.POST["firstName"]
        ln = request.POST["lastName"]
        em = request.POST["email"]
        ag = request.POST["age"]
        phone = request.POST["phoneNumber"]
        gen = request.POST["gender"]
        sub = request.POST["subject"]
        b=request.POST["bio"]

    #email validation
        if Student.objects.filter(email=em).exclude(id=sid).exists():
            messages.error(request,"Email already exists")
            return redirect("edit_student", sid)    
    #phone number validation
        if Student.objects.filter(phone_number=phone).exclude(id=sid).exists():
            messages.error(request, "phone number already exist")
            return redirect("edit_student",sid)

    #for update data
        student.first_name = fn
        student.last_name = ln
        student.email = em
        student.phone_number = phone
        student.age = ag
        student.gender = gen
        student.subjects = sub
        student.bio = b
    
    #save update data in database
        student.save()
    
    #success mesage
        messages.success(request,"Data updated successfully")
        return redirect("student_list") 
    
    
    return render(request,"pages/editStudent.html", {"stud":student}) #context dictionay