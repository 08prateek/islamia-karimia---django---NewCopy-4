from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def index_view(request):
    
    return render(request, 'index.html')

def aboutus_view(request):
    return render(request, 'about-us.html')

def androiddeveloper_view(request):
    return render(request, 'android-developer.html')

def antiragging_view(request):
    return render(request, 'anti-ragging.html')

def applytoik_view(request):
    return render(request, 'apply-to-ik.html')

def aspcore_view(request):
    return render(request, 'asp-core.html')

def baeconomics_view(request):
    return render(request, 'bachelor-of-arts-in-economics.html')

def baenglish_view(request):
    return render(request, 'bachelor-of-arts-in-english.html')

def bahindi_view(request):
    return render(request, 'bachelor-of-arts-in-hindi-literature.html')

def bahistory_view(request):
    return render(request, 'bachelor-of-arts-in-history.html')

def bapoliticalscience_view(request):
    return render(request, 'bachelor-of-arts-in-political-science.html')

def basociology_view(request):
    return render(request, 'bachelor-of-arts-in-sociology.html')

def baurdu_view(request):
    return render(request, 'bachelor-of-arts-in-urdu-literature.html')

def bcomcomputer_view(request):
    return render(request, 'bachelor-of-commerce-in-computer-application.html')

def bcom_view(request):
    return render(request, 'bachelor-of-commerce.html')

def bca_view(request):
    return render(request, 'bachelor-of-computer-application.html')

def bsccs_view(request):
    return render(request, 'bachelor-of-science-in-computer-science.html')

def bscmaths_view(request):
    return render(request, 'bachelor-of-science-in-mathematics.html')

def bscmicrobiology_view(request):
    return render(request, 'bachelor-of-science-in-microbiology.html')

def bscbiology_view(request):
    return render(request, 'bachlor-of-science-in-biology.html')

def backend_view(request):
    return render(request, 'back-end.html')

def career_view(request):
    return render(request, 'career.html')

def dsa_view(request):
    return render(request, 'dsa.html')

def exploreindore_view(request):
    return render(request, 'explore-indore.html')

def faq_view(request):
    return render(request, 'faq.html')

def frontend_view(request):
    return render(request, 'front-end.html')

def ikalumni_view(request):
    return render(request, 'ik-alumni.html')

def ikbotanical_view(request):
    return render(request, 'ik-botanical-garden.html')

def ikbotanylab_view(request):
    return render(request, 'ik-botany-lab.html')

def ikboysschool_view(request):
    return render(request, 'ik-boys-hr-sec-school.html')

def ikchemistrylab_view(request):
    return render(request, 'ik-chemistry-lab.html')

def ikcochingclasses_view(request):
    return render(request, 'ik-coching-classes.html')

def ikcomputerlab_view(request):
    return render(request, 'ik-computer-lab.html')

def ikgallery_view(request):
    return render(request, 'ik-gallery.html')

def ikgirlscolloge_view(request):
    return render(request, 'ik-girls-colloge.html')

def ikhistory_view(request):
    return render(request, 'ik-history.html')

def ikcsmngmt_view(request):
    return render(request, 'ik-institute-of-cs-and-mangmt.html')

def iklaboratory_view(request):
    return render(request, 'ik-laboratory.html')

def iklibrary_view(request):
    return render(request, 'ik-library.html')

def ikmission_view(request):
    return render(request, 'ik-mission.html')

def ikphysicslab_view(request):
    return render(request, 'ik-physics-lab.html')

def ikpresidentmessage_view(request):
    return render(request, 'ik-president-message.html')

def ikroboticslab_view(request):
    return render(request, 'ik-robotics-lab.html')

def ikskyheight_view(request):
    return render(request, 'Ik-Sky-Height-International-Prep-School.html')

def iksports_view(request):
    return render(request, 'ik-sports.html')

def ikzoologylab_view(request):
    return render(request, 'ik-zoology-lab.html')

def ikcollegepalasia_view(request):
    return render(request, 'islamia-karamia-college-palasia.html')

def ikgirlsschool_view(request):
    return render(request, 'islamia-karimia-girls-school-ushaganj.html')

def ikiti_view(request):
    return render(request, 'Islamia-Private-I.T.I .html')

def itvi_view(request):
    return render(request, 'islamia-technical-vocational-institute.html')

def maeconomics_view(request):
    return render(request, 'master-of-arts-in-economic.html')

def mapoliticalscience_view(request):
    return render(request, 'master-of-arts-in-political-science.html')

def masociology_view(request):
    return render(request, 'master-of-arts-in-sociology.html')

def maurdu_view(request):
    return render(request, 'master-of-arts-in-urdu.html')

def mcom_view(request):
    return render(request, 'master-of-commerce.html')

def mscbotany_view(request):
    return render(request, 'master-of-science-in-botany.html')

def mscchemistry_view(request):
    return render(request, 'master-of-science-in-chemistry.html')

def mscmaths_view(request):
    return render(request, 'master-of-science-in-maths.html')

def mscmicrobiology_view(request):
    return render(request, 'master-of-science-in-microbiology.html')

def msczoology_view(request):
    return render(request, 'master-of-science-in-zoology.html')

def ncc_view(request):
    return render(request, 'NCC.html')

def oraclejava_view(request):
    return render(request, 'oracle-java.html')

def oraclesql_view(request):
    return render(request, 'oracle-sql.html')

def pgdca_view(request):
    return render(request, 'pgdca.html')

def privacypolicy_view(request):
    return render(request, 'privacy-policy.html')

def python_view(request):
    return render(request, 'python.html')

def sitemap_view(request):
    return render(request, 'sitemap.html')

def stmustafa_view(request):
    return render(request, 'St-Mustafa-Raza-High-School-(Azad Nagar).html')

def stumar_view(request):
    return render(request, 'St.-Umar-Hr-Sec.-School.html')

def stumaracademy_view(request):
    return render(request, 'St.umar-Academy-C.B.S.E..html')

def uiuxdesign_view(request):
    return render(request, 'ui-ux-design.html')

def videoediting_view(request):
    return render(request, 'video-editing.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Set session variable for create_tender page
            request.session['create_tender_logged_in'] = True
            return redirect('create_tender')  # Redirect to create_tender page
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')

def user_logout(request):
    # Clear session variables
    if 'create_tender_logged_in' in request.session:
        del request.session['create_tender_logged_in']
    logout(request)
    return redirect('login')




