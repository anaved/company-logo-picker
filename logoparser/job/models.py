from django.db import models

class Industry(models.Model):
    name = models.TextField(blank=True, null=True)


class Company(models.Model):
    source_link=models.URLField(blank=True, null=True)
    name =  models.TextField(blank=True, null=True)
    industry = models.ForeignKey('Industry', blank=True, null=True)
    type =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    url = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

class CompanyLogo(models.Model):
    company=models.TextField(blank=True, null=True)
    source_link=models.URLField(blank=True, null=True)
    logo_location=models.TextField(blank=True, null=True)
    biglogo_location=models.TextField(blank=True, null=True)

PART_FULL_TIME = {
    'true': 'Full-Time',
    'false': 'Part-Time',
}

PAID_UNPAID = {
    'true': 'Paid',
    'false': 'Unpaid',
}

GPA = (
       (1.0, '1.0'),
       (1.5, '1.5'),
       (2.0, '2.0'),
       (2.5, '2.5'),
       (3.0, '3.0'),
       (3.5, '3.5'),
       (4.0, '4.0'),
       )

YEAR_IN_UNIV_CHOICES = (
                        ('FR', 'Freshman'),
                        ('SO', 'Sophomore'),
                        ('JR', 'Junior'),
                        ('SR', 'Senior'),
                        ('GR', 'Graduate'),
                        )

class ParsedJobs(models.Model):
    company             = models.CharField(max_length=300, blank=True, null=True)
    source              = models.CharField(max_length=300, blank=True, null=True)
    title               = models.CharField(max_length=300, blank=True, null=True)
    description         = models.TextField(blank=True, null=True)
    qualification       = models.TextField(blank=True, null=True)
    all_text            = models.TextField(blank=True, null=True)
    location            = models.CharField(max_length=900, blank=True, null=True)
    posting_date        = models.DateTimeField(null=True, blank=True)
    source_joburl       = models.CharField(max_length=900, blank=True, null=True)
    company_joburl      = models.CharField(max_length=900, blank=True, null=True)
    timestamp           = models.DateTimeField(auto_now=True)
    major               = models.TextField(blank=True, null = True)
    gpa                 = models.FloatField(null=True, choices=GPA, blank=True)
    paid_unpaid         = models.BooleanField(default=True)
    full_parttime       = models.BooleanField(default=True)
    course_credit       = models.BooleanField(default=False)
    year                = models.CharField(max_length=2, choices=YEAR_IN_UNIV_CHOICES, null=True, blank=True)
    contact_info        = models.CharField(max_length=900, blank=True, null=True)
    number_applicants   = models.IntegerField(default=1)
    is_sent             = models.BooleanField(default=False)
    manual_done         = models.BooleanField(default=False)#manual operations done
    is_available        = models.BooleanField(default=False)#majors checked
    is_valid            = models.BooleanField(default=True)
    manual_by           = models.TextField(blank=True, null = True)
    
    
class NameKeys(models.Model):
    key=models.CharField(max_length=300, blank=True, null=True)
    occurance=models.IntegerField(blank=True, null=True)
    
class KeyMatch(models.Model):
    key_company=models.CharField(max_length=300, blank=True, null=True)
    value_company=models.CharField(max_length=300, blank=True, null=True)
    key_logo=models.CharField(max_length=300, blank=True, null=True)
    value_logo=models.CharField(max_length=300, blank=True, null=True)
    matchp=models.FloatField(blank=True, null=True)
    
    
class KeyCompany(models.Model):
    key=models.CharField(max_length=300, blank=True, null=True)
    company= models.ManyToManyField('Company',symmetrical=False, blank=True, null=True)


class KeyLogo(models.Model):
    key=models.CharField(max_length=300, blank=True, null=True)
    logo= models.ManyToManyField('CompanyLogo',symmetrical=False, blank=True, null=True)
    
class CompanyDuckduckGo(models.Model):
    company=models.CharField(max_length=300, blank=True, null=True)
    manual_key=models.CharField(max_length=300, blank=True, null=True)
    job_count=models.IntegerField(blank=True,null=True)
    duck_key=models.CharField(max_length=300, blank=True, null=True)
    url=models.URLField(blank=True,null=True)
    result=models.TextField(blank=True,null=True)
    related=models.TextField(blank=True,null=True)
