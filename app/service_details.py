from flask.ext.babel import gettext as _

MONDAY = _('Monday')
TUESDAY = _('Tuesday')
WEDNESDAY = _('Wednesday')
THURSDAY = _('Thursday')
FRIDAY = _('Friday')
WEEKDAYS = _('Monday - Friday')
ENGLISH = _('English')
SPANISH = _('Spanish')

daily_planet = {
        'slug': 'daily_planet',
        'locations': [
            {'name': _('Daily Planet Downtown'),
                'phone': { 'number': '804-783-2505'},
             'address': '517 W Grace St, Richmond, VA 23220',
             'hours': [
                 { 'name': _('Registration Hours'), 'listings': [
                     [WEEKDAYS, '8:00 AM - 11:00 AM', '1:00 PM - 3:00 PM']]},
                 { 'name': _('Open Hours'), 'listings': [
                     [WEEKDAYS, '8:00 AM - 4:30 PM']]},
                 ],
             'services':[
                _("Primary care"),
                _("Oral health"),
                _("Behavioral health"),
                _("Case management"),
                _("Specialty referrals (through Access Now)"),
                _("Some Spanish-speaking staff"),
                _("Phone translation available on-demand"),
                 ]
             },
            {'name': _('Southside Community Health Center'),
                'phone': { 'number':'804-292-3011' },
             'address': '180 East Belt Blvd., Richmond VA 23224',
             'hours': [
                 {'name': _('Registration Hours'), 'listings': [
                     [WEEKDAYS, '8:00 AM - 11:00 AM', '1:00 PM - 3:00 PM']]},
                 {'name': _('Open Hours'), 'listings': [
                     [WEEKDAYS, '8:00 AM - 4:30 PM']]},
                 ],
             'services':[
                _("Primary care"),
                _("Eye Clinic"),
                _("Specialty referrals (through Access Now)"),
                _("Full-time Spanish speaking staff at front desk"),
                _("Phone translation available on-demand"),
                 ]
             },
            ],
        'steps':_("""
### For primary care, oral health, and eye clinic

1. Arrive at Downtown or Southside Community Health Center during registration hours. Bringing proof of income documents is helpful but not required.
2. Complete the intake packet and wait to speak with the screening staff (typically about 30 minutes)
3. Talk with the screening staff to learn fee levels and make an appointment.  The first appointment is typically within 2 weeks of registration. Proof of income documentation must be provided within 30 days of the first appointment, otherwise the patient will be charged the highest sliding scale fee.
"""),
        'more information':_("""
Call 804-783-2505
Visit http://www.dailyplanetva.org/services/
"""),
        'interpreters':_("""
Limited Spanish-speaking staff is available.
On-demand phone interpreters are available for many languages. What is the service or contractor?
"""),
        'eligibility':_("""
Everyone is eligible for care at Daily Planet. However, discounted care is
available for those who qualify based on their household income level,
calculated as a percentage of the Federal Poverty Level (FPL).
""")
        }

crossover = {
        'slug': 'crossover',
        'locations': [
            {'name': _('CrossOver Downtown'),
             'phone': {'number': '804-783-2505','ext':'320'},
             'address': '108 Cowardin Avenue, Richmond, VA',
             'hours': [
                 {'name': _('Open Hours'), 'listings': [
                     [ WEEKDAYS,'8:30 AM - 5:00 PM']]},
                 {'name': _('Screening Times'), 'listings': [
                     [ENGLISH, MONDAY, '12:30 PM'],
                     [SPANISH, WEDNESDAY, '12:30 PM']]},
                 ],
             },
            {'name': _('CrossOver Western Henrico'),
             'phone': { 'number':'804-622-0803', 'note': 'machine' },
             'address': '8600 Quioccasin Road, Suite 105',
             'hours': [
                 {'name': _('Open Hours'), 'listings': [
                     [ MONDAY,'8:30 AM - 5:00 PM'],
                     [ TUESDAY,'8:30 AM - 8:00 PM'],
                     [ WEDNESDAY,'8:30 AM - 5:00 PM'],
                     [ THURSDAY,'8:30 AM - 5:00 PM'],
                     [ FRIDAY,'8:30 AM - 3:00 PM'],
                     ]},
                 {'name': _('Screening Times'), 'listings': [
                     [ENGLISH, TUESDAY, '1:00 PM'],
                     [SPANISH, THURSDAY, '12:00 PM']]},
                 ],
             },
            ],
        'interpreters':_("""
Screening is available in Spanish at once per week at designated times. Once a
patient is screened, volunteer translators are broguht in for patient
appointments and are subject to volunteer availability.
"""),
        'eligibility':_("""
Crossover serves uninsured patients that fall under 200%% of the Federal Poverty Level.
"""),
        }

