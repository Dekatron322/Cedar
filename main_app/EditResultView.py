from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from .models import Subject, Staff, Student, StudentResult
from .forms import EditResultForm, EditStResultForm, EditTtResultForm
from django.urls import reverse


class EditResultView(View):
    def get(self, request, *args, **kwargs):
        resultForm = EditResultForm()
        staff = get_object_or_404(Staff, admin=request.user)
        resultForm.fields['subject'].queryset = Subject.objects.filter(staff=staff)
        context = {
            'form': resultForm,
            'page_title': "Edit Student's Result"
        }
        return render(request, "staff_template/edit_student_result.html", context)

    def post(self, request, *args, **kwargs):
        form = EditResultForm(request.POST)
        context = {'form': form, 'page_title': "Edit Student's Result"}
        if form.is_valid():
            try:
                student = form.cleaned_data.get('student')
                subject = form.cleaned_data.get('subject')
                first_test = form.cleaned_data.get('first_test')
                second_test = form.cleaned_data.get('second_test')
                third_test = form.cleaned_data.get('third_test')
                exam = form.cleaned_data.get('exam')

                # Validating
                result = StudentResult.objects.get(student=student, subject=subject)
                result.exam = exam
                result.first_test = first_test
                result.second_test = second_test
                result.third_test = third_test

                result.save()
                messages.success(request, "Result Updated")
                return redirect(reverse('edit_student_result'))
            except Exception as e:
                messages.warning(request, "Result Could Not Be Updated")
        else:
            messages.warning(request, "Result Could Not Be Updated")
        return render(request, "staff_template/edit_student_result.html", context)


class EditStResultView(View):
    def get(self, request, *args, **kwargs):
        resultForm = EditStResultForm()
        staff = get_object_or_404(Staff, admin=request.user)
        resultForm.fields['subject'].queryset = Subject.objects.filter(staff=staff)
        context = {
            'form': resultForm,
            'page_title': "Edit Student's Result"
        }
        return render(request, "staff_template/edit_student_stresult.html", context)

    def post(self, request, *args, **kwargs):
        form = EditStResultForm(request.POST)
        context = {'form': form, 'page_title': "Edit Student's Result"}
        if form.is_valid():
            try:
                student = form.cleaned_data.get('student')
                subject = form.cleaned_data.get('subject')
                first_ca = form.cleaned_data.get('first_ca')
                second_ca = form.cleaned_data.get('second_ca')
                third_ca = form.cleaned_data.get('third_ca')
                examination = form.cleaned_data.get('examination')

                # Validating
                result = StudentResult.objects.get(student=student, subject=subject)
                result.examination = examination
                result.first_ca = first_ca
                result.second_ca = second_ca
                result.third_ca = third_ca

                result.save()
                messages.success(request, "Result Updated")
                return redirect(reverse('edit_student_stresult'))
            except Exception as e:
                messages.warning(request, "Result Could Not Be Updated")
        else:
            messages.warning(request, "Result Could Not Be Updated")
        return render(request, "staff_template/edit_student_stresult.html", context)


class EditTtResultView(View):
    def get(self, request, *args, **kwargs):
        resultForm = EditTtResultForm()
        staff = get_object_or_404(Staff, admin=request.user)
        resultForm.fields['subject'].queryset = Subject.objects.filter(staff=staff)
        context = {
            'form': resultForm,
            'page_title': "Edit Student's Result"
        }
        return render(request, "staff_template/edit_student_ttresult.html", context)

    def post(self, request, *args, **kwargs):
        form = EditTtResultForm(request.POST)
        context = {'form': form, 'page_title': "Edit Student's Result"}
        if form.is_valid():
            try:
                student = form.cleaned_data.get('student')
                subject = form.cleaned_data.get('subject')
                tt_first_test = form.cleaned_data.get('tt_first_test')
                tt_second_test = form.cleaned_data.get('tt_second_test')
                tt_third_test = form.cleaned_data.get('tt_third_test')
                tt_exam = form.cleaned_data.get('tt_exam')

                # Validating
                result = StudentResult.objects.get(student=student, subject=subject)
                result.tt_exam = tt_exam
                result.tt_first_test = tt_first_test
                result.tt_second_test = tt_second_test
                result.tt_third_test = tt_third_test

                result.save()
                messages.success(request, "Result Updated")
                return redirect(reverse('edit_student_ttresult'))
            except Exception as e:
                messages.warning(request, "Result Could Not Be Updated")
        else:
            messages.warning(request, "Result Could Not Be Updated")
        return render(request, "staff_template/edit_student_ttresult.html", context)
