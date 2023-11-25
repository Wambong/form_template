import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import FormTemplate

def form_input(request):
    return render(request, 'form_input.html')
@csrf_exempt
@require_POST
def get_form(request):
    submitted_data = dict(request.POST)
    submitted_data.pop('csrfmiddlewaretoken', None)

    matching_template = find_matching_template(submitted_data)

    if matching_template:
        return JsonResponse({'template_name': matching_template.name})
    else:
        field_types = get_field_types(submitted_data)
        save_form_template(request.POST)  # Save the form template to the database
        return JsonResponse(field_types)

def save_form_template(form_data):
    # Extract form name and fields from the submitted data
    form_name = form_data.get('Template_name', '')
    fields = {key: form_data[key] for key in form_data if key.startswith('f_name_')}

    # Create and save the FormTemplate instance
    form_template = FormTemplate(name=form_name, fields=fields)
    form_template.save()

def find_matching_template(submitted_data):
    for template in FormTemplate.objects.all():
        if all(
            field_name in submitted_data and submitted_data[field_name][0] == field_type
            for field_name, field_type in template.fields.items()
        ):
            return template
    return None
def get_field_types(submitted_data):
    field_types = {}
    for field_name, values in submitted_data.items():
        if is_valid_date(values[0]):
            field_types[field_name] = 'date'
        elif is_valid_phone(values[0]):
            field_types[field_name] = 'phone'
        elif is_valid_email(values[0]):
            field_types[field_name] = 'email'
        else:
            field_types[field_name] = 'text'
    return field_types

def is_valid_date(value):
    formats = ['%d.%m.%Y', '%Y-%m-%d']

    for date_format in formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            continue

    return False

def is_valid_phone(value):
    phone_pattern = re.compile(r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$')
    return bool(phone_pattern.match(value))

def is_valid_email(value):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(email_pattern.match(value))


