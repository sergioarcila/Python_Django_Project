from django.db import models
from django.contrib.auth import get_user_model
import uuid
from localflavor.us.models import USStateField
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from pyuploadcare.dj.models import ImageField

User = get_user_model()

class PlayerProfile(models.Model):

    def get_file_path(inst, fn):
        return str(inst.id) + "/" + fn


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)
    contact_email = models.EmailField(blank=True)
    parent_name = models.CharField(max_length=126, blank=True)
    parent_cell = PhoneNumberField(blank=True)
    parent_email = models.EmailField(blank=True)
    parent2_name = models.CharField(max_length=126, blank=True)
    parent2_cell = PhoneNumberField(blank=True)
    parent2_email = models.EmailField(blank=True)
    location_town = models.CharField(max_length=126, blank=True)
    location_state = USStateField(null=True, blank=True)
    facebook = models.URLField(max_length=510, blank=True)
    twitter = models.URLField(max_length=510, blank=True)
    instagram = models.URLField(max_length=510, blank=True)
    hs_coach_name = models.CharField(max_length=126, blank=True)
    hs_coach_phone = PhoneNumberField(blank=True)
    hs_coach_email = models.EmailField(blank=True)
    travel_team = models.CharField(max_length=254, blank=True)
    travel_coach_name = models.CharField(max_length=126, blank=True)
    travel_coach_phone = PhoneNumberField(blank=True)
    travel_coach_email = models.EmailField(blank=True)

    # MEDIA
    profile_picture = models.ImageField(blank=True, upload_to=get_file_path)
    prof_pic_uploadcare = ImageField(manual_crop="1:1", blank=True, null=True)
    # general_pictures = models.FileField(upload_to='uploads/')
    highlight_video_link = models.URLField(max_length=510, blank=True)
    skills_video_link = models.URLField(max_length=510, blank=True)
    # other_video_links

    # ATHLETIC INFO
    jersey_number = models.IntegerField(blank=True, null=True)
    primary_position = models.CharField(max_length=126, blank=True)
    secondary_position = models.CharField(max_length=126, blank=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    HAND_CHOICES = [
        ('R', 'Right'),
        ('L', 'Left'),
    ]
    dominant_hand = models.CharField(max_length=1, blank=True, choices=HAND_CHOICES)
    vertical_leap = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ppg = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    apg = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    rpg = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    free_throw_perc = models.IntegerField(blank=True, null=True)
    three_point_perc = models.IntegerField(blank=True, null=True)
    basketball_honors = models.CharField(max_length=510, blank=True)
    joined_ncaa_eligib = models.BooleanField()

    # ACADEMIC INFO
    high_school = models.CharField(max_length=126, blank=True)
    grad_year = models.IntegerField(blank=True, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    act_score = models.IntegerField(blank=True, null=True)
    math_sat = models.IntegerField(blank=True, null=True)
    reading_sat = models.IntegerField(blank=True, null=True)
    academic_honors_awards = models.CharField(max_length=510, blank=True)
    ncaa_elig_num = models.CharField(max_length=126, blank=True)
    naia_elig_num = models.CharField(max_length=126, blank=True)

    # OTHER INFO
    personal_message = models.TextField(max_length=1022, blank=True)
    schedule = models.TextField(max_length=510, blank=True)
    coaches_evaluation = models.CharField(max_length=1022, blank=True)
    desired_colleges = models.CharField(max_length=510, blank=True)
    desired_major = models.CharField(max_length=126, blank=True)
    desired_minor = models.CharField(max_length=126, blank=True)
    other_info = models.TextField(max_length=510, blank=True)

    # SCOUT FILLS OUT
    scouting_report = models.TextField(max_length=1022, blank=True)

    def __str__(self):
        ret = f"{self.user.first_name} {self.user.last_name}'s Profile"
        return ret

    def get_absolute_url(self):
        return reverse('view_profile', args=[str(self.id)])

class VideoLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    parent_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    url = models.URLField(max_length=510)

    def __str__(self):
        ret = f"{self.parent_profile.user.first_name} {self.parent_profile.user.last_name}'s link {self.url}"
        return ret

class GeneralPicture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    parent_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        ret = f"{self.parent_profile.user.first_name} {self.parent_profile.user.last_name}'s picture"
        return ret
