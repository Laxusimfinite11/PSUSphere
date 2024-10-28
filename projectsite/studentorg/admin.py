from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")
    search_fields = ("name",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college")
    search_fields = ("name",)

@admin.register(Student)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program", "get_college")
    search_fields = ("lastname", "firstname",)

    def get_college(self, obj):
        try:
            prog = Program.objects.get(prog_name=obj.program)
            return prog.college
        
        except Program.DoesNotExist:
            return None

@admin.register(OrgMember)
class OrgMemberrAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined",)
    search_fields = ("student_lastname", "student_firstname",)

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        
        except Student.DoesNotExist:
            return None