# users/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#-------------------------------------------------------------------------
# Used by admin
#-------------------------------------------------------------------------
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = (
              'username',
              'email',
              'first_name',
              'last_name',
              )


#-------------------------------------------------------------------------
# Used by admin
#-------------------------------------------------------------------------
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = (
              'username',
              'email',
              'first_name',
              'last_name',
              )

