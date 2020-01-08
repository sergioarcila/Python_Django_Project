from django import forms
from django.forms import ModelForm
from .models import PlayerProfile
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from allauth.account.forms import SignupForm

User = get_user_model()


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    tos = forms.BooleanField(label='I agree to the Terms of Service')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class EditUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        labels = {"first_name": "First Name", "last_name": "Last Name", "email": "Email", "password": "Password"}


class FullProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FullProfileForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['phone_number'].required = True
        self.fields['contact_email'].required = True
        self.fields['parent_name'].required = True
        self.fields['parent_cell'].required = True
        self.fields['parent_email'].required = True
        self.fields['hs_coach_name'].required = True
        self.fields['hs_coach_phone'].required = True
        self.fields['hs_coach_email'].required = True
        self.fields['jersey_number'].required = True
        self.fields['primary_position'].required = True
        self.fields['secondary_position'].required = True
        self.fields['height'].required = True
        self.fields['weight'].required = True
        # self.fields['profile_picture'].required = True
        self.fields['dominant_hand'].required = True
        self.fields['high_school'].required = True
        self.fields['grad_year'].required = True
        self.fields['gpa'].required = True

    # phone_number = PhoneNumberField(required=True)
    # contact_email = forms.EmailField(required=True)
    # parent_name = forms.CharField(required=True)
    # parent_cell = PhoneNumberField(required=True)
    # parent_email = forms.EmailField(required=True)
    # hs_coach_name = forms.CharField(required=True)
    # hs_coach_phone = PhoneNumberField(required=True)
    # hs_coach_email = forms.EmailField(required=True)
    # # profile_picture = forms.ImageField(required=True)
    # jersey_number = forms.IntegerField(required=True)
    # primary_position = forms.CharField(required=True)
    # secondary_position = forms.CharField(required=True)
    # height = forms.IntegerField(required=True)
    # weight = forms.IntegerField(required=True)
    # HAND_CHOICES = [
    #     ('R', 'Right'),
    #     ('L', 'Left'),
    # ]
    # dominant_hand = forms.ChoiceField(widget=forms.Select, choices=HAND_CHOICES, required=True)
    # high_school = forms.CharField(required=True)
    # grad_year = forms.IntegerField(required=True)
    # gpa = forms.DecimalField(required=True)

    class Meta:
        model = PlayerProfile
        fields = [
            # "profile_picture",
            "prof_pic_uploadcare",
            "phone_number",
            "contact_email",
            "facebook",
            "twitter",
            "instagram",
            "parent_name",
            "parent_cell",
            "parent_email",
            # "parent2_name",
            # "parent2_cell",
            # "parent2_email",
            "location_town",
            "location_state",
            "hs_coach_name",
            "hs_coach_phone",
            "hs_coach_email",
            "travel_team",
            "travel_coach_name",
            "travel_coach_phone",
            "travel_coach_email",
            "highlight_video_link",
            "skills_video_link",
            "jersey_number",
            "primary_position",
            "secondary_position",
            "height",
            "weight",
            "dominant_hand",
            "vertical_leap",
            "ppg",
            "apg",
            "rpg",
            "free_throw_perc",
            "three_point_perc",
            "basketball_honors",
            "high_school",
            "grad_year",
            "gpa",
            "act_score",
            "math_sat",
            "reading_sat",
            "academic_honors_awards",
            "joined_ncaa_eligib",
            "ncaa_elig_num",
            "naia_elig_num",
            "personal_message",
            # "schedule",
            "coaches_evaluation",
            "desired_colleges",
            "desired_major",
            "desired_minor",
            # "other_info",
            # "scouting_report",
        ]
        help_texts = {
            "act_score": "Leave blank if not taken yet.",
            "math_sat": "Leave blank if not taken yet.",
            "reading_sat": "Leave blank if not taken yet.",
        }
        exclude = ['user', 'scouting_report']
        labels = {
            "id": "Id",
            "user": "User",
            "phone_number": "Phone Number",
            "contact_email": "Contact Email",
            "parent_name": "Parent Name",
            "parent_cell": "Parent Cell",
            "parent_email": "Parent Email",
            "parent2_name": "2nd Parent Name",
            "parent2_cell": "2nd Parent Cell",
            "parent2_email": "2nd Parent Email",
            "location_town": "Town",
            "location_state": "State",
            "facebook": "Facebook URL",
            "twitter": "Twitter URL",
            "instagram": "Instagram URL",
            "hs_coach_name": "High School Coach's Name",
            "hs_coach_phone": "High School Coach's Phone",
            "hs_coach_email": "High School Coach's Email",
            "travel_team": "Travel Team",
            "travel_coach_name": "Travel Coach's Name",
            "travel_coach_phone": "Travel Coach's Phone",
            "travel_coach_email": "Travel Coach's Email",
            "profile_picture": "Profile Picture",
            "prof_pic_uploadcare": "Profile Pic",
            "highlight_video_link": "Highlight Video Youtube Link",
            "skills_video_link": "Skills Video Youtube Link",
            "jersey_number": "Jersey Number",
            "primary_position": "Primary Position",
            "secondary_position": "Secondary Position",
            "height": "Height in inches",
            "weight": "Weight lbs.",
            "dominant_hand": "Dominant Hand",
            "vertical_leap": "Vertical Leap (in.)",
            "ppg": "Points Per Game",
            "apg": "Assists Per Game",
            "rpg": "Rebounds Per Game",
            "free_throw_perc": "Free Throw %",
            "three_point_perc": "Three Point %",
            "basketball_honors": "List Any Basketball Honors",
            "joined_ncaa_eligib": "Have You Joined NCAA Eligibility Enter?",

            "high_school": "High School",
            "grad_year": "Graduation Year",
            "gpa": "GPA",
            "act_score": "ACT Score",
            "math_sat": "Math SAT",
            "reading_sat": "Reading SAT",
            "academic_honors_awards": "Academic Honors Awards",
            "ncaa_elig_num": "NCAA Eligibility Number",
            "naia_elig_num": "NAIA Eligibility Number",

            "personal_message": "Personal Message",
            "schedule": "Schedule",
            "coaches_evaluation": "Coaches Evaluation",
            "desired_colleges": "Desired Colleges",
            "desired_major": "Desired Major",
            "desired_minor": "Desired Minor",
            "other_info": "Other Info",

            "scouting_report": "Scouting Report",
        }


class EditProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['phone_number'].required = True
        self.fields['contact_email'].required = True
        self.fields['parent_name'].required = True
        self.fields['parent_cell'].required = True
        self.fields['parent_email'].required = True
        self.fields['hs_coach_name'].required = True
        self.fields['hs_coach_phone'].required = True
        self.fields['hs_coach_email'].required = True
        self.fields['jersey_number'].required = True
        self.fields['primary_position'].required = True
        self.fields['secondary_position'].required = True
        self.fields['height'].required = True
        self.fields['weight'].required = True
        # self.fields['profile_picture'].required = True
        self.fields['dominant_hand'].required = True
        self.fields['high_school'].required = True
        self.fields['grad_year'].required = True
        self.fields['gpa'].required = True

    class Meta:
        model = PlayerProfile
        fields = [
            # "profile_picture",
            "prof_pic_uploadcare",
            "phone_number",
            "contact_email",
            "facebook",
            "twitter",
            "instagram",
            "parent_name",
            "parent_cell",
            "parent_email",
            # "parent2_name",
            # "parent2_cell",
            # "parent2_email",
            "location_town",
            "location_state",
            "hs_coach_name",
            "hs_coach_phone",
            "hs_coach_email",
            "travel_team",
            "travel_coach_name",
            "travel_coach_phone",
            "travel_coach_email",
            "highlight_video_link",
            "skills_video_link",
            "jersey_number",
            "primary_position",
            "secondary_position",
            "height",
            "weight",
            "dominant_hand",
            "vertical_leap",
            "ppg",
            "apg",
            "rpg",
            "free_throw_perc",
            "three_point_perc",
            "basketball_honors",
            "high_school",
            "grad_year",
            "gpa",
            "act_score",
            "math_sat",
            "reading_sat",
            "academic_honors_awards",
            "joined_ncaa_eligib",
            "ncaa_elig_num",
            "naia_elig_num",
            "personal_message",
            # "schedule",
            "coaches_evaluation",
            "desired_colleges",
            "desired_major",
            "desired_minor",
            # "other_info",
            # "scouting_report",
        ]
        help_texts = {
            "act_score": "Leave blank if not taken yet.",
            "math_sat": "Leave blank if not taken yet.",
            "reading_sat": "Leave blank if not taken yet.",
        }
        exclude = ['user', 'scouting_report']
        labels = {
            "id": "Id",
            "user": "User",
            "phone_number": "Phone Number",
            "contact_email": "Contact Email",
            "parent_name": "Parent Name",
            "parent_cell": "Parent Cell",
            "parent_email": "Parent Email",
            "parent2_name": "2nd Parent Name",
            "parent2_cell": "2nd Parent Cell",
            "parent2_email": "2nd Parent Email",
            "location_town": "Town",
            "location_state": "State",
            "facebook": "Facebook URL",
            "twitter": "Twitter URL",
            "instagram": "Instagram URL",
            "hs_coach_name": "High School Coach's Name",
            "hs_coach_phone": "High School Coach's Phone",
            "hs_coach_email": "High School Coach's Email",
            "travel_team": "Travel Team",
            "travel_coach_name": "Travel Coach's Name",
            "travel_coach_phone": "Travel Coach's Phone",
            "travel_coach_email": "Travel Coach's Email",
            "profile_picture": "Profile Picture",
            "prof_pic_uploadcare": "Profile Pic",
            "highlight_video_link": "Highlight Video Youtube Link",
            "skills_video_link": "Skills Video Youtube Link",
            "jersey_number": "Jersey Number",
            "primary_position": "Primary Position",
            "secondary_position": "Secondary Position",
            "height": "Height in inches",
            "weight": "Weight lbs.",
            "dominant_hand": "Dominant Hand",
            "vertical_leap": "Vertical Leap (in.)",
            "ppg": "Points Per Game",
            "apg": "Assists Per Game",
            "rpg": "Rebounds Per Game",
            "free_throw_perc": "Free Throw %",
            "three_point_perc": "Three Point %",
            "basketball_honors": "List Any Basketball Honors",
            "joined_ncaa_eligib": "Have You Joined NCAA Eligibility Enter?",

            "high_school": "High School",
            "grad_year": "Graduation Year",
            "gpa": "GPA",
            "act_score": "ACT Score",
            "math_sat": "Math SAT",
            "reading_sat": "Reading SAT",
            "academic_honors_awards": "Academic Honors Awards",
            "ncaa_elig_num": "NCAA Eligibility Number",
            "naia_elig_num": "NAIA Eligibility Number",

            "personal_message": "Personal Message",
            "schedule": "Schedule",
            "coaches_evaluation": "Coaches Evaluation",
            "desired_colleges": "Desired Colleges",
            "desired_major": "Desired Major",
            "desired_minor": "Desired Minor",
            "other_info": "Other Info",

            "scouting_report": "Scouting Report",
        }
