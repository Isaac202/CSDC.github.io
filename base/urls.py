from django.urls import path
from base.views import registercsds ,ips_round_tables, local, short_courses, keynotespeakers, registrationcsds,conference_schedule, venue,contact, home, awards,call_papers,soic_special_issue,committees
urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact, name='contact'),
    path('awards/', awards,name='awards'),
    path('call_papers/',call_papers,name='call_papers'),
    path('soic_special_issue/',soic_special_issue, name='soic_special_issue'),
    path('committees/', committees, name='committees'),
    path('venue/',venue,name='venue'),
    path('conference_schedule/',conference_schedule,name='conference_schedule'),
    path('registrationcsds/',registrationcsds, name='registrationcsds'),
    path('keynotespeakers/', keynotespeakers, name='keynotespeakers'),
    path('short_courses/',short_courses, name='short_courses'),
    path('local/',local,name='local'),
    path('ips_round_tables/',ips_round_tables,name='ips_round_tables'),
    path('registercsds/',registercsds, name='registercsds'),
]