access_now = {
        'slug': 'access_now',
        'summary':_("""
Access Now offers specialty referrals for uninsured patients at partner
safety-net providers in the Richmond Area.
        """),
        'steps': _("""
To be seen by a specialist, patients must be referred to Access Now by one of
the partner clinics:

* Bon Secours' Care-A-Van
* Capital Area Health Network
* Center for High Blood Pressure
* Cheryl Watson Memorial Free Clinic
* Chesterfield Health Department
* Chickahominy Health District
* Cornerstone Free Health Clinic
* Crossover Ministries
* Daily Planet
* Fan Free Clinic
* Free Clinic of Powhatan
* Goochland Free Clinic and Family Services
* Henrico Health Department
* Northern Neck Free Clinic
* Pathways
* Richmond City Health District
* Cornerstone Free Health Clinic
* St. James the Less Free Clinic
* Surry Area Free Clinic
* Tappahannock Free Clinic
"""),
        'interpreters': _("""
For patients who need language interpretation, Access Now will find
interpreters to assist the patient during clinical appointments.
"""),
        'eligibility':_("""
To be eligible, patients must be able to document that they are under 200%% of
the Federal Poverty Level, are uninsured, are not eligible for Medicaid, and
have lived in the Richmond metropolitan area for more than 6 months.

Patients must have lived in one of the following counties for at least 6
months:

* Amelia County
* Caroline County
* Charles City County
* Chesterfield County
* Cumberland County
* Dinwiddie County
* Essex County
* Gloucester County
* Goochland County
* Hanover County
* Henrico County
* Isle of Wight County
* King and Queen County
* King George County
* King William County
* Lancaster County
* Louisa County
* Mathews County
* Middlesex County
* New Kent County
* Northumberland County
* Powhatan County
* Prince George County
* Richmond County
* Southampton County
* Surry County
* Sussex County
* Westmoreland County
* City of Colonial Heights
* City of Hopewell
* City of Petersburg
* City of Richmond
* Town of Ashland
"""),
        'services':[
_("Allergy & Immunology"),
_("Nephrology"),
_("Pulmonary Disease"),
_("General Surgery"),
_("Anesthesiology"),
_("Oncology"),
_("Radiation Oncology"),
_("Orthopaedic Surgery"),
_("Cardiology"),
_("Ophthalmology"),
_("Rheumatology"),
_("Plastic Surgery"),
_("Dermatology"),
_("Oral Surgery"),
_("Sleep Medicine"),
_("Thoracic Surgery"),
_("Endocrinology"),
_("Otolaryngology"),
_("Breast Surgery"),
_("Vascular Surgery"),
_("Gastroenterology"),
_("Physical Therapy"),
_("Cardiothoracic Surgery"),
_("Urology"),
_("GYN and GYN Oncology"),
_("Podiatry"),
_("Colon and Rectal Surgery"),
            ]}


rchd = {
        'slug': 'rchd',
        'locations': [
            {'name': _('RCHD Downtown'),
                'phone': {'number': '804-482-5500', 'notes': 'machine'},
             'address': '400 East Cary Street, Richmond, VA',
             'hours': [
                 {'name':_('Open Hours'), 'listings': [
                     [ WEEKDAYS,'8:00 AM - 5:00 PM']]},
                 {'name':_('Phone Hours'), 'listings':[
                     [WEEKDAYS, '8:00 AM - 12:00 PM', '1:00 PM - 5:00 PM']]}
                 ],
             'services': [
                _("Prenatal Services (for Richmond City residents)"),
                _("Walk-in services"),
                _("Teen Experience"),
                _("STI/HIV Services"),
                _("Family Planning Services"),
                _("Immunization Services"),
                _("TB Services"),
                _("Refugee Newcomer Services"),
                 ]
             },
            {'name': 'Resource Centers', 'type': 'LocationGroup',
                'services':[
                    _("Family Planning and STI Services"),
                    _("Health Screenings"),
                    _("Wellness Services"),
                    _("Nutrition Education"),
                    _("Community Resource Information"),
                    _("Budget Management"),
                    _("Health Education"),
                    ],
                'sublocations':[
                   {'name':'Bellemeade Commmunity Center',
                    'phone': {'number':'804-646-1475'},
                    'address': '1800 Lynhaven Avenue, Richmond, VA',
                    'hours': [
                        {'listings':[[MONDAY, '1:00 PM - 5:00 PM']]}]},
                    {'name': 'Broad Rock Community Center',
                     'phone':{'number': '804-646-1478'},
                     'address': '4615 Ferguson Lane, Richmond, VA',
                     'hours': [
                         {'listings':[[WEDNESDAY, '1:00 PM - 5:00 PM']]}]},
                    {'name': 'Creighton Resource Center',
                     'phone':{'number': '804-371-0433'},
                     'address': '2150 Creighton Road, Richmond, VA',
                     'hours': [
                         {'listings':[[MONDAY, '9:00 AM - 5:00 PM']]}]},
                    {'name': 'Fairfield Resource Center',
                     'phone':{'number': '804-786-4099'},
                     'address': '2311 North 25th Street, Richmond, VA',
                     'hours': [
                         {'listings':[[THURSDAY, '9:00 AM - 5:00 PM']]}]},
                    {'name': 'Gilpin Resource Center',
                     'phone':{'number': '804-786-1960'},
                     'address': '436 Calhoun St, Richmond, VA',
                     'hours': [
                         {'listings':[[TUESDAY, '9:00 AM - 5:00 PM']]}]},
                    {'name': 'Hillside Resource Center',
                     'phone':{'number': '804-230-7740'},
                     'address': '1615 Glenfield Avenue, Richmond, VA',
                     'hours': [
                         {'listings':[[THURSDAY, '9:00 AM - 5:00 PM']]}]},
                    {'name': 'Mosby Resource Center',
                     'phone':{'number': '804-786-0204'},
                     'address': '1536 Coalter Street, Richmond VA',
                     'hours': [{ 'listings':[
                         [TUESDAY, '1:00 PM - 5:00 PM'],
                         [WEDNESDAY, '9:00 AM - 5:00 PM'],
                         ]}]},
                    {'name': 'Whitcomb Resource Center',
                     'phone':{'number': '804-786-0555'},
                     'address': '2106 Deforrest Street, Richmond, VA',
                     'hours': [
                         {'listings':[[TUESDAY, '1:00 PM - 5:00 PM']]}]},
                ]
            }],
        'eligibility':_("""Anyone can be seen at the Richmond City Health District and its
Resource Centers, but may be charged a fee corresponding to their
household income.
"""),
        }


SERVICES = {
    "Daily Planet": daily_planet,
    "CrossOver": crossover,
    "Access Now": access_now,
    "RCHD Resource Centers": rchd
    }
