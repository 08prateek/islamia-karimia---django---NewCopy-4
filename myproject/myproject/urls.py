
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views






from .views import (
    index_view, aboutus_view, androiddeveloper_view, antiragging_view, applytoik_view,
    aspcore_view, baeconomics_view, baenglish_view, bahindi_view, bahistory_view,
    bapoliticalscience_view, basociology_view, baurdu_view, bcomcomputer_view, bcom_view,
    bca_view, bsccs_view, bscmaths_view, bscmicrobiology_view, bscbiology_view, backend_view,
    career_view, dsa_view, exploreindore_view, faq_view, frontend_view, ikalumni_view, ikbotanical_view,
    ikbotanylab_view, ikboysschool_view, ikchemistrylab_view, ikcochingclasses_view,
    ikcomputerlab_view, ikgallery_view, ikgirlscolloge_view, ikhistory_view, ikcsmngmt_view,
    iklaboratory_view, iklibrary_view, ikmission_view, ikphysicslab_view, ikpresidentmessage_view,
    ikroboticslab_view, ikskyheight_view, iksports_view, ikzoologylab_view, ikcollegepalasia_view,
    ikgirlsschool_view, ikiti_view, itvi_view, maeconomics_view, mapoliticalscience_view,
    masociology_view, maurdu_view, mcom_view, mscbotany_view, mscchemistry_view, mscmaths_view,
    mscmicrobiology_view, msczoology_view, ncc_view, oraclejava_view, oraclesql_view, pgdca_view,
    privacypolicy_view, python_view, sitemap_view, stmustafa_view, stumar_view,
    stumaracademy_view, uiuxdesign_view, videoediting_view
)
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendor/', include('vendor.urls')),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('about-us/', aboutus_view, name='aboutus'),
    path('android-developer/', androiddeveloper_view, name='androiddeveloper'),
    path('anti-ragging/', antiragging_view, name='antiragging'),
    path('apply-to-ik/', applytoik_view, name='applytoik'),
    path('asp-core/', aspcore_view, name='aspcore'),
    path('bachelor-of-arts-in-economics/', baeconomics_view, name='baeconomics'),
    path('bachelor-of-arts-in-english/', baenglish_view, name='baenglish'),
    path('bachelor-of-arts-in-hindi-literature/', bahindi_view, name='bahindi'),
    path('bachelor-of-arts-in-history/', bahistory_view, name='bahistory'),
    path('bachelor-of-arts-in-political-science/', bapoliticalscience_view, name='bapoliticalscience'),
    path('bachelor-of-arts-in-sociology/', basociology_view, name='basociology'),
    path('bachelor-of-arts-in-urdu-literature/', baurdu_view, name='baurdu'),
    path('bachelor-of-commerce-in-computer-application/', bcomcomputer_view, name='bcomcomputer'),
    path('bachelor-of-commerce/', bcom_view, name='bcom'),
    path('bachelor-of-computer-application/', bca_view, name='bca'),
    path('bachelor-of-science-in-computer-science/', bsccs_view, name='bsccs'),
    path('bachelor-of-science-in-mathematics/', bscmaths_view, name='bscmaths'),
    path('bachelor-of-science-in-microbiology/', bscmicrobiology_view, name='bscmicrobiology'),
    path('bachlor-of-science-in-biology/', bscbiology_view, name='bscbiology'),
    path('back-end/', backend_view, name='backend'),
    path('career/', career_view, name='career'),
    path('dsa/', dsa_view, name='dsa'),
    path('explore-indore/', exploreindore_view, name='exploreindore'),
    path('faq/', faq_view, name='faq'),
    path('front-end/', frontend_view, name='frontend'),
    path('ik-alumni/', ikalumni_view, name='ikalumni'),
    path('ik-botanical-garden/', ikbotanical_view, name='ikbotanical'),
    path('ik-botany-lab/', ikbotanylab_view, name='ikbotanylab'),
    path('ik-boys-hr-sec-school/', ikboysschool_view, name='ikboysschool'),
    path('ik-chemistry-lab/', ikchemistrylab_view, name='ikchemistrylab'),
    path('ik-coching-classes/', ikcochingclasses_view, name='ikcochingclasses'),
    path('ik-computer-lab/', ikcomputerlab_view, name='ikcomputerlab'),
    path('ik-gallery/', ikgallery_view, name='ikgallery'),
    path('ik-girls-colloge/', ikgirlscolloge_view, name='ikgirlscolloge'),
    path('ik-history/', ikhistory_view, name='ikhistory'),
    path('ik-institute-of-cs-and-mangmt/', ikcsmngmt_view, name='ikcsmngmt'),
    path('ik-laboratory/', iklaboratory_view, name='iklaboratory'),
    path('ik-library/', iklibrary_view, name='iklibrary'),
    path('ik-mission/', ikmission_view, name='ikmission'),
    path('ik-physics-lab/', ikphysicslab_view, name='ikphysicslab'),
    path('ik-president-message/', ikpresidentmessage_view, name='ikpresidentmessage'),
    path('ik-robotics-lab/', ikroboticslab_view, name='ikroboticslab'),
    path('Ik-Sky-Height-International-Prep-School/', ikskyheight_view, name='ikskyheight'),
    path('ik-sports/', iksports_view, name='iksports'),
    path('ik-zoology-lab/', ikzoologylab_view, name='ikzoologylab'),
    path('islamia-karamia-college-palasia/', ikcollegepalasia_view, name='ikcollegepalasia'),
    path('islamia-karimia-girls-school-ushaganj/', ikgirlsschool_view, name='ikgirlsschool'),
    path('Islamia-Private-I.T.I/', ikiti_view, name='ikiti'),
    path('islamia-technical-vocational-institute/', itvi_view, name='itvi'),
    path('master-of-arts-in-economic/', maeconomics_view, name='maeconomics'),
    path('master-of-arts-in-political-science/', mapoliticalscience_view, name='mapoliticalscience'),
    path('master-of-arts-in-sociology/', masociology_view, name='masociology'),
    path('master-of-arts-in-urdu/', maurdu_view, name='maurdu'),
    path('master-of-commerce/', mcom_view, name='mcom'),
    path('master-of-science-in-botany/', mscbotany_view, name='mscbotany'),
    path('master-of-science-in-chemistry/', mscchemistry_view, name='mscchemistry'),
    path('master-of-science-in-maths/', mscmaths_view, name='mscmath'),
    path('master-of-science-in-microbiology/', mscmicrobiology_view, name='mscmicrobiology'),
    path('master-of-science-in-zoology/', msczoology_view, name='msczoology'),
    path('NCC/', ncc_view, name='ncc'),
    path('oracle-java/', oraclejava_view, name='oraclejava'),
    path('oracle-sql/', oraclesql_view, name='oraclesql'),
    path('pgdca/', pgdca_view, name='pgdca'),
    path('privacy-policy/', privacypolicy_view, name='privacypolicy'),
    path('python/', python_view, name='python'),
    path('sitemap/', sitemap_view, name='sitemap'),
    path('St-Mustafa-Raza-High-School-(Azad-Nagar)/', stmustafa_view, name='stmustafa'),
    path('St.-Umar-Hr-Sec.-School/', stumar_view, name='stumar'),
    path('St.umar-Academy-C.B.S.E./', stumaracademy_view, name='stumaracademy'),
    path('ui-ux-design/', uiuxdesign_view, name='uiuxdesign'),
    path('video-editing/', videoediting_view, name='videoediting'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)