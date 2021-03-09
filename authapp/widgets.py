from django.forms.widgets import ClearableFileInput, DateInput


class CustomImageWidget(ClearableFileInput):
    template_name = "widgets/image_only_input_template.html"


class CustomDateWidget(DateInput):
    template_name = "widgets/date_input_template.html"